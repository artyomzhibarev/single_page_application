from django.views.generic import ListView
from .models import Entity


class TableView(ListView):
    template_name = 'main/table.html'
    model = Entity
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fields = [field.name for field in Entity._meta.get_fields()]
        context['title'] = 'Entity table'
        context['fields'] = fields
        return context
