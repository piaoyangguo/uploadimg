from django.shortcuts import render
from img.models import Tu
# Create your views here.
def index(request):
    res = {}
    tus = Tu.objects.all()
    res['tus'] = tus
    file = request.FILES.get("img", "")
    print file
    if file:
        name = request.FILES.get('img').name
        t = Tu()
        t.image = file
        t.name = name
        t.save()
    return render(request, 'index.html', res)