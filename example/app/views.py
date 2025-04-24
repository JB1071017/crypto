from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
from django.contrib import messages
from .models import db, Feedback
from .import models
from .models import cart


# Create your views here.
def show(request):
    return render(request, 'index.html')
def show1(request):
    return render(request,'about.html')
def show2(request):
    return render(request,'service.html')
def show3(request):
    return render(request,'team.html')
def show4(request): 
    return render(request,'why.html')
def admin(request):
    return render(request,'admindash.html')



def reg(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        profileimg=request.FILES.get('profileimg')
        choices=request.POST.get('choices')
        gender=request.POST.get('gender')
        age=request.POST.get('age')
        cpwd=request.POST.get('cpwd')


        try:
            user=db.objects.get(email=email)
            alert="<script> alert('Email already exist'); window.location.href='/register/';</script>"
            return HttpResponse(alert)
        except:
            if password==cpwd:
                models.db(name=name,email=email,password=password,profileimg=profileimg,gender=gender,age=age).save()
                print(profileimg)
                return redirect('login')
            else:
                alert="<script> alert('Incorrect password'); window.location.href='/index/';</script>"
                return HttpResponse(alert)
    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        var=db.objects.filter(email=email,password=password)
        if var.exists():
            var2=var.first()
            if var2.approvalstatus==1:
                request.session['email']=email 
                print(email)
                return redirect('send_otp')
            else:
                alert="<script> alert('user not approved by admin'); window.location.href='/login/'; </script>"
                return HttpResponse(alert)
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('login')
    else:
        return render(request,'login.html')
        # try:
        #     user1=db.objects.get(email=email)
        #     request.session['email']=user1.email
        #     print(email)
        #     return redirect('about')
        # except:
        #     alert="<script> alert('Invalid email or password'); window.location.href='/index/';</script>"
        #     return HttpResponse(alert)
    # else:
    #     return render(request,'login.html')
def profile(request):
    email= request.session.get('email')
    if email:
        user1=db.objects.get(email=email)
        return render(request,'profile.html', {'user1':user1})
    else:
        return redirect('login')

def edit(request):
    email=request.session.get('email')
    user1=db.objects.get(email=email)
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        profileimg=request.FILES.get('profileimg')
        gender=request.POST.get('gender')
        age=request.POST.get('age')
        user1.name=name
        user1.email=email
        user1.password=password
        user1.gender=gender
        user1.age=age
        if profileimg:
            user1.profileimg=profileimg
        user1.save()
        alert="<script> alert('Profile updated successfully'); window.location.href='/profile/';</script>"
        return HttpResponse(alert)
    else:
        return render(request,'edit.html', {'user1':user1})
    
def logout(request):
    
    email=request.session.get('email')
    if email:
        request.session.flush()
        alert="<script> alert('Logged out successfully'); window.location.href='/login/';</script>"
        return HttpResponse(alert)
    else:
        return redirect('login')

def logoutadmin(request):
    
    email=request.session.get('email')
    if email:
        request.session.flush()
        alert="<script> alert('Logged out successfully'); window.location.href='/adminlogin/';</script>"
        return HttpResponse(alert)
    else:
        return redirect('adminlogin')
    

def adminlogin(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        e='admin@gmail.com'
        p='123456'
        if email==e:
            if password==p:
                request.session['email']=email
                print(email)
                return redirect('admindash')
        else:
            alert="<script> alert('Invalid email or password'); window.location.href='/index/';</script>"
            return HttpResponse(alert)
    else:
        return render(request,'adminlogin.html')
    
def userslist(request):
    users=db.objects.all()
    return render(request,'users.html',{'users':users})

def approve_user(request,id):
    try:
        user1=db.objects.get(id=id)
        if user1.approvalstatus:
            user1.approvalstatus=False
            user1.save()
            messages.success(request, f'User "{user1.name}" has been successfully disapproved.')
        else:
            user1.approvalstatus=True
            user1.save()
            messages.success(request, f'User "{user1.name}" has been successfully approved.')
        return redirect('users')
    except user1.DoesNotExist:
        messages.error(request, f'User not found')
        return redirect('users')
       
    
def delete_user(request,id):
    user1=db.objects.get(id=id)
    user1.delete()
    messages.success(request, f'User "{user1.name}" has been successfully deleted.')
    return redirect('users')

def product_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        price = request.POST.get('price')
        description = request.POST.get('description')
        category = request.POST.get('category')
        stock = request.POST.get('stock')
        discount = request.POST.get('discount')
        models.products.objects.create(
            name=name,
            image=image,
            price=price,
            description=description,
            category=category,
            stock=stock,
            discount=discount
        )
        return redirect('product_list')
    else:
        return render(request, 'products.html')

    
def productlist(request):
    products=models.products.objects.all()
    return render(request,'product_list.html',{'products':products})

def userview(request):
    prod=models.products.objects.all()
    return render(request,'userview.html',{'pro':prod})
def addcart(request, pid):
    if 'email' in request.session:
        email = request.session.get('email')
        user1 = db.objects.get(email=email)
        product = models.products.objects.get(id=pid)
        if request.method == 'POST':
            quantity = request.POST.get('quantity')
            if quantity is not None and quantity.isdigit():  
                quantity = int(quantity)
            
                total = product.price * quantity
                cart_item, created = models.cart.objects.get_or_create(
                    user=user1,
                    product=product,
                    defaults={'quantity': quantity, 'total': total}
                )
                if created:
                    return redirect('viewcart')
                else:
                    cart_item.quantity += quantity  # Add the new quantity to the existing quantity
                    cart_item.total = product.price * cart_item.quantity  # Recalculate total
                    cart_item.save()
                    return redirect('viewcart')
            else:
                error_message = "Please enter a valid quantity."
                return render(request, 'addcart.html', {'product': product, 'error_message': error_message})
        else:
            return render(request, 'addcart.html', {'product': product})
    else:
        return render(request, 'login.html')
from django.db.models import Sum
def viewcart(request):
    email = request.session.get('email')
    user1 = db.objects.get(email=email)
    cart_items = models.cart.objects.filter(user=user1)
    total = cart_items.aggregate(Sum('total'))['total__sum']
    return render(request, 'viewcart.html', {'cart_items': cart_items,'total':total})



def remove_from_cart(request, cart_item_id):
    if request.method == 'POST' and 'email' in request.session:
        try:
            cart_item = cart.objects.get(id=cart_item_id)
            cart_item.delete()
        except cart.DoesNotExist:
            pass
    return redirect('viewcart')


# def remove_product(request, product_id):
#     product = products.objects.get(id=product_id)
#     product.delete()
#     return render(request,'product_list') 

from django.contrib import messages
from .models import products

def delete_product(request, product_id):
    product =products.objects.get(id=product_id)
    product.delete()
    messages.success(request, 'Product has been deleted successfully.')
    return redirect('product_list') 

# #payment section

import razorpay
from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from . import models  # Adjust according to your actual app name
from decimal import Decimal

# Initiate payment
def initiate_payment(request, cid):
    email = request.session.get('email')
    print(f"Session email: {email}")  # Debug

    if email:
        try:
            product = models.cart.objects.get(id=cid)
            print(f"Product: {product}")  # Debug

            amount = int(product.total) * 100
            print(f"Amount (paise): {amount}")  # Debug

            client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
            payment_order = client.order.create({
                'amount': amount,
                'currency': 'INR',
                'payment_capture': '1'
            })
            print(f"Order created: {payment_order}")  # Debug

            order_id = payment_order['id']
            user = models.db.objects.get(email=email)
            return JsonResponse({
                'order_id': order_id,
                'amount': amount,
                'buyer': {
                    'id': user.id,
                    'name': user.name,
                    'email': user.email
                }
            })
        except models.cart.DoesNotExist:
            print("Cart item not found")  # Debug
            return JsonResponse({'error': 'Cart item not found'}, status=404)
        except models.db.DoesNotExist:
            print("User not found")  # Debug
            return JsonResponse({'error': 'User not found'}, status=404)
        except Exception as e:
            print(f"Error: {str(e)}")  # Debug
            return JsonResponse({'error': str(e)}, status=500)

    print("Email not found in session")  # Debug
    return redirect('login')



# Confirm payment after Razorpay completes the payment
@csrf_exempt
def confirm_payment(request,order_id, payment_id, crti_id):
    client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

    try:
        # Fetch payment details
        payment = client.payment.fetch(payment_id)
        if payment['order_id'] == order_id and payment['status'] == 'captured':
            pemail = payment.get('email')
            amount = payment.get('amount')
            # Ensure cart ID is being passed correctly
            
            # Validate amount in rupees
            amount_in_rupees = Decimal(amount) / Decimal(100)
            
            if pemail:
                # Fetch user and cart item details
                user = models.db.objects.get(email=pemail)
                cart_item = models.cart.objects.get(id=crti_id)
                product = cart_item.product  # Associated product

                # Create transaction record
                transaction = models.Transaction(
                    user=user,
                    products=product,
                    amount=amount_in_rupees,
                    quantity=cart_item.quantity,
                    order_id=order_id
                )
                transaction.save()

                product.stock -= cart_item.quantity  # Decrease stock by quantity purchased
                if product.stock < 0:
                    return JsonResponse({'status': 'failure', 'error': 'Not enough stock available'}, status=400)
                product.save()
                # Remove the cart item after payment
                cart_item.delete()

                # Redirect to product list
                return redirect('payment_successful', transaction_id=transaction.id)

            else:
                return JsonResponse({'status': 'failure', 'error': 'User email not found'})
        else:
            return JsonResponse({'status': 'failure', 'error': 'Payment not captured or order ID mismatch'})

    except Exception as e:
        print('Error:', str(e))
        return redirect('index')  # In case of an error, redirect to home

def edit_product(request, id):
    product = get_object_or_404(products, id=id)

    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.category = request.POST.get('category')
        product.description = request.POST.get('description')
        product.price = request.POST.get('price')
        product.stock = request.POST.get('stock')
        product.discount = request.POST.get('discount')
        if 'image' in request.FILES:
            product.image = request.FILES['image']
        product.save()
        return redirect('product_list')  # Replace with the name of your product list view

    return render(request, 'edit_product.html', {'product': product})

import random
import string
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse

# views.py
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
import string

# Function to generate OTP
def generate_otp(length=6):
    characters = string.digits  # Only digits for the OTP
    otp = ''.join(random.choice(characters) for i in range(length))
    return otp

# View to send OTP email
def send_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Get email from the form
        otp = generate_otp()  # Generate OTP

        # Store OTP and email in session for later verification
        request.session['otp'] = otp
        request.session['email'] = email

        # Send OTP email
        subject = 'Your OTP Code'
        message = f'Your OTP code is {otp}. Please enter this code to verify your email.'
        from_email = 'nefsal003@gmail.com'  # Your email address
        
        send_mail(subject, message, from_email, [email])  # Sending email with OTP

        return redirect('verify_otp')  # Redirect to OTP verification page

    return render(request, 'send_otp.html')  # Render OTP form template



    # views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse

# views.py
def verify_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')  # Get OTP entered by the user

        # Check if the entered OTP matches the one stored in the session
        if entered_otp == request.session.get('otp'):
            alert="<script> alert('OTP verified successfully'); window.location.href='/about/';</script>"
            return HttpResponse(alert)
        else:
            return HttpResponse('Invalid OTP. Please try again.')

    return render(request, 'verify_otp.html')  # Render OTP verification page



# views.py
from django.shortcuts import render, get_object_or_404
from .models import Transaction

def payment_successful(request, transaction_id):
    # Get the transaction details
    transaction = get_object_or_404(Transaction, id=transaction_id)
    
    # Render the payment successful page
    return render(request, 'payment_successful.html', {'transaction': transaction})


# views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from .models import Transaction, db, products

def generate_invoice(request, transaction_id):
    # Fetch the transaction by its ID
    transaction = get_object_or_404(Transaction, id=transaction_id)

    # Fetch associated user and product details
    user = transaction.user
    product = transaction.products

    # Create an HTTP response with the appropriate content-type header for PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="invoice_{transaction.order_id}.pdf"'

    # Create a PDF document
    doc = SimpleDocTemplate(response, pagesize=letter)

    # Invoice header
    elements = []
    header_data = [
        [f"Invoice for Order ID: {transaction.order_id}"],
        [f"Date: {transaction.created_at.strftime('%Y-%m-%d %H:%M:%S')}"],
        [f"Customer Name: {user.name}"],
        [f"Email: {user.email}"],
    ]
    for line in header_data:
        elements.append(Table([line], colWidths=[500]))

    elements.append(Table([[" "]]))  # Add empty row for spacing

    # Table data for product details
    table_data = [
        ["Product Name", "Quantity", "Price Per Item (₹)", "Total (₹)"],  # Header row
        [
            product.name,
            transaction.quantity,
            f"{product.price}",
            f"{transaction.amount}",
        ],  # Transaction details
    ]

    # Create table
    table = Table(table_data, colWidths=[150, 100, 150, 150])

    # Add table style
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header row background color
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header row text color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Align all cells to center
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Header row font
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Padding for header row
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Add grid lines
    ]))

    # Add the table to the PDF
    elements.append(table)

    # Add total amount
    total_table = Table(
        [[f"Total Amount: ₹{transaction.amount}"]],
        colWidths=[550]
    )
    total_table.setStyle(TableStyle([
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
    ]))
    elements.append(total_table)

    # Build the PDF
    doc.build(elements)

    return response

def feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        rating = request.POST.get('rating')

        # Save feedback to the database
        feedback = Feedback(name=name, email=email, message=message, rating=rating)
        feedback.save()

        return render(request, 'index')  # Redirect to home page after submitting feedbackout
    
    return render(request, 'feedback.html')

def adminfeed(request):
    feedbacks = Feedback.objects.all()
    if not feedbacks:
        messages.info(request, 'No feedbacks available.')
    return render(request, 'adminfeed.html', {'feedbacks': feedbacks})

def services(request):
    servi = models.services.objects.all()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        description = request.POST.get('description')
        models.services.objects.create(
            name=name,
            image=image,
            description=description
        )
        return redirect('services')  

    else:
        return render(request, 'services.html', {'serv': servi})  

def service_list(request):
    services = models.services.objects.all()
    return render(request, 'services_view.html', {'services': services})

def existingservices(request):
    servi = models.services.objects.all()
    return render(request, 'existingservices.html', {'serv': servi})





