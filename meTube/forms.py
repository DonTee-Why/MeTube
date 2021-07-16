from django.forms import ModelForm
from django.forms.widgets import EmailInput, PasswordInput, TextInput, FileInput, Textarea
from meTube.models import AppUser, Video

class SignInForm(ModelForm):
    class Meta:
        model = AppUser
        fields = ['email', 'password']
        widgets = {
            'email': EmailInput(attrs={
                'class': "form-control",
                'id': "floatingEmail",
                'name': "floatingEmail",
                'placeholder': "Email Address"
            }),
            'password': PasswordInput(attrs={
                'class': "form-control",
                'id': "floatingPassword",
                'name': "floatingPassword",
                'placeholder': "Password"
            })
        }

class SignUpForm(ModelForm):
    class Meta:
        model = AppUser
        fields = ['first_name','surname', 'email', 'password']
        widgets = {
            'first_name': TextInput(attrs={
                'class': "form-control",
                'id': "floatingFirstName",
                'name': "floatingFirstName",
                'placeholder': "John"
            }),
            'surname': TextInput(attrs={
                'class': "form-control",
                'id': "floatingSurname",
                'name': "floatingSurname",
                'placeholder': "Doe"
            }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'id': "floatingEmail",
                'name': "floatingEmail",
                'placeholder': "Email Address"
            }),
            'password': PasswordInput(attrs={
                'class': "form-control",
                'id': "floatingPassword",
                'name': "floatingPassword",
                'placeholder': "Password"
            })
        }

class VideoUploadForm(ModelForm):
    class Meta:
        model = Video
        fields = ['title','caption', 'video']
        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'id': "floatingTitle",
                'name': "floatingTitle",
                'placeholder': "Title"
            }),
            'caption': Textarea(attrs={
                'rows': "4",
                'class': "form-control",
                'id': "floatingCaption",
                'name': "floatingCaption",
                'style': "height: auto;",
                'placeholder': "Caption"
            }),
            'video': FileInput(attrs={
                'class': "form-control",
                'id': "floatingVideo",
                'name': "floatingVideo",
            })
        }