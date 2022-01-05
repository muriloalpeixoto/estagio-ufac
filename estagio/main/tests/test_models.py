# estagio/main/tests/test_models.py
from django.test import TestCase

from estagio.main.models import Contact

class ContactModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Setup data on form
        Contact.objects.create(name="Elon Musk", email="elon@musk.com", message="This is a message")

    def test_form_content(self):
        contact = Contact.objects.get(id=1)
        expected_objects_in_form = f'{contact.name}', f'{contact.email}', f'{contact.message}'
        self.assertEquals(expected_objects_in_form, ('Elon Musk', 'elon@musk.com', 'This is a message'))

    def test_name_label(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_email_label(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    def test_message_label(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('message').verbose_name
        self.assertEquals(field_label, 'message')

    def test_name_max_length(self):
        contact = Contact.objects.get(id=1)
        max_length = contact._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_email_max_length(self):
        contact = Contact.objects.get(id=1)
        max_length = contact._meta.get_field('email').max_length
        self.assertEquals(max_length, 50)

class ProjectModelTest(TestCase):

    def setUp(self):
        Project.objects.create(
            title="Acme",
            slug="acme",
            live_site="www.example.com",
            github_link="www.github.com/learnetto/eventlite",
            description="Example description",
        )

    def test_project_data(self):
        project_details = Project.objects.get(id=1)
        expected_object_details = f'{project_details.title}', f'{project_details.slug}', f'{project_details.live_site}', f'{project_details.github_link}', f'{project_details.description}'
        self.assertEqual(expected_object_details, ("Acme", "acme", "www.example.com", "www.github.com/learnetto/eventlite", "Example description"))

    def project_list_view(self):
        response = self.client.get(reverse('project_details'))
        self.assertEqual(response.status_code, 200)
        self.assertContacts(response, ("Acme", "www.example.com", "www.github.com/learnetto/eventlite", "Example description"))
        self.assertTemplateUsed(response, 'pages/projects.html')

class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(
            title="Test title",
            slug="test-title",
            overview="This is the overview.",
            body="This is the body.",
            image="image.jpg",
            created_on="2020-07-28",
            updated_on="2020-07-29",
            status="published",
        )

    def test_post_data(self):
        post = Post.objects.get(id=1)
        expected_post_details = f'{post.title}', f'{post.slug}', f'{post.overview}', f'{post.body}', f'{post.image}', f'{post.created_on}', f'{post.updated_on}', f'{post.status}'
        self.assertEqual(expected_post_details, ("Test title", "test-title", "This is the overview.", "This is the body.", "image.jpg", "2020-07-28", "2020-07-29", "published"))

    def post_list_view(self):
        response = self.client.get(reverse('post'))
        self.assertEqual(response.status_code, 200)
        self.assertContacts(response, ("Test title", "test-title", "This is the overview.", "This is the body.", "image.jpg", "2020-07-28", "2020-07-29", "published"))
        self.assertTemplateUsed(response, 'pages/home.html')

class CategoryModelTest(TestCase):

    def setUp(self):
        Category.objects.create(
            title="blog", 
            slug="blog", 
        )

    def test_category_data(self):
        category = Category.objects.get(id=1)
        expected_category_details = f'{category.title}', f'{category.slug}'
        self.assertEqual(expected_category_details, ("blog", "blog", ))

    def category_list_view(self):
        response = self.client.get(reverse('category'))
        self.assertEqual(response.status_code, 200)
        self.assertContacts(response, ("blog", "blog", ))
        self.assertTemplateUsed(response, 'pages/category_list.html')

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