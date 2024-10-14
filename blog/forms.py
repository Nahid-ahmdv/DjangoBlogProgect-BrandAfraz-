from django import forms
from .models import Post, Category


class PostForm(forms.ModelForm): #پس فرم‌ها هم مثل مدل‌ها خود یک کلاس هستند   #This line defines a form class called 'PostForm' that inherits from 'forms.ModelForm'. This is part of Django's form handling system, which allows you to create forms based on your models easily.
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), empty_label=None)
    class Meta:          #The 'Meta' class is a special inner class used to configure the behavior of the 'PostForm'.
        model = Post     #model: Specifies that this form is associated with the 'User' model. This means that when the form is submitted, it will create or update an instance of the 'User' model.
        fields = ['category', 'title', 'description']  #مون انداختیم یه آتر داره یه کتگوری یه تایتل یه دسکریپشن یه پستدآن و آخری هم لایکدبای که البته به دوتای آخری نیازی نداریم و آتر هم باید اتوماتیک بگیریم نه اینکه توی فرممون باشهPost و نگاهی به مدل models.py برای نوشتن فیلدها رفتیم توی فایل        #fields: A list of fields that will be included in the form.
        widgets = {      #The 'widgets' dictionary allows you to customize how each field is rendered in HTML. Each key corresponds to a field name in the model, and each value is an instance of a widget class that defines how that field should be displayed.
            'category': forms.TextInput(attrs={'class':'form-control'}), 
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # 'description': forms.TextInput(attrs={'class': 'form-control', 'rows': 10, 'cols': 70})
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 1,  # Initial number of rows
                'style': 'resize: vertical;'  # Allow vertical resizing
            }),
            }