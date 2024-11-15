from .models import TeamMember

def team_stats(request):
    return {
        'total_members': TeamMember.objects.count()
    } 