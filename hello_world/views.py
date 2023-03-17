from django.shortcuts import render
from django.views.generic import TemplateView


class Hello(TemplateView):
    template_name = "hello_world/index.html"

    def get(self, request):
        return render(request, "hello_world/index.html", {})
