from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, Textarea, EmailInput, FileInput
from .models import User, Car


class MyUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["name", "email", "address", "avatar", "bio", "password1", "password2"]
        widgets = {
            'address': TextInput(attrs={'class': "appearance-none border rounded w-full py-2 px-3 text-gray-700 "
                                                 "leading-tight focus:outline-none focus:shadow-outline",
                                        'id': "autocomplete", 'placeholder': "Parish, airport, street or hotel..."}),
            'bio': Textarea(attrs={'rows': 4, 'class': "appearance-none border rounded w-full py-2 px-3 text-gray-700 "
                                                       "leading-tight focus:outline-none focus:shadow-outline",
                                   'placeholder': "Say something about yourself"}),
            'avatar': FileInput(attrs={'class': "appearance-none w-full py-2 px-3 text-gray-700 "
                                                "leading-tight focus:outline-none focus:shadow-outline",
                                       }),
            'name': TextInput(attrs={'class': "appearance-none border rounded w-full py-2 px-3 text-gray-700 "
                                              "leading-tight focus:outline-none focus:shadow-outline",
                                     'placeholder': "John Doe"
                                     }),
            'email': EmailInput(attrs={'class': "appearance-none border rounded w-full py-2 px-3 text-gray-700 "
                                                "leading-tight focus:outline-none focus:shadow-outline",
                                       'placeholder': "email@example.com"
                                       })
        }


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
