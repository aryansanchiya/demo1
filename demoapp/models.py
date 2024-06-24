from djongo import models

class Info(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=15)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username
