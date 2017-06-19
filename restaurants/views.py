from bs4 import BeautifulSoup
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ImportMenuForm
from .models import Restaurant, Category, Dish


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

                category_box = meal.find_previous('div', class_='menu-meals-group')
                category_head = category_box.find('div', class_="menu-category-head")
                category_name = category_head.find('span').text

                # save data
                cat, cat_created = Category.objects.get_or_create(name=category_name, restaurant=restaurant)
                dish, dish_created = Dish.objects.get_or_create(name=dish, price=price, restaurant=restaurant)
                dish.categories.add(cat)

            return HttpResponseRedirect('import_menu')

    else:
        form = ImportMenuForm()

    return render(request, 'restaurants/import_menu.html', {'form': form})