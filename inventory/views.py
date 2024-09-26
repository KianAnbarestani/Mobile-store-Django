from django.shortcuts import render, redirect, get_object_or_404
from .models import Brand, Phone
from .forms import BrandForm, PhoneForm
from django.db.models import Q


def brand_list(request):
    brands = Brand.objects.all().order_by('id') 
    return render(request, 'inventory/brand_list.html', {'brands': brands})

def phone_list(request):
    query = Q()
    q = request.GET.get('q', '')
    brand = request.GET.get('brand')
    nationality = request.GET.get('nationality')
    manufacturing_country = request.GET.get('manufacturing_country')
    color = request.GET.get('color')
    screen_size = request.GET.get('screen_size')
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')

    if q:
        query &= (Q(brand__name__icontains=q) | Q(model__icontains=q) | Q(color__icontains=q) | Q(manufacturer_country__icontains=q) | Q(screen_size__icontains=q) | Q(price__icontains=q))

    if brand:
        query &= Q(brand__name__icontains=brand)
    if nationality:
        query &= Q(brand__nationality__icontains=nationality)
    if manufacturing_country:
        query &= Q(manufacturer_country__icontains=manufacturing_country)
    if color:
        query &= Q(color__icontains=color)
    if screen_size:
        query &= Q(screen_size=screen_size)
    if price_min:
        query &= Q(price__gte=price_min)
    if price_max:
        query &= Q(price__lte=price_max)

    phones = Phone.objects.filter(query).order_by('id')  
    return render(request, 'inventory/phone_list.html', {'phones': phones})

def add_brand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('brand_list')
    else:
        form = BrandForm()
    return render(request, 'inventory/add_brand.html', {'form': form})

def add_phone(request):
    if request.method == 'POST':
        form = PhoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('phone_list')
    else:
        form = PhoneForm()
    return render(request, 'inventory/add_phone.html', {'form': form})

def update_phone(request, pk):
    phone = get_object_or_404(Phone, pk=pk)
    if request.method == 'POST':
        form = PhoneForm(request.POST, instance=phone)
        if form.is_valid():
            form.save()
            return redirect('phone_list')
    else:
        form = PhoneForm(instance=phone)
    return render(request, 'inventory/update_phone.html', {'form': form, 'phone': phone})

def delete_phone(request, pk):
    phone = get_object_or_404(Phone, pk=pk)
    if request.method == 'POST':
        phone.delete()
        return redirect('phone_list')
    return render(request, 'inventory/delete_confirm.html', {'object': phone})

def update_brand(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    if request.method == 'POST':
        form = BrandForm(request.POST, instance=brand)
        if form.is_valid():
            form.save()
            return redirect('brand_list')
    else:
        form = BrandForm(instance=brand)
    return render(request, 'inventory/update_brand.html', {'form': form, 'brand': brand})

def delete_brand(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    if request.method == 'POST':
        brand.delete()
        return redirect('brand_list')
    return render(request, 'inventory/delete_confirm.html', {'object': brand})
