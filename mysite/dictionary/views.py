from django.shortcuts import render
from django.utils import timezone
from .models import Word
# Create your views here.

def word_list(request):
    words = Word.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'index.html', {'words': words})