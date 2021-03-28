from .models import Answer, Test, Result


def get_recruit_answers(recruit_id):
    """Получение ответов рекрута на все испытания по индетификатору recruit_id"""
    recruit_answers = Answer.objects.filter(
        recruit_id=recruit_id)
    data = {
        'recruit_answers': recruit_answers,
    }

    return data


def get_visible_test():
    """Получение тестов доступных для отображения"""
    visible_tests = Test.objects.filter(is_visible=True)

    data = {
        'visible_tests': visible_tests,
    }

    return data


def get_test_questions(test_id):
    """Получение вопрос теста по индетификатору test_id"""
    test = Test.objects.get(id=test_id)
    data = {
        'test': test,
    }
    return data


def save_test_answers(recruit_id, test_id, request):
    """Сохранение ответа на вопросы теста"""
    test = Test.objects.get(id=test_id)
    for question in test.questions.all():
        Answer.objects.get_or_create(recruit_id=recruit_id, test_id=test_id,
                                     question_id=question.id, variant_id=request.POST.get(str(question.id)))
    save_test_result = Result.objects.get_or_create(
        recruit_id=recruit_id, test_id=test_id, mark_as_pass=True)
    return save_test_result
