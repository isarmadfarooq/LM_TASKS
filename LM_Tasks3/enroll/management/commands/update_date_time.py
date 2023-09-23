from django.core.management.base import BaseCommand
from enroll.models import TimeTrackinEntry
from pytz import timezone
from datetime import datetime


def pst_to_utc(date_object: TimeTrackinEntry):
    converted_date = date_object.datetime_col.astimezone(timezone("UTC"))
    return converted_date


def utc_to_pst(date_object: TimeTrackinEntry):
    converted_date = date_object.datetime_col.astimezone(timezone("US/Pacific"))
    return converted_date


class Command(BaseCommand):
    help = "Change Time"

    def handle(self, *args, **kwargs):
        items = TimeTrackinEntry.objects.all()
        print("items: ", len(items))
        objects_ids = []
        for item in items:
            objects_ids.append(item.id)

        with open("file.txt", "r") as f:
            counter = f.read()
        intcounter = int(counter)
        print("int counter: ", intcounter)

        objec = objects_ids[intcounter: intcounter + 10]
        # changing time
        for i in objec:
            dt = TimeTrackinEntry.objects.get(pk=i)
            print("before conversion dt: ", dt.datetime_col.tzname())
            if "PDT" in dt.datetime_col.tzname():
                new_time = pst_to_utc(dt)
                dt.datetime_col = new_time
                dt.save()
                print("it was PST")
            else:
                new_time = utc_to_pst(dt)
                dt.datetime_col = new_time
                dt.save()
                print("it was UTC")
            print("After conversion dt: ", new_time.tzname())
            dt.last_update = datetime.now()
            dt.save()

        with open("file.txt", "w") as f:
            if intcounter > 90:
                f.write("0")
            else:
                intcounter = intcounter + 10
                f.write(str(intcounter))
