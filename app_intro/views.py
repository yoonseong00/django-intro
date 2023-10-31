from django.shortcuts import render
import random
from faker import Faker

# Create your views here.

def index(request):
    return render(request, 'index.html')

def hello(request):
    username = '김윤성'

    result = {
        'username' : username,
    }

    return render(request, 'hello.html', result)

def dinner(request):
    menus = ['치킨', '피자', '돈까스']

    pick = random.choice(menus)

    result = {
        'pick' : pick,
    }

    return render(request, 'dinner.html', result)

def lotto(request):
    lottos = [i for i in range(1, 46)]

    pick = random.sample(lottos, 6)

    result = {
        'pick' : pick
    }

    return render(request, 'lotto.html', result)

def greeting(request, name):

    result = {
        'name' : name,
    }

    return render(request, 'greeting.html', result)

def cube(request, num):
    result = {
        'num' : num,
        'cube' : num ** 3,
    }

    return render(request, 'cube.html', result)

def posts(request):
    posts = []
    fake = Faker()

    for i in range(100):
        posts.append(fake.text())

    result = {
        'posts' : posts,
    }

    return render(request, 'posts.html', result)