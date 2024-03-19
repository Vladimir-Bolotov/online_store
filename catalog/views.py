from django.shortcuts import render
from catalog.models import Product, Contact, Category
from _datetime import date


def catalog_home(request):
    # print(Product.objects.all()[:5])
    context = {'title': 'Главная',
               'products': Product.objects.all()}
    return render(request, 'catalog/catalog.html', context)


def contacts(request):
    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     phone = request.POST.get('phone')
    #     message = request.POST.get('message')
    #     print(f'Имя - {name}\nТелефон - {phone}\nСообщение - {message}')

    context = {'contact': Contact.objects.order_by('pk').reverse()[0],
               'title': 'O нас'}

    return render(request, 'catalog/contacts.html', context=context)


def product(request, pk):
    context = {'product': Product.objects.get(pk=pk),
               'title': 'Информация о товаре'}
    return render(request, 'catalog/product.html', context)


def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.POST.get('image')
        category = request.POST.get('category')
        id_cetegory = Category.objects.get(name=category)

        Product.objects.create(name=name, price=price, description=description, image=image, category=id_cetegory,
                               created_at=date.today(), updated_at=date.today())

    context = {'categories': Category.objects.all(),
               'title': 'Добавить товар'}
    return render(request, 'catalog/add_product.html', context)
