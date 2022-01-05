# estagio/main/tests/test_views.py

from django.test import TransactionTestCase
from django.urls import reverse

from blog_tutorial.main.views import AboutView


class AboutPageTest(TransactionTestCase):
    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('about'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/about.html')

    def test_about_page_contains_correct_html(self):
        response = self.client.get('/about/')
        self.assertContains(response, '<h1>Hello from the about test!</h1>')

    def test_about_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'John Cena is here.')

class TestPostListView(TestCase):

    def setUp(self):
        blog_posts = 10

        for post_id in range(blog_posts):
            Post.objects.create(
                title=f'Test title',
                slug=f'test-title',
                overview=f'This is the overview.', 
                body=f'This is the body.', 
                image=f'image.jpg', 
                created_on=f'2020-07-28', 
                updated_on=f'2020-07-29',
                status=f'published',
                )

    def test_if_url_exist(self):
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)

    def test_if_view_accessible_by_name(self):
        response = self.client.get(reverse('blog'))
        self.assertEquals(response.status_code, 200)

    def test_if_view_uses_right_template(self):
        response = self.client.get(reverse('blog'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/home.html')

    def test_if_pagination_is_three(self):
        response = self.client.get(reverse('blog'))
        self.assertEquals(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['posts']) == 3)

    def test_list_all_blog_posts(self):
         # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('blog')+'?page=2')
        self.assertEquals(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['posts']) == 3)

class TestPostDetailView(TestCase):

    def setUp(self):
        Post.objects.create(
            title=f"Test title", 
            slug=f"test-title", 
            overview=f"This is the overview.", 
            body=f"This is the body.", 
            image=f"image.jpg", 
            created_on=f"2020-07-28", 
            updated_on=f"2020-07-29",
            status=f"published",
            )

    def test_if_url_exist(self):
        response = self.client.get('/blog/test-title/')
        self.assertEqual(response.status_code, 200)

    def test_if_view_uses_right_template(self):
        response = self.client.get('/blog/test-title/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/post_detail.html')


class TestProjectDetailView(TestCase):

    def setUp(self):
        Project.objects.create(
            title='Learnetto',
            slug="learnetto",
            image="learnetto.jpg",
            live_site='www.vgreyes.com',
            github_link='www.github.com/learnetto',
            description='This is a test description for the project.',
            )

    def test_if_url_exist(self):
        response = self.client.get('/portfolio/learnetto/')
        self.assertEquals(response.status_code, 200)

    def test_if_view_uses_right_template(self):
        response = self.client.get('/portfolio/learnetto/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/project_details.html')


class TestProjectListView(TestCase):

    def setUp(self):
        project_list = 10

        for project_id in range(project_list):
            Project.objects.create(
                title=f'Acme',
                slug=f'acme',
                image=f'project_image.jpg',
                live_site=f'www.learnetto.com',
                github_link=f'www.github.com/reyesvicente',
                description=f'This is a test description',
                )

    def test_if_url_exist(self):
        response = self.client.get('/portfolio/')
        self.assertEquals(response.status_code, 200)

    def test_if_view_accessible_by_name(self):
        response = self.client.get(reverse('portfolio'))
        self.assertEquals(response.status_code, 200)

    def test_if_view_uses_right_template(self):
        response = self.client.get(reverse('portfolio'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/projects.html')

    def test_if_pagination_is_five(self):
        response = self.client.get(reverse('portfolio'))
        self.assertEquals(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['projects']) == 5)

    def test_list_all_projects(self):
        response = self.client.get(reverse('portfolio')+'?page=2')
        self.assertEquals(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['projects']) == 5)


class TestCategoryView(TestCase):

    def setUp(self):
        Category.objects.create(
            title="Test Blog Category", 
            slug="test-blog-category", 
            )

    def test_if_url_exist(self):
        response = self.client.get('/blog/category/test-blog-category/')
        self.assertEqual(response.status_code, 200)

    def test_if_view_uses_right_template(self):
        response = self.client.get('/blog/category/test-blog-category/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/category_list.html')