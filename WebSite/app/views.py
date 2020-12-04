from django.shortcuts import render
import requests


# Create your views here.
def home_page(request, *args, **kwargs):
    context = {}
    data = []
    if request.method == 'POST':
        number = request.POST.get('number', 1)
        try:
            number = int(number)
        except:
            return render(request=request, template_name='HomePage.html', context=context, content_type=None,
                          status=None,
                          using=None)
        for i in range(0, number):
            data.append(request_api(int(i)))
            
        context['DATA'] = data

    return render(request=request, template_name='HomePage.html', context=context, content_type=None,
                  status=None,
                  using=None)


def request_api(number):
    respond = requests.get('https://pythonapp.ir/api/get?number={}'.format(str(number))).json()
    return respond
