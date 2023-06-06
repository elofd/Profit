from django.views.generic import TemplateView

from .models import MySite


class MySiteView(TemplateView):
    template_name = 'mysite/example.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mysite = MySite.objects.first()
        context['mysite'] = mysite
        return context
