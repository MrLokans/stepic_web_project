from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render_to_response

from qa.models import Answer, Question


def test(request, *args, **kwargs):
    return HttpResponse(b'OK')


def page(request, *args, **kwargs):
    questions = Question.objects.order_by("-added_at")
    page_number = request.GET.get("page", 1)
    paginator = Paginator(questions, 10)
    try:
        questions_page = paginator.page(page_number)
    except PageNotAnInteger:
        questions_page = paginator.page(1)
    except EmptyPage:
        questions_page = paginator.page(paginator.num_pages)
    return render_to_response("page.html", context={"questions": questions_page})


def popular(request, *args, **kwargs):
    questions = Question.objects.order_by("-rating")
    page_number = request.GET.get("page", 1)
    paginator = Paginator(questions, 10)
    try:
        questions_page = paginator.page(page_number)
    except PageNotAnInteger:
        questions_page = paginator.page(1)
    except EmptyPage:
        questions_page = paginator.page(paginator.num_pages)
    return render_to_response("page.html", context={"questions": questions_page})


def question(request, qid, *args, **kwargs):
    q = Question.objects.filter(id=qid).first()
    if not q:
        return Http404()
    print(q)
    answers = q.answer_set.all()
    print(answers)
    print(answers[0].text)
    return render_to_response("question.html", context={"question": q,
                                                        "answers": answers})
