from django_e2e_benchmarks import __version__


def metadata(request):
    return {"django_e2e_benchmarks": {"meta": {"version": __version__}}}
