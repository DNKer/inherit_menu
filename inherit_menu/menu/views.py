from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    """ Cтартовое (главное) окно. """
    template_name = 'index.html'
