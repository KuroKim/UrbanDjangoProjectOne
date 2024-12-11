from django.shortcuts import render
from django.http import HttpResponse
from task5.forms import UserRegister

users = ['bobr', 'kurwa', 'perdole']


def sign_up_by_django(request):
    info = {'form': UserRegister(), 'method': 'django'}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password_repeat = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != password_repeat:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                users.append(username)
                return HttpResponse(f'Приветствуем, {username}!')
        info['form'] = form
    return render(request, 'fifth_task/reg_page.html', info)


def sign_up_by_html(request):
    info = {'method': 'html'}
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password_repeat = request.POST.get('repeat_password', '')
        age = int(request.POST.get('age', 0))

        if password != password_repeat:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            users.append(username)
            return HttpResponse(f'Приветствуем, {username}!')

    return render(request, 'fifth_task/reg_page.html', info)
