from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import InputForm
from .models import Input
import json

# Create your views here.

def get_tokens(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            element = form.save()
            return redirect(reverse('tokens', kwargs = {'pk': element.id}))
    else:
        form = InputForm()
    return render(request, 'tokeniser/form.html', {'form': form})

def show_tokens(request, pk):
    entry = Input.objects.get(id=pk)
    tokens = json.loads(entry.tokenised_text)
    context = {'tokens': tokens}
    return render(request, 'tokeniser/output.html', context)