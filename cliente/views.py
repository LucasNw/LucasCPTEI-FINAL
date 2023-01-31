from django.shortcuts import render
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from cliente.forms import ClienteModelFrom
from cliente.models import Cliente



class ClientesView(ListView):
    model = Cliente
    template_name = 'clientes.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(ClientesView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(nome__icontains=buscar)
        return qs


class ClienteAddView(CreateView):
    from_class = ClienteModelFrom
    model = Cliente
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('clientes')

