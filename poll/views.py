from django.shortcuts import render, get_object_or_404, redirect
from poll.models import Question, Choice

def home_page_view(request):
    template_name = 'home.html'
    return render(request, template_name)

def poll_list_page_view(request):
    question = Question.objects.all()
    template_name = 'poll/poll_list.html'
    context = {
        'question': question,
    }
    return render(request, template_name, context)

def vote_page_view(request, pk):
    question = get_object_or_404(Question, id=pk)
    options = request.POST.getlist('choice')
    if len(options) == 0:
        template_name = 'poll/vote.html'
        context = {
            'question': question,
        }
        return render(request, template_name, context)
    else:
        for item in options:
            selected_choice = question.choice_set.get(pk=item)
            selected_choice.votes += 1
            selected_choice.save()
        return redirect('detials', pk)

def poll_details_page_view(request, pk):
    question = get_object_or_404(Question, id=pk)
    template_name = 'poll/details.html'
    context = {
        'question': question,
    }
    return render(request, template_name, context)

