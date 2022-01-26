from pickle import TRUE
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


User = get_user_model()

def gera_pdf_view(request):
    #Bytestream buffer
    buffer = io.BytesIO()
    #Canvas
    canvas = canvas.Canvas(buffer, pagesize=letter, bottomup=0)
    #Text object
    textobject = canvas.beginText()
    textobject.setTextOrigin(inch,inch)
    textobject.setFont("Helvetica", 14)
    #Text
    lines = [
        "Linha 1",
        "Linha 2",
        "Linha 3",
    ]
    #Loop
    for line in lines:
        textobject.textLine(line)
    
    #Finalização
    canvas.drawText(textobject)
    canvas.showPage()
    canvas.save()
    buffer.seek(0)

    #Retorno
    return FileResponse(buffer, as_attachment=True, filename="file.pdf")

class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()
