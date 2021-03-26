from django.urls import path
from recruiting_service.views import Main, SithList, RecruitAdd, TestList, QuestionList, RecruitList, RecruitAnswer

urlpatterns = [
    path('', Main.as_view(), name = 'main'),
    path('sith/', SithList.as_view(), name = 'sith'),
    path('sith/<int:sith_id>', RecruitList.as_view(), name = 'recruits'),
    path('recruit-answer/<int:sith_id>/<int:recruit_id>/', RecruitAnswer.as_view(), name = 'recruit-answers'),
    path('recruit/', RecruitAdd.as_view(), name = 'recruit'),
    path('tests/<int:recruit_id>', TestList.as_view(), name = 'tests'),
    path('test/<int:recruit_id>/<int:test_id>/', QuestionList.as_view(), name = 'test'),

]