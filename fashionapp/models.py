from django.db import models


class Clothe(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)    
    # M='Male'
    # F='Female'
    # GENDER=[(M,'Male'),(F,'Female')]
    # gender=models.CharField(max_length=10,choices=GENDER)
    category=models.CharField(max_length=10)
    size=models.CharField(max_length=10)
    material=models.CharField(max_length=10)
    price=models.FloatField(default=0.0)
    description=models.CharField(max_length=80)
    Clothe_image=models.ImageField(null=True,blank=True,upload_to="image/")

class ClotheWomen(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)    
    # M='Male'
    # F='Female'
    # GENDER=[(M,'Male'),(F,'Female')]
    # gender=models.CharField(max_length=10,choices=GENDER)
    category=models.CharField(max_length=10)
    size=models.CharField(max_length=10)
    material=models.CharField(max_length=10)
    price=models.FloatField(default=0.0)
    description=models.CharField(max_length=80)
    Clothe_image=models.ImageField(null=True,blank=True,upload_to="image/") 

class Clothechild(models.Model):
    cid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)    
    # M='Male'
    # F='Female'
    # GENDER=[(M,'Male'),(F,'Female')]
    # gender=models.CharField(max_length=10,choices=GENDER)
    category=models.CharField(max_length=10)
    size=models.CharField(max_length=10)
    material=models.CharField(max_length=10)
    price=models.FloatField(default=0.0)
    description=models.CharField(max_length=80)
    Clothe_image=models.ImageField(null=True,blank=True,upload_to="image/")

class MenAccessories(models.Model):
    id=models.AutoField(primary_key=True)   
    name=models.CharField(max_length=30)
    category=models.CharField(max_length=20)
    size=models.CharField(max_length=10)
    material=models.CharField(max_length=15)
    price=models.CharField(max_length=10)
    description=models.CharField(max_length=20)
    Men_Accessoriesimage=models.ImageField(null=True,blank=True,upload_to="image/")

class WomenAccessories(models.Model):
    id=models.AutoField(primary_key=True)   
    name=models.CharField(max_length=30)
    category=models.CharField(max_length=20)
    size=models.CharField(max_length=10)
    material=models.CharField(max_length=15)
    price=models.CharField(max_length=10)
    description=models.CharField(max_length=20)
    Women_Accessoriesimage=models.ImageField(null=True,blank=True,upload_to="image/")    

class Customer(models.Model):
    name=models.CharField(max_length=50)
    emailId=models.EmailField(primary_key=True)
    password=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    contactNo=models.IntegerField()




class CartModel(models.Model):
    cid = models.ForeignKey(Clothe, on_delete=models.CASCADE, null=True, blank=True)
    # cid = models.ForeignKey(ClotheWomen, on_delete=models.CASCADE, null=True, blank=True)
    # cid = models.ForeignKey(Clothechild, on_delete=models.CASCADE, null=True, blank=True)
    # aid = models.ForeignKey(MenAccessories, on_delete=models.CASCADE, null=True, blank=True)
    # aid = models.ForeignKey(WomenAccessories, on_delete=models.CASCADE, null=True, blank=True)
    emailId = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    totalPrice = models.FloatField(default=0.0)

class AdminModel(models.Model):
    adminEmailId=models.CharField(primary_key=True,max_length=50)
    adminpassword=models.CharField(max_length=50)


class Orders(models.Model):
    orderId=models.AutoField(primary_key=True)
    emailId=models.CharField(max_length=100)
    ordernumber=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.CharField(max_length=100)
    phoneno=models.BigIntegerField()
    totalbillamount=models.FloatField(default=0.0)

class Payment(models.Model):
    emailId=models.CharField(max_length=100)
    payment_id=models.CharField(max_length=100)
    amount_paid=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    created_st=models.DateTimeField(auto_now=True)    