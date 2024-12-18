from django.shortcuts import render
from blog.models import Article



def index(request):
    data = Article.objects.all()

    context = {
        "data": data,
    }

    return render(request, "list.html", context)

# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("polls/index.html")
#     context = {
#         "latest_question_list": latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))