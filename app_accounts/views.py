from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.views import View
from testcase import settings


def registration(request):
    if request.method == 'POST':
        reg_form = CustomUserCreationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            return redirect('main_page')
    else:
        reg_form = CustomUserCreationForm()
    return render(request, 'account/registration.html', {'registration_form': reg_form})


class UserView(View):

    def get_object(self):
        return self.request.user

    def get(self, request):
        print(settings.BASE_DIR)
        user = self.get_object()
        books = user.books.all()
        return render(request, 'account/profile.html', {'user':user, 'books':books})


