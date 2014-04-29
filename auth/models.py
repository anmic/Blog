from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30, unique=True)
    username = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)

    def __unicode__(self):
        return "<Name: %r, Username: %r, Email: %r,Password : %r.>" % \
            (self.name, self.username, self.email, self.password)
