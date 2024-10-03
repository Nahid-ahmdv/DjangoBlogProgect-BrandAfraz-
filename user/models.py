from django.db import models #This imports Django's ORM (Object-Relational Mapping) models module, which is used to define database models.
from django.contrib.auth.models import AbstractUser,BaseUserManager #This imports the AbstractUser class and the BaseUserManager class from Django's authentication framework. AbstractUser is used to create a custom user model, while BaseUserManager provides methods for managing users.



class UserManager(BaseUserManager):  #this class defines a custom user manager for a Django application (in this case user application ). This custom manager is responsible for creating user instances with specific fields and validation checks (you can customize how users are created in your application).

    def create_user(self, email, first_name, password=None, **extra_fields):  #This method is defined to create a new user instance. It takes several parameters:1)email: The email address of the user (required).2) first_name: The first name of the user (required). 3)password: The password for the user account (optional).4)**extra_fields: Allows additional keyword arguments to be passed in, which can be used to set other fields on the user model.

        if not email:  #Validation Checks
            raise ValueError('Email field is required')
        if not first_name:  #Validation Checks
            raise ValueError('First name is required.')
        email = self.normalize_email(email)   #This line normalizes the email address (e.g., converting it to lowercase) to ensure consistency in how email addresses are stored.
        user = self.model(email=email, first_name=first_name, **extra_fields) #This creates an instance of the user model using the provided fields (email, first_name, and any additional fields in extra_fields). The method self.model refers to the model associated with this manager (which would typically be your custom user model).
        user.set_password(password)  #This method hashes the provided password before storing it in the database. It ensures that plain-text passwords are not saved directly, enhancing security.
        user.save() #This saves the newly created user instance to the database.

        return user

    def create_superuser(self, email, first_name, password=None, **extra_fields):  #The method is defined as create_superuser(self, email, first_name, password=None, **extra_fields). It takes several parameters: email: The email address of the superuser (required). first_name: The first name of the superuser (required). password: The password for the superuser account (optional).**extra_fields: Additional keyword arguments that can be used to set other fields on the user model.
        extra_fields.setdefault('is_staff', True)   #The 'setdefault' method is used to ensure that the is_staff and is_superuser fields are set to True by default.This means that when creating a superuser, these fields will automatically be marked as True, granting the user staff and superuser privileges.
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:  #These lines check whether the 'is_staff' and 'is_superuser' fields are indeed set to True.If either field is not set to True, a ValueError is raised with an appropriate message. This ensures that any superuser created must have both flags enabled.
            raise ValueError('super user should has is_staff True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('super user should has is_superuser True')

        return self.create_user(email, first_name, password, **extra_fields) #After performing the necessary checks and setting defaults, this line calls the previously defined 'create_user' method. It passes along the required parameters (email, first_name, and password) along with any additional fields specified in extra_fields. This method handles creating the actual user instance in the database.
        #is_staff # به یوزر اجازه میده وارد پلن ادمین بشه  #Allows login to the admin site
        #is_superuser   #تمام دسترسی‌ها رو میده به یوزر و حالا دسترسی‌ها چیاس؟ خوندن نوشتن تغییر دادن و پاک کردن

'''
In summary, the above code snippet defines a custom user manager ('UserManager') for creating users in user application:
It validates that essential fields ('email' and 'first_name') are provided.
It normalizes the email address.
It creates a new user instance with hashed passwords for security.
Finally, it saves the user to the database and returns the created user instance.
This approach allows you to customize how users are created while ensuring that necessary validations are enforced and security best practices are followed.
'''
'''
Validation Location:
In the 'UserManager', the validation is performed within the 'create_user' method, which is used to create users programmatically.
In the 'User' model, the validation is defined using the 'REQUIRED_FIELDS' attribute, which is specific to the 'createsuperuser' command.
Validation Scope:
The validation in 'UserManager' applies to all user creation scenarios where the 'create_user' method is used.
The validation in 'REQUIRED_FIELDS' is limited to the 'createsuperuser' command and does not enforce field requirements in other contexts, such as forms or admin interfaces.
Summary
In summary, the validation in 'UserManager' is performed at the manager level and applies to all user creation scenarios, ensuring that essential fields are provided. On the other hand, the validation using 'REQUIRED_FIELDS' in the 'User' model is specific to the 'createsuperuser' command and does not automatically enforce field requirements in other contexts. The choice between these approaches depends on the specific requirements and use cases of your application.
پس ولیدیشن یوزر عادی مون در کلاس یوزرمنیجر و متد کریت یوزر انجام میشه هوتن میگه اون ولیدیشنی که توی مدل یوزرمون نوشتیم با اسم ریکوآیرد فیلدز برای ادمین (سوپریوزر) مونه ولی اینی که توی کلاس بالا نوشتیم برای یوزر عادی هاست یعنی اینستنس‌های مدل یوزرمون

'''
'''
Regular users, Staff users, 
In summary:
Regular users are created through the custom 'create_user' method and have no special permissions.
Staff users can access the admin but have no other special permissions.
Superusers are created through 'create_superuser', have all permissions, and can access and perform any action in the admin.
The 'User' model is customized to use 'email' as the unique identifier and require 'first_name' and 'last_name' when creating superusers.
The key difference between the 'create_user' and 'create_superuser' methods is that 'create_superuser' sets the 'is_staff' and 'is_superuser' flags to True and performs additional validation checks. Regular users created through 'create_user' have neither of these flags set.
So, in summary, 'REQUIRED_FIELDS' is not necessary for regular users created through 'create_user', as the validation is handled within the method itself. It is only used for creating superusers via the 'createsuperuser' command to enforce additional field requirements.
'''














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

class User(AbstractUser): #The User class inherits from Django's AbstractUser, which means it includes all the fields and methods of the default user model (like username, first_name, last_name, etc.) while allowing for customization.    #The 'User' model is defined as a subclass of 'django.contrib.auth.models.AbstractUser'. 'AbstractUser' is a base user model provided by Django that includes a set of default fields and methods for user authentication. 'AbstractUser' is a base class provided by Django that you can subclass to create a custom user model. AbstractUser:This is an abstract base class that includes fields and methods for a fully featured user model, including fields like username, password, email, first_name, last_name, and others. It allows developers to extend or modify the default user model while retaining its functionality. Built-in 'User' Model: The built-in 'User' model in Django is actually defined as a subclass of AbstractUser. It provides a concrete implementation of the user model with default fields and behaviors.Custom User Models: When creating a custom user model, you can either subclass 'AbstractUser' (to retain most of its features) or subclass 'AbstractBaseUser' (for more customization but requiring more work). In summary, while the built-in 'User' model is based on 'AbstractUser', they are not the same. The built-in model is what you typically interact with when using Django's authentication system, whereas 'AbstractUser' serves as a foundation for creating custom user models.
    email = models.EmailField(unique=True)    #The 'email' field is defined as a unique email field using 'models.EmailField(unique=True)'. 'unique=True' enforces that each email address must be unique across all instances of this model, meaning no two users can have the same email address.
    birthday = models.DateField(null=True, blank=True)   #This line adds a birthday field that can store a date. The parameters 'null=True' and 'blank=True' indicate that this field is optional; it can be left empty in forms and can also be stored as 'NULL' in the database.
    USERNAME_FIELD = 'email'     #The 'USERNAME_FIELD' is a special attribute defined in the 'User' model that specifies which field should be used as the unique identifier for authentication purposes. By setting USERNAME_FIELD = 'email', you are telling Django to use the email field instead of the default 'username' field for authentication.
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']#This list specifies additional fields that are required when creating a superuser via the command line (using the createsuperuser command). In this case, when creating a superuser, both first_name, last_name, and username must be provided in addition to the email and password. #Requires 'first_name' and 'last_name' to be provided when creating a superuser via the 'createsuperuser' command. #مختص ادمین است  #The'REQUIRED_FIELDS' attribute is used to define additional fields that should be prompted for when creating a user interactively, specifically through the createsuperuser management command. This allows you to specify which fields are necessary beyond the default username and password. When you write 'REQUIRED_FIELDS = ['first_name', 'last_name', 'username']' in your custom user model that inherits from AbstractUser(which is a class in Django provides a fully featured user model that includes several fields by default.), it means that you want to specify additional fields that should be required besides the default required fields (username and password) when creating a user through the command line management command 'createsuperuser'.The fields listed in 'REQUIRED_FIELDS' are required in addition to the default required fields (username and password). This means that when you run the command 'python manage.py createsuperuser', Django will prompt you for the 'username', 'password', 'first_name', and 'last_name', 'username'.
    # username = None   #چون یوزر هست ما خط بالا می‌نویسیمش تا ریکوایرد بشه ERD الان با این مقداردهی دستی که انجام دادیم دیگه فیلد یوزرنیم ریکوایرد نیست ولی توی    #Django's 'AbstractUser',The default required fields are 'username' and 'password', and they're mandatory unless you customize your user model to remove them.The 'password' field is always required but is not included in the 'REQUIRED_FIELDS'.
    objects = UserManager()  #Utilizing a custom user manager ('UserManager') to handle user creation logic.#This line assigns an instance of the custom user manager ('UserManager') to the objects attribute of the user model. The custom manager provides methods for creating regular users and superusers with specific validation logic.


    class Meta:                  #class Meta: is an inner class used to provide metadata to the model. ' db_table = "auth_user" ' specifies the name of the database table that will store this model's data. By default, Django would create a table named 'appname_user', but this line changes it to 'auth_user', which is commonly used for user-related tables in Django applications.
        db_table = "auth_user"   #user_user اسم اون تیبلی که در دیتابیس قراره ساخته بشه برای ذخیره دیتای مربوط به این مدل‌مان، را مشخص کردیم اگه این خط را نمینوشتیم اسم تیبل‌مان می‌شد




class Profile(models.Model):   #defines a Django model named 'Profile' that inherits from Django's base 'models.Model' class. This allows you to create a database table to store additional information about a user, beyond what is provided by Django's built-in User model.
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female")
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')  #اسم مدلی که قراره بهش فارن‌کی زده بشه، مدل یوزر هست که بالاتر تعریفش کردیم. کلا اگه بخواهید ریلیشن بزنید این سه تا آرگمان جز واجبات است
    image = models.ImageField(upload_to='profile_images/')    #فقط یک پارامتر باید بهش بدیم و اون پارامتر هم مربوط به اینه که در چه فولدری باید بره اون عکسه رو ذخیره کنه ما خود اون عکس رو که نمی‌تونیم اینجا سیو کنیم، آدرسش رو توی اون فولدر سیو می‌کنیم و موقعی که به کاربر می‌خواهیم اون عکس رو نمایش بدیم، یوآرال‌اش رو میایم برمی‌گردونیم
    bio = models.TextField()
    gender = models.CharField(max_length=1, choices = GENDER_CHOICES)
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