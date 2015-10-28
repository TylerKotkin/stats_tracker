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

    # def __str__(self):
    #     return "Date: {}. Count: {}.".format(self.date_done, self.count)


def make_fake_data(num_activities=50):
    from faker import Faker
    from random import randint
    fake = Faker()

    # if delete_all:
    #     Activity.objects.all().delete()
    #     Stat.objects.all().delete()

    for _ in range(num_activities):
        a = Activity(act_title=fake.bs().title(), act_description=fake.text(max_nb_chars=200))
        a.created_on = fake.date_time_this_year()
        a.save()

        for __ in range(10):
            s = Stat(count=randint(1, 101), activity=a)
            s.created_on = fake.date_time_this_month(before_now=True, after_now=False)
            s.save()
