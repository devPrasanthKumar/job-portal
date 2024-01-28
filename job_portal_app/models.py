from django.db import models
from job_portal_auth.models import User


class UserProfileModel(models.Model):
    GENDER = [("Male", "Male"), ("Female", "Female"), ("Others", "Others")]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username=models.CharField(max_length=400)
    email = models.EmailField(unique=True)
    phone = models.IntegerField()
    gender = models.CharField(choices=GENDER, max_length=300)
    user_profile_img = models.ImageField(upload_to="uploads/")
    head_line = models.CharField(max_length=300)
    user_resume = models.FileField(upload_to="files/")
    location = models.CharField(max_length=300)
    website = models.URLField()
    ready_to_work = models.BooleanField(default=True)
    
    def __str__(self):
        return self.user.username


class UserEducationModel(models.Model):
    user = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE)
    school = models.CharField(max_length=400)
    degree = models.CharField(max_length=400)
    field_of_study = models.CharField(max_length=400)
    start_date = models.DateField()
    end_date = models.DateField()
    grade = models.PositiveIntegerField()
    activites = models.CharField(max_length=400)


class UserSkillsModel(models.Model):
    user = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE)
    skils = models.CharField(max_length=400)


class UserExperienceModel(models.Model):
    user = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=400)
    company_name = models.CharField(max_length=400)
    year = models.DurationField()


class UserCertificationsModel(models.Model):
    user = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE)
    certification_name = models.CharField(max_length=400)
    expiration_month = models.DateField()
    expiration_year = models.DateField()


class UserLanguagesModel(models.Model):
    LEVEL = [("Beginner","Beginner"),("Expert","Expert"),("Fluent","Fluent"),("Native","Native")]
    user = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE)
    language = models.CharField(max_length=400)
    proficiency = models.CharField(choices=LEVEL,max_length=400)



class UserJobPreferences(models.Model):
    job_titles = models.TextField() 
    JOB_TYPE_CHOICES = [
        ('part_time', 'Part-Time'),
        ('full_time', 'Full-Time'),
        ('internship', 'Internship'),
        ('fresher', 'Fresher'),
    ]
    