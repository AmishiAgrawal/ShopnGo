from django.db import models

# Create your models here.
class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=500)
    product_sdesc = models.CharField(max_length=1500)
    product_ldesc = models.CharField(max_length=5000)
    product_category = models.CharField(max_length=50,default='')
    product_subcategory = models.CharField(max_length=50,default='')
    product_img = models.ImageField(upload_to='MyShop/images',default='')
    product_pub_date = models.DateField()
    product_price = models.IntegerField()
    # qty_in_stock = 
 
    def __str__(self):
        return self.product_name
    

class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15,blank=True,null=True)
    email = models.EmailField(max_length=50,default='')
    issue = models.CharField(max_length=1500,default='')
    issue_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.user_name