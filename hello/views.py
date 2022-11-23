# from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic import TemplateView


def hello_world_view(request):
    """Simple function based view that returns JSON response."""

    if request.method == "GET":
        return JsonResponse({
            "Message": "Hello World!"
        })
    else:
        # FOR ANY OTHER HTTP METHODS
        return HttpResponse("Not supported")


class HomeView(TemplateView):
    """Simple class based view that returns HTML page."""
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["message"] = "Hello World!"
        context["author"] = "Satshree Shrestha"
        context["student_id"] = "L30063661"

        return context
