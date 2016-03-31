# -*- coding: utf-8 -*-
from audioop import reverse

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import CustomerForm
from .models import Customer
from .models import Vendor


def customers(request):
    customers = Customer.objects.all()

    return render(request, 'customer.html', {'customers': customers})


def customers_form(request, pk):
    customers = Customer.objects.get(id=1)
    form = CustomerForm(instance=customers)
    return render(request, 'customer_form.html', {'customers': form})

def customers_edit(request, pk=None):
    if pk:
        customer = Customer.objects.get(id=pk)
    else:
        customer = Customer(id=1)

    if request.POST:
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()

            # If the save was successful, redirect to another page
            redirect_url = reverse('produtos')
            return HttpResponseRedirect(redirect_url)
    else:
        form = CustomerForm(instance=customer)

    return render(request, 'customer_form.html', {'form': form, 'customer': customer})

def vendors(request):
    vendors = Vendor.objects.all()

    return render(request, 'vendor.html', {'vendors': vendors})


"""
class ItemUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer_form.html'

    def dispatch(self, *args, **kwargs):
        self.id = kwargs['pk']
        return super(ItemUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.save()
        customer = Customer.objects.get(id=self.id)
        return HttpResponse(render_to_string('clientesFormSuccess.html', {'customer': customer}))

    def get_context_data(self, **kwargs):
        context = super(ItemUpdateView, self).get_context_data(**kwargs)
        return context
"""