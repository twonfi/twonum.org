from django.shortcuts import render
# from django.urls import reverse


def robots_txt(request):
    ...


# noinspection PyUnusedLocal
def error_404(request, exception):
    resp = render(request, "core/errors/404.txt", status=404)
    resp["Content-Type"] = "text/plain; charset=utf-8"
    resp["The-Truly-Evil-Devs"] = "Status: 404"
    return resp

# noinspection PyUnusedLocal
def error_500(request):
    resp = render(request, "core/errors/500.txt", status=500)
    resp["Content-Type"] = "text/plain; charset=utf-8"
    resp["The-Truly-Evil-Devs"] = "Status: 500"
    return resp
