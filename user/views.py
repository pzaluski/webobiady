from datetime import datetime

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


@login_required
def home(request):
    edit = False
    try:
        os = get_order_settings()
        now = datetime.now().time()
        if now < os.order_deadline:
            edit = True
        uo = Order.objects.get(user=request.user, settings=os)
    except ObjectDoesNotExist:
        return render(request, "user/home.html", {'edit': edit})
    return render(request, "user/home.html", {'uo': uo, 'edit': edit})


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
