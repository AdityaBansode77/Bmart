from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order, OrderUpdate
from math import ceil
import json

# Create your views here.
def index(request):
    products = Product.objects.all()
    allProds=[]
    catprods= Product.objects.values('category', 'id')
    cats= {item["category"] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params= {'allProds':allProds}
    return render(request, 'mart/index.html', params)

def about(request):
    return render(request, 'mart/about.html')

def contact(request):
    thank=False
    if request.method=="POST":
            name=request.POST.get('name', '')
            email=request.POST.get('email', '')
            phone=request.POST.get('phone', '')
            desc=request.POST.get('desc', '')
            contact = Contact(name=name, email=email, phone=phone, desc=desc)
            contact.save()
            thank=True
    return render(request, 'mart/contact.html',{'thank':thank})

def tracker(request):
    return render(request, 'mart/tracker.html')

def search(request):
    return render(request, 'mart/search.html')

def products(request, myid):
    product=Product.objects.filter(id=myid)
    return render(request, 'mart/prodView.html', {'product1':product[0]})

def checkout(request):
    if request.method=="POST":
        items_json= request.POST.get('itemsJson', '')
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        address=request.POST.get('add1', '') + " " + request.POST.get('add2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone', '')
        district=request.POST.get('district','')

        orders = Order(items_json= items_json, name=name,phone=phone, email=email, address= address, state=state, district=district, city=city, zip_code=zip_code)
        orders.save()
        update= OrderUpdate(order_id= orders.order_id, update_desc="The order has been placed")
        update.save()
        thank=True
        id=orders.order_id
        return render(request, 'mart/checkout.html', {'thank':thank, 'id':id})
    return render(request, 'mart/checkout.html')

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates,order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'mart/tracker.html')
