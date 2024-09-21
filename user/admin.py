from django.contrib import admin
from .models import User         #The dot (.) signifies that you are importing from a module that is in the same package as the current module (in this case, admin.py). This means that models is a module located in the same directory as the admin.py file.
# Register your models here.


#this is a Django admin configuration for a custom user model.
@admin.register(User) ##This is a decorator that registers the 'User' model with the Django admin site. It tells Django to use the 'UserAdmin' class to manage how the 'User' model is displayed and interacted with in the admin interface. #یه دکوریتور هست که یه پارامتر ورودی می‌گیره
class UserAdmin(admin.ModelAdmin):  #This line defines a new class 'UserAdmin', which inherits from 'admin.ModelAdmin'. This class customizes the admin interface for the 'User' model. By subclassing 'ModelAdmin', you can override various attributes and methods to customize how your model appears and behaves in the admin.
    list_display = ['email', 'username', 'birthday'] #The list_display attribute specifies which fields should be displayed in the list view of the admin for this model. In this case, it will show the email, username, and birthday fields in the list of users.
    #fields = ['username', 'birthday'] #چه فیلدهایی رو موقع ادیت‌کردن حق داری عوض کنی # If uncommented, this would define which fields are displayed in the detail view when editing a user.
    # exclude = ['username', 'birthday'] #بیشتر برای پسورد بکار میاد#If uncommented, this would specify which fields should be excluded from the detail view when editing a user.
    ordering = ['birthday'] #The 'ordering' attribute specifies the default ordering of records in the admin list view. In this case, users will be ordered by their birthday.
    search_fields = ['email', 'username'] #The search_fields attribute allows you to specify which fields should be searchable in the admin interface.Here, it enables searching by both email and username, allowing admins to quickly find users based on these attributes.

    '''
    Summary
In summary, this code snippet configures how the custom 'User' model is managed within the Django admin interface:
It registers the 'User' model to be managed by a custom admin class (UserAdmin) that specifies how users are displayed and interacted with.
The configuration includes display settings, ordering, and search capabilities, enhancing usability for administrators managing user accounts.
This setup is crucial for effectively managing user data within a Django application’s administrative backend.


In summary, http://127.0.0.1:8000 is the address used to access a Django application running locally on your computer via the development server. It allows developers to test their applications in a controlled environment before deploying them to a production server.
    '''