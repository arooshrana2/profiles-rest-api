from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
# Create your models here.


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None, nick_name=None):
        """Create new user profile"""
        if not email:
            raise ValueError("Users must have an email address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, nick_name=nick_name)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name, password, nick_name=None):
        """Create a superuser with given details"""
        user = self.create_user(email=email, name=name, password=password, nick_name=nick_name)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user
    

class UserProfile(AbstractUser, PermissionsMixin):
    """Model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    nick_name = models.CharField(max_length=255)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def get_full_name(self) -> str:
        """Get full name of the user"""
        return self.name
    
    def get_short_name(self) -> str:
        """Get short name of the user"""
        return self.nick_name
    
    def __str__(self):
        """Return string representation of user"""
        return self.email
    
