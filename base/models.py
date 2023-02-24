from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


class User(AbstractUser):
    name: str = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True)
    address = models.TextField(max_length=200, null=True, blank=True)
    bio = models.TextField(max_length=200, null=True, blank=True)
    avatar = models.ImageField(null=True, default='avatar.svg')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Car(models.Model):
    AVAILABLE = 'A'
    NOT_AVAILABLE = "N/A"

    STATUS_CHOICES = [
        (AVAILABLE, 'Available'),
        (NOT_AVAILABLE, 'Not available')
    ]

    name = models.CharField(max_length=100, null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    year = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(1900),
        MaxValueValidator(3000)
    ])
    capacity = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(1)
    ])
    brand = models.CharField(max_length=100, null=True)
    image = models.ImageField(null=True)
    plate = models.CharField(max_length=10)
    rate = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(5)
    ], default=0)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    status = models.CharField(
        max_length=3,
        choices=STATUS_CHOICES,
        default=AVAILABLE,
    )
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, )
    cars = models.ManyToManyField(Car, related_name='cars', blank=True)
    payment = models.DecimalField(max_digits=20, decimal_places=2)

    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.user.username


class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    review = models.TextField(max_length=200, null=True, blank=True)
    score = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(5)
    ], default=0)

    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.review[0:50]
