from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.db.models import Count
from .models import TeamMember
from .forms import TeamMemberForm

class MemberListView(ListView):
    model = TeamMember
    template_name = 'members/member_list.html'
    context_object_name = 'members'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_members'] = TeamMember.objects.filter(is_active=True).count()
        context['unique_roles'] = TeamMember.objects.values('role').distinct().count()
        context['all_roles'] = TeamMember.objects.values_list('role', flat=True).distinct()
        return context

class MemberDetailView(DetailView):
    model = TeamMember
    template_name = 'members/member_detail.html'

class MemberCreateView(CreateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'members/member_form.html'
    success_url = reverse_lazy('member-list')

class MemberUpdateView(UpdateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'members/member_form.html'
    success_url = reverse_lazy('member-list')

def about_view(request):
    total_members = TeamMember.objects.count()
    return render(request, 'members/about.html', {
        'version': '2.0.0',
        'team_size': total_members
    }) 