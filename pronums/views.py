from datetime import date

from django.shortcuts import render
from rest_framework import viewsets, permissions

from pronums import models, serializers, filters


def home(request):
    context = {
        "title": "Pronums",
        "pronums": models.Pronum.objects.filter(
            date__year=date.today().year,
        ).order_by("-date"),
        "years": models.Pronum.objects.values_list(
            "date__year",
            flat=True,
        ).distinct().reverse(),
    }

    return render(request, 'pronums/home.html', context)


def year_view(request, year):
    context = {
        "title": f"Pronums of {year}",
        "pronums": models.Pronum.objects.filter(
            date__year=year,
        ).order_by("-date"),
        "years": models.Pronum.objects.values_list(
            "date__year",
            flat=True,
        ).distinct().reverse(),
    }

    return render(request, 'pronums/year.html', context)


class PronumViewSet(viewsets.ModelViewSet):
    queryset = models.Pronum.objects.all()
    serializer_class = serializers.PronumSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    filterset_class = filters.PronumFilter
