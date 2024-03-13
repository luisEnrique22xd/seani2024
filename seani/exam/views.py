from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Stage, Exam
from django.contrib.auth.models import User
from career.models import Career

from .forms import CandidateForm

def home(request):
    user = request.user
    return render(request, 'exam/home.html', {"user":user})

def question(request, m_id, q_id=1):
    user = request.user
    exam = user.exam

    if request.method == "POST":
        answer = request.POST['answer']
        questions = exam.breakdown_set.filter(question__module_id = m_id)
        question = questions[q_id-1]
        questions.answer = answer
        question.save()
        return redirect('exam:question', m_id, q_id+1)
    
    
    try: 
        questions = exam.breakdown_set.filter(question__module_id = m_id)
        question = questions[q_id-1].question
        answer = questions[q_id-1 ].answer
        return render(request, 
                  'exam/question.html',
                  {"question":question,
                   "m_id": m_id,
                   "q_id":q_id,
                   "answer": answer})
    except IndexError: 
        return redirect('exam:home')

def create(request):
    if request.method == "GET": 
        form = CandidateForm
        return render(request, 'exam/add_user.html' , {"form": form })
    if request.method == "POST":
        form = CandidateForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            career = form.cleaned_data['career']
            stage = form.cleaned_data['stage']
            user = User.objects.create(username = username, email = email, password= password)
            exam = Exam.objects.create(user = user,
                                       stage = stage,
                                       career = career)
            exam.set_modules()
            exam.set_questions()

            user.first_name = first_name
            user.last_name = last_name
            user.save

            return HttpResponse('Usuario y examen creado')
