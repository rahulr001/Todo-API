import requests

 #2cd0c63289ba4ff780c9f45ad1d92251bfb636f1
 #ce87865757d78a22ac0f031b73ea4078efa2fd0d online
####user-profile create
headers = {"Authorization":"Token 549836d6b58c0ba66d8f6ab9a1c0afad7b528b3c"}
#response = requests.get("http://localhost:8000/user-profile/ravinder@gmail.com/")
#response = requests.post("http://localhost:8000/user-profile/",json={"email":"vijay@gmail.com", "name":"Vijay Kumar"},headers=headers)
####

####user-profile edit

'''response = requests.put("http://localhost:8000/user-profile/",
	json={"email":"ravinder@gmail.com",
		  "name":"Ravinder",
		  "phone":"8978472671",
		  "location":"Hyderabad",
		  "facebook":"ravinder@fb.com",
		  "instagram":"ravinder@insta.com",
		  "twitter":"ravinder@twitter.com",
		  "paypal":"ravinder@paypal.com",

		  })'''

####

#### user-profile list
#response = requests.get("http://localhost:8000/user-profile/",json={"email":"ravinder@gmail.com"})
#response = requests.get("http://localhost:8000/user-profile/ravinder@gmail.com/")
#response = requests.get("http://localhost:8000/user-profile/")

####

####
#response =requests.get("https://dev.api.promoterplus.co/user-profile/",headers=headers)
##response =requests.get("https://dev.api.promoterplus.co/user-profile/ravinder@gmail.com/",headers=headers)
#response =requests.get("http://localhost:8000/user-profile/",headers=headers)
#response =requests.post("https://dev.api.promoterplus.co//user-auth/",json={"email":"aditeya@gmail.com"})
#response =requests.get("https://dev.api.promoterplus.co//user-profile/",headers=headers)
#response =requests.put("https://dev.api.promoterplus.co//user-auth/",json={"email":"aditeya@gmail.com","name":"Aditeya Davuda","user_id":"1"},headers=headers)
####

###Tasks
'''
response =requests.post("http://localhost:8000/task/",json={
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

#response =requests.get("http://localhost:8000/task/Task2/",headers=headers)
'''response = requests.put("http://localhost:8000/task/",json={
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
###

####fieldteams
#response =requests.get("http://localhost:8000/field-team/1",headers=headers)
#response = requests.delete("http://localhost:8000/field-team/2/",headers=headers)
'''response = requests.post("http://localhost:8000/field-team/",json={
				"name":"Second location",
				"location":"Mumbai",
				"image":"mumbai.png",
				"created_by":99,
				"created_date":"2019-07-04"
				},headers=headers)'''

####

#########Promotion Team
#response =requests.get("http://localhost:8000/promotion-team/1",headers=headers)
'''response = requests.put("http://localhost:8000/promotion-team/",json={
				"id":2,
				"name":"promotion-team Modified",
				"location":"Mumbai",
				"image":"mumbai.png",
				"created_by":99,
				"created_date":"2019-07-05"
				},headers=headers)'''
#response = requests.delete("http://localhost:8000/promotion-team/1/",headers=headers)
####
print(response)
print(response.json())
