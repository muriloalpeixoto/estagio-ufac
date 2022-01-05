# estagio/main/tests/test_contact_form.py

class ContactFormTest(TestCase):

    def test_contact_form_field_labels(self):
        form = ContactForm()
        self.assertTrue(form.fields['name'].label == None or form.fields['name'].label == 'Your name')
        self.assertTrue(form.fields['email'].label == None or form.fields['email'].label == 'Your email')
        self.assertTrue(form.fields['message'].label == None or form.fields['message'].label == 'Your inquiry')

    def test_contact_form_submission(self):
        form_data = {'name': "Walter White", 'email': "walterwhite@breakingbad.com", "message": 'I want some gasoline.'}
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)

    def test_contact_form_failed_submission(self):
        form = ContactForm(data = {'name': "Walter Brown", 'email': "", "message": ''})
        self.assertFalse(form.is_valid())