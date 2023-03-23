from django.contrib import admin
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

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list = ("title", "description")

    admin.site.register(Profile)


class SkillAdmin(admin.ModelAdmin):
    list = ("name", "level", "type")

    admin.site.register(Skill)


class EducationAdmin(admin.ModelAdmin):
    list = ("school_name", "degree_earned", "date_completed")

    admin.site.register(Education)


class ExperienceAdmin(admin.ModelAdmin):
    list = ("position", "employer_name", "start_date")

    admin.site.register(Experience)


class ProjectAdmin(admin.ModelAdmin):
    list = ("title", "tech_used")

    admin.site.register(Project)


class WebsiteAdmin(admin.ModelAdmin):
    list = ("name", "url")

    admin.site.register(Website)


class HobbyAdmin(admin.ModelAdmin):
    list = ("name", "start_date", "url")

    admin.site.register(Hobby)


class ProfilePicAdmin(admin.ModelAdmin):
    list = "name"

    admin.site.register(ProfilePic)

class MyInfoAdmin(admin.ModelAdmin):
    list = ("last_name", "first_name", "email", "postal", "country")
    
    admin.site.register(MyInfo) 