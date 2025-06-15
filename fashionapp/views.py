from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from fashionapp.models import Clothe
from fashionapp.models import Orders
from fashionapp.models import Payment
from fashionapp.models import Clothechild
from fashionapp.models import MenAccessories
from fashionapp.models import WomenAccessories
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from fashionapp.models import Customer
from fashionapp.models import CartModel
from datetime import date
from fashionapp.models import AdminModel
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password,check_password
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login as auth_login, logout
from fashionapp.models import ClotheWomen
from django.contrib import messages
import razorpay
from django.http import JsonResponse
import hmac
import hashlib

# Create your views here.

class SuccessTemplate(TemplateView):
    template_name='fashionapp/Success.html'

class ClothecreateView(CreateView):
    model=Clothe
    fields=['name','category','size','material','price','description','Clothe_image']    
    success_url='/success/'

class ClotheListView(ListView):
    model=Clothe
    context_object_name='clothe'
    template_name='fashionapp/clothe_list.html'     

class ClothedetailsView(DetailView):
    model=Clothe
    context_object_name='clothes'
    template_name='fashionapp/updateclothe.html'


class EditClothe(DetailView):
    model=Clothe
    context_object_name='clothes'
    template_name='fashionapp/Updateclothe.html'    

def updateClothe(request):
    if request.method=='POST':
        cid=request.POST['id']
        cname=request.POST['name']
        # gen=request.POST['gender']
        cat=request.POST['category']
        sz=request.POST['size']
        ma=request.POST['material']
        pr=request.POST['price']
        desc=request.POST['description']
        img=request.POST['Clothe_image']
        ce=Clothe.objects.filter(id=cid)
        ce.update(id=cid,name=cname,category=cat,size=sz,material=ma,price=pr,description=desc,Clothe_image=img)
        return HttpResponse("Data Updated successfully")
    else:
        return render(request,'fashionapp/Updateclothe.html')

def deleteclothe(request,id):
    data=Clothe.objects.get(id=id)        
    data.delete()
    return redirect("clothelist")





class ClothecreateViewwomen(CreateView):
    model=ClotheWomen
    fields=['name','category','size','material','price','description','Clothe_image']    
    success_url='/success/'

class ClotheListViewwomen(ListView):
    model=ClotheWomen
    context_object_name='clothe'
    template_name='fashionapp/clothewomen_list.html'     

class ClothedetailsViewwomen(DetailView):
    model=ClotheWomen
    context_object_name='clothes'
    template_name='fashionapp/updateclothewomen.html'

class EditClothewomen(DetailView):
    model=ClotheWomen
    context_object_name='clothes'
    template_name='fashionapp/Updateclothewomen.html'    

def updateClothewomen(request):
    if request.method=='POST':
        cid=request.POST['id']
        cname=request.POST['name']
        # gen=request.POST['gender']
        cat=request.POST['category']
        sz=request.POST['size']
        ma=request.POST['material']
        pr=request.POST['price']
        desc=request.POST['description']
        img=request.POST['Clothe_image']
        ce=ClotheWomen.objects.filter(id=cid)
        ce.update(id=cid,name=cname,category=cat,size=sz,material=ma,price=pr,description=desc,Clothe_image=img)
        return redirect("clothelistwomen")
    else:
        return render(request,'updateclothewomen.html')

def deleteclothewomen(request,id):
    data=ClotheWomen.objects.get(id=id)        
    data.delete()
    return redirect("clothelistwomen")






class ClothecreateViewchild(CreateView):
    model=Clothechild
    fields=['name','category','size','material','price','description','Clothe_image']    
    success_url='/success/'

class ClotheListViewchild(ListView):
    model=Clothechild
    context_object_name='clothes'
    template_name='fashionapp/clothechild_list.html'     

class ClothedetailsViewchild(DetailView):
    model=Clothechild
    context_object_name='clothes'
    template_name='fashionapp/updateclothechild.html'


class EditClothechild(DetailView):
    model=Clothechild
    context_object_name='clothes'
    template_name='fashionapp/Updateclothechild.html'    

def updateClothechild(request):
    if request.method=='POST':
        cid=request.POST['id']
        cname=request.POST['name']
        # gen=request.POST['gender']
        cat=request.POST['category']
        sz=request.POST['size']
        ma=request.POST['material']
        pr=request.POST['price']
        desc=request.POST['description']
        img=request.POST['Clothe_image']
        ce=Clothechild.objects.filter(id=cid)
        ce.update(id=cid,name=cname,category=cat,size=sz,material=ma,price=pr,description=desc,Clothe_image=img)
        return redirect("clothelistchild")
    else:
        return render(request,'updateclothechild.html')

def deleteclothechild(request,id):
    data=Clothechild.objects.get(id=id)        
    data.delete()
    return redirect("clothelistchild")






class MenAccessoriesCreateView(CreateView):
    model=MenAccessories
    context_object_name='accessories'
    fields=['name','category','size','material','price','description','Men_Accessoriesimage']
    success_url='/success/'

class MenAccessoriesListView(ListView):
    model=MenAccessories
    context_object_name='accessories'
    template_name='fashionapp/MenAccessories_list.html'

class MenAccessoriesDetailView(DetailView):
    model=MenAccessories
    context_object_name='accessories'
    template_name='fashionapp/updateMenAccessories.html'


class EditMenAccessories(DetailView):
    model=MenAccessories
    context_object_name='accessories'
    template_name='fashionapp/UpdateMenAccessories.html' 

def updateMenaccessories(request):
    if request.method=='POST':
        aid=request.POST['id']
        aname=request.POST['name']
        # gen=request.POST['gender']
        cat=request.POST['category']
        sz=request.POST['size']
        ma=request.POST['material']
        pr=request.POST['price']
        desc=request.POST['description']
        img=request.POST['Men_Accessoriesimage']
        ce=MenAccessories.objects.filter(id=aid)
        ce.update(id=aid,name=aname,category=cat,size=sz,material=ma,price=pr,description=desc,Men_Accessoriesimage=img)
        return redirect("menaccessorieslist")
    else:
        return render(request,'UpdateMenAccessories.html')

def deleteMenAccessories(request,id):
    data=MenAccessories.objects.get(id=id)        
    data.delete()
    return redirect("MenAccessories_list")    





class WomenAccessoriesCreateView(CreateView):
    model=WomenAccessories
    context_object_name='accessories'
    fields=['name','category','size','material','price','description','Women_Accessoriesimage']
    success_url='/success/'

class WomenAccessoriesListView(ListView):
    model=WomenAccessories
    context_object_name='accessories'
    template_name='fashionapp/WomenAccessories_list.html'

class WomenAccessoriesDetailView(DetailView):
    model=WomenAccessories
    context_object_name='accessories'
    template_name='fashionapp/updateWomenAccessories.html'


class EditWomenAccessories(DetailView):
    model=WomenAccessories
    context_object_name='accessories'
    template_name='fashionapp/UpdateWomenAccessories.html' 

def updateWomenaccessories(request):
    if request.method=='POST':
        aid=request.POST['id']
        aname=request.POST['name']
        # gen=request.POST['gender']
        cat=request.POST['category']
        sz=request.POST['size']
        ma=request.POST['material']
        pr=request.POST['price']
        desc=request.POST['description']
        img=request.POST['Women_Accessoriesimage']
        ce=WomenAccessories.objects.filter(id=aid)
        ce.update(id=aid,name=aname,category=cat,size=sz,material=ma,price=pr,description=desc,Women_Accessoriesimage=img)
        return redirect("womenaccessorieslist")
    else:
        return render(request,'UpdateWomenAccessories.html')

def deleteWomenAccessories(request,id):
    data=WomenAccessories.objects.get(id=id)        
    data.delete()
    return redirect("WomenAccessories_list") 






class CompleteTemplate(TemplateView):
    template_name='fashionapp/Complete.html'

class CustomerCreateView(CreateView):
    model=Customer
    fields=['name','emailId','password','address','contactNo']
    success_url='/login/'

class CustomerListView(ListView):
    model=Customer
    context_object_name='customers'
    template_name='fashionapp/customerlist.html'

class CustomerDetailView(DetailView):
    model=Customer
    context_object_name='customers'
    template_name='fashionapp/updatecustomer.html'

class EditCustomer(DetailView):
    model=Customer
    context_object_name='customers'
    template_name='fashionapp/updatecustomer.html'

def updateCustmore(request):
    if request.method=='POST':
        cname=request.POST['name']
        email=request.POST['emailId']
        paswrd=request.POST['password']
        adrs=request.POST['address']
        contact=request.POST['contactNo']
        cust=Customer.objects.filter(emailId=email)
        cust.update(name=cname,emailId=email,password=paswrd,address=adrs,contactNo=contact)
        return redirect("/custlist/")
    else:
        return render(request,'updatecustomer.html')    

def deleteCustomer(request,emailId):
    data=Customer.objects.get(emailId=emailId)
    data.delete()
    return redirect("/custlist/")






# from django.shortcuts import render, redirect
# from .models import CartModel

def addCartForm(request, id):
    if request.method == 'GET':
        data = Clothe.objects.get(id=id)
        quantity = range(1, 101)  # Ensure the range is from 1 to 100
        return render(request, 'fashionapp/AddCart.html', {'clothe': data, 'quant': quantity})
    else:
        data = Clothe.objects.get(id=id)
        email = request.POST['emailId']
        cust = Customer.objects.get(emailId=email)
        quantity = int(request.POST['quantity'])  # Ensure quantity is an integer
        totalPrice = float(request.POST['totalPrice'])  # Ensure totalPrice is a float
        cart = CartModel.objects.create(cid=data, emailId=cust, quantity=quantity, totalPrice=totalPrice)
        cart.save()
        return redirect("/cartList/")
    
def deleteCartItem(request, id):
    cart = CartModel.objects.get(id=id)
    
    cart.delete()
    
    return redirect("/cartList/")  # Update with the correct URL name for the cart list view



def womenaddCartForm(request, id):    
    if request.method == 'GET':
        data = ClotheWomen.objects.get(id=id)
        quantity = range(1, 101)  # Ensure the range is from 1 to 100
        return render(request, 'fashionapp/AddCart.html', {'clothe': data, 'quant': quantity})
    else:
        data = ClotheWomen.objects.get(id=id)
        email = request.POST['emailId']
        cust = Customer.objects.get(emailId=email)
        quantity = int(request.POST['quantity'])  # Ensure quantity is an integer
        totalPrice = float(request.POST['totalPrice'])  # Ensure totalPrice is a float
        cart = CartModel.objects.create(cid=data, emailId=cust, quantity=quantity, totalPrice=totalPrice)
        cart.save()
        return redirect("/cartList/")



def childaddCartForm(request, id):    
    if request.method == 'GET':
        data = Clothechild.objects.get(id=id)
        quantity = range(1, 101)  # Ensure the range is from 1 to 100
        return render(request, 'fashionapp/AddCart.html', {'clothe': data, 'quant': quantity})
    else:
        data = Clothechild.objects.get(id=id)
        email = request.POST['emailId']
        cust = Customer.objects.get(emailId=email)
        quantity = int(request.POST['quantity'])  # Ensure quantity is an integer
        totalPrice = float(request.POST['totalPrice'])  # Ensure totalPrice is a float
        cart = CartModel.objects.create(cid=data, emailId=cust, quantity=quantity, totalPrice=totalPrice)
        cart.save()
        return redirect("/cartList/")    

def menaccessoriesaddCartForm(request, id):    
    if request.method == 'GET':
        data = MenAccessories.objects.get(id=id)
        quantity = range(1, 101)  # Ensure the range is from 1 to 100
        return render(request, 'fashionapp/AddCart.html', {'accessories': data, 'quant': quantity})
    else:
        data = MenAccessories.objects.get(id=id)
        email = request.POST['emailId']
        cust = Customer.objects.get(emailId=email)
        quantity = int(request.POST['quantity'])  # Ensure quantity is an integer
        totalPrice = float(request.POST['totalPrice'])  # Ensure totalPrice is a float
        cart = CartModel.objects.create(cid=data, emailId=cust, quantity=quantity, totalPrice=totalPrice)
        cart.save()
        return redirect("/clothelist//") 

def womenaccessoriesaddCartForm(request, id):    
    if request.method == 'GET':
        data = WomenAccessories.objects.get(id=id)
        quantity = range(1, 101)  # Ensure the range is from 1 to 100
        return render(request, 'fashionapp/AddCart.html', {'accessories': data, 'quant': quantity})
    else:
        data = WomenAccessories.objects.get(id=id)
        email = request.POST['emailId']
        cust = Customer.objects.get(emailId=email)
        quantity = int(request.POST['quantity'])  # Ensure quantity is an integer
        totalPrice = float(request.POST['totalPrice'])  # Ensure totalPrice is a float
        cart = CartModel.objects.create(cid=data, emailId=cust, quantity=quantity, totalPrice=totalPrice)
        cart.save()
        return redirect("/clothelist/") 




from django.shortcuts import render, redirect
from .models import CartModel

def showCart(request):
        # email="a@1234.gmail.com"
        email = request.session['username']
        data = CartModel.objects.filter(emailId=email)  # Ensure proper filtering
        return render(request, 'fashionapp/cartlist.html', {'cart': data})
      # Redirect to login if the user is not authenticated


from django.shortcuts import redirect
from .models import CartModel

def showOrderForm(request):
    if request.method == "POST":
        # Process order placement logic
        emailId = request.session['username']
        data = CartModel.objects.filter(emailId=emailId)
        totalbill = sum(item.totalPrice for item in data)

        # Assuming order placement logic is here
        # Example: Creating Orders instance and saving it
        # Redirect to payment success page
        return redirect('paymentsuccess', data.id)  # Redirect to payment success page

        # Empty the cart after successful order placement
        data.delete()  # This deletes all items in the cart for the user
    else:
        return render(request, 'fashionapp/Order.html')



# def placeorder(request):
#     if request.method == 'POST':
#         email = request.session['username']
#         cart_items = CartModel.objects.filter(emailId=email)

#         if cart_items.exists():
#             for item in cart_items:
#                 # Here you can add your logic to create an order
#                 Orders.objects.create(
#                     emailId=item.emailId,
#                     cid=item.cid,
#                     quantity=item.quantity,
#                     totalPrice=item.totalPrice
#                 )
            
#             # Clear the cart
#             cart_items.delete()

#             messages.success(request, "Order placed successfully and cart is cleared!")
#             return redirect('cartList')  # Redirect back to the cart list or any other page
#         else:
#             messages.error(request, "No items in cart to place an order.")
#             return redirect('cartList')
#     else:
#         return redirect('cartList')



def Login(request):
    if request.method=='POST':
        emailId=request.POST['email']
        type=request.POST['type']
        if type=='user':
            cust=Customer.objects.filter(emailId=emailId)
            if cust:
                print("hello")
                custobj=Customer.objects.get(emailId=emailId)
                password=request.POST['password']
                if password==custobj.password:
                    request.session['username']=emailId
                    return redirect('index')
                else:
                    return HttpResponse("<h1>Wrong</h1>")
        if type=='admin':
            admin=AdminModel.objects.filter(adminEmailId=emailId)
            if admin:
                print("hello")
                adminobj=AdminModel.objects.get(adminEmailId=emailId)
                password=request.POST['password']
                if password==adminobj.adminpassword:
                    request.session['adminEmailId']=emailId
                    return redirect('index')
            else:
                return HttpResponse("<h1>Wrong</h1>")
       
    else:
        return render(request,'fashionapp/Login.html')
    

def logout(request):
    session_keys=list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return render(request,'fashionapp/index.html')


class IndexTemplate(TemplateView):
    template_name="fashionapp/index.html"

class aboutTemplate(TemplateView):
    template_name="fashionapp/about.html"

class contactTemplate(TemplateView):
    template_name="fashionapp/contactpage.html"    

class footerTemplate(TemplateView):
    template_name="fashionapp/Footer.html"

# def logout_view(request):
#     logout(request)
#     return redirect('index')


def emailDemo(request):
    subject="Subject here."
    email_body="Here is the message."
    from_email=settings.EMAIL_HOST_USER
    fail_silently=False
    send_mail(subject=subject,message=email_body,from_email=from_email,recipient_list=['microsoftwindows119@gmail.com'])
    return HttpResponse("email Successful")

def paymentsucess(request,tid,orderid):
    emailId=request.session["username"]
    data1=Orders.objects.get(ordernumber=orderid)
    payment=Payment.objects.create(emailId=emailId,amount_paid=data1.totalbillamount,payment_id=tid,status='completed')
    payment.save()
    subject="Thank You For Your Order"
    email_body="email:"+emailId +"tid :"+tid +"id: "+orderid+"message: order get placed"

    from_mail=settings.EMAIL_HOST_USER

    send_mail(subject=subject, message=email_body, from_email=from_mail, recipient_list=['microsoftwindows119@gmail.com'])
    return HttpResponse("<h1>Payment Sucessful</h1>")        


'''def placeOrder(request):
    if request.method=="POST":
        email=request.session['username']
        Data=Customer.objects.get(Email=email)
        data=CartModel.objects.filter(Customerfk=Data)
        totalbill=0
        for i in data:
            totalbill=totalbill+i.totalPrice
        Name=request.POST['name']
        Add=request.POST['address']
        City=request.POST['City']
        State=request.POST['State']
        Pin=request.POST['Pin']
        Phone=request.POST['phone']

        data=Orders.objects.create(EmailId=email,Name=Name,Address=Add,City=City,State=State,Pincode=Pin,PhoneNum=Phone,TotalBill=totalbill,OrderNumber=1)
        data.save()

        Today=date.today()
        today=str(Today).replace('-','')
        OrderId=str(data.id)+today
        data.ordernumber=OrderId
        data.save()
        data=Orders.objects.get(EmailId=email,OrderNumber=OrderId)'''

'''def placeOrder(request):
    if request.method=="POST":
        email=request.session['username']
        Data=Customer.objects.get(Email=email)
        data=CartModel.objects.filter(Customerfk=Data)
        totalbill=0
        for i in data:
            totalbill=totalbill+i.totalPrice
        name=request.POST['name']
        add=request.POST['address']
        city=request.POST['city']
        st=request.POST['state']
        pin=request.POST['pincode']
        pno=request.POST['phoneno']
        data=Orders.objects.create(emailId=email,name=name,address=add,city=city,state=st,pincode=pin,phoneno=pno)
        data.save()
        dateobj=date.today()
        dateobj=str(dateobj).replace('-','')
        datedata=str(data.orderId)+dateobj
        data.ordernumber=datedata
        data.save()
        data=Orders.objects.get(emailId=email,ordernumber=datedata)
        total=data.totalbillamount


        razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    
        currency = 'INR'
        amount = 20000  # Rs. 200
    
        # Create a Razorpay Order
        razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                        currency=currency,
                                                        payment_capture='0'))
    
        # order id of newly created order.
        razorpay_order_id = razorpay_order['id']
    
        # we need to pass these details to frontend.
        context = {}
        context['razorpay_order_id'] = razorpay_order_id
        context['razorpay_merchant_key'] = settings.RAZORPAY_KEY_ID
        context['razorpay_amount'] = amount
        context['currency'] = currency

        return render(request,'fashionapp/payment.html',{'orderobj':data,'totalbill':totalbill,'context':context})
        #return HttpResponse("Order Placed Successfully")
    else:
        return render(request,"fashionapp/Order.html")'''
    
#PayPal function ..................
def showOrderForm(request):
    if request.method=="POST":
        emailId=request.session['username']
        data=CartModel.objects.filter(emailId=emailId)
        totalbill=0
        for i in data:
            totalbill=totalbill+i.totalPrice
        name=request.POST['name']
        add=request.POST['address']
        city=request.POST['city']
        st=request.POST['state']
        pin=request.POST['pincode']
        pno=request.POST['phoneno']
        data=Orders.objects.create(emailId=emailId,name=name,address=add,city=city,state=st,pincode=pin,phoneno=pno)
        data.save()
        dateobj=date.today()
        dateobj=str(dateobj).replace('-','')
        datedata=str(data.orderId)+dateobj
        data.ordernumber=datedata
        data.save()
        data=Orders.objects.get(emailId=emailId,ordernumber=datedata)
        total=data.totalbillamount
        return render(request,'fashionapp/Payment_page.html',{'order':data,'total':totalbill})
    else:
        return render(request,'fashionapp/Order.html')

#Edit from here..........

'''def showOrderForm(request):
    if request.method=="POST":
        emailId=request.session['username']
        data=CartModel.objects.filter(emailId=emailId)
        totalbill=0
        for i in data:
            totalbill=totalbill+i.totalPrice
        name=request.POST['name']
        add=request.POST['address']
        city=request.POST['city']
        st=request.POST['state']
        pin=request.POST['pincode']
        pno=request.POST['phoneno']
        data=Orders.objects.create(emailId=emailId,name=name,address=add,city=city,state=st,pincode=pin,phoneno=pno)
        data.save()
        dateobj=date.today()
        dateobj=str(dateobj).replace('-','')
        datedata=str(data.orderId)+dateobj
        data.ordernumber=datedata
        data.save()
        data=Orders.objects.get(emailId=emailId,ordernumber=datedata)
        total=data.totalbillamount

        razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    

        currency = 'INR'
        amount = 20000  # Rs. 200
    
        # Create a Razorpay Order
        razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                        currency=currency,
                                                        payment_capture='0'))
    
        # order id of newly created order.
        razorpay_order_id = razorpay_order['id']
    
        # we need to pass these details to frontend.
        context = {}
        context['razorpay_order_id'] = razorpay_order_id
        context['razorpay_merchant_key'] = settings.RAZORPAY_KEY_ID
        context['razorpay_amount'] = amount
        context['currency'] = currency

        return render(request,'fashionapp/Payment_page.html',{'orderobj':data,'totalbill':totalbill,'context':context})
    else:
        return render(request,'fashionapp/Order.html')
'''



razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))


def initiate_payment(request):
    amount = 50000  # Amount in paise (₹500.00)
    currency = "INR"
    receipt = "order_rcptid_11"
    
    razorpay_order = razorpay_client.order.create({
        "amount": amount,
        "currency": currency,
        "receipt": receipt,
        "payment_capture": 1  # Auto-capture
    })
    
    context = {
        "razorpay_key_id": settings.RAZORPAY_KEY_ID,
        "order_id": razorpay_order["id"],
        "amount": amount,
    }
    return render(request, "fashionapp/payment_1.html", context)




def verify_payment(request):
    if request.method == "POST":
        try:
            # Retrieve payment details
            payment_id = request.POST.get("razorpay_payment_id")
            order_id = request.POST.get("razorpay_order_id")
            signature = request.POST.get("razorpay_signature")
            
            # Verify signature
            generated_signature = hmac.new(
                settings.RAZORPAY_KEY_SECRET.encode(),
                f"{order_id}|{payment_id}".encode(),
                hashlib.sha256
            ).hexdigest()
            
            if generated_signature == signature:
                return JsonResponse({"status": "success"})
            else:
                return JsonResponse({"status": "failure", "reason": "signature mismatch"})
        except Exception as e:
            return JsonResponse({"status": "failure", "reason": str(e)})
        


def Footer(request):
    return render(request, "fashionapp/Footer.html")