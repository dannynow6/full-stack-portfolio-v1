from rest_framework import serializers
from backend_api.models import (
    Profile,
    Skill,
    Education,
    Experience,
    Project,
    Website,
    Hobby,
)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = "__all__"


class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = "__all__"
