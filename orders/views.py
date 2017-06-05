from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import reverse
from django.http import HttpResponseRedirect
from main.utils import get_order_settings
from .forms import OrderForm
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
        self.object.user = self.request.user
        self.object.total_price = self.object.price + os.restaurant.delivery_price
        self.object.settings = os
        self.object = form.save()

        return HttpResponseRedirect(self.get_success_url())


class OrderDelete(DeleteView):
    model = Order

    def get_success_url(self):
        return reverse('user_home')



'''
@login_required
def new_order(request):
    os = get_order_settings()
    order = Order(user=request.user, settings=os, total_price=0)
    if request.method == 'POST':
        form = OrderForm(data=request.POST, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            order.total_price = order.price + order.settings.restaurant.delivery_price
            order.save()
            return redirect('user_home')
    else:
        form = OrderForm(instance=order)
'''