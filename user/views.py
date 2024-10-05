from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import UserRegisterForm
'''
A)'from django.shortcuts import render'
Purpose: This line imports the 'render' function from Django's 'shortcuts' module. The 'render' function is a convenient way to combine a template with a context dictionary and return an 'HttpResponse' object containing the rendered HTML.
Functionality:
. Combines Template and Context: The 'render()' function takes three main arguments:
  1)request: The HTTP request object that contains metadata about the request.
  2)template_name: The name of the template file to be rendered (e.g., 'myapp/index.html').
  3)context (optional): A dictionary of data that will be passed to the template, allowing dynamic content to be displayed.
Example Usage:
  def home(request):
    context = {'message': 'Hello, Django!'}
    return render(request, 'myapp/index.html', context)
In this example, when a user accesses the 'home' view, Django will render the 'index.html' template with the provided context, replacing any placeholders with actual data.



B)'from django.http import HttpResponse'
Purpose: This line imports the 'HttpResponse' class from Django's 'http' module. The 'HttpResponse' class is used to create HTTP responses in your views.  کاملتر: it is used to create an HTTP response object that can be returned to the client (e.g., a web browser). It allows you to send content back to the user, such as HTML, plain text, JSON, etc.
Functionality:
. Creating Responses: You can use 'HttpResponse' to return simple text or HTML content directly from your view without rendering a template.
Example Usage:
    def simple_view(request):
        return HttpResponse("Hello, World!")
In this case, when the 'simple_view' function is called, it returns an HTTP response containing the text "Hello, World!" directly to the client.

Summary
The line from 'django.shortcuts import render' allows you to use the 'render()' function for rendering templates with context data, which is essential for creating dynamic web pages in Django.
The line from 'django.http import HttpResponse' enables you to create and return simple HTTP responses directly from your views.
Both of these imports are fundamental for building views in Django, allowing you to serve both dynamic content (using templates) and static responses.
'''
# Create your views here.
@csrf_exempt
#است request همه ویوهای فانکشن‌بیسد یک پارامتر می‌گیرند که
def test_view(request):     #This line defines a function named 'test_view', which will serve as our view. The function takes one parameter, 'request', which is an instance of the 'HttpRequest' class. This parameter contains all the information about the incoming HTTP request.
    #return HttpResponse("Hello!")    #این فقط برای مثال بود
#when the 'test_view' function is called, it returns an HTTP response containing the text "Hello!" directly to the client.
# ها را ست کنیمurl هوتن بلافاصله گفت حالا که اینو نوشتیم (خط 36 و 37) بریم 
#ایی باشدurl در واقع الان نحوه دسترسی به این فانکشن باید از طریق ریکوئست زدن به یک
    if request.method == 'GET':   #Here, we check the HTTP method of the incoming request using 'request.method'. The method attribute indicates how the client made the request (e.g., GET, POST). In this case, we are checking if the method is 'GET', which is commonly used to retrieve data from a server.
        return HttpResponse("This is a GET request!")   ##If the request method is GET, this line creates an 'HttpResponse' object containing the string "This is a GET request!" and returns it to the client. When the client accesses this view with a GET request (e.g., by entering the URL in a web browser), they will see this message displayed on their screen.
    if request.method == 'POST':    #This line checks if the HTTP method of the incoming request is 'POST'. POST requests are typically used when submitting data to be processed by the server (e.g., form submissions).
        return HttpResponse("This is a POST request!")  ##If the method is POST, this line creates another 'HttpResponse' object containing "This is a POST request!" and returns it to the client. If a client submits data via a form that points to this view with a POST method, they will see this message in response.


def home_page(request):
    # context = {'welcome_title': 'welcome to our blog'}
    context = {
    'welcome_title': 'Welcome to our blog',
    'messages': messages.get_messages(request)}
    return render(request, 'HomePage.html', context)


def register_view(request):   #It is a Django view function named 'register_view', which handles user registration. This line defines a view function named 'register_view' that takes a single parameter, 'request'. The request object contains all the information about the current HTTP request.
    if request.method == 'POST':  #This checks if the request method is 'POST', which indicates that the user has submitted the registration form.
        form = UserRegisterForm(request.POST) #فرم را با اطلاعات سابمیت شده پر می‌کند  # An instance of 'UserRegisterForm' is created with the submitted data (request.POST). This form class is expected to handle user registration.
        if form.is_valid():        #This checks if the form data is valid according to the validation rules defined in the 'UserRegisterForm'. If valid, it proceeds to save the user.
            user = form.save()     #If the form is valid, this line saves the new user instance to the database and assigns it to the variable 'user'.
            login(request, user)   #This uses Django's built-in 'login' function to log in the newly registered user immediately after they are created. This means they will be authenticated and can access protected views without needing to log in again.
            messages.success(request, 'register successful') #A success message is added to Django's messaging framework, indicating that the registration was successful. This message can be displayed on the next page load.
            return redirect('home_page')#نوشتیم اینجا به کار میاد که صرفا اسم اون یوآل‌ال رو می‌نویسیم و ما چون هوم‌پیجمون آماده نبود به تست ریدایرکت کردیم ولی معمولا به هوم‌پیج ریدایرکت می‌کنن urls.py در فایل urlpatterns اون اسم‌هایی که برای یوآرال‌ها در #After successful registration and login, this line redirects the user to a view named 'test'. The string 'test' should correspond to a URL pattern defined in your Django project's URL configuration.

        else:  #If the form is not valid (i.e., there are errors), it prints out those errors to the console for debugging purposes. An error message is added to inform the user that registration failed and that they can see the errors (although you might want to display these errors on the front end).
            print(form.errors)
            messages.error(request, f'registeration failed you can see the errors.')
    else:  #If the request method is not 'POST' (i.e., it's a 'GET' request), a new instance of 'UserRegisterForm' is created with no data, which will be used to render an empty registration form.
        form = UserRegisterForm()
    context = {'form': form} #نوشتیم) این اطلاعات با تمپلیت مربوطه رندر می‌شه، پس اینا اطاعاتیه که داره سمت فرانت می‌ره templates این همون اطلاعاتیه که قراره بره سمت فرانت و اونجا با استفاده از جنگو تمپلیت (همون تمپلیتهایی که در فولدر  #This line passes the 'form' object to your template through the context dictionary in the register_view function. This creates a context dictionary where the key is 'form' and the value is the 'form' instance created from 'UserRegisterForm' class.  #A context dictionary is created containing the form instance. This context will be passed to the template for rendering.
    return render(request, "UserRegister.html", context)#داریم میگیم این فایله رو رندر کن و این اطلاعات داخل دیکشنری کانتکست هم براش بفرست #Finally, this line renders a template named "UserRegister.html" using Django's render function, passing in the request object and context containing the form.

'''
In summary, this 'register_view' function performs several key tasks:
It handles both 'POST' requests (when users submit their registration data) and 'GET' requests (when users first visit the registration page).
It validates and saves user data if valid, logs them in automatically, and provides feedback messages.
It manages errors by printing them for debugging and notifying users of any issues during registration.
It prepares a context for rendering a registration template with either an empty or populated form based on user input.
This view encapsulates a common pattern for handling user registrations in Django applications effectively.

'''
def logout_custom(request):
    logout(request)
    return redirect("home_page")