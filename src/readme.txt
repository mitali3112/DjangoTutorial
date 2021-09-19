#Make Migrations
    python manage.py makemigrations
#Migrate
    python manage.py migrate
#Creating SuperUser
    python manage.py createsuperuser
#Create new apps
    python manage.py startapp tryout
#Run Django Server
    python manage.py runserver
#Create products in terminal
    python manage.py shell

    In [1]: from tryout.models import Product                                       

    In [2]: Product.objects.all                                                     
    Out[2]: <bound method BaseManager.all of <django.db.models.manager.Manager object at 0x7fd235d3b2d0>>

    In [3]: Product.objects.all()                                                   
    Out[3]: <QuerySet [<Product: Product object (1)>]>

    In [4]: Product.objects.create(title = 'P2', description = 'D2', price = '100', 
    ...: summary = 'S2')                                                         
    Out[4]: <Product: Product object (2)>


