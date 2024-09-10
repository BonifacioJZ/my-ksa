from django import forms
from .models import Category


#TODO(editar las proporciones)
class CategoryForms(forms.ModelForm):
    name = forms.CharField(max_length=150,required=True,label='Nombre')
    description = forms.Textarea()
    guard_name = forms.CharField(max_length=13,required=True)
    class Meta:
        model = Category
        fields = ['name','description','guard_name',]