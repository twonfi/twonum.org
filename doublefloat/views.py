from django.shortcuts import render, get_object_or_404
from django.contrib.sites.shortcuts import get_current_site
from django.core.paginator import Paginator

from .models import Post, Category


def view_post(request, slug: str):
    post = get_object_or_404(Post, slug=slug, sites=get_current_site(request))

    context = {
        "title": post.title,
        "post": post,
    }

    return render(request, "doublefloat/view_post.html", context)


def home(request):
    paginator = Paginator(Post.objects.all().order_by("-date"), 10)
    page_obj = paginator.get_page(request.GET.get("page"))
    elided_page_range = paginator.get_elided_page_range(page_obj.number)

    context = {
        "title": "DoubleFloat, the twonum blog",
        "h1_from_title": False,
        "posts": page_obj,
        "elided": elided_page_range,
    }

    return render(request, "doublefloat/home.html", context)


def category(request, slug):
    cat = get_object_or_404(Category, slug=slug)

    paginator = Paginator(Post.objects.filter(
        categories=cat).order_by("-date"), 10)
    page_obj = paginator.get_page(request.GET.get("page"))
    elided_page_range = paginator.get_elided_page_range(page_obj.number)

    context = {
        "title": f"{cat.title} on DoubleFloat",
        "h1_from_title": False,
        "cat": cat,
        "posts": page_obj,
        "elided": elided_page_range,
    }

    return render(request, "doublefloat/category.html", context)
