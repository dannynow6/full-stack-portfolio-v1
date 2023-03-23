from backend_api.views import (
    ProfileViewSet,
    SkillViewSet,
    EducationViewSet,
    ExperienceViewSet,
    ProjectViewSet,
    WebsiteViewSet,
    HobbyViewSet,
    ProfilePicViewSet,
    MyInfoViewSet,
)
from rest_framework.routers import DefaultRouter
from backend_api import views

router = DefaultRouter()
router.register(r"profiles", views.ProfileViewSet, basename="profile")
router.register(r"skills", views.SkillViewSet, basename="skills")
router.register(r"education", views.EducationViewSet, basename="education")
router.register(r"experiences", views.ExperienceViewSet, basename="experience")
router.register(r"projects", views.ProjectViewSet, basename="project")
router.register(r"websites", views.WebsiteViewSet, basename="website")
router.register(r"hobbies", views.HobbyViewSet, basename="hobby")
router.register(r"profilepics", views.ProfilePicViewSet, basename="profilepic")
router.register(r"myinfo", views.MyInfoViewSet, basename="myinfo")
urlpatterns = router.urls
