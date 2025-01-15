from django import forms
from .models import Contact

# Contact form
class ContactForm(forms.ModelForm):
    """ Summary:
        This is a form for the contact model.
    """
    class Meta:
        model = Contact
        fields = "__all__"
        