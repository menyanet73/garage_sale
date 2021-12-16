from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls.base import reverse
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import CreationForm, UserProfileForm
from .models import UserProfile


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('users:profile_update')
    template_name = 'users/signup.html'


@login_required
def profile_update(request):
    profile = UserProfile(user=request.user)
    form = UserProfileForm(
        request.POST or None,
        files=request.FILES or None,
        instance=profile
    )
    if form.is_valid():
        form.save()
        #TODO Заменить редирект
        return redirect('saleboard:index')
    context = {
        'title': 'Редактирование профиля',
        'form': form,
    }
    return render(request, 'users/profile_update.html', context)


def profile(request, username):
    if request.user.username != username:
        return redirect(reverse('saleboard:index'))
    profile = get_object_or_404(UserProfile, user__username=username)
    context = {
        'title': '',
        'profile': profile
    }
    return render(request, 'users/profile.html', context)
