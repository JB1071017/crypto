from django.db import models

# Create your models here.

class db(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=12)
    profileimg=models.ImageField(upload_to='userimages/')
    choices=(
        ('Male', 'MALE'),
        ('Female','FEMALE'),
        ('Others','OTHERS')

    )
    gender=models.CharField(max_length=10,choices=choices)
    age=models.IntegerField()
    approvalstatus=models.BooleanField(default=False)

class products(models.Model):
    name=models.CharField(max_length=25)
    image=models.ImageField(upload_to='productimages/')
    price=models.IntegerField()
    description=models.TextField()
    category=models.CharField(max_length=25)
    stock=models.IntegerField()
    discount=models.IntegerField()

class cart(models.Model):
    user=models.ForeignKey(db,on_delete=models.CASCADE)
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    total=models.IntegerField()

class Transaction(models.Model):
    user = models.ForeignKey(db,on_delete=models.CASCADE)
    products = models.ForeignKey(products,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveBigIntegerField(default=1)
    order_id = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    

class OTP(models.Model):
    email = models.EmailField(unique=True)
    otp = models.CharField(max_length=6)
    timestamp = models.DateTimeField(auto_now_add=True)

class Feedback(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    message=models.TextField()
    choice=(
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5')
    )
    rating=models.IntegerField(choices=choice)
    timestamp=models.DateTimeField(auto_now_add=True)

class services(models.Model):
    name=models.CharField(max_length=25)
    image=models.ImageField(upload_to='serviceimages/')
    description=models.TextField()
    

