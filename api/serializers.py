from rest_framework import serializers
from api.models import FieldTeam, PromotionTeam, TeamUsers

class FieldTeamSerializer(serializers.ModelSerializer):
	class Meta:
		model = FieldTeam
		fields = "__all__"

class PromotionTeamSerializer(serializers.ModelSerializer):
	class Meta:
		model = PromotionTeam
		fields = "__all__"

class TeamUsersSerializer(serializers.ModelSerializer):
	class Meta:
		model = TeamUsers
		fields = "__all__"
