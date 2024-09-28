from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
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
    context = {'welcome_title': 'welcome to our blog'}
    return render(request, 'HomePage.html', context)