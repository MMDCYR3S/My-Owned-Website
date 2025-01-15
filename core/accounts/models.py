from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _

# User Manager model
class CustomUserManager(BaseUserManager):
    """ User Manager model:
        Create user with email and password and permissions.
        if the user is not permitted, it will just create a
        normal user.
    """
    def create_user(self, email, password, **extra_fields):
        """ Register user:
            This function create a user with an email and a password.
        """
        if not email:
            raise ValueError(_("Your email must be set!"))
        else:
            email = self.normalize_email(email)
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save()
            return user
        
    def create_superuser(self, email, password, **extra_fields):
        """ Register superuser
            Create and save a user with an email and a password.
            Then it gets user permissions and check if the permissions
            are set or not.
        """
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        
        if extra_fields.get("is_staff") != True:
            raise ValueError("The superuser must have staff permissions")
        if extra_fields.get("is_superuser") != True:
            raise ValueError("The superuser must have superuser permissions")
        
        return self.create_user(email, password, **extra_fields)

# User model
class User(AbstractBaseUser, PermissionsMixin):
    """ User model:
        This model gets email as username and then register
        user with email and password. 
    """
    email = models.EmailField(max_length=254, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email
    
# Profile model
class Profile(models.Model):
    """ Profile model:
        Gets email as user from the User model. Then, it will
        complete the information about the user such as first name.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    image = models.ImageField(upload_to="accounts/", blank=True, null=True)
    description = models.TextField()
    job = models.CharField(max_length=150)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.email

# Save profile
@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)