from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import createuserform


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = createuserform(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('login')
    else:
        form = createuserform()
    context = {
        'form':form,
        }
    return render(request, 'user/register.html',context)

