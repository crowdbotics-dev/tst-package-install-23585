from django.shortcuts import render


def home(request):
    packages = [
	{'name':'blognajd', 'url': 'http://pypi.python.org/pypi/blognajd/1.1.1'},
	{'name':'blocky', 'url': 'http://pypi.python.org/pypi/blocky/0.0.2'},
	{'name':'BlazeForm', 'url': 'http://pypi.python.org/pypi/BlazeForm/0.4.1'},
	{'name':'blee.icmPlayer', 'url': 'http://pypi.python.org/pypi/blee.icmPlayer/0.1'},
	{'name':'django-allauth', 'url': 'https://pypi.org/project/django-allauth/0.38.0/'},
	{'name':'django-bootstrap4', 'url': 'https://pypi.org/project/django-bootstrap4/0.0.7/'},
	{'name':'djangorestframework', 'url': 'https://pypi.org/project/djangorestframework/3.9.0/'},
    ]
    context = {
        'packages': packages
    }
    return render(request, 'home/index.html', context)
