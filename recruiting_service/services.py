from .models import ShadowHand, Recruit, Sith
from test_service.models import Result
from django.db.models import Count

def get_recruit_list_for_enrollment():
    """Получение списка рекрутов для зачисления Рукой тени"""
    test_result = Result.objects.all().values_list('recruit_id', flat=True)
    shadowhands = ShadowHand.objects.all().values_list('recruit_id', flat=True)
    recruits = Recruit.objects.filter(
            id__in=test_result).exclude(id__in=shadowhands)

    data = {
        'recruits':recruits,
    }

    return data

def get_sith_shadow_hands_count():
    """Получения Количества Рук Теней у каждого ситха"""
    shadowhand_counts = ShadowHand.objects.values(
            'sith').annotate(total=Count('id'))
    siths = Sith.objects.all()
    data = {
        'shadowhand_counts': shadowhand_counts,
        'siths': siths,
    }
    return data

def recruit_enrollment(recruit_id, sith_id):
    """Зачисление рекрута Рукой тени"""
    create_result = ShadowHand.objects.get_or_create(recruit_id=recruit_id, sith_id=sith_id)

    return create_result

