from django.db import models

# Models for Portfolio Project


class Profile(models.Model):
    """A model representing Profile Description"""

    title = models.CharField(max_length=125)
    description = models.TextField()

    def __str__(self):
        return f"{self.id} {self.title.title()}"


class Skill(models.Model):
    """A Model representing resume skills"""

    name = models.CharField(max_length=150)
    # make level options restricted on front-end (advanced, familiar, ...)
    level = models.CharField(max_length=125, blank=True, null=True)
    # make skill type options restricted on front-end (hard/soft)
    type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} {self.name.title()}, {self.type}"


class Education(models.Model):
    """a model representing education earned"""

    school_name = models.CharField(max_length=200)
    school_city = models.CharField(max_length=200, blank=True, null=True)
    school_state = models.CharField(max_length=200, blank=True, null=True)
    school_country = models.CharField(max_length=200)
    degree_earned = models.CharField(max_length=200, blank=True, null=True)
    program = models.CharField(max_length=125, blank=True, null=True)
    date_started = models.DateField()
    date_completed = models.DateField()
    accolades = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return (
            f"{self.school_name.title()} | {self.degree_earned} | {self.date_completed}"
        )


class Experience(models.Model):
    """a model representing work experience"""

    position = models.CharField(max_length=200)
    employer_name = models.CharField(max_length=250)
    employer_city = models.CharField(max_length=200, blank=True, null=True)
    employer_state = models.CharField(max_length=150, blank=True, null=True)
    employer_country = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.CharField(max_length=25, blank=True, null=True)
    current_employer = models.CharField(max_length=50, help_text="yes or no")
    description = models.TextField()

    def __str__(self):
        return f"{self.position} | {self.employer_name.title()} | {self.start_date}"


class Project(models.Model):
    """a model representing coding projects on resume"""

    title = models.CharField(max_length=250)
    tech_used = models.CharField(max_length=300)
    description = models.TextField()
    git_repo = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.title.title()}"


class Website(models.Model):
    """a model representing domains"""

    name = models.CharField(max_length=200)
    url = models.URLField()
    description = models.CharField(max_length=175, blank=True, null=True)

    def __str__(self):
        return f"{self.name}: {self.url}"


class Hobby(models.Model):
    """a model representing hobbies or additional info from resume"""

    name = models.CharField(max_length=200)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.CharField(max_length=25, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    additional_info = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        verbose_name_plural = "hobbies"

    def __str__(self):
        return f"{self.name.title()}"


class ProfilePic(models.Model):
    """a model representing pictures for use on resume/website"""

    name = models.CharField(max_length=125)
    picture = models.ImageField(upload_to="photos/")

    def __str__(self):
        return f"{self.name.title()}"


class MyInfo(models.Model):
    """A model representing basic user contact info"""
    # Note: will move this to user account later
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(blank=True, null=True) 
    street = models.CharField(max_length=300, blank=True, null=True) 
    city = models.CharField(max_length=300, blank=True, null=True) 
    state = models.CharField(max_length=300, blank=True, null=True) 
    postal = models.CharField(max_length=25, blank=True, null=True) 
    country = models.CharField(max_length=300, blank=True, null=True) 
    
    def __str__(self):
        full_name = f"{self.last_name.title()}, {self.first_name.title()}"
        return f"{full_name}"
    