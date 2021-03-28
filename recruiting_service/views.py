from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from . import models
from . import services
from test_service import services as test_services


class Main(generic.TemplateView):
    template_name = 'main/main.html'

    def get_context_data(self, **kwargs):
        context = services.get_sith_shadow_hands_count()
        return context


class SithList(generic.ListView):
    model = models.Sith
    template_name = 'sith/sith_list.html'

    context_object_name = 'siths'


class RecruitCreate(generic.CreateView):
    model = models.Recruit
    template_name = 'recruit/recruit_create.html'

    fields = [
        'name',
        'planet',
        'age',
        'email',
    ]

    def get_success_url(self):
        return reverse('test_service:test_list', args=(self.object.id,))


class RecruitList(generic.TemplateView):
    template_name = 'recruit/recruit_list.html'

    def get_context_data(self, **kwargs):
        context = services.get_recruit_list_for_enrollment()
        context['sith_id'] = self.kwargs.get('sith_id')
        return context


class RecruitEnrollment(generic.TemplateView):
    template_name = 'recruit/recruit_enrollment.html'

    def get_context_data(self, **kwargs):
        context = test_services.get_recruit_answers(self.kwargs.get('recruit_id'))
        return context
        
    def post(self, request, *args, **kwargs):
        recruit = self.kwargs.get('recruit_id')
        sith = self.kwargs.get('sith_id')
        result = services.recruit_enrollment(recruit, sith)
        if result[1] == True: # Проверка на зачисление, если рекрут, с таким id уже был зачислен функция вернет этот объект и False
            messages.info(request, 'Рекрут успешно зачислен')
        else:
            messages.info(request, 'Ошибка')
        return HttpResponseRedirect('/')
