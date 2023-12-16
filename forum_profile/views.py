from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from forum_profile.forms import ProfileCreationForm
from forum_profile.models import Profile


class ProfileCreateView(CreateView, LoginRequiredMixin):
    model = Profile
    form_class = ProfileCreationForm
    template_name = 'forum_profile/create_profile.html'
    success_url = reverse_lazy('profile:create')

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user = self.request.user
        profile.save()
        return redirect(self.success_url)
