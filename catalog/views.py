from django.shortcuts import render
from catalog.models import Product, Contact


def catalog_home(request):
    print(Product.objects.all()[:5])
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя - {name}\nТелефон - {phone}\nСообщение - {message}')

    contact = Contact.objects.order_by('pk').reverse()[0]
    data = {'country': contact.country,
            'inn': contact.inn,
            'address': contact.address}

    return render(request, 'catalog/contacts.html', context=data)
