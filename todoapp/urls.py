from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home-page'),
    path('register', views.register, name='register-page'),
    path('login', views.login_page, name='login-page'),
    path('logout/', views.logout_view, name='logout'),
    path('create-task', views.create_task, name='create-task'),
    path('delete-task/<int:id>/', views.delete_task, name='delete'),
    path('update-status/<int:id>/', views.update_task, name='update'),
]
