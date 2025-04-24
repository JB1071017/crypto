from django.urls import path
from . import views

urlpatterns = [
    path('', views.show, name='index'),
    path('index/', views.show, name='index'),
    path('about/', views.show1,name='about'),
    path('service/', views.show2,name='service'),
    path('team/', views.show3,name='team'),  
    path('why/', views.show4,name='why'),  
    path('register/',views.reg,name='register'),
    path('login/',views.login,name='login'),
    path('profile/',views.profile,name='profile'),
    path('edit/',views.edit,name='edit'),
    path('logout/',views.logout,name='logout'),
    path('userview/',views.userview,name='userview'),
    path('feedback/',views.feedback,name='feedback'),
    
   
    
    #ADMIN PANEL
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('admindash/',views.admin,name='admindash'),
    path('users/',views.userslist,name='users'),
    path('delete_user/<int:id>/',views.delete_user,name='delete_user'),
    path('approve_user/<int:id>/',views.approve_user,name='approve_user'),
    path('products/',views.product_view,name='products'),
    path('product_list/',views.productlist,name='product_list'),
    path('adminfeed/',views.adminfeed,name='adminfeed'),
    path('logoutadmin/',views.logoutadmin,name='logoutadmin'),

    #PRODUCTS
    path('addcart/<int:pid>/',views.addcart,name='addcart'),
    path('viewcart/',views.viewcart,name='viewcart'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    # path('remove_product/<int:product_id>/',views.remove_product,name='remove_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('edit_product/<int:id>/', views.edit_product, name='edit_product'),
    
    #payement
   path('initiate-payment/<int:cid>/', views.initiate_payment, name='initiate_payment'),
   path('confirm-payment/<str:order_id>/<str:payment_id>/<int:crti_id>/', views.confirm_payment, name='confirm_payment'),
   path('payment-successful/<int:transaction_id>/', views.payment_successful, name='payment_successful'),
   path('invoice/<int:transaction_id>/', views.generate_invoice, name='generate_invoice'),


    #OTP
    path('send-otp/', views.send_otp, name='send_otp'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),

    path('services/',views.services,name='services'),
    path('services_view/',views.service_list,name='services_view'),
    path('services/',views.existingservices,name='services'),

]
 


