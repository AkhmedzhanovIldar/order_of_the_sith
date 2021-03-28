from django.urls import path
from . import views

app_name='test_service'
urlpatterns = [
    path('test_list/<int:recruit_id>/', views.TestList.as_view(), name='test_list'),
    path('question_list/<int:recruit_id>/<int:test_id>/', views.QuestionList.as_view(), name = 'question_list'),
]
#