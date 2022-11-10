# Promoter plus API

##Required Softwares
-  Python  3.7.3
-  Django  2.2.2
- Postgresql 10
- psycopg2
- django-rest-swagger
#Code set up

From cmd

go to the code available folder

Run the following commands to start the api

1. python manage.py makemigrations
2. python manage.py migrate
3. python manage.py runserver

Run the following command to test the api

1. python client.py
# API Descriptions
##1. User authentication
requests.post("https://dev.api.promoterplus.co/user-auth/",
		json{"email":"ravinder@gmail.com",
		"image":"",
		"social_auth_type":"google",
		"social_auth_code":"wwfpwmf#dvniveirv"
		})

Accepts user email-id , iamge, social_auth_code and social_auth_type then creates a user-profile record and 
 returns authentication token. If user-profile is already exists
 then returns authentication token for further communication.
 Response message would be like {"username":username, "token":token}
 this is a POST Method '''

### 2. Edit profile settings

requests.put("https://dev.api.promoterplus.co/user-profile/",
	    json={"email":"ravinder@gmail.com",
		  "name":"Ravinder",
		  "image":"",
		  "phone":"8978472671",
		  "location":"Hyderabad",
		  "facebook":"ravinder@fb.com",
		  "instagram":"ravinder@insta.com",
		  "twitter":"ravinder@twitter.com",
		  "paypal":"ravinder@paypal.com"
		  })
 Accepts user email-id and other setting details then updates the
user-profile settings.
Response message would be like "user-profile settings got updated"

### 3. Get profiles
requests.get("https:/dev.api.promoterplus.co/user-profile/ravinder@gmail.com/")
Returns  the specified profile details in json format to diaplay 

requests.get("https://dev.api.promoterplus.co/user-profile/")
Returns all the profiles in json format to diaplay 
###4. Creat Task

requests.post("https://dev.api.promoterplus.co/task/",json={
				"name":"Task2",
				"promoter":"Ravinder",
				"amount":500000,
				"duration":"6 Months",
				"pay":200000,
				"media":"Vedio",
				"status":"started",
				"collection_date":"2019-07-03",
				"collection_location":"Hyderabad",
				"due_date":"2019-07-20",
				"responsible_user_id":99
				},headers=headers)'''
				

###5. Get all Tasks
requests.get("https://dev.api.promoterplus.co/task/Task2/",headers=headers)
###6. Update a Task
response = requests.put("https://dev.api.promoterplus.co/task/",
				json={
				"task_id":3,
				"name":"First Task",
				"promoter":"Ravinder",
				"amount":500000,
				"duration":"6 Months",
				"pay":200000,
				"media":"Vedio",
				"status":"started",
				"collection_date":"2019-07-03",
				"collection_location":"Hyderabad",
				"due_date":"2019-07-20",
				"responsible_user_id":99
				},headers=headers)'''


##Fieldteam
###1.Get all
requests.get("https://dev.api.promoterplus.co/field-team/",headers=headers)
###2. Get a team
requests.get("https://dev.api.promoterplus.co/field-team/1/",headers=headers)
###3. Creat a team
requests.post("https://dev.api.promoterplus.co/field-team/",
			json={
				"name":"Second location",
				"location":"Mumbai",
				"image":"mumbai.png",
				"created_by":99,
				"created_date":"2019-07-04"
				},headers=headers)'''
###4. Delete a team
requests.delete("https://dev.api.promoterplus.co/field-team/1/",headers=headers)

###Promotion Team
###1.Get all
requests.get("https://dev.api.promoterplus.co/promotion-team/",headers=headers)

###2.Get a Team
requests.get("https://dev.api.promoterplus.co/promotion-team/1/",headers=headers)
###3.Creat a Team
requests.post("https://dev.api.promoterplus.co/promotion-team/",
			json={
				"name":"promotion-team ",
				"location":"Mumbai",
				"image":"mumbai.png",
				"created_by":99,
				"created_date":"2019-07-05"
				},headers=headers)'''

###4. Delete a Team
requests.delete("https://dev.api.promoterplus.co/promotion-team/1/",headers=headers)



