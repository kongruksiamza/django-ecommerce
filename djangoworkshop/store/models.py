from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255,unique=True)
    slug=models.SlugField(max_length=255,unique=True)


    def __str__(self):
        return self.name

    class Meta :
        ordering=('name',)
        verbose_name='หมวดหมู่สินค้า'
        verbose_name_plural="ข้อมูลประเภทสินค้า"
    
    def get_url(self):
        return reverse('product_by_category',args=[self.slug])

class Product(models.Model):
    name=models.CharField(max_length=255,unique=True)
    slug=models.SlugField(max_length=255,unique=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="product",blank=True)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta :
        ordering=('name',)
        verbose_name='สินค้า'
        verbose_name_plural="ข้อมูลสินค้า"

    def get_url(self):
        return reverse('productDetail',args=[self.category.slug,self.slug])

class Cart(models.Model):
    cart_id=models.CharField(max_length=255,blank=True)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id
    
    class Meta:
        db_table='cart'
        ordering=('date_added',)
        verbose_name='ตะกร้าสินค้า'
        verbose_name_plural="ข้อมูลตะกร้าสินค้า"

class CartItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)

    class Meta:
        db_table='cartItem'
        verbose_name='รายการสินค้าในตะกร้า'
        verbose_name_plural="ข้อมูลรายการสินค้าในตะกร้า"
    
    def sub_total(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return self.product.name

class Order(models.Model):
    name=models.CharField(max_length=255,blank=True)
    address=models.CharField(max_length=255,blank=True)
    city=models.CharField(max_length=255,blank=True)
    postcode=models.CharField(max_length=255,blank=True)
    total=models.DecimalField(max_digits=10,decimal_places=2)
    email=models.EmailField(max_length=250,blank=True)
    token=models.CharField(max_length=255,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta :
        db_table='Order'
        ordering=('id',)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product=models.CharField(max_length=250)
    quantity=models.IntegerField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta :
        db_table='OrderItem'
        ordering=('order',)

    def sub_total(self):
        return self.quantity*self.price
    
    def __str__(self):
        return self.product