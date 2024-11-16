from django import forms
from .models import Contact, TechStack, TechSkill


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = [
            "first_name",
            "last_name",
            "email",
            "subject",
            "message"
        ]

class ToolForm(forms.ModelForm):

    class Meta:
        model = TechStack
        fields = [
            "tool",
            "preferred_color"
        ]

class SkillForm(forms.ModelForm):

    class Meta:
        model = TechSkill
        fields = [
            "skill",
            "progress"
        ]

