from django.views import generic
from . import models
from django.http import HttpResponseRedirect
from django.contrib import messages
from . import services

class TestList(generic.TemplateView):
    template_name = 'test/test_list.html'


    def get_context_data(self, **kwargs):
        context = services.get_visible_test()
        context['recruit_id'] = self.kwargs.get('recruit_id')
        return context

class QuestionList(generic.TemplateView):
    template_name = 'test/question_list.html'

    def get_context_data(self, **kwargs):
        context = services.get_test_questions(self.kwargs.get('test_id'))
        print(context)
        return context
        
    def post(self, request, *args, **kwargs):
        recruit = self.kwargs.get('recruit_id')
        test = self.kwargs.get('test_id')
        save_test_result = services.save_test_answers(recruit, test, request)
        if save_test_result[1] == True: # Проверка сохрания результат, если тест, с таким id уже был выполненым данным рекрутом, то функция вернет этот объект и False
            messages.info(request, 'Ответы на тест сохранены')
        else:
            messages.info(request, 'Ошибка')
        return HttpResponseRedirect('/')