from django.db import models

# Create your models here.


class Activity(models.Model):
    user_id = models.PositiveSmallIntegerField(null=True, blank=True)
    # user = models.ForeignKey(User)
    act_title = models.CharField(max_length=100)
    act_description = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.act_title)


class Stat(models.Model):
    # stat_title = models.CharField(max_length=100)
    activity = models.ForeignKey(Activity, related_name='stats')
    # activity = models.ForeignKey(Activity)
    count = models.PositiveIntegerField(null=True, blank=True)
    date_done = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Date: {}. Count: {}.".format(self.date_done, self.count)
