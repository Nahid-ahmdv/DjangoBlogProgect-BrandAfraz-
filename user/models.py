from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
'''
Default Models in Django
User Model:
The 'User' model is located in 'django.contrib.auth.models' and provides fields for user authentication, such as 'username', 'password', 'email', 'first_name'', last_name', and various permissions-related fields.
AbstractUser:
The 'AbstractUser' class serves as a base class for creating custom user models. It includes all the fields and methods of the default User model but allows developers to extend or modify it.
AbstractBaseUser:
This is another base class that provides the core implementation for user authentication but does not include any fields by default (other than password). It requires developers to define their own fields.
PermissionsMixin:
This mixin provides fields and methods related to user permissions, which can be included in custom user models.
'''

class User(AbstractUser):     #The 'User' model is defined as a subclass of 'django.contrib.auth.models.AbstractUser'. 'AbstractUser' is a base user model provided by Django that includes a set of default fields and methods for user authentication. 'AbstractUser' is a base class provided by Django that you can subclass to create a custom user model. AbstractUser:This is an abstract base class that includes fields and methods for a fully featured user model, including fields like username, password, email, first_name, last_name, and others. It allows developers to extend or modify the default user model while retaining its functionality. Built-in 'User' Model: The built-in 'User' model in Django is actually defined as a subclass of AbstractUser. It provides a concrete implementation of the user model with default fields and behaviors.Custom User Models: When creating a custom user model, you can either subclass 'AbstractUser' (to retain most of its features) or subclass 'AbstractBaseUser' (for more customization but requiring more work). In summary, while the built-in 'User' model is based on 'AbstractUser', they are not the same. The built-in model is what you typically interact with when using Django's authentication system, whereas 'AbstractUser' serves as a foundation for creating custom user models.
    email = models.EmailField(unique=True)    #The 'email' field is defined as a unique email field using 'models.EmailField(unique=True)'. 'unique=True' enforces that each email address must be unique across all instances of this model, meaning no two users can have the same email address.
    birthday = models.DateField(null=True, blank=True)
    USERNAME_FIELD = 'email'     #The USERNAME_FIELD is a special attribute defined in the User model that specifies which field should be used as the unique identifier for authentication purposes. By setting USERNAME_FIELD = 'email', you are telling Django to use the email field instead of the default 'username' field for authentication.
    REQUIRED_FIELDS = ['first_name', 'last_name']   #The'REQUIRED_FIELDS' attribute is used to define additional fields that should be prompted for when creating a user interactively, specifically through the createsuperuser management command. This allows you to specify which fields are necessary beyond the default username and password. When you write 'REQUIRED_FIELDS = ['first_name', 'last_name']' in your custom user model that inherits from AbstractUser(which is a class in Django provides a fully featured user model that includes several fields by default.), it means that you want to specify additional fields that should be required besides the default required fields (username and password) when creating a user through the command line management command 'createsuperuser'.The fields listed in 'REQUIRED_FIELDS' are required in addition to the default required fields (username and password). This means that when you run the command 'python manage.py createsuperuser', Django will prompt you for the 'username', 'password', 'first_name', and 'last_name'.
    
    class Meta:                  #class Meta: is an inner class used to provide metadata to the model. ' db_table = "auth_user" ' specifies the name of the database table that will store this model's data. By default, Django would create a table named 'appname_user', but this line changes it to 'auth_user', which is commonly used for user-related tables in Django applications.
        db_table = "auth_user"   #user_user اسم اون تیبلی که در دیتابیس قراره ساخته بشه برای ذخیره دیتای مربوط به این مدل‌مان، را مشخص کردیم اگه این خط را نمینوشتیم اسم تیبل‌مان می‌شد




class Profile(models.Model):   #defines a Django model named 'Profile' that inherits from Django's base 'models.Model' class. This allows you to create a database table to store additional information about a user, beyond what is provided by Django's built-in User model.
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')  #اسم مدلی که قراره بهش فارن‌کی زده بشه، مدل یوزر هست که بالاتر تعریفش کردیم. کلا اگه بخواهید ریلیشن بزنید این سه تا آرگمان جز واجبات است
    image = models.ImageField(upload_to='profile_images/')    #فقط یک پارامتر باید بهش بدیم و اون پارامتر هم مربوط به اینه که در چه فولدری باید بره اون عکسه رو ذخیره کنه ما خود اون عکس رو که نمی‌تونیم اینجا سیو کنیم، آدرسش رو توی اون فولدر سیو می‌کنیم و موقعی که به کاربر می‌خواهیم اون عکس رو نمایش بدیم، یوآرال‌اش رو میایم برمی‌گردونیم
    bio = models.TextField()
#ما الان اسم تیبلی که قراره در دیتابیس ساخته بشه برامون برای ذخیره دیتای مربوط به مدلمان را، مثل خط 23 نیامدیم تغییر بدهیم. پس تیبل ساخته شده در دیتابیس اسم دیفالتش را خواهد داشت
#'user_profile' که خب اینجا اسم اپ‌مون یوزر هست و اسم مدلمون هم پروفایل پس اسم تیبلمون میشه 'appname_user'اسم دیفالتش هم اینجوریه
#
'''
'ForeignKey' Field: (one-to-many relation)
user = models.ForeignKey(User, on_delete=models.CASCADE) defines a field named user in the Profile model.
The 'ForeignKey' field creates a many-to-one relationship between the 'Profile' model and the 'User' model. This means that each profile can be associated with one user, but a user can have multiple profiles (if you were to allow that). 

'OneToOneField' Field:
user = models.OneToOneField(User, on_delete=models.CASCADE)
you establish a one-to-one relationship between the Profile model and the User model. This means that each user can have only one profile, and each profile is linked to exactly one user.
Parameters Explained
User:
This specifies the model that the foreign key points to (in this case it would be User model that we've definded lately).Each instance of the Profile model will be linked to a specific user.
on_delete=models.CASCADE:
This parameter specifies the behavior to adopt when the referenced user is deleted.
CASCADE: If the user associated with a profile is deleted, then the corresponding profile will also be deleted automatically. This is useful for maintaining data integrity, ensuring that there are no orphaned profiles left in the database if their associated user is removed.
اگر هم دستور زیر را وارد کنیم، با حذف شدن یوزر مربوطه، پروفایل متناظرش پاک نمی‌شود بلکه نال میشود

user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
models.SET_NULL:
If the referenced user is deleted, set the user field in the profile to NULL. This requires that the field is nullable (null=True).
The choice of 'on_delete' behavior depends on how you want to manage related data when a user is deleted from your application.other appropriate options for 'on_delete':
models.PROTECT:  #در واقع نمی‌ذاره اون مدلی که ما داریم بهش فارن‌کی می‌زنیم، پاک بشه و پروتکشن‌ارور ریز می‌کنه
Prevent deletion of the referenced user if there are associated profiles. This raises a ProtectedError.
models.RESTRICT:
Similar to PROTECT, but it prevents deletion only if there are existing references.
models.SET_DEFAULT:
Set the field to its default value if the referenced user is deleted.
models.DO_NOTHING:
Do nothing when the referenced user is deleted. You must handle any necessary cleanup manually.
________________________________________________________________________________________________
related_name='profile': This optional parameter sets the name of the reverse relation from the 'User' model back to the Profile. By using 'related_name='profile'', you can access a user's profile instance using:
in python write:
user_instance.profile
Instead of the default behavior, which would use 'user_instance.profile_set'. This makes the code cleaner and more intuitive.
اگه بیشتر بخواهیم بگیم: ببینید الان من اگه از پروفایل بخواهم به یوزر دسترسی پیدا کنم، مینویسم related_name در رابطه با 
Profile.user
ولی برعکس، اگه از یوزر بخواهیم به پروفایل دسترسی پیدا کنیم به صورت دیفالت باید بنویسیم
user_instance.profile_set
ولی خب وقتی اون مقدار رو ست می‌کنیم به صورت بالا دیگه کار راحت می‌شه 
'''