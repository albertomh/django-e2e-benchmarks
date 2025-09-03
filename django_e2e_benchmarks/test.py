import os

from django.test.runner import DiscoverRunner
from django.test.utils import override_settings


class TestRunner(DiscoverRunner):
    """Custom test runner to apply test-specific settings.

    Override per-test with the following decorator:
    ```
    @override_settings(DEBUG=False)
    def test_unit(self):
        ...
    ```
    """

    def __init__(self, *args, exclude_tags=None, **kwargs):
        # exclude tests tagged 'slow' when running locally
        is_ci = os.getenv("GITHUB_ACTIONS") == "true"
        if exclude_tags is None and not is_ci:
            exclude_tags = ["slow"]
        super().__init__(*args, exclude_tags=exclude_tags, **kwargs)

    def run_tests(self, *args, **kwargs):
        with override_settings(**TEST_SETTINGS):
            return super().run_tests(*args, **kwargs)


TEST_SETTINGS = {
    "DEBUG": False,
}
