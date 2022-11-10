import datetime
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import UserProfile, Task, FieldTeam, PromotionTeam, TeamUsers
from rest_framework.authtoken.models import Token
from api.serializers import FieldTeamSerializer, PromotionTeamSerializer,TeamUsersSerializer
from rest_framework	 import viewsets

class HomeAPIView(APIView):
	authenctication_classes = []
	permission_classes=[]
	def get(self,request,format=None):
		return Response()

class UserAuthAPIView(APIView):

	authenctication_classes = []
	permission_classes=[]
	def post(self, request, format=None):

		data = request.data
		username = data['email']
		image = data['image']
		social_auth_type = data["social_auth_type"]
		social_auth_code = data["social_auth_code"]

		user = UserProfile.objects.filter(username=username)
		if user:
			user=user[0]
			tk = Token.objects.filter(user=user)
			if tk:
				token = tk[0].key
			else:
				tk = Token(user=user)
				tk.save()
				token = tk.key
		else:
			user = UserProfile.objects.create_user(
				password="12345678",#default user password
				username=username,
				image=image,
				social_auth_type=social_auth_type,
				social_auth_code=social_auth_code,
				created_by=999999,#default user id
				created_date=datetime.datetime.now()
				)
			tk = Token(user=user)
			tk.save()
			token = tk.key
		message = {"user_id":user.id, "token":token}

		return Response(message)

# Create your views here.
class UserProfileAPIView(APIView):
	def post(self, request, format=None):
		data = request.data
		username = data['email']
		message=""
		user = UserProfile.objects.filter(username=username)
		if user:
			message="user already exists"

		else:
			user = UserProfile.objects.create_user(
				password="12345678",
				username=data["email"],
				biodata = data["biodata"],
				name=data["name"],
				image=data["image"],
				phone=data["phone"],
				location=data["location"],
				facebook=data["facebook"],
				instagram=data["instagram"],
				twitter=data["twitter"],
				paypal=data["paypal"],
				created_by=data["created_by_user_id"],
				created_date=datetime.datetime.now()
				)
			if user:
				message="user created successfully!!!!"
			else:
				message="Please try again"
		return Response(message)

	def put(self,request,email=None,format=None):
		data = request.data

		profiles = UserProfile.objects.filter(username=data["email"])
		profile = profiles[0]
		profile.name = data["name"]
		profile.phone = data["phone"]
		profile.location = data["location"]
		profile.facebook =  data["facebook"]
		profile.instagram = data["instagram"]
		profile.twitter =  data["twitter"]
		profile.paypal =  data["paypal"]

		profile.save()

		return Response("user-profile settings got updated")

	def get(self,request,pk=None,format=None,email=None):

		if email:
			profiles = UserProfile.objects.filter(username=email)
			#import pdb; pdb.set_trace()
		else:
			profiles = UserProfile.objects.all()
		data = [{
			"userid":i.id,
			"name":i.name,
			"phone":i.phone,
			"location":i.location,
			"facebook":i.facebook,
			"instagram":i.instagram,
			"twitter":i.twitter,
			"paypal":i.paypal,
			"email":i.username,
			"biodata":i.biodata,
			"member_since":i.created_date,
	 		} for i in profiles]

		return Response(data)



class UserStatisticAPIView(APIView):
	def get(self,request,pk=None,format=None,email=None):
		if email:
			profiles = UserProfile.objects.filter(username=email)
			#import pdb; pdb.set_trace()
		else:
			profiles = UserProfile.objects.all()
		data = [{
			"userid":i.id,
			"name":i.name,
			"phone":i.phone,
			"location":i.location,
			"facebook":i.facebook,
			"instagram":i.instagram,
			"twitter":i.twitter,
			"paypal":i.paypal,
			"email":i.username,
			"biodata":i.biodata,
			"member_since":i.created_date,
	 		} for i in profiles]

		return Response(data)



class TaskAPIView(APIView):
	def get(self,request,task_id=None,format=None):

		if task_id:
			tasks = Task.objects.filter(id=task_id)
			#import pdb; pdb.set_trace()
		else:
			tasks = Task.objects.all()

		data = [{
		"id":i.id,
			"name":i.name,
			"promoter":i.promoter,
			"amount":i.amount,
			"duration":i.duration,
			"pay":i.pay,
			"media":i.media,
			"status":i.status,
			"collection_date":i.collection_date,
			"collection_location":i.collection_location,
			"due_date":i.due_date,
			"responsible_user_id":i.responsible_user_id,
 		} for i in tasks]

		return Response(data)


	def post(self,request,format=None):
		data = request.data
		task = Task.objects.filter(name=data["name"])

		if task:
			message = "Task already exists"
		else:
			task = Task(
				name=data["name"],
				promoter=data["promoter"],
				amount=data["amount"],
				duration=data["duration"],
				pay=data["pay"],
				media=data["media"],
				status=data["status"],
				collection_date=data["collection_date"],
				collection_location=data["collection_location"],
				due_date=data["due_date"],
				responsible_user_id=data["responsible_user_id"],
				created_by=99,
				created_date=datetime.datetime.now()
				)

			task.save()
			message = "Task is created.."

		return Response(message)

	def put(self,request,format=None):
		data = request.data
		tasks = Task.objects.filter(id=data["task_id"])
		if tasks:
			task = tasks[0]
			if task:

				task.name=data["name"]
				task.promoter=data["promoter"],
				task.amount=data["amount"]
				task.duration=data["duration"]
				task.pay=data["pay"]
				task.media=data["media"]
				task.status=data["status"]
				task.collection_date=data["collection_date"]
				task.collection_location=data["collection_location"]
				task.due_date=data["due_date"]
				task.responsible_user_id=data["responsible_user_id"]

				task.save()
				message= "Task got updated"

		else:
			message="No Task exxists to edit"



		return Response(message)

	def delete(self):
		pass


class FieldTeamView(viewsets.ModelViewSet):
	# create update destroy list retrieve
	queryset = FieldTeam.objects.all()
	serializer_class = FieldTeamSerializer

	def destroy(self, request,pk):
		viewsets.ModelViewSet.destroy(self, request,pk)
		return Response("FieldTeam deleted successfully")


class PromotionTeamView(viewsets.ModelViewSet):
	queryset = PromotionTeam.objects.all()
	serializer_class = PromotionTeamSerializer

	def destroy(self, request,pk):
		viewsets.ModelViewSet.destroy(self, request,pk)
		return Response("PromotionTeam deleted successfully")


	def update(self, request,pk):
		viewsets.ModelViewSet.update(self, request,pk)
		return Response("PromotionTeam updated successfully")



class TeamUsersView(viewsets.ModelViewSet):
	queryset = TeamUsers.objects.all()
	serializer_class = TeamUsersSerializer

	def get_queryset(self):
		userTeams = self.queryset.filter(user_id=self.kwargs.get('user_id'))
		return userTeams
