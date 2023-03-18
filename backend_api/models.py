from django.db import models

# Models for Portfolio Project


class Profile(models.Model):
    """A model representing Profile Description"""

    title = models.CharField(max_length=125)
    description = models.TextField()

    def __str__(self):
        return f"{self.title.title()}"


class Skill(models.Model):
    """A Model representing resume skills"""

    name = models.CharField(max_length=150)
    # make level options restricted on front-end (advanced, familiar, ...)
    level = models.CharField(blank=True)
    # make skill type options restricted on front-end (hard/soft)
    type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name.title()}, {self.type}"


class Education(models.Model):
    """a model representing education earned"""

    school_name = models.CharField(max_length=200)
    school_city = models.CharField(max_length=200, blank=True)
    school_state = models.CharField(max_length=200, blank=True)
    school_country = models.CharField(max_length=200)
    degree_earned = models.CharField(max_length=200, blank=True)
    discipline = models.CharField(max_length=125, blank=True)
    date_started = models.DateField()
    date_completed = models.DateField()
    accolades = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return f"{self.school_name.title()} | {self.date_completed}"
