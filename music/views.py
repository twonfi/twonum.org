from django.core.exceptions import PermissionDenied
from django.http.response import HttpResponse
from django.shortcuts import render
from django.db import transaction

from music.forms import TrackAdderForm
from music.models import Track
from core.views import error_401


def track_adder(request):
    if not request.user.is_authenticated:
        return error_401(request)

    if not request.user.is_staff or not request.user.has_perm("music.add_track"):
        raise PermissionDenied

    if request.method == "POST":
        form = TrackAdderForm(request.POST)

        if form.is_valid():
            # Transactions are simple
            try:
                with transaction.atomic():
                    text = form.cleaned_data['text'].strip().splitlines()

                    for i, track in enumerate(text):
                        ln = i + 1
                        track = track.strip()

                        if not track:
                            continue

                        try:
                            number, title = track.split(maxsplit=1)
                        except ValueError as e:
                            raise ValueError(f"Line {ln}: Number or title not present.") from e

                        release = form.cleaned_data["release"]

                        try:
                            number = int(number.strip())
                        except ValueError as e:
                            raise ValueError(f"Line {ln}: Number must be a number.") from e
                        # 0 is allowed here for singles and other
                        # non-standard album labels
                        if not (0 <= number <= 4096):
                            raise ValueError(f"Line {ln}: Number must not be outrageous.")

                        title = title.strip()
                        if len(title) > 255:
                            raise ValueError(f"Line {ln}: Title must be less than 256 characters.")

                        if Track.objects.filter(release=release, number=number).exists():
                            raise ValueError(f"Line {ln}: Track {number} for release {release} already exists.")

                        track = Track()
                        track.release = release
                        track.number = number
                        track.title = title
                        track.save()
            except ValueError as e:
                form.add_error('text', str(e))
            else:
                return HttpResponse("Done.", content_type="text/plain")
    else:
        form = TrackAdderForm()

    context = {
        "title": "Track adder",
        "form": form,
        "bare": True,
    }

    return render(request, "music/track_adder.html", context)
