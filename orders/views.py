from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import reverse, render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, MonthArchiveView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from main.utils import get_order_settings, EmailMessageCreator
from .forms import OrderPurchaserForm, OrderForm
from .models import Order
from datetime import datetime
import logging

'''
@method_decorator(login_required, name='dispatch')
class DailyOrdersList(ListView):
    context_object_name = 'daily_orders'
    template_name = 'orders/daily_orders.html'

    def get_queryset(self):
        return Order.objects.filter(settings=get_order_settings())
'''

logger = logging.getLogger(__name__)


@method_decorator(login_required, name='dispatch')
class OrderCreate(CreateView):
    model = Order
    form_class = OrderForm
    template_name = "orders/order_form_modal.html"

    def get_form_kwargs(self):
        kwargs = super(OrderCreate, self).get_form_kwargs()
        kwargs['order_settings'] = get_order_settings()
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(OrderCreate, self).get_context_data(**kwargs)
        context['destination_url'] = reverse('order_form')
        return context

    def get_success_url(self):
        return reverse('user_home')

    def form_valid(self, form):
        order = form.save(commit=False)
        order.settings = form.order_settings
        order.user = self.request.user
        order.price = 0
        order = form.save()

        for dish in order.dishes.all():
            order.price = order.price + dish.price
        order.save()

        return HttpResponseRedirect(self.get_success_url())


@method_decorator(login_required, name='dispatch')
class OrderUpdate(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = "orders/order_form_modal.html"

    def get_form_kwargs(self):
        kwargs = super(OrderUpdate, self).get_form_kwargs()
        kwargs['order_settings'] = get_order_settings()
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(OrderUpdate, self).get_context_data(**kwargs)
        context['destination_url'] = reverse('order_update', kwargs={'pk': context['order'].id})
        return context

    def get(self, request, *args, **kwargs):
        return super(OrderUpdate, self).get(request)

    def get_success_url(self):
        return reverse('user_home')

    def form_valid(self, form):
        order = form.save()
        order.price = 0
        for dish in order.dishes.all():
            order.price = order.price + dish.price
        order.save()

        return HttpResponseRedirect(self.get_success_url())


@method_decorator(login_required, name='dispatch')
class OrderDelete(DeleteView):
    model = Order

    def get_success_url(self):
        return reverse('user_home')


@method_decorator(login_required, name='dispatch')
class PurchaserOrdersList(FormView):
    model = Order
    fields = ['order_status', 'paid']
    template_name = 'orders/daily_orders.html'
    form_class = OrderPurchaserForm

    def get_context_data(self, **kwargs):
        logger.error("HALIK")
        kwargs['object_list'] = Order.objects.all_orders_for_today().order_by('date_created')
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        return reverse('daily_orders')

    def post(self, request, *args, **kwargs):
        op = request.POST['op']
        oid = request.POST['order_id']
        order = Order.objects.get(pk=oid)
        if op == 'status':
            order.order_status = request.POST['status']
            order.save()
        if op == 'paid':
            if request.POST.get('paid'):
                order.paid = request.POST['paid']
            else:
                order.paid = False
            order.save()
        return self.get(request)


@method_decorator(login_required, name='dispatch')
class PurchaserOrderEdit(OrderUpdate):

    def get_context_data(self, **kwargs):
        context = super(PurchaserOrderEdit, self).get_context_data(**kwargs)
        context['destination_url'] = reverse('order_edit', kwargs={'pk': context['object'].id})
        return context

    def get_success_url(self):
        return reverse('daily_orders')


@method_decorator(login_required, name='dispatch')
class MessageCollectView(TemplateView):

    def __init__(self):
        super(MessageCollectView, self).__init__()
        self.purchaser = get_order_settings().purchaser
        self.orders = Order.objects.all_orders_for_today()

    def get(self, request, *args, **kwargs):
        """
        :param request:
        :param args:
        :param kwargs:
        :return: Ustawia status wszystkich zamówień na Do odbioru
                 Wysyła maila z powiadomieniem do użytkowników
        """
        Order.objects.all_orders_for_today().update(order_status='COMPLETED')

        message = EmailMessageCreator()
        message.set_subject('Odbierz zamówienie')
        message.set_body_template('email_messages/email_message_collect.txt')
        #message.set_body_template_html('email_messages/email_message_collect.html')

        for o in self.orders:
            email = o.user.email

            context = {
                'place': self.purchaser.userprofile.collect_place,
                'username': o.user.username,
                'dishes': o.dishes.all(),
            }
            message.set_message_context(context=context)
            print(email)
            logger.error(email)
            #print(context)
            #message.send_message([email])
            #break

        return redirect('message_sent')


@method_decorator(login_required, name='dispatch')
class OrderArchiveMonthView(MonthArchiveView):
    date_field = 'date_created'
    month_format = '%m'
    make_object_list = True
    allow_empty = True

    def get(self, request, *args, **kwargs):
        self.queryset = Order.objects.filter(user=request.user).order_by('date_created')
        self.month = kwargs['month']
        self.year = kwargs['year']
        return super().get(request, *args, **kwargs)

    def get_month(self):
        if not self.month:
            return datetime.today().strftime('%m')
        else:
            return self.month

    def get_year(self):
        if not self.year:
            return datetime.today().strftime('%Y')
        else:
            return self.year


@login_required
def message_sent(request):
    return render(request, 'orders/message_sent.html')

