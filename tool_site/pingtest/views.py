from django.shortcuts import render, redirect
from . import views
from .forms import PingForm
from . import ping

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = PingForm(request.POST)
        data = request.POST.copy()
        print(data)
        print(data['subnet'])
        print(data['start'])
        print(data['end'])
        # subnet = form.subnet
        # start = form.start
        # end = form.end
        # print(subnet, start, end)
        ping.onePing(data['subnet'],int(data['start']),int(data['end']))
        return redirect('ping-test')
    # if form.is_valid():
    #         pass  # does nothing, just trigger the validation
    else:
        form = PingForm()
    # form = PingForm()
    return render(request, 'pingtest/pingtest.html', {'form': form})

def run_test(request):
    print('test')