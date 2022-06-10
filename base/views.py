from django.shortcuts import render, get_object_or_404
from .models import Base


# Create your views her.
def base_detail_page(request, slug):
    base_one = get_object_or_404(Base, slug=slug)
    template_name = 'base_one.html'
    context = {'base_one': base_one}
    return render(request, template_name, context)
    