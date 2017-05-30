from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from orders.models import Order
from datetime import date
from django.views.generic import CreateView


@login_required
def home(request):
    #uo_all = Order.objects.filter(user__username=request.user)
    #uo_prev = uo_all.exclude(settings__order_date__gte=date.today())
    uo = Order.objects.filter(user__username=request.user).filter(settings__order_date__gte=date.today())
    return render(request, "user/home.html", {'uo': uo})


class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'user/registration.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data('username')
            password = form.cleaned_data('password')
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('user_home')

        return render(request, self.template_name, {'form': form})



