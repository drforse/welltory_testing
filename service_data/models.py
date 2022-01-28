from django.db import models


class UserWeight(models.Model):
    user_id = models.IntegerField()
    day = models.DateField()
    weight = models.FloatField()

    def __str__(self):
        return f"user_id={self.user_id}, day={self.day}, weight={self.weight}"
