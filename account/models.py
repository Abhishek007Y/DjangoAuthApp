from django.db import models

# Create your models here.

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class Myuser(AbstractBaseUser):
    email=models.EmailField(verbose_name='email address',
                            max_length=255,
                            unique=True,)
    
    name=models.CharField(max_length=200)
    tc=models.BooleanField()
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    USERNAME_FILED='email'
    REQUIRED_FIELDS=['name','tc']

    def __str_(self):
        return self.email
    
    def has_perm(self, perm,obj=None):
        "Does the user have specific permissiom??"
        return self.is_admin
    
    def has_module_perms(self,app_label):
        "Does the user have permission to view the app  `app_label`?"
        return True