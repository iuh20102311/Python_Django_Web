from django import forms
from .models import Item, Category
from django.core.exceptions import ValidationError

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category', 'name', 'description', 'price', 'image']
        
        widgets = {
            'category': forms.Select(attrs={
                'class': 'pl-10 w-full py-3 px-4 border border-gray-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200'
            }),
            'name': forms.TextInput(attrs={
                'placeholder': 'Item name',
                'class': 'pl-10 w-full py-3 px-4 border border-gray-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Item description',
                'class': 'pl-10 w-full py-3 px-4 border border-gray-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200',
                'rows': 4
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': '0.00',
                'class': 'pl-10 w-full py-3 px-4 border border-gray-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200'
            }),
            'image': forms.FileInput(attrs={
                'class': 'sr-only'
            })
        }
        
class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'image', 'is_sold']
        
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Item name',
                'class': 'pl-10 w-full py-3 px-4 border border-gray-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Item description',
                'class': 'pl-10 w-full py-3 px-4 border border-gray-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200',
                'rows': 4
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': '0.00',
                'class': 'pl-10 w-full py-3 px-4 border border-gray-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200'
            }),
            'image': forms.FileInput(attrs={
                'class': 'sr-only',
                'id': 'imageUploadInput',
                'accept': 'image/*'
            }),
            'is_sold': forms.CheckboxInput(attrs={
                'class': 'h-5 w-5 text-teal-500 rounded border-gray-300 focus:ring-teal-500 mr-2'
            })
        }