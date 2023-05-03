from django.urls import path, include
from . import views
from django.shortcuts import redirect

app_name = 'users'

# [name='home']
# account/ account/login/ [name='login']
# account/ account/two_factor/setup/ [name='setup']
# account/ account/two_factor/qrcode/ [name='qr']
# account/ account/two_factor/setup/complete/ [name='setup_complete']
# account/ account/two_factor/backup/tokens/ [name='backup_tokens']
# account/ account/two_factor/backup/phone/register/ [name='phone_create']
# account/ account/two_factor/backup/phone/unregister/<int:pk>/ [name='phone_delete']
# account/ account/two_factor/ [name='profile']
# account/ account/two_factor/disable/ [name='disable']
# account/ default/ [name='home']

urlpatterns = [   
    path('login/', lambda request: redirect('two_factor:login')),
    path('register/', views.register, name='register'), 
    path('logout/', views.logout_user, name='logout'), 
]