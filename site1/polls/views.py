from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from .models import question, choice
from django.urls import reverse
from django.views import generic

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = question
    template_name = 'polls/details.html'


class ResultsView(generic.DetailView):
    model = question
    template_name = 'polls/results.html'

def vote(request, question_id):
    q = get_object_or_404(question, pk=question_id)
    try:
        selected_choice = q.choice_set.get(pk=request.POST['choice'])
    except (KeyError, choice.DoesNotExist):
        # redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question' : q,
            'error_message' : "You didn't select a choice.",
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(         q.id,)))
