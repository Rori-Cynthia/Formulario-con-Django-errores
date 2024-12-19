from django.shortcuts import render
from .forms import BookForm

def input_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html', {'title': form.cleaned_data['title']})
    else:
        form = BookForm()

    return render(request, 'inputbook.html', {'form': form})
