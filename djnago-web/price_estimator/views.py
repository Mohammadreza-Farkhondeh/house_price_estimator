from django.views import generic
from . import forms

class EstimateView(generic.FormView):
    template_name = 'price_estimator\estimate.html'
    form_class = forms.DataForm
    success_url = '/estimate/'

    def form_valid(self, form):
        location = form.cleaned_data['location']
        rooms = form.cleaned_data['rooms']
        parking = form.cleaned_data['parking']
        warehouse = form.cleaned_data['warehouse']
        elevator = form.cleaned_data['elevator']

        result = form.process_data(location, rooms, parking, warehouse, elevator)

        return self.render_to_response(self.get_context_data(form=form, result=result))