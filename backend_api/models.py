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
    level = models.CharField(max_length=125, blank=True)
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
    program = models.CharField(max_length=125, blank=True)
    date_started = models.DateField()
    date_completed = models.DateField()
    accolades = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return f"{self.school_name.title()} | {self.degree_earned} | {self.date_completed}"


class Experience(models.Model):
    """a model representing work experience"""

    position = models.CharField(max_length=200)
    employer_name = models.CharField(max_length=250)
    employer_city = models.CharField(max_length=200, blank=True)
    employer_state = models.CharField(max_length=150, blank=True)
    employer_country = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    current_employer = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        return f"{self.position} | {self.employer_name.title()} | {self.start_date}"


class Project(models.Model):
    """a model representing coding projects on resume"""

    title = models.CharField(max_length=250)
    tech_used = models.CharField(max_length=300)
    description = models.TextField()
    git_repo = models.URLField(blank=True)

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
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    additional_info = models.CharField(max_length=250, blank=True)

    class Meta:
        verbose_name_plural = "hobbies"

    def __str__(self):
        return f"{self.name.title()}"
