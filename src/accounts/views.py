from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, GuestForm
from django.utils.http import is_safe_url
from .models import GuestEmail


def login_page(request):
    form = LoginForm(request.POST or None)

    args = {
        'form': form,
    }
    next_ = request.GET.get('next')
    post_next = request.POST.get('next')
    redirect_path = next_ or post_next or None
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                del request.session['guest_email_id'] 
            except:
                pass
            
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect('home')
            args['form'] = LoginForm()
        else:
            print('Error')
    return render(request, 'accounts/login_page.html', args)


User = get_user_model()


def register_page(request):
    form = RegisterForm(request.POST or None)

    args = {
        'form': form,
    }
    if form.is_valid():
        form.save()
    return render(request, 'accounts/register_page.html', args)

def guest_register_view(request):
    form = GuestForm(request.POST or None)
    c = {
        'form': form
    }
    next_ = request.GET.get('next')
    post_next = request.POST.get('next')
    redirect_path = next_ or post_next or None
    if form.is_valid():
        email = form.cleaned_data.get('email')
        new_guest_email = GuestEmail.objects.create(email = email)
        request.session['guest_email_id'] = new_guest_email.id
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect('/register/')
    return redirect('/register/')