from django.shortcuts import render
from base.models import Word
from django.db.models import Count
from base.forms import WordForm

# This is to be used if web-server level blocking is not possible
BLOCKED_IP_LIST = []


# To get the IP of unwanted clients, in case blocking on web server level
# is not possible
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def base_view(request):
    form = WordForm()

    ip = get_client_ip(request)
    if ip in BLOCKED_IP_LIST:
        return render(request, 'index.html', {'form': form})

    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            obj = Word()
            word = form.cleaned_data['word'].lower()
            obj.word = word
            obj.save()
            count = len(Word.objects.filter(word=word.lower())) - 1 # To show words entered before 
            return render(request, 'index.html', {'form': form, 'count': count, 'word': word})

    elif request.method == 'GET':
        most_common_qs = Word.objects.all().values('word').annotate(total=Count('word')).order_by('-total')[:10]

        return render(request, 'index.html', {'form': form, 'most_common_qs': most_common_qs})

    return render(request, 'index.html', {'form': form})
