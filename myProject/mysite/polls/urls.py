from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('details/<int:poll_id>/', views.details, name='poll_detail'),
    path('create/', views.create, name='create_poll'),
    path('login/', views.my_login, name='login'),
    path('logout/', views.my_logout, name='logout'),
    path('update/<int:poll_id>', views.update, name='update_poll'),
    path('delete/<int:question_id>', views.delete_question, name='delete_question'),
    path('<int:question_id>/add-choice', views.add_choice, name='add_choice'),
    path('api/<int:question_id>/add-choice', views.add_choice_api, name='add_choice_api')
]