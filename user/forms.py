from django import forms  
from .models import User    #وقتی کنار ماژولی دات می‌گذاریم منظورمون ماژولی به همین اسم در همین فولدر جاری است تا جنگو نره توی فولدر دیگه‌ای دنبالش بگرده
from django.contrib.auth.forms import UserCreationForm  #it refers to importing the 'UserCreationForm' class from Django's authentication framework. This class is specifically designed for creating new user accounts in a Django application.

class UserRegisterForm(UserCreationForm):  #The 'UserCreationForm' is a built-in form provided by Django that simplifies the process of user registration. It includes fields for a username and password, as well as validation logic to ensure that the data entered meets certain criteria (e.g., checking if the username already exists).
    birthday = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})) #مربوطه را فراخوانی کنیم و تایپش را دیت بگذاریم widget داره که برای استفاده ازش باید date picker یدونه html خود 
    '''
    Breakdown of the Code:
    birthday = forms.DateField(...):
    This defines a form field named 'birthday' that uses Django's 'DateField'. This type of field is specifically designed to handle date inputs, ensuring that the data entered is validated as a date.
    widget=forms.DateInput(...):
    The widget parameter allows you to specify which HTML widget should be used to render the form field. Here, it uses 'forms.DateInput', which renders an <input> element of type "date". This provides a date picker in modern web browsers, allowing users to select a date from a calendar interface.
    attrs={'class': 'form-control', 'type': 'date'}:
    The attrs dictionary is used to set HTML attributes for the widget. In this case:
    'class': 'form-control': This applies Bootstrap's '.form-control' class to the input field, ensuring it has consistent styling (like padding, width, etc.) across different browsers.
    'type': 'date': This explicitly sets the input type to "date". This is important because it tells the browser to render a date input field, which typically includes a built-in calendar widget for easier date selection.
    
    Purpose and Benefits
    User Experience: By using type='date', users can easily select dates using a calendar interface provided by their browser, improving usability and reducing input errors.
    Validation: The DateField ensures that the input is validated correctly as a date format (e.g., YYYY-MM-DD), which matches the HTML5 date input format.
    Styling: Using Bootstrap's .form-control class gives the input field a visually appealing style that aligns with modern web design practices.
        
    Conclusion
    In summary, the line of code creates a date input field for user registration that leverages Django's form handling capabilities along with Bootstrap styling. 
    It enhances user experience by providing an intuitive way to select dates while ensuring that the data entered is valid and well-formatted. 
    This approach is commonly used in web applications where user input for dates is required.

    اضافه
    In summary, an HTML widget in Django forms is an essential component that defines how input fields are displayed and interacted with on a web page. 
    It manages both the rendering of the HTML elements and the extraction of user input data upon form submission. 
    Understanding widgets allows developers to create more interactive and user-friendly web applications by leveraging various input types effectively.
        '''







    class Meta:  #اطلاعات مربوط به فرم‌مان را به این کلاس متا می‌دهیم
        model = User  #یعنی هست در واقع، می‌نویسیمش وگرنه که باید یوزر دیفالت خود جنگو را بنویسیم custom model مدلی که فرم‌مان بر اساس آن دارد ساخته می‌شود که چون این مدل‌مان را خودمان ساختیم 
        fields = ['email', 'username', 'first_name', 'last_name', 'birthday', 'password1', 'password2'] #است پس باید ولیدیشن‌های مربوط بهش رو انجام بدم...برای بقیه اعضای این لیست هم همینطوره منوال EmailField داره یک User در کلاس یوزر و اونجا ایمیل رو میبینه و میگه این فیلد ایمیلی که این مدل  models.py داریم می‌گیم چه فیلدهایی را، بیا فرمشان را تشکیل بده، خودش میاد براساس دیتابیس ما این فیلدها را تشکیل میده و حالا با توجه به اینکه چی هستن این فیلدا (ایمیلن، پسوردن یا...) میاد ولیدیشن‌های لازم را روشون انجام می‌ده مثلا ما ایمیل نوشتیم ایجا، جنگو میاد ایمیل رو از کجا پیدا میکنه؟ میره توی 
        #نوشتیم را فرممون میاد یه تگ اینپوت برای هرکدومشون در نظر می‌گیره برای دریافت اینپوت از کاربر و یکمی خوشگل و اینا نمایششون می‌ده fields کارش اینه که ورودی بگیره دیگه، اینایی هم که خط بالا در <input> توی فرانت این فیلدهایی که در خط بالا نوشتم تگشون چیه؟ تگشون یه اینپوت هست دیگه تگ 
        #که کلاسی در بوت استرپ است به منظور کنترل فرم‌ها class="form_control" هم داشته باشن که هست class حالا ما می‌خواهیم این تگ‌های اینپوتمان (که فرممان قراره برای هرکدام از فیلدهایی که بهش معرفی کردیم تشکیل بده) یک
        #The class 'form-control' in Bootstrap is used to style various types of form elements, including <input>, <select>, and <textarea>. The '.form-control' class provides a uniform look and feel across different browsers for form controls. This helps ensure that all input elements appear consistent in size, padding, and border styling.
        #نوشتیم بدیم؟ به صورت زیر fields را به این فیلدهایی که در form_control حالا چجوری کلاس

    def __init__(self, *args, **kwargs):  #با اینکار متد این‌ایت در کلاس والد اورراید میشه اما با استفاده از کلمه کلیدی سوپر در خط بعدی دوباره با متد این‌ایت تعریف شده در کلاس والد دسترسی پیدا خواهیم کرد #'__init__' method is used to customize the initialization of the form and set specific attributes for the form fields. This line defines the '__init__' method, which is a special method in Python that initializes a new instance of a class. The '*args' and '**kwargs' allow the method to accept any number of positional and keyword arguments, respectively. This is useful for passing arguments to the parent class.
        super().__init__(*args, **kwargs)  #This calls the '__init__' method of the parent class (the superclass) to ensure that any initialization defined in the parent class is executed.In a Django form context, this typically initializes the form fields and sets up any necessary configurations.
        self.fields['email'].widget.attrs['class'] = 'form-control' #This line and the following lines modify the attributes of specific fields in the form:
        self.fields['username'].widget.attrs['class'] = 'form-control' #Here, 'self.fields' is a dictionary-like object that contains all the fields defined in the form. For each specified field (e.g., 'email', 'username', etc.), it accesses the widget associated with that field and sets its 'attrs' dictionary to include a CSS class.'class': 'form-control': This assigns Bootstrap's '.form-control' class to each field. By doing this, you ensure that all these input fields will be styled according to Bootstrap's styling conventions.
        self.fields['first_name'].widget.attrs['class'] = 'form-control'  #Styling: By adding the 'form-control' class to each field's widget, you ensure that they will have consistent styling provided by Bootstrap. This means they will be full-width, have appropriate padding, and look visually appealing. Customization: This approach allows you to customize how your form fields are rendered without having to redefine them in your form class. It keeps your code clean and maintainable.
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control' #دارم بهش می‌گم اون اتریبیوت‌هایی که مدنظرم است را برای فیلدهام توی فرانت قرار بده
        self.fields['password2'].widget.attrs['class'] = 'form-control'














#هوتن اینا رو نوشت ولی جلسه بعدش کامنتشون کرد و به‌جاشون بالایی‌ها رو نوشت
#creating a user registeration form:
# class UserRegisterForm(forms.ModelForm): #پس فرم‌ها هم مثل مدل‌ها خود یک کلاس هستند   #This line defines a form class called 'UserRegisterForm' that inherits from 'forms.ModelForm'. This is part of Django's form handling system, which allows you to create forms based on your models easily.
#     class Meta:          #The 'Meta' class is a special inner class used to configure the behavior of the 'UserRegisterForm'.
#         model = User     #model: Specifies that this form is associated with the 'User' model. This means that when the form is submitted, it will create or update an instance of the 'User' model.
#         fields = ['email', 'username', 'first_name', 'last_name', 'birthday', 'password']   #fields: A list of fields that will be included in the form.
#         widgets = {      #The 'widgets' dictionary allows you to customize how each field is rendered in HTML. Each key corresponds to a field name in the model, and each value is an instance of a widget class that defines how that field should be displayed.
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),  #EmailInput: Renders an input field specifically for email addresses.
#             'username': forms.TextInput(attrs={'class': 'form-control'}), #TextInput: Standard text input for fields like username, first name, and last name.
#             'first_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),  #DateInput: Renders a date picker for the birthday field, with HTML5 date input type specified.
#             'password': forms.PasswordInput(attrs={'class': 'form-control'}),  #PasswordInput: Renders a password input field, masking the entered text.
#         }
# '''
# In a Django application, this form would typically be used in a view to handle user registration. Here’s how it might fit into the workflow:
# Display the Form: When a user navigates to the registration page, this form can be instantiated and rendered in a template.
# Handle Form Submission: When the user submits the form:
# Django validates the input data based on the rules defined in the model (e.g., required fields, unique constraints).
# If valid, it creates a new user instance using the provided data.
# Feedback to User: If there are validation errors (e.g., missing fields or invalid email), those errors can be displayed back to the user on the same page.

# '''