import os
from datetime import datetime
from .models import CustomUser
from django.http import HttpResponseRedirect
from .forms import CustomUserLoginForm


def custom_authenticate(username, password):
    try:
        user = CustomUser.objects.get(username=username)
        if not user.check_password(password):
            return HttpResponseRedirect("/login/")
    except CustomUser.DoesNotExist:
        return None


class CustomAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == "POST":
            form = CustomUserLoginForm(request, data=request.POST)
            if form.is_valid():
                username = request.POST.get("username")
                password = request.POST.get("password")
                custom_authenticate(username, password)
                request.custom_authenticated = True
            else:
                HttpResponseRedirect("/")

        response = self.get_response(request)
        return response


class UserLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            log_data = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "user": request.user.username,
                "ip_address": request.META.get("REMOTE_ADDR"),
                "method": request.method,
                "path": request.path,
            }

            log_line = (
                f"{log_data['timestamp']} - User: {log_data['user']} - "
                f"IP: {log_data['ip_address']} - {log_data['method']}- "
                f"{log_data['path']}\n"
            )

            log_file_path = os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "user_logs.txt"
            )

            with open(log_file_path, "a") as log_file:
                log_file.write(log_line)
        return response
