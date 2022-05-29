from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user


@login_required
def somente_logado(request):

    user = get_user(request)

    return HttpResponse(f'O {user.username} esta logado')


def nao_logado(request):

    user = get_user(request)

    if user.is_authenticated:
        return HttpResponse(f'Erro, o {user.username} ainda esta logado')

    return HttpResponse('Você não esta logado')


def deslogado(request):

    user = get_user(request)

    if user.is_authenticated:
        return HttpResponse(f'Erro, o {user.username} ainda esta logado')

    return HttpResponse('Você se deslogou')
