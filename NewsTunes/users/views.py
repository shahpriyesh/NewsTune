# users/views.py
from django.shortcuts import render
from django.template import RequestContext
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.shortcuts import redirect


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

@login_required
def profile(request, template_name='profile.html'):
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, template_name, locals())
