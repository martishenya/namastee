from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput
from django.utils.translation import gettext, gettext_lazy as _
class SignUpForm(UserCreationForm):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'required': '',
            'name': 'username',
            'id': 'username',
            'type': 'text',
            'class': 'form-input',
            'placeholder': _('Иван Иванов'),
            'maxlength': '16',
            'minlength': '6'
            })
        self.fields['email'].widget.attrs.update({
            'required': '',
            'name': 'email',
            'id': 'email',
            'type': 'email',
            'class': 'form-input',
            'placeholder': _('Ivanov@mail.ru'),
            })
        self.fields['password1'].widget.attrs.update({
            'required': '',
            'name': 'password1',
            'id': 'password1',
            'type': 'password',
            'class': 'form-input',
            'placeholder': _('Пароль'),
            'maxlength': '22',
            'minlength': '8'
        })
        self.fields['password2'].widget.attrs.update({
            'required': '',
            'name': 'password2',
            'id': 'password2',
            'type': 'password',
            'class': 'form-input',
            'placeholder': _('Пароль еще раз'),
            'maxlength': '22',
            'minlength': '8'
        })
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {'username': TextInput(attrs={'placeholder': 'Ваше ФИО','class': 'form-input'}),
                   'email': TextInput(attrs={'placeholder': 'Электронная почта','class': 'form-input'}),
                   'password1': forms.PasswordInput(attrs={'placeholder': 'Пароль'}),
                   'password2': TextInput(attrs={'placeholder': 'Повторите пароль'})
                   }

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль','class': 'form-input'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль','class': 'form-input'}))
