# estagio/main/models.py
# Create your models here.
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

STATUS_CHOICES = [
    ("draft", "Draft"),
    ("published", "Published"),
]


class Project(models.Model):
    """ This model defines our Project class which will
        handles the portfolio of the user.
    """
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=140, default=title)
    image = models.ImageField(upload_to="projects/", blank=True)
    live_site = models.CharField(max_length=255)
    github_link = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        """ Meta for the naming in the django admin that
            describes a model if the object is singular or
            plural
        """
        verbose_name = _("Project")
        verbose_name_plural = _("Project")

    def __str__(self):
        """ Returns the title of Project models instead
            of a primary key
        """
        return self.title


class Category(models.Model):
    """ This model defines the categories field in the Post model
        with a ManyToManyField.
    """
    title = models.CharField(max_length=140)
    slug = models.SlugField(max_length=140, default=title)

    class Meta:
        """ Meta for the naming in the django admin that
            describes a model if the object is singular or
            plural
        """
        verbose_name = _("Category")
        verbose_name_plural = _("Category")

    def __str__(self):
        """ Returns the title of Project models instead
            of a primary key
        """
        return self.title

    def get_context_data(self, **kwargs):
        context = super(self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter('category')
        return context

    def get_absolute_url(self):
        return reverse("category-list", kwargs={"slug": self.slug})


class Post(models.Model):
    """ The main model that defines the Post class which
        has a relationship with the Category class
    """
    title = models.CharField(max_length=140)
    slug = models.SlugField(max_length=140, default=title)
    overview = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to="blog/")
    created_on = models.DateField()
    updated_on = models.DateField()
    categories = models.ManyToManyField(Category, related_name='posts')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")

    class Meta:
        """ Meta for the naming in the django admin that
            describes a model if the object is singular or
            plural
        """
        verbose_name = _("Post")
        verbose_name_plural = _("Post")

    def __str__(self):
        """ Returns the title of Project models instead
            of a primary key
        """
        return self.title


class Contact(models.Model):
    """ The Contact model that accepts name, email and message
        in the contact page.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        """ Meta for the naming in the django admin that
            describes a model if the object is singular or
            plural
        """
        verbose_name = _("Contact")
        verbose_name_plural = _("Contact")

    def __str__(self):
        """ Returns the title of Project models instead
            of a primary key
        """
        return self.name