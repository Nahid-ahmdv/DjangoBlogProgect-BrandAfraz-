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

#To serve static files during development, you need to modify your project's main 'urls.py' file:
#1)Import Required Modules:
#You need to import the necessary modules at the top of your urls.py file:

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

#2)Add Static File Serving Logic:
#After defining your URL patterns, add a condition to serve static files when in debug mode:
urlpatterns = [
    path('admin/', admin.site.urls),

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




