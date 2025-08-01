from django.shortcuts import render, get_object_or_404
from django.contrib.sites.shortcuts import get_current_site
from django.core.paginator import Paginator

from .models import Post


def view_post(request, slug: str):
    post = get_object_or_404(Post, slug=slug, sites=get_current_site(request))

    context = {
        "title": post.title,
        "post": post,
    }

    return render(request, "doublefloat/view_post.html", context)


def home(request):
    paginator = Paginator(Post.objects.all().order_by("-date"), 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    elided_page_range = paginator.get_elided_page_range(page_obj.number)

    context = {
        "title": "DoubleFloat, the twonum blog",
        "h1_from_title": False,
        "posts": page_obj,
        "elided": elided_page_range,
    }

    return render(request, "doublefloat/home.html", context)
