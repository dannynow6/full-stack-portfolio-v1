from django.shortcuts import render
from .models import (
    Profile,
    Skill,
    Education,
    Experience,
    Project,
    Website,
    Hobby,
    ProfilePic,
    MyInfo,
)
from .serializers import (
    ProfileSerializer,
    SkillSerializer,
    EducationSerializer,
    ExperienceSerializer,
    ProjectSerializer,
    WebsiteSerializer,
    HobbySerializer,
    ProfilePicSerializer,
    MyInfoSerializer,
)
from rest_framework import viewsets

# Create your views here.
class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class SkillViewSet(viewsets.ModelViewSet):
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()


class EducationViewSet(viewsets.ModelViewSet):
    serializer_class = EducationSerializer
    queryset = Education.objects.all()


class ExperienceViewSet(viewsets.ModelViewSet):
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class WebsiteViewSet(viewsets.ModelViewSet):
    serializer_class = WebsiteSerializer
    queryset = Website.objects.all()


class HobbyViewSet(viewsets.ModelViewSet):
    serializer_class = HobbySerializer
    queryset = Hobby.objects.all()


class ProfilePicViewSet(viewsets.ModelViewSet):
    serializer_class = ProfilePicSerializer
    queryset = ProfilePic.objects.all()


class MyInfoViewSet(viewsets.ModelViewSet):
    serializer_class = MyInfoSerializer 
    queryset = MyInfo.objects.all() 