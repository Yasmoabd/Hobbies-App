from django.forms import ModelForm

from hobbyapp.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


