
from django import forms
from .models import BoardGame


class BoardGameForm(forms.ModelForm):
    class Meta:
        model = BoardGame
        fields = ['title', 'description']  # Add more fields as needed
class EditBoardGameForm(forms.ModelForm):
    class Meta:
        model = BoardGame
        fields = ['title', 'description']  # Add more fields as needed