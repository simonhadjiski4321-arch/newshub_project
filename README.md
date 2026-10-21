# NewsHub

NewsHub е уеб приложение за новини, създадено с Django.

## Функционалности

- Създаване, преглеждане, редактиране и изтриване на новини
- Категории и тагове към новините
- Търсене по заглавие и съдържание
- Филтриране по категория или таг
- Странициране на списъка с новини
- Коментари и отговори към коментари
- Редактиране и изтриване на коментари и отговори
- Създаване и преглед на категории и тагове през сайта
- Управление на категориите и таговете през Django Admin

## Изисквания

- Python
- Django, посочен в `requirements.txt`

## Стартиране в Windows PowerShell

Отвори PowerShell в папката на проекта и изпълни:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Ако `DJANGO_SECRET_KEY` още не е зададен, създай го локално:

```powershell
if (-not $env:DJANGO_SECRET_KEY) {
    $djangoSecret = python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
    [Environment]::SetEnvironmentVariable("DJANGO_SECRET_KEY", $djangoSecret, "User")
    $env:DJANGO_SECRET_KEY = $djangoSecret
}
```

Подготви базата и стартирай приложението:

```powershell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Отвори приложението на <http://127.0.0.1:8000/>.

## Django Admin

Административният панел е на <http://127.0.0.1:8000/admin/>. Влез с акаунта, създаден чрез `createsuperuser`, за да управляваш категориите и таговете.

## Приложения

- `news` — новини и формата за новина
- `comments` — коментари и отговори
- `catalog` — категории и тагове
