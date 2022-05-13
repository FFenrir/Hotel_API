from django.db import models

from rooms.models import Room
from users.models import Department

# Create your models here.

class Report(models.Model):
    room = models.ForeignKey(Room,on_delete=models.DO_NOTHING,null=True)
    report_title = models.CharField(max_length=200)
    report_description = models.TextField()
    report_left_by = models.ForeignKey(Department,on_delete=models.DO_NOTHING,null=True,related_name='Department_that_left_report')
    report_left_to = models.ForeignKey(Department,on_delete=models.DO_NOTHING,null=True,related_name='Department_that_report_is_left_to')

    def __str__(self):
        return self.room