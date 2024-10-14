from django.shortcuts import render
from .models import Post
from django.urls import reverse_lazy    
# 'reverse_lazy()' is designed to defer URL resolution until the URL is actually needed. This is particularly useful in scenarios where the URL configuration might not be fully loaded at the time of evaluation, which is often the case with class attributes. 
# You might see 'reverse_lazy()' used in decorators or situations where you want to ensure that URL resolution does not occur until the function is executed. while 'reverse_lazy()' can be used in function-based views, its advantages are more relevant in class-based views where URL resolution timing can lead to errors if not handled properly. In most cases for FBVs, using 'reverse()' is straightforward and effective.
from django.views.generic import CreateView, ListView, UpdateView, DeleteView  #را انجام دهیم CRUD درون‌ساخت پایتون استفاده می‌کنیم، بعدی برای مشاهده لیستی از آبجکت‌ها است، بعدی برای آپدیت آبجکت‌ها است و آخری هم برای پاک کردن آبجکت است پس در واقع به کمک این 4 تا می‌تونیم عملیات CBV که یک CreatView برای ساخت آبجکت‌های جدید در دیتابیس، از این 
from .forms import PostForm
from django.contrib.auth.decorators import login_required
# from django import http
# Create your views here.
'''
The statement from 'django.views.generic' import 'CreateView', 'ListView', 'UpdateView', 'DeleteView' imports four class-based views from Django's generic views module. Each of these views serves a specific purpose in handling common web application tasks. Here’s a breakdown of each:
1. CreateView
Purpose: The 'CreateView' is used to handle the creation of new objects in the database.
Functionality: It provides a form for users to input data, validates that input, and saves the new object to the database.
Usage: Typically, you specify the model to create and the fields to include in the form. It automatically handles GET and POST requests.
2. ListView
Purpose: The 'ListView' is designed to display a list of objects from a specified model.
Functionality: It automatically retrieves all instances of a model and passes them to a template for rendering.
Usage: You can customize the queryset, pagination, and context variables.
3. UpdateView
Purpose: The 'UpdateView' is used for updating existing objects in the database.
Functionality: It displays a form pre-filled with the current data of the object and processes updates when submitted.
Usage: You specify which model to update and the fields to include in the form.
4. DeleteView
Purpose: The 'DeleteView' is used for deleting existing objects from the database.
Functionality: It prompts the user for confirmation before deleting an object.
Usage: You specify which model to delete and can customize the template used for confirmation.
'''






#@login_required  #urls.py و مستقیما اونجا اثرش بدیم مثل خط 7 در فایل urls.py ها نمیشه و برای اونا باید بریم توی فایلCBV ها میشه اینجوری دکوریتور گذاشت، ولی انگاری برایFBV برای
# Create your views here.
def post_list_view(request):
    # queryset = Post.objects.all()   #این می‌ره تمام پست‌هایی که در دیتابیس داریم را اطلاعاتشون را برای ما برمی‌گرداند و می‌ریزه توی اون کوئری‌ست‌ای که سمت چپ داریم
    ## objects_list = list(queryset)
    ## return render(request, 'posts.html' , {"objects_list" : objects_list})          
    # queryset = Post.objects.filter(category__title = 'bakery')

    ###queryset = Post.objects.filter(title = 'How to Build a Morning Routine That Sets You Up for Success')
    ###return render(request, 'posts.html', {"objects_list" : queryset})

    #####queryset = Post.objects.filter(category__parent_category__title = "cooking")
    #####return render(request, 'posts.html', {"objects_list" : queryset})

    ###### queryset = Post.objects.select_related('category').filter(category__parent_category__title = "cooking")
    ###### return render(request, 'posts.html', {"objects_list" : queryset})

    queryset = Post.objects.select_related('category').all()   #رو هم نذاریم اوکیه all() این
    return render(request, 'posts.html', {"objects_list" : queryset})


class PostListView(ListView): #a class-based view in Django for displaying a list of posts. This line defines a new class called 'PostListView' that inherits from Django's 'ListView', which is a generic view designed to display a list of objects.
    model = Post  #This specifies that the view will use the 'Post' model. Django will query this model to retrieve the objects (which are\that are) to be displayed (باید نمایش داده شوند).
    template_name = 'posts.html' #This indicates the template file that will be used to render the list of posts. In this case, it is 'posts.html'.
    context_object_name = 'posts'  #This sets the name of the context variable that will be passed to the template. Instead of using the default name (which would be 'object_list'), you can reference the list of posts in your template as 'posts'.
    paginate_by = 3  #This specifies that the list should be paginated, showing 3 posts per page. If there are more than 3 posts, Django will automatically provide pagination controls.


    # queryset = Post.objects.all()
    # objects_list = list(queryset)
    # output = []
    # for object in objects_list:
    #     if object.title == 'How to Build a Morning Routine That Sets You Up for Success':
    #         output.append(object)
    # return render(request, 'posts.html', {"objects_list" : output})


class PostCreateView(CreateView):  # we define a new class 'PostCreateView' that inherits from 'CreateView'. This means it will have all the functionality of a standard create view but can be customized further.
    model = Post  # This specifies that the view will be working with the 'Post' model, which represents the data structure for a blog post or similar entity.
    form_class = PostForm # This indicates that the view will use 'PostForm', a Django form class, to handle validation and rendering of the form fields for creating a new post.
    template_name = 'PostCreate.html'  # This line specifies the template that will be used to render the form. In this case, it's 'PostCreate.html', where users will input data for their new post.
    success_url = reverse_lazy('posts_list') #مون post.html و حالا می‌خواهیم بعد از اینکه کاربر پستش رو ساخت ری‌دایرکت بشه به همون posts_list اسم ویومون رو گذاشتیم urls.py در فایل  # After successfully creating a post, the user will be redirected to the URL defined by reverse_lazy('posts_list'). The reverse_lazy function is used to lazily resolve the URL, which is useful in class-based views.
    #Overriding form_valid Method:
    def form_valid(self, form):  # This method is called when the submitted form is valid. It allows you to customize what happens before redirecting to 'success_url'.
        obj = form.save(commit=False) # This saves the form data to an object named "form" but does not commit it to the database yet. This allows you to make additional modifications before saving.
        obj.author = self.request.user # Here, we set the 'author' field of the post object to the currently logged-in user (self.request.user). This associates the newly created post with its author.
        obj.save() #Now that we've set all necessary fields (including author), we save the object to the database.
        return super().form_valid(form) # Finally, we call the parent class's 'form_valid' method to handle any additional processing and perform the redirect.
    
    '''
    The last line 'return super().form_valid(form)' in the context of a Django class-based view is crucial for handling what happens after a form submission is successfully validated. Here's a detailed explanation:
    Breakdown of return super().form_valid(form)
    1. Calling the Parent Class Method
    super(): This function returns a temporary object of the superclass (the parent class) that allows you to call its methods. In this case, it refers to the parent class of 'PostCreateView', which is 'CreateView'.
    form_valid(form): This method is defined in the 'CreateView' class and is responsible for processing the form when it has been validated successfully.
    2. What Happens in 'form_valid'
    When you call 'super().form_valid(form)', you are executing the 'form_valid' method from the parent class (CreateView). This method performs several important tasks:
    Saves the Form Data: It saves the instance of the model associated with the form to the database.
    Sets the Current Object: It sets 'self.object' to the newly created instance, making it available for use in subsequent methods.
    Redirects to Success URL: It determines where to redirect the user after successful form submission, using the 'success_url' attribute defined in your view.
    3. Why Use super()?
    Using 'super()' helps maintain the functionality provided by Django's built-in views while allowing you to extend or customize behavior. In this case, it ensures that all standard processing (like saving data and redirecting) occurs after you've added your custom logic (e.g., setting the author).
    '''