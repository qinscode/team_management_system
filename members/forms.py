from django import forms
from .models import TeamMember

class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['first_name', 'last_name', 'email', 'role', 'bio', 'is_active']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        } 