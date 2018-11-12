from django.urls import path
from . import views
# 현재 폴더에 있는 views 파일 추가
app_name = 'todo'

urlpatterns = [
    # 이 아래 들어가는 url들의 앞에 todos/가 생략
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
    path('<int:id>/', views.read),
    path('todo_create/', views.todo_create),
    path('<int:id>/update/', views.update, name='update'),
    path('<int:id>/delete/', views.delete, name='delete'),
]