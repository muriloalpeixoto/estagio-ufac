from django import forms
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Field

class UploadFileForm(forms.Form):
    file = forms.FileField(label='Selecione um arquivo',
    help_text='preferencialmente *.pdf, *.docx ou *.odt')

class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_method = 'post'
        self.helper.form_action = '/contact/'
        self.helper.form_class = "form-group"
        self.helper.form_id = 'contact-form'

        self.helper.add_input(Submit('submit', 'Submit'))

    name = forms.CharField(max_length=100, label="Your name", widget=forms.TextInput(attrs={'class': 'col', 'placeholder':'Vicente Reyes'}))
    email = forms.CharField(label="Your email", widget=forms.EmailInput(attrs={'class': 'col', 'placeholder':'highcenbugtv@vgreyes.com'}))
    message = forms.CharField(max_length=500, label="Your inquiry", widget=forms.Textarea(attrs={'placeholder':'I need to...'}))