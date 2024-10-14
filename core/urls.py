"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
#ابن نارنجی بالایی رو من ننوشتم پیش‌فرض خودش بود
#To serve static files during development, you need to modify your project's main 'urls.py' file:
#1)Import Required Modules:
#You need to import the necessary modules at the top of your urls.py file:

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from user.views import home_page

#2)Add Static File Serving Logic:
#After defining your URL patterns, add a condition to serve static files when in debug mode:
urlpatterns = [
    path('admin/', admin.site.urls), ##This line maps the URL path 'admin/' to the Django admin site. When a user visits 'http://yourdomain.com/admin/', Django will serve the admin interface, which is a built-in feature for managing your application's data and users.
    path('user/', include('user.urls')),#اش که الان رفتیم ساختیم در فولدر یوزر urls هم یعنی برو توی اپ (فولدر) یوزر قسمت فایل user.urls اون  #path رو هم رفتم اضافه کردم به قسمت ایمپورت‌ها بغل include اینجا اون 
    ##درباره خط بالایی ##This line uses the 'include()' function to include another set of URL patterns defined in the 'user' application’s 'urls.py' file. The 'include()' function allows you to reference another URL configuration module, which helps in organizing your URLs and keeping them modular. Here, any URL that starts with 'user/' will be routed to the URL patterns defined in 'user.urls'. For example, if you have a URL like 'http://yourdomain.com/user/profile/', Django will look for that path in the 'user/urls.py' file.
    ##How 'include()' Works: When Django encounters an 'include()' statement, it "chops off" the part of the URL that matches the specified path (in this case, 'user/') and sends the remaining part of the URL to the included URLconf (the 'user.urls' module) for further processing. For instance, if a request comes in for '/user/profile/', Django will match '/user/', remove that part, and then pass '/profile/' to the URL patterns defined in 'user/urls.py'.
    ##In summary, these two lines set up routing for your Django application:1)The first line connects the admin interface to the '/admin/' URL.2)The second line includes all URLs from the 'user' application's URL configuration under the '/user/' path, allowing for organized and modular URL management. This structure is beneficial for larger applications where different functionalities are separated into different apps.
    path('blog/', include('blog.urls')), #اضافه شده در جلسه هجدهم
    path('', home_page, name="home_page")
    # Include other app URLs here
]

#When 'DEBUG' is True, it indicates that the application is running in a development environment.
if settings.DEBUG:  #یک پارامتری داریم به دیباگ در خط 27 که وقتی ترو باشه باگ و اینا رو به نشون میده ولی موقع دیپلویمنت نمیخواهیم ترو باشد و این داره میگه تازمانی که ترو بود بیا دستور زیر رو انجام بده بیا استاتیک فایل و مدیا فایل رو خودت سرو کن  settings.py ما در فایل 
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #This line adds a URL pattern to serve static files during development. static() is a function provided by Django that generates the necessary URL patterns for serving static files. settings.STATIC_URL is the base URL for serving static files, as defined in your 'settings.py' file (e.g., /static/). 'document_root=settings.STATIC_ROOT' specifies the directory where the static files are located, as defined by the 'STATIC_ROOT' setting in 'settings.py'.
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#Summary
#By configuring both 'settings.py' and 'urls.py', you ensure that Django can properly serve static files during development (and deployment خودم اینو اضافه کردم):
#In 'settings.py': You define where Django should look for static files (STATICFILES_DIRS) and how they should be accessed (STATIC_URL).
#In 'urls.py': You set up routing so that requests for static files are handled correctly when the server is running in development mode.
#This setup allows you to manage and serve your static assets effectively while developing your Django application.




