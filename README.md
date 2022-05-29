# Login logout Django

## Criando um usuario

```console
python manage.py shell
```

```python
>>> from django.contrib.auth.models import User
>>> user = User.objects.create_user('user', 'user@user.com', '1234')
```

Rotas:

* /login/
* /logout/
* /
* nao_logado/
* deslogou/
