from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE, null = True, blank = True)
    name = models.CharField(max_length = 200, null=True)
    email = models.CharField(max_length = 200, null = True)


    def __str__(self):
        return self.name
    

class Usuario(models.Model):
    # Campos de texto
    
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    DPI = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=50)
    nombre_usuario = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    contrasenia = models.CharField(max_length=50)
    con_contrasenia = models.CharField(max_length=50)

    # Campos con opciones
    OPCIONES_ROL = [
        ('usuario', 'Usuario normal'),
        ('admin', 'Administrador'),
    ]
    roles = models.CharField(max_length=7, choices=OPCIONES_ROL, default='usuario')
    def __str__(self):
        return f"{self.nombre} {self.apellidos} ({self.nombre_usuario})"
    

class Product(models.Model):
    name = models.CharField(max_length = 200, null = True)
    price = models.FloatField()
    digital = models.BooleanField(default = False, null = True)
    image = models.ImageField(null = True , blank=True)
    def __str__(self):
        return self.name
    
    @property
    def imageURl(self):
        try:

            url = self.image.url
        except:

            url = ''
        return url

class Order(models.Model):

    customer = models.ForeignKey(Customer,on_delete= models.SET_NULL,null=True,blank=True)
    date_orderd = models.DateTimeField(auto_now_add =True)
    complete = models.BooleanField(default = False, null = True, blank = False)
    transaction_id = models.CharField(max_length = 200, null = True)
    def __str__(self):
        return str(self.id)
    


    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping
    




    @property
    def get_cart_total(self):

        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):

        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    
class OrderItem(models.Model):
      product = models.ForeignKey(Product,on_delete= models.SET_NULL,null=True,blank=True)
      order = models.ForeignKey(Order,on_delete= models.SET_NULL,null=True,blank=True)
      quantity = models.IntegerField(default = 0,null = True, blank = True)
      date_added = models.DateTimeField(auto_now_add = True)



      @property
      def get_total(self):
          total = self.product.price * self.quantity
          return total

class ShippingAddress(models.Model):
       customer = models.ForeignKey(Customer,on_delete= models.SET_NULL,null=True)
       order = models.ForeignKey(Order,on_delete= models.SET_NULL,null=True)
       address = models.CharField(max_length = 200, null = False)
       city = models.CharField(max_length = 200, null = False)
       state = models.CharField(max_length = 200, null = False)
       zipcode = models.CharField(max_length = 200, null = False)
       date_added = models.DateTimeField(auto_now_add = True)

       def __str__(self):
        return str(self.address)
       



