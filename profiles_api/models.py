from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
  """User Profiles manager"""

  def create_user(self, email, name, password=None):
    """A new user profile created"""
    if not email:
      raise ValueError('User must have an email address')
    
    email = self.normalize_email(email)
    user = self.model(email=email, name=name)

    user.set_password(password)
    user.save(using=self._db)

    return user
  
  def super_user(self, email, name, password):
    """Creating and saving a new superuser with the given details"""
    user = self.create_user(email, name, password)

    user.is_superuser = True
    user.is_staff = True
    user.save(using=self._db)

    return user 

class UserProfile(AbstractBaseUser, PermissionsMixin):
  """Users Database model in the system"""
  email = models.EmailField(max_length=255, unique=True)
  name = models.CharField(max_length=255)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)

  objects = UserProfileManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['name']

  def get_full_name(self):
    """get full name of the user"""
    return self.name

  def get_short_name(self):
    """get short name of the user"""
    return self.name

  def __str__(self):
    """String representation of the User"""
    return self.email

