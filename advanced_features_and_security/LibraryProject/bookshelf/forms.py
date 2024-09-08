from django import forms
from .models import Book  # Adjust if you're using a different model

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book  # Replace with your model if different
        fields = ['title', 'author', 'publication_date']  # Adjust fields as needed

    # Optional: Add custom validation or widgets
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError("Title is required.")
        return title
