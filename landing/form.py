from django import forms
from .models import Mails

class MailForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MailForm, self).__init__(*args, **kwargs)
        self.fields['mail'].widget.attrs['placeholder'] = 'Votre adresse mail'
        self.fields['mail'].label = ""

    class Meta:
        model = Mails
        fields = ["mail"]
        error_messages = {
            'mail': {
                'invalid': 'Adresse mail invalid ou déja utilisé',
                'required': 'Ce champ est obligatoire',
            },
        }