from django.db import models
from django.contrib.auth.models import AbstractUser


class AuditModel(models.Model):
	created_by = models.IntegerField()
	created_date = models.DateField()
	modified_by = models.IntegerField(blank=True, null=True)
	modified_date = models.DateField(blank=True, null=True)
	is_enabled =models.BooleanField(default=True)

	class Meta:
		abstract=True


# Create your models here.
class UserProfile(AbstractUser):
	name = models.CharField(max_length=250)
	image = models.CharField(max_length=500,blank=True, null=True)
	social_auth_type=models.CharField(max_length=250,blank=True, null=True)
	social_auth_code=models.CharField(max_length=500,blank=True, null=True)
	phone = models.CharField(max_length=250,blank=True, null=True)
	location = models.CharField(max_length=250,blank=True, null=True)
	biodata = models.CharField(max_length=2500,blank=True, null=True)
	facebook =  models.CharField(max_length=250,blank=True, null=True)
	instagram =  models.CharField(max_length=250,blank=True, null=True)
	twitter =  models.CharField(max_length=250,blank=True, null=True)
	paypal =  models.CharField(max_length=250,blank=True, null=True)
	created_by = models.IntegerField(blank=True, null=True)
	created_date = models.DateField(blank=True, null=True)
	modified_by = models.IntegerField(blank=True, null=True)
	modified_date = models.DateField(blank=True, null=True)
	is_enabled =models.BooleanField(default=True)


class Team(AuditModel):
	name = models.CharField(max_length=250)
	staus = models.CharField(max_length=250)


	class Meta:
		db_table="Teams"


class TeamUsers(AuditModel):
	team_id = models.IntegerField()
	user_id = models.IntegerField()
	team_type = models.CharField(max_length=250,blank=True, null=True)
	class Meta:
		db_table="TeamUsers"



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class FieldTeam(AuditModel):
	name = models.CharField(max_length=250)
	location = models.CharField(max_length=250)
	image =  models.CharField(max_length=250)


	class Meta:
		db_table="FieldTeams"

class PromotionTeam(AuditModel):
	name = models.CharField(max_length=250)
	location = models.CharField(max_length=250)
	image =  models.CharField(max_length=250)


	class Meta:
		db_table="PromotionTeams"

class Task(AuditModel):
    task_status_choices = [("started", "started"),("completed","completed")]

    name = models.CharField(max_length=250)
    promoter = models.CharField(max_length=250)
    amount =  models.IntegerField()
    duration = models.CharField(max_length=250)
    pay = models.IntegerField()
    media = models.CharField(max_length=250)
    status = models.CharField(choices=task_status_choices,max_length=10)

    collection_date = models.DateField()
    collection_location = models.CharField(max_length=250)
    due_date = models.DateField()
    responsible_user_id = models.IntegerField()
    def __str__(self):
        return self.name

    class Meta:
        db_table="Tasks"

    


class Media(AuditModel):
	name = models.CharField(max_length=250)
	promoter = models.CharField(max_length=250)
	status = models.CharField(max_length=250)
	amount =  models.IntegerField()
	duration = models.CharField(max_length=250)
	pay = models.IntegerField()
	media = models.CharField(max_length=250)
	media_version = models.IntegerField()
	version_comment  = models.CharField(max_length=1000)

	class Meta:
		db_table="Media"

class MediaBrief(AuditModel):
	media_choices = [("video", "video"),("image", "image"),("file", "file")]

	designer_number = models.CharField(max_length=250)
	promoter = models.CharField(max_length=250)
	status = models.CharField(max_length=250)
	amount =  models.IntegerField()
	duration = models.CharField(max_length=250)
	pay = models.IntegerField()
	media = models.CharField(max_length=250)
	media_version = models.IntegerField()
	version_comment  = models.CharField(max_length=1000)

	class Meta:
		db_table="MediaBriefs"

class Campaign(AuditModel):
	name = models.CharField(max_length=250)
	from_date = models.DateField()
	to_date = models.DateField()
	location = models.CharField(max_length=250)
	budget = models.IntegerField()
	field_team_id = models.IntegerField()

	class Meta:
		db_table="Campaigns"
