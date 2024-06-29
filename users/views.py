from django.shortcuts import render , redirect
from django.views import View
from .forms import UserCrationForm
from django.contrib.auth import authenticate, login , logout

class LogoutView(View):
    template_name = 'registration/logout.html'

    def get(self, request):
        return render(request,self.template_name)
    
    def post(self, request):
        if request.method == 'POST':
            logout(request)
            return redirect('/')

class Registr(View):
    template_name = 'registration/registr.html'
    forms = UserCrationForm()
    def get(self, request):
        context = {
            "form":UserCrationForm()
        }
        return render(request,self.template_name, context)

    def post(self, request):
        form = UserCrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('login')
        context = {
            "form":form
        }
        return render(request,self.template_name, context)
    
