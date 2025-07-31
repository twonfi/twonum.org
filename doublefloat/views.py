from django.shortcuts import render, get_object_or_404
from django.contrib.sites.shortcuts import get_current_site

from .models import Post


def view_post(request, slug: str):
    post = get_object_or_404(Post, slug=slug, sites=get_current_site(request))

    context = {
        "title": post.title,
        "post": post,
    }

    return render(request, "doublefloat/view_post.html", context)
