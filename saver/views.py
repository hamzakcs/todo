from django.shortcuts import render, redirect
from .models import model
from .forms import form
from django.http import HttpResponseRedirect


# Create your views here.
def delete_data(request, data_id):
    model_data = model.objects.get(id=data_id)
    model_data.delete()
    return redirect('data')


def data(request):
    model_data = model.objects.all()
    submitted = False
    if request.method == 'POST':
        all_data = form(request.POST)
        if all_data.is_valid():
            all_data.save()
            return HttpResponseRedirect('/data?submitted=True')
    else:
        all_data = form(request.POST)
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'saver/data_show.html', {'all_data': all_data, 'submitted': submitted, 'model_data': model_data})
