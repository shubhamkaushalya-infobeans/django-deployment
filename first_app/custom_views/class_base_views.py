from django.views.generic import View,TemplateView

class ClassBasedView(TemplateView):
    template_name = 'first_app/cbv.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_current_topic'] = 'Data send from CBD Template View'
        return context
