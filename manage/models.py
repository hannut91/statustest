from django.db import models


class Applist(models.Model):
    app_name = models.CharField(max_length=10)
    class Meta:
        db_table = "Applist"

    def __str__(self):
        return self.app_name

class Maintenance(models.Model):
    url = models.URLField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    register_time = models.DateTimeField(auto_now_add = True)
    applist = models.ForeignKey(Applist, on_delete=models.CASCADE)

    class Meta:
        db_table = "Maintenance"


class Notice(models.Model):
    title = models.CharField(max_length = 40)
    text = models.TextField()
    url = models.URLField(blank=True)
    locale = models.CharField(max_length=2)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    register_time = models.DateTimeField(auto_now_add = True)
    show_notice = models.BooleanField()
    applist = models.ManyToManyField(Applist)


    class Meta:
        db_table = "Notice"

    def __str__(self):
        return self.title

class UpdateList(models.Model):
    title = models.CharField(max_length = 40)
    text = models.TextField()
    url = models.URLField(blank=True)
    register_time = models.DateTimeField(auto_now_add=True)
    rec_ver = models.CharField(max_length=5)
    man_ver = models.CharField(max_length=5)
    build_ver = models.IntegerField(unique=True)
    locale = models.CharField(max_length=2)
    applist = models.ForeignKey(Applist, on_delete=models.CASCADE)

    class Meta:
        db_table = "UpdateList"

    def __str__(self):
        return self.title

"""
class Version(models.Model):

    rec_ver = models.CharField(max_length=5)
    man_ver = models.CharField(max_length=5)
    reg_dt = models.DateTimeField(auto_now = True)

    applist = models.OneToOneField(Applist, on_delete=models.CASCADE)

    class Meta:
        db_table = "Version"
"""
