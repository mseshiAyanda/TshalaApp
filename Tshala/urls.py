from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'Tshala'
urlpatterns = [
    path('', views.home, name='home'),
    
    
    path('aboutus/', views.aboutus, name='aboutus'),
    path('trending/', views.trending, name='trending'),
    path('registerbus/', views.registerbus, name='registerbus'),
    path('pitch/', views.pitch, name='pitch'),
    

    
    path('video/<str:tittle>/', views.getInfo, name='video'),
    path('more-info/<str:pk>/', views.info, name='more-info'),
    path('update/<str:pk>/', views.updateInfo, name='update'),
    


    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),


    path('simple-checkout/', views.simpleCheckout, name="simple-checkout"),
    path('checkout/<int:pk>/', views.checkout, name="checkout"),
    


    
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html", email_template_name = 'registration/password_reset_email.html'),
     name="reset_password"),

    path('reset_password_sent/', 
     auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"), 
     name="rese_password_done"),
     
    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
     auth_views.PasswordResetCompleteView.as_view(template_name="egistration/password_reset_done.html"), 
     name="password_reset_complete"),
]
