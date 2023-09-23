from django.db import models


class TimeTrackinEntry(models.Model):
    datetime_col = models.DateTimeField()
    last_update = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.datetime_col)