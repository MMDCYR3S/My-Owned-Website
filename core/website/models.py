from django.db import models

# Contact model
class Contact(models.Model):
    """ Summary:
        This model is used for contact. Gets email from user
        and then save it to the database.
    """
    email = models.EmailField(max_length=200)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
