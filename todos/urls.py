from django.urls import path
from todos import views

urlpatterns = [
    path('', views.TodoListView.as_view(), name='todo_list'),
    path('new/', views.TodoCreateView.as_view(), name='todo_new'),
    path('<int:pk>/edit/', views.TodoUpdateView.as_view(), name='todo_update'),
    path('<int:pk>/delete/', views.TodoDeleteView.as_view(), name='todo_delete'),
]
