from django.shortcuts import render, redirect
from .forms import ParserForm
from .parsers import parse
from .models import Book
from django.contrib.auth.decorators import login_required


@login_required
def parsing(request):
    if request.method == 'POST':
        user = request.user
        form = ParserForm(request.user ,request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            parse.delay(url, user.email)
            return redirect('profile')
    else:
        form = ParserForm(request.POST)
    return render(request, 'bookmarks/add.html', {'form_add':form})

