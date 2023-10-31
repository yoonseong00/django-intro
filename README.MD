# django

1. 프로젝트 생성

```
django-admin startproject <pjtname> .
```

2. 가상환경 설정
```
python -m venv venv
```

3. 가상환경 활성화/비활성화
```
<!-- window -->
source venv/Scripts/activate
<!-- macOS -->
source venv/bin/activate

deactivate
```

4. 가상환경 내부에 django 설치
```
pip install django
```

5. 서버 실행 확인(종료 `Ctrl + c`)
```
python manage.py runserver
```

6. 앱생성
```
django-admin startapp <appname>
```

7. 앱등록
- `settings.py`의 `INSTALLED_APPS` 에 등록
    `<appname>`을 등록

8. `urls.py`
```python
from django.urls import path
from app_intro import views

urlpatterns = [
    ...
    path('index/', views.index),
]

```

9. `views.py`
```python
def index(request):
    return render(reqeust, 'index.html')
```

10. templates 폴더 생성 => index.html 생성

## MTV

![MTV](./assets/MTV.PNG)



# django 팁


- 이름.html안에서 for문 돌리는 방법
```
{% for 데이터 in {돌리고자하는 리스트} %}
{% endfor %}  <-- endfor을 통해 for문이 끝났다는걸 선언

만약 리스트가 인덱스인데 깔끔하게 보여주고 싶으면
{% for 데이터 in {돌리고자하는 리스트} %}
<div class="alert alert-primary">{{데이터}}</div>      <-- 이런식으로 for문 사이에 class 추가
{% endfor %}  <-- endfor을 통해 for문이 끝났다는걸 선언
```