from bs4 import BeautifulSoup
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ImportMenuForm
from .models import Restaurant, Dish


@login_required
def import_menu(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = ImportMenuForm(request.POST)

        if form.is_valid():
            read_data = form.cleaned_data['menu_html_src']
            r_name = form.cleaned_data['restaurant']
            restaurant = Restaurant.objects.get(name=r_name)
            soup = BeautifulSoup(read_data, "html.parser")
            for meal in soup.find_all('div', attrs=('class', 'meal')):
                dish = meal.find('span', attrs=('class', 'meal-name')).text
                price = meal.find(attrs={"itemprop": "price"}).text

                price = float(price.replace(' zł', '').replace(',','.'))

                # save data
                Dish.objects.get_or_create(name=dish, price=price, restaurant=restaurant)

            return HttpResponseRedirect('import_menu')

    else:
        form = ImportMenuForm()

    return render(request, 'restaurants/import_menu.html', {'form': form})