from django.shortcuts import render
from base.models import Word
from django.db.models import Count
from base.forms import WordForm


def base_view(request):
    form = WordForm()

    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            obj = Word()
            word = form.cleaned_data['word']
            obj.word = word.lower()
            obj.save()
            count = len(Word.objects.filter(word=word.lower())) - 1 # To show words entered before 
            return render(request, 'index.html', {'form': form, 'count': count})

    elif request.method == 'GET':
        most_common_qs = Word.objects.all().values('word').annotate(total=Count('word')).order_by('-total')[:10]

        return render(request, 'index.html', {'form': form, 'most_common_qs': most_common_qs})

    return render(request, 'index.html', {'form': form})
