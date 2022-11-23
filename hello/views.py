# from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView


def hello_world_view(request):
    return JsonResponse({
        "Message": "Hello World!"
    })


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["message"] = "Hello World!"
        context["author"] = "Satshree Shrestha"
        context["student_id"] = "L30063661"

        return context
