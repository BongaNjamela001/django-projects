from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your models here.

# contact model for any visitors who wish to get in touch via the website
class Contact(models.Model):
    class Meta:
        verbose_name_plural = "Contact Me"
        verbose_name = "Contact"
    name = models.CharField(max_length=100, null=False) # visitor name can't be null or more than 100 words
    email = models.CharField(verbose_name = "Email", max_length=254,null=False)
    brief = models.TextField(verbose_name = "Brief Message", null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    isValid = models.BooleanField(default=False)
   
    def __str__(self):
        return f"{str(self.name) + ' Created: ' + str(self.timestamp)}"

    def checkEmail(self):
        if str.__contains__(str(self.email), '@'):
            self.isValid = True
        else:
            self.isValid = False

# portfolios including Computer Engineering, Chemistry and Physics, Electrical Engineering and Mathematics
class Portfolio(models.Model):
    class Meta:
        verbose_name_plural = "Projects"
        verbose_name = "Portfolio"

    name = models.CharField(max_length=200)
    zipproject = models.FileField(blank=True, null=True, upload_to="portfolio")
    tarproject = models.FileField(blank=True, null=True, upload_to="portfolio")
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return f"/portfolio/{self.slug}"

# resume model allows updating resume
class Resume(models.Model):
    class Meta:
        verbose_name_plural = "Resumes"
        verbose_name = "Resume"

    name = models.CharField(verbose_name="Bonga_Njamela_Resume",max_length=30)  
    resume = models.FileField(blank=True, null=True, upload_to="resume")

    def __str__(self):
        return f"{self.name}"