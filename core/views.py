from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['motto'] = "Unity Culture Progress and Service"
        context['branch_title'] = "United Kabye Association of Ghana - Eastern Region Branch"
        return context


class AboutView(TemplateView):
    template_name = 'core/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['motto'] = "Unity Culture Progress and Service"
        context['branch_title'] = "United Kabye Association of Ghana - Eastern Region Branch"
        return context


class ImpactView(TemplateView):
    template_name = 'core/impact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['motto'] = "Unity Culture Progress and Service"
        context['branch_title'] = "United Kabye Association of Ghana - Eastern Region Branch"
        return context


class ContactView(TemplateView):
    template_name = 'core/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['motto'] = "Unity Culture Progress and Service"
        context['branch_title'] = "United Kabye Association of Ghana - Eastern Region Branch"
        return context