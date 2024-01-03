# django
django template for new projects with minimum dependencies

- django 5
- python 3.12
- postgresql
- redis

```
.
├── .editorconfig
├── .github
│   └── workflows
│       ├── docker.yml
│       └── main.yml
├── .gitignore
├── Dockerfile
├── LICENSE
├── Makefile
├── README.md
├── compose.yaml
├── requirements.prod.txt
├── requirements.txt
└── src
    ├── core
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings
    │   │   ├── __init__.py
    │   │   ├── base.py
    │   │   ├── ci.py
    │   │   ├── dev.py
    │   │   ├── local.py
    │   │   ├── local.py.sample
    │   │   └── prod.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── identity
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── managers.py
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    └── manage.py

8 directories, 31 files
```
