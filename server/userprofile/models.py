from django.db import models

# Profile Model

class Profile(models.Model):

    fullname = models.CharField(max_length=200)
    dob = models.DateTimeField(verbose_name='Date of Birth', auto_now_add=False)
    picture = models.CharField(max_length=1000) # we are going to use firestore to store our images
    bio = models.TextField(verbose_name="About yourself")
    website = models.URLField(blank=True, null=True)
    phonenumber = models.TextField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.fullname
    
    class Meta:
        verbose_name_plural = "Profiles"