from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin
from django.conf import settings


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new User"""
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Movie(models.Model):
    """Movie models to store all movies"""
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    info = models.TextField()

    def __str__(self):
        return self.name

class User_Movie(models.Model):
    """Model to assign a movie to a user after rental"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    status = models.BinaryField()
    insert_date = models.DateField()