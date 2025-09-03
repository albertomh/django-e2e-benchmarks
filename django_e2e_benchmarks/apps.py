from django.apps import AppConfig
from django.core import checks


class Django_e2e_benchmarksConfig(AppConfig):
    name = "django_e2e_benchmarks"

    def ready(self) -> None:
        from django_e2e_benchmarks.checks import check_dev_mode, check_model_names

        checks.register(check_dev_mode)
        checks.register(check_model_names)
