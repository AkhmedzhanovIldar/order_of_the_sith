from django.urls import path
from . import views

app_name = 'recruiting_service'
urlpatterns = [
    path('', views.Main.as_view(), name='recruiting_service_main'),
    path('sith_list/', views.SithList.as_view(),
         name='recruiting_service_sith_list'),
    path('recruit_create/', views.RecruitCreate.as_view(),
         name='recruiting_service_recruit_create'),
    path('recruit_list/<int:sith_id>/',
         views.RecruitList.as_view(), name='recruit_list'),
    path('recruit_enrollment/<int:sith_id>/<int:recruit_id>/',
         views.RecruitEnrollment.as_view(), name='recruit_enrollment'),
]
