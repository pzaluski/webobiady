from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from main.utils import get_order_settings
from .forms import OrderPurchaserForm
from .models import Order


@method_decorator(login_required, name='dispatch')
class DailyOrdersList(ListView):
    context_object_name = 'daily_orders'
    template_name = 'orders/daily_orders.html'

    def get_queryset(self):
        return Order.objects.filter(settings=get_order_settings())



@method_decorator(login_required, name='dispatch')
class OrderCreate(CreateView):
    model = Order
    fields = ['dishes']

    def get_success_url(self):
        return reverse('user_home')

    def form_valid(self, form):
        os = get_order_settings()
        order = form.save(commit=False)
        order.settings = os
        order.user = self.request.user
        order.total_price = 0
        order = form.save()
        for dish in order.dishes.all():
            order.total_price = order.total_price + dish.price
        order.save()

        return HttpResponseRedirect(self.get_success_url())


@method_decorator(login_required, name='dispatch')
class OrderUpdate(UpdateView):
    model = Order
    fields = ['dishes']

    def get_success_url(self):
        return reverse('user_home')

    def form_valid(self, form):
        order = form.save()
        for dish in order.dishes.all():
            order.total_price = order.total_price + dish.price
        order.save()

        return HttpResponseRedirect(self.get_success_url())


@method_decorator(login_required, name='dispatch')
class OrderDelete(DeleteView):
    model = Order

    def get_success_url(self):
        return reverse('user_home')


@method_decorator(login_required, name='dispatch')
class OrderPurchaserEdit(FormView):
    model = Order
    fields = ['order_status', 'paid']
    template_name = 'orders/daily_orders.html'
    form_class = OrderPurchaserForm

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Order.objects.filter(settings=get_order_settings())
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        return reverse('daily_orders')

    def post(self, request):
        op = request.POST['op']
        oid = request.POST['order_id']
        order = Order.objects.get(pk=oid)
        if op == 'status':
            ostatus = request.POST['status']
            order.order_status = ostatus
            order.save()
        if op == 'paid':
            if request.POST.get('paid'):
                opaid = request.POST['paid']
            else:
                opaid = False
            order.paid = opaid
            order.save()
        return self.get(request)
