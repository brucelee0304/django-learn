# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
from models import Poll

def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = Context({
        'latest_poll_list': latest_poll_list,
    })
    return HttpResponse(template.render(context))

def detail(request, poll_id):
   context = {'poll_id': poll_id}
   return render(request, 'polls/detail.html', context)

def results(request, poll_id):

    id =request.GET['poll_id'];
    content = Context({
        'id':id,
        'poll_id':poll_id
    })

    return render(request,'polls/results.html',content)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)