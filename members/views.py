from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import TeamMember
from .forms import TeamMemberForm

class MemberListView(ListView):
    model = TeamMember
    template_name = 'members/member_list.html'
    context_object_name = 'members'

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
    return render(request, 'members/about.html', {
        'version': '1.0.0',
        'team_size': TeamMember.objects.count()
    }) 