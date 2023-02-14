from dataclasses import field
from itertools import product
from django import forms
from app1.models import *


class message_Form(forms.ModelForm):
    class Meta:
        model=message
        fields='__all__'
