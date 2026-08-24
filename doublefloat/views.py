from django.shortcuts import render, get_object_or_404
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

from doublefloat.models import Post


def view_post(request, slug: str):
    post = get_object_or_404(Post, slug=slug, sites=get_current_site(request))

    context = {
        "title": post.title,
        "post": post,
        "admin_url": post.get_admin_url(),
        "admin_name": "edit",
    }

    return render(request, "doublefloat/view_post.html", context)


def home(request):
    years = Post.objects.values_list(
        "date__year",
        flat=True,
    ).order_by("-date")
    # Remove duplicated
    years = list(dict.fromkeys(years))

    posts = []

    for year in years:
        year_posts = Post.objects.filter(
            date__year=year,
        ).order_by("-date")
        item = (year, year_posts)
        posts.append(item)

    context = {
        "title": "Blog",
        "h1_from_title": False,
        "posts": posts,
        "admin_url": reverse("admin:doublefloat_post_add"),
        "admin_name": "write",
    }

    return render(request, "doublefloat/home.html", context)


# def category(request, slug):
#     cat = get_object_or_404(Category, slug=slug)
#
#     paginator = Paginator(
#         Post.objects.filter(categories=cat).order_by("-date"), 10
#     )
#     page_obj = paginator.get_page(request.GET.get("page"))
#     elided_page_range = paginator.get_elided_page_range(page_obj.number)
#
#     try:
#         project = Project.objects.prefetch_related("doublefloat_category").get(
#             doublefloat_category=cat
#         )
#     except ObjectDoesNotExist:
#         project = None
#
#     context = {
#         "title": f"{cat.title} on DoubleFloat",
#         "h1_from_title": False,
#         "cat": cat,
#         "posts": page_obj,
#         "elided": elided_page_range,
#         "pagination": paginator,
#         "project": project,
#     }
#
#     return render(request, "doublefloat/category.html", context)
