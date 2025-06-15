"""
URL configuration for fashionpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from fashionapp import views
from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('success/',views.SuccessTemplate.as_view(),name='success'),

    path('clothecreate/',views.ClothecreateView.as_view(), name='clothecreate'),
    path('clothelist/', views.ClotheListView.as_view(),name='clothelist'),
    path('clothelist/edit/<int:pk>',views.EditClothe.as_view(),name='edit'),
    path('clothelist/edit/update',views.updateClothe,name="update"),
    path('clothelist/delete/<int:id>',views.deleteclothe),

    path('clothecreatewomen/',views.ClothecreateViewwomen.as_view(), name='clothecreatewomen'),
    path('clothelistwomen/', views.ClotheListViewwomen.as_view(),name='clothelistwomen'),
    path('clothelistwomen/edit/<int:pk>',views.EditClothewomen.as_view(),name='edit'),
    path('clothelistwomen/edit/update',views.updateClothewomen),
    path('clothelistwomen/delete/<int:id>',views.deleteclothewomen),
    
    path('clothecreatechild/',views.ClothecreateViewchild.as_view(), name='clothecreatechild'),
    path('clothelistchild/', views.ClotheListViewchild.as_view(),name='clothelistchild'),
    path('clothelistchild/edit/<int:pk>',views.EditClothechild.as_view(),name='edit'),
    path('clothelistchild/edit/update',views.updateClothechild),
    path('clothelistchild/delete/<int:id>',views.deleteclothechild),

    path('menaccessories/',views.MenAccessoriesCreateView.as_view(), name='menaccessories'),
    path('MenAccessorieslist/', views.MenAccessoriesListView.as_view(),name='MenAccessorieslist'),
    path('MenAccessorieslist/edit/<int:pk>',views.EditMenAccessories.as_view(),name='edit'),
    path('MenAccessorieslist/edit/update',views.updateMenaccessories),
    path('MenAccessorieslist/delete/<int:id>',views.deleteMenAccessories),

    path('womenaccessories/',views.WomenAccessoriesCreateView.as_view(), name='womenaccessories'),
    path('womenAccessorieslist/', views.WomenAccessoriesListView.as_view(),name='womenAccessorieslist'),
    path('womenAccessorieslist/edit/<int:pk>',views.EditWomenAccessories.as_view(),name='edit'),
    path('womenAccessorieslist/edit/update',views.updateWomenaccessories),
    path('womenAccessorieslist/delete/<int:id>',views.deleteWomenAccessories),

    path('thanks/',views.CompleteTemplate.as_view(),name='thanks'),
    path('custcreate/',views.CustomerCreateView.as_view(),name='custcreate'),
    path('custlist/',views.CustomerListView.as_view(),name='custlist'),
    path('custlist/edit/<str:pk>', views.EditCustomer.as_view(), name='edit'),
    path('custlist/edit/update/', views.updateCustmore, name='update'),
    path('custlist/delete/<str:emailId>',views.deleteCustomer),

    path('clothelist/addCart/<int:id>',views.addCartForm,name='addCart'),
    path('clothelistwomen/addCart/<int:id>',views.womenaddCartForm,name='addCart'),
    path('clothelistchild/addCart/<int:id>',views.childaddCartForm,name='addCart'),
    path('MenAccessorieslist/addCart/<int:id>',views.menaccessoriesaddCartForm,name='addCart'),
    path('womenAccessorieslist/addCart/<int:id>',views.womenaccessoriesaddCartForm,name='addCart'),
    path('cartList/',views.showCart,name='cartList'),

    path('login/', views.Login, name='Login'),
    path('about/',views.aboutTemplate.as_view(),name='about'),
    path('index/',views.IndexTemplate.as_view(),name='index'),
    path('contact/',views.contactTemplate.as_view(),name='contact'),
    path('logout/', views.logout, name='logout'),
    path('footer/',views.footerTemplate.as_view(),name='footer'),

    path('cartList/placeorder',views.showOrderForm,name='placeorder'),
    path('paymentsucess/<str:tid>/<str:orderid>/',views.paymentsucess,name="paymentsucess"),
    path('cartList/delete/<int:id>/', views.deleteCartItem, name='delete'),
    #path("sample",views.placeOrder,name="sample"),

    path('initiate-payment/', views.initiate_payment, name='initiate_payment'),
    path('verify-payment/', views.verify_payment, name='verify_payment'),
    path('Footer',views.Footer),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
