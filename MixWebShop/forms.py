from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from .models import Profile
from django import forms
from django.db import models


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta(UserCreationForm.Meta):
        # constraints = [
        #     models.UniqueConstraint(fields=['username',
        #                                     'first_name',
        #                                     'last_name',
        #                                     'email'], name='unique in here')
        # ]
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email']

    def save(self, commit=True):
        self.instance.is_active = True

        saved_user = super().save(commit)

        simple_group = Group.objects.get(name='simple')
        saved_user.groups.add(simple_group)
        saved_user.save()

        Profile.objects.create(user=saved_user)

        return saved_user
