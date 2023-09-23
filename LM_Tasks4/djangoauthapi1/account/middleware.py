import os
import jwt
from datetime import datetime
from django.core.cache import cache
from django.http import HttpResponse
from .models import User


class UserLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = self.validate_user(request)
        if user:
            log_data = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "user": user.email,
                "group": user.group,
                "ip_address": request.META.get("REMOTE_ADDR"),
                "method": request.method,
                "path": request.path,
            }

            log_line = (
                f"{log_data['timestamp']} - User: {log_data['user']} - "
                f"IP: {log_data['ip_address']} - "
                f"Method: {log_data['method']} - "
                f"Path: {log_data['path']} \n"
            )

            log_file_path = os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "user_logs.txt"
            )

            with open(log_file_path, "a") as log_file:
                log_file.write(log_line)

            group = user.group
            request_key = f"{user.id}"
            request_count = cache.get(request_key)
            if not request_count:
                cache.set(request_key, 1, 60)
            else:
                cache.set(request_key, request_count + 1, 60)

            if group.upper() == "GOLD":
                request_limit = 10
            elif group.upper() == "BRONZE":
                request_limit = 5
            elif group.upper() == "SILVER":
                request_limit = 2
            else:
                request_limit = 0

            if cache.get(request_key) > request_limit:
                return HttpResponse("Too many requests", status=429)
        response = self.get_response(request)
        return response

    def validate_user(self, request):
        token = request.META.get("HTTP_AUTHORIZATION")
        if token:
            try:
                token = token.split(" ")
                if len(token) == 2:
                    decoded_token = jwt.decode(
                        token[1],
                        options={
                            "verify_signature": False,
                            "verify_aud": False,
                        },
                        algorithms=["HS256"],
                    )
                user_id = decoded_token.get("user_id")
                try:
                    user = User.objects.get(pk=user_id)
                    return user
                except User.DoesNotExist:
                    return None
                else:
                    pass

            except jwt.ExpiredSignatureError:
                return None
            except jwt.DecodeError:
                return None

        return None
