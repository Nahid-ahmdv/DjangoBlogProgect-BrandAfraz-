##ساختیم و نوشتیم core فولدر urls.py در path('user/', include('user.urls')) این صفحه را بلافاصله بعد از نوشتن
from django.urls import path
from .views import test_view
urlpatterns =[
    #path('register/', registerview, name='register')  #ما هنوز ویوی مربوط به رجیستر رو ننوشتیم برای همین فعلا کامنتش میکنیم
    path('test/', test_view, name='test')    #را test_view براش نمایش بده test/ نوشت user اگه کاربر مثلا اومد توی
]

'''
'path('register/', registerview, name='register')'

is a URL pattern definition in a Django application. Here's a breakdown of what each part means:
Breakdown of the Code
path(): This is a function provided by Django's 'django.urls' module that is used to define URL patterns. It maps a specific URL to a view function.
'register/': This is the URL pattern that users will visit in their web browser. When a user navigates to 'http://yourdomain.com/register/', this pattern will match.
registerview: This is the view function that will be called when the URL pattern is matched. It should be defined in your views file (usually views.py). The view function contains the logic for what happens when the user accesses this URL (e.g., rendering a registration form).
name='register': This is an optional argument that assigns a name to the URL pattern. Naming URLs is useful for reverse URL matching, allowing you to refer to this URL in your templates and views without hardcoding the URL string. For example, you can use '{% url 'register' %}' in templates to generate the URL for this path.
Summary
In summary, this line of code defines a route in your Django application that:
 .Matches requests to '/register/'
 .Calls the 'registerview' function when that URL is accessed
 .Allows you to refer to this URL pattern as 'register' throughout your application.
This setup is commonly used for user registration functionality in web applications.

##a 'view' refers to a Python function (or class) that takes an HTTP request and returns an HTTP response. Views are a core component of the Django framework and serve as the bridge between the web server and the user interface.
'''