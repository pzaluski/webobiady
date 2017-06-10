from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from main.utils import get_order_settings
from .models import Order


@method_decorator(login_required, name='dispatch')
class DailyOrdersList(ListView):
    context_object_name = 'daily_orders'
    template_name = 'orders/daily_orders.html'

    def get_queryset(self):
        return Order.objects.filter(settings=get_order_settings())


@method_decorator(login_required, name='dispatch')
class OrderDetail(DetailView):
    model = Order
    template_name = 'orders/order_detail.html'
    context_object_name = 'order'


@method_decorator(login_required, name='dispatch')
class OrderCreate(CreateView):
    model = Order
    fields = ['description', 'price']

    def get_success_url(self):
        return reverse('user_home')

    def form_valid(self, form):
        os = get_order_settings()
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.total_price = self.object.price + os.restaurant.delivery_price
        self.object.settings = os
        self.object = form.save()

        return HttpResponseRedirect(self.get_success_url())


@method_decorator(login_required, name='dispatch')
class OrderUpdate(UpdateView):
    model = Order
    fields = ['description', 'price']

    def get_success_url(self):
        return reverse('user_home')

    def form_valid(self, form):
        os = get_order_settings()
        self.object = form.save(commit=False)
        self.object.total_price = self.object.price + os.restaurant.delivery_price
        self.object = form.save()

        return HttpResponseRedirect(self.get_success_url())


@method_decorator(login_required, name='dispatch')
class OrderDelete(DeleteView):
    model = Order

    def get_success_url(self):
        return reverse('user_home')


@login_required
def order_edit(request):
    if request.method == 'GET':
        oid = request.GET['id']
        ostatus = request.GET['status']

        order = Order.objects.get(pk=oid)
        order.order_status = ostatus
        order.save()
    return HttpResponseRedirect(reverse('daily_orders'))
