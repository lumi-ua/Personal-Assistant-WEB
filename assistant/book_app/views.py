from datetime import datetime, timedelta

from django.db import IntegrityError
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator

from .models import Nickname, Name, Surname, Email, Birthday, Address, Country


# Create your views here.
def main(request):
    nicknames = Nickname.objects.all()
    paginator = Paginator(nicknames, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'book_app/index.html', {"page_obj": page_obj})


def contact(request):
    try:
        if request.method == 'POST':
            nickname = request.POST['nickname']
            phone = request.POST['phone']
            if nickname and phone:
                nk = Nickname(nickname=nickname, phone=phone)
                nk.save()
            return redirect(to='/book_app/')
    except IntegrityError:
        return render(request, 'book_app/contact_err.html', {})
    return render(request, 'book_app/contact.html', {})


def nick_edit(request, nickname_id):
    try:
        nickname = Nickname.objects.get(pk=nickname_id)
        phone = Nickname.objects.get(pk=nickname_id)
        if request.method == 'POST':
            nickname.nickname = request.POST.get('nickname')
            nickname.phone = request.POST.get('phone')
            nickname.save()
            return redirect(to='/book_app/')
        else:
            return render(request, 'book_app/nick_edit.html', {"nickname": nickname, "phone": phone})
    except IntegrityError:
        return render(request, 'book_app/contact_err.html', {})
    except ObjectDoesNotExist:
        return HttpResponseRedirect("/book_app/")


# def info(request, nickname_id):
#     try:
#         nickname = Nickname.objects.get(pk=nickname_id)
#         phone = Nickname.objects.get(pk=nickname_id)
#         if request.method == 'POST':
#             name = request.POST['name']
#             surname = request.POST['surname']
#             email = request.POST['email']
#             birthday = request.POST['birthday']
#             country = request.POST['country']
#             address = request.POST['address']
#
#             if name:
#                 name_ = Name(pk=nickname_id, name=name)
#                 name_.save()
#
#             if surname:
#                 surname_ = Surname(pk=nickname_id, surname=surname)
#                 surname_.save()
#
#             if email:
#                 email_ = Email(pk=nickname_id, email=email)
#                 email_.save()
#
#             if birthday:
#                 birthday_ = Birthday(pk=nickname_id, birthday=birthday)
#                 birthday_.save()
#
#             if country:
#                 country_ = Country(pk=nickname_id, country=country)
#                 country_.save()
#
#             if address:
#                 address_ = Address(pk=nickname_id, address=address)
#                 address_.save()
#             return HttpResponseRedirect("/book_app/")
#         else:
#             return render(request, 'book_app/info.html', {"nickname": nickname, "phone": phone})
#     except ObjectDoesNotExist:
#         return HttpResponseRedirect("/book_app/")


def contact_edit(request, nickname_id):
    try:
        nickname = Nickname.objects.get(pk=nickname_id)
        phone = Nickname.objects.get(pk=nickname_id)
        if request.method == 'POST':
            name = request.POST['name']
            surname = request.POST['surname']
            email = request.POST['email']
            birthday = request.POST['birthday']
            country = request.POST['country']
            address = request.POST['address']

            if name:
                name_ = Name(pk=nickname_id, name=name)
                name_.save()

            if surname:
                surname_ = Surname(pk=nickname_id, surname=surname)
                surname_.save()

            if email:
                email_ = Email(pk=nickname_id, email=email)
                email_.save()

            if birthday:
                birthday_ = Birthday(pk=nickname_id, birthday=birthday)
                birthday_.save()

            if country:
                country_ = Country(pk=nickname_id, country=country)
                country_.save()

            if address:
                address_ = Address(pk=nickname_id, address=address)
                address_.save()
            return HttpResponseRedirect("/book_app/")
        else:
            return render(request, 'book_app/contact_edit.html', {"nickname": nickname, "phone": phone})
    except IntegrityError:
        err = "Email is exist, try enter another email..."
        return render(request, 'book_app/contact_edit.html', {"nickname": nickname, "phone": phone, "error": err})
    except ObjectDoesNotExist:
        return HttpResponseRedirect("/book_app/")


def detail(request, nickname_id):
    nickname = Nickname.objects.get(pk=nickname_id)
    phone = Nickname.objects.get(pk=nickname_id)

    try:
        name = Name.objects.get(pk=nickname_id)
    except ObjectDoesNotExist:
        name = None

    try:
        surname = Surname.objects.get(pk=nickname_id)
    except ObjectDoesNotExist:
        surname = None

    try:
        email = Email.objects.get(pk=nickname_id)
    except ObjectDoesNotExist:
        email = None

    try:
        birthday = Birthday.objects.get(pk=nickname_id)
    except ObjectDoesNotExist:
        birthday = None

    try:
        country = Country.objects.get(pk=nickname_id)
    except ObjectDoesNotExist:
        country = None

    try:
        address = Address.objects.get(pk=nickname_id)
    except ObjectDoesNotExist:
        address = None

    return render(request, 'book_app/detail.html', {"nickname": nickname, "phone": phone, "name": name,
                                                    "surname": surname, "email": email, "birthday": birthday,
                                                    "country": country, "address": address})


def delete_name(request, nickname_id):
    try:
        name = Name.objects.get(pk=nickname_id)
        name.delete()
    except ObjectDoesNotExist:
        name = None

    return detail(request, nickname_id)


def delete_surname(request, nickname_id):
    try:
        surname = Surname.objects.get(pk=nickname_id)
        surname.delete()
    except ObjectDoesNotExist:
        surname = None

    return detail(request, nickname_id)


def delete_email(request, nickname_id):
    try:
        email = Email.objects.get(pk=nickname_id)
        email.delete()
    except ObjectDoesNotExist:
        email = None

    return detail(request, nickname_id)


def delete_birthday(request, nickname_id):
    try:
        birthday = Birthday.objects.get(pk=nickname_id)
        birthday.delete()
    except ObjectDoesNotExist:
        birthday = None

    return detail(request, nickname_id)


def delete_country(request, nickname_id):
    try:
        country = Country.objects.get(pk=nickname_id)
        country.delete()
    except ObjectDoesNotExist:
        country = None

    return detail(request, nickname_id)


def delete_address(request, nickname_id):
    try:
        address = Address.objects.get(pk=nickname_id)
        address.delete()
    except ObjectDoesNotExist:
        address = None

    return detail(request, nickname_id)


def delete_all(request, nickname_id):
    try:
        nickname = Nickname.objects.get(pk=nickname_id)
        nickname.delete()
    except ObjectDoesNotExist:
        nickname = None

    try:
        phone = Nickname.objects.get(pk=nickname_id)
        phone.delete()
    except ObjectDoesNotExist:
        phone = None

    try:
        name = Name.objects.get(pk=nickname_id)
        name.delete()
    except ObjectDoesNotExist:
        name = None

    try:
        surname = Surname.objects.get(pk=nickname_id)
        surname.delete()
    except ObjectDoesNotExist:
        surname = None

    try:
        email = Email.objects.get(pk=nickname_id)
        email.delete()
    except ObjectDoesNotExist:
        email = None

    try:
        birthday = Birthday.objects.get(pk=nickname_id)
        birthday.delete()
    except ObjectDoesNotExist:
        birthday = None

    try:
        country = Country.objects.get(pk=nickname_id)
        country.delete()
    except ObjectDoesNotExist:
        country = None

    try:
        address = Address.objects.get(pk=nickname_id)
        address.delete()
    except ObjectDoesNotExist:
        address = None

    return redirect(to='/book_app/')


def search_contact(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        nicknames = Nickname.objects.filter(
            Q(nickname__icontains=query) | Q(phone__icontains=query)
        )
    else:
        nicknames = []
    return render(request, 'book_app/search_results.html', {'nicknames': nicknames})

# def search_contact(request):
#     if request.method == 'GET':
#         query = request.GET.get('q')
#         nicknames = Nickname.objects.filter(nickname__icontains=query)
#     else:
#         nicknames = []
#     return render(request, 'book_app/search_results.html', {'nicknames': nicknames})


def day_to_birthday(request):
    try:
        date_now = datetime.now().date()
        days = []
        all_contacts = Nickname.objects.all()
        for user in all_contacts:
            users = {}
            users['nickname'] = Nickname.objects.get(pk=user.id)
            users['birthday'] = Birthday.objects.get(pk=user.id)
            date_birth = users['birthday']
            date = datetime(date_now.year, date_birth.birthday.month, date_birth.birthday.day)
            date_n = datetime.strftime(date, '%Y-%m-%d')
            happy = datetime.strptime(date_n, '%Y-%m-%d') - datetime.strptime(str(date_now), '%Y-%m-%d')
            if happy.days < 0:
                users['happy'] = happy + timedelta(days=365)
            else:
                users['happy'] = happy
            days.append(users)
        return render(request, 'book_app/day_to_birthday.html', {'days': days})
    except ObjectDoesNotExist:
        return render(request, 'book_app/day_to_birthday.html', {'days': days})
