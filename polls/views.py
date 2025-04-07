'''
INF601 - Programming in Python
Assignment #
I,     Riley Weaver   , affirm that the work submitted for this assignment is entirely my own. I have not engaged in any form of
academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials. I have neither provided
 nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards. I understand that failing
 to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor
 and outlined in institutional policies. By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.
'''

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

def about(request):
    return render(request, 'polls/about.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('polls:login')
    else:
        form = UserCreationForm()
    return render(request, 'polls/register.html', {'form': form})