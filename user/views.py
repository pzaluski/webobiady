from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from main.utils import get_order_settings
from orders.models import Order
from .forms import PurchaserEditForm
from .models import UserProfile
from datetime import datetime


@login_required
def home(request):
    edit = False
    os = get_order_settings()
    now = datetime.now().time()
    today = datetime.today()
    if now < os.order_deadline:
        edit = True
    try:
        uo = Order.objects.get(
            user=request.user,
            date_created__year=today.year,
            date_created__month=today.month,
            date_created__day=today.day,
        )
    except ObjectDoesNotExist:
        return render(request, "user/home.html", {'edit': edit, 'restaurant': os.restaurant})
    return render(request, "user/home.html", {'uo': uo, 'edit': edit, 'restaurant': os.restaurant})


@method_decorator(login_required, name='dispatch')
class PurchaserEditView(UpdateView):
    model = UserProfile
    form_class = PurchaserEditForm
    template_name = "user/purchaser_edit.html"

    def get_success_url(self):
        return reverse('webobiady_home')

    def form_valid(self, form):
        profile = form.save()
        profile.save()

        return HttpResponseRedirect(self.get_success_url())
