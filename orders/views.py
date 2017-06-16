from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect
from django.shortcuts import reverse, render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from main.utils import get_order_settings
from .forms import OrderPurchaserForm, OrderForm
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
    form_class = OrderForm
    template_name = "orders/order_form_modal.html"

    def get_context_data(self, **kwargs):
        context = super(OrderCreate, self).get_context_data(**kwargs)
        context['destination_url'] = reverse('order_form')
        return context

    def get_success_url(self):
        return reverse('user_home')

    def form_valid(self, form):
        os = get_order_settings()
        order = form.save(commit=False)
        order.settings = os
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
        kwargs['object_list'] = Order.objects.filter(settings=get_order_settings())
        for order in kwargs['object_list']:
            order.total_price = order.price + order.get_delivery_price()
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


@method_decorator(login_required, name='dispatch')
class PurchaserOrderEdit(OrderUpdate):

    def get_context_data(self, **kwargs):
        context = super(PurchaserOrderEdit, self).get_context_data(**kwargs)
        context['destination_url'] = reverse('order_edit', kwargs={'pk': context['object'].id})
        return context

    def get_success_url(self):
        return reverse('daily_orders')


@login_required
def send_message_collect(request):
    purchaser = get_order_settings().purchaser

    Order.objects.filter(settings=get_order_settings()).update(order_status='COMPLETED')
    orders = Order.objects.filter(settings=get_order_settings())

    messages = []

    for o in orders:
        email = o.user.email

        message = 'Twoje zamówienie:\n'
        message_html = '<h3 style="color:#3b85bf">Witaj' + o.user.username + '</h3>'
        message_html += '<p>Twoje zamówienie:</p><ul>'
        for dish in o.dishes.all():
            message += dish.name + ', '
            message_html += '<li>dish.name</li>'
        message_html += '</ul>'
        message = message[:-2]
        message += '\n'
        message_html += '<p>zostało dostarczone. <br />Miejsce odbioru: </p>'
        message += 'zostało dostarczone. \nMiejsce odbioru: '
        message += purchaser.userprofile.collect_place
        message += '\n\nOdbierz czym prędzej, bo inni Ci zjedzą!!!'

        subject, from_email, to = 'Odbierz zamówienie', 'WebObiady <noreply@webobiady.pl>', email
        text_content = message
        html_content = message_html

        #msg = EmailMessage(subject, html_content, from_email, [to])
        #msg.content_subtype = "html"  # Main content is now text/html
        #msg.send()

        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()


    #send_mass_mail(messages)
    return redirect('daily_orders')
    return redirect('message_sent')


@login_required
def message_sent(request):
    return render(request, 'orders/message_sent.html')

