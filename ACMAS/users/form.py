from django.contrib.auth.forms import UserCreationForm
from user.models import User

class User(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email')
