from django import forms 
from .models import Request


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['name', 'phone', 'message']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Телефон', 'type': 'tel'}),
            'message': forms.Textarea(
                attrs={
                    'placeholder': 'Сообщение',
                    'rows': 3,
                }
            ),
        }
