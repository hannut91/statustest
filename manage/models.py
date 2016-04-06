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

class DeployStatus(models.Model):

    title = models.CharField(max_length = 40)
    deploy_info = models.TextField()
    card_link = models.URLField()
    register_time = models.DateTimeField(auto_now_add=True)
    git_link = models.URLField()
    
    class Meta:
        db_table = "Deploy"
        
    def __str__(self):
        return self.title
        
class GitInfo(models.Model):
    commit_id = models.CharField(max_length = 40)
    commit_message = models.CharField(max_length=255)
    commit_time = models.DateTimeField()
    commit_url = models.URLField()
    commit_added = models.CharField(max_length=255)
    commit_removed = models.CharField(max_length=255)
    commit_modified = models.CharField(max_length=255)
    repository_name = models.CharField(max_length=40)
    repository_url = models.URLField()
    repository_default_branch = models.CharField(max_length=40)
    repository_master_branch = models.CharField(max_length=40)
    
    class Meta:
        db_table = "Gitinfo"
        
    def __str__(self):
        return self.commit_message