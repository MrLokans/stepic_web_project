from django.http import HttpResponse, HttpResponseNotFound


def resp_404(request, *args, **kwargs):
    return HttpResponseNotFound()


def test(request, *args, **kwargs):
    return HttpResponse(b'OK')
