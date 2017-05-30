from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from orders.models import Order
from datetime import date
from django.views.generic import View


@login_required
def home(request):
    #uo_all = Order.objects.filter(user__username=request.user)
    #uo_prev = uo_all.exclude(settings__order_date__gte=date.today())
    uo = Order.objects.filter(user__username=request.user).filter(settings__order_date__gte=date.today())
    return render(request, "user/home.html", {'uo': uo})


class UserRegisterView(View):
    form_class = UserRegisterForm
    template_name = 'user/registration.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save()
            username = user.username
            password = user.password
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('user_home')

        return render(request, self.template_name, {'form': form})



