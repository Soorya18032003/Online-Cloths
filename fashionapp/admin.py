from django.contrib import admin

# Register your models here.
from django.contrib import admin
from fashionapp.models import Clothe,Customer,AdminModel,ClotheWomen,Clothechild,MenAccessories,WomenAccessories,CartModel

admin.site.register(Clothe)
admin.site.register(Customer)
admin.site.register(AdminModel)
admin.site.register(ClotheWomen)
admin.site.register(Clothechild)
admin.site.register(MenAccessories)
admin.site.register(WomenAccessories)
admin.site.register(CartModel)

