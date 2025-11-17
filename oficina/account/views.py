from django.shortcuts import render, HttpResponse
from account.forms import AccountSignupForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
User = get_user_model()

class AccountCreateView(CreateView):
    model = User
    template_name = 'registration/signup_form.html'
    form_class = AccountSignupForm
    success_url = reverse_lazy('index')
    def form_valid(self, form):
        form.instance.password = make_password(form.instance.password)
        form.save()
        
        return super(AccountCreateView, self).form_valid(form)
#Create your views here.
def login(request):
    return HttpResponse("teste")