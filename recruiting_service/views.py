from django.shortcuts import render
from django.views import generic
from .models import Recruit, Test, Sith, Answer, Question, Variant, Result, ShadowHand
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Count


class Main(generic.ListView):
    model = ShadowHand
    template_name = 'main/main.html'

    context_object_name = 'shadowhands'

    def get_context_data(self, **kwargs):
        context = super(Main, self).get_context_data(**kwargs)
        siths = Sith.objects.all()
        shadowhand_counts = ShadowHand.objects.values('sith').annotate(total = Count('id'))
        context['shadowhand_counts'] = shadowhand_counts
        context['siths'] = siths
        
        return context

class RecruitAdd(generic.CreateView):
    model = Recruit
    template_name = 'recruit/recruit.html'

    fields = [
        'name',
        'planet',
        'age',
        'email',
    ]

    def get_success_url(self):
        return reverse('tests', args=(self.object.id,))


class RecruitList(generic.ListView):
    model = Recruit
    template_name = 'recruit/recruit_list.html'

    context_object_name = 'recruits'

    def get_context_data(self, **kwargs):
        context = super(RecruitList, self).get_context_data(**kwargs)
        test_result = Result.objects.all().values_list('recruit_id', flat=True)
        shadowhands = ShadowHand.objects.all().values_list('recruit_id', flat=True)
        context['recruits'] = Recruit.objects.filter(id__in = test_result).exclude(id__in = shadowhands)
        context['sith_id'] = self.kwargs.get('sith_id')
        return context

class RecruitAnswer(generic.ListView):
    model = Answer
    template_name = 'recruit/recruit_answer.html'

    context_object_name = 'answers'

    def get_context_data(self, **kwargs):
        context = super(RecruitAnswer, self).get_context_data(**kwargs)
        context['answers'] = Answer.objects.filter(recruit_id = self.kwargs.get('recruit_id'))
        return context

    def post(self, request, *args, **kwargs):
        recruit = self.kwargs.get('recruit_id')
        sith = self.kwargs.get('sith_id')
        check_shadowhand = ShadowHand.objects.filter(recruit_id = recruit).exists()
        count_shadowhands = ShadowHand.objects.filter(sith_id = sith).count()
        if check_shadowhand == False:
            shadowhand = ShadowHand()
            shadowhand.recruit_id = recruit
            shadowhand.sith_id = sith
            shadowhand.save()
            messages.info(request, 'Рекрут зачислен Рукой тени')
        else:
            if check_shadowhand != False:
                messages.info(request, 'Рекрут уже зачислен Рукой тени')
            else:
                messages.info(request, 'У вас 3 руки тени.')
        return HttpResponseRedirect('/')

class SithList(generic.ListView):
    model = Sith
    template_name = 'sith/sith.html'

    context_object_name = 'siths'


class TestList(generic.ListView):
    model = Test
    template_name = 'test/tests.html'

    context_object_name = 'tests'

    def get_context_data(self, **kwargs):
        context = super(TestList, self).get_context_data(**kwargs)
        
        context['tests'] = Test.objects.filter(visible=True)
        context['recruit_id'] = self.kwargs.get('recruit_id')
        return context


class QuestionList(generic.base.TemplateResponseMixin, generic.list.BaseListView):
    model = Question
    template_name = 'test/question_list.html'


    def get_context_data(self, **kwargs):
        context = super(QuestionList, self).get_context_data(**kwargs)
        test = Test.objects.get(id=self.kwargs.get('test_id'))
        questions = Question.objects.filter(id__in=test.question.all())
        context['questions'] = questions
        context['variants'] = Variant.objects.filter(question__in=questions)
        return context

    def post(self, request, *args, **kwargs):
        recruit = self.kwargs.get('recruit_id')
        tests = self.kwargs.get('test_id')
        test = Test.objects.get(id = tests)
        check_pass = Result.objects.filter(test_id = test, recruit_id = recruit).exists()
        if check_pass == False:
            for question in test.question.all():
                answer = Answer()
                answer.recruit_id = recruit
                answer.test_id = tests
                answer.question_id = question.id
                answer.variant_id = request.POST.get(str(question.id))
                answer.save()
            result = Result()
            result.recruit_id = recruit
            result.test_id = tests
            result.mark_as_pass = True
            result.save()
            messages.info(request, 'Ответы на тест сохранены')
        else:
            messages.info(request, 'Тест уже пройден')
        return HttpResponseRedirect('/')
        


