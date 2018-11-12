from django.urls import path
from . import views
# 현재 폴더에 있는 views 파일 추가

urlpatterns = [
    # 이 아래 들어가는 url들의 앞에 todos/가 생략
    path('', views.index),
    path('new/', views.new),
    path('create'),
]