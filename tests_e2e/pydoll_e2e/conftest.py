# >>> uv run pytest tests_e2e/pydoll_e2e/

import asyncio

import pytest
from environs import Env
from pydoll.browser import Chrome
from pydoll.browser.options import ChromiumOptions

env = Env()
env.read_env()

BASE_URL = "http://127.0.0.1:8000"


def make_chromium_options() -> ChromiumOptions:
    options = ChromiumOptions()
    if env.bool("CI", default=False) or env.bool("GITHUB_ACTIONS", default=False):
        # options.binary_location = "/usr/bin/chromium-browser"
        options.add_argument("--headless=new")
    return options


@pytest.fixture(scope="session")
def event_loop():
    """Provide a dedicated asyncio loop for the whole test session."""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def browser(event_loop):
    """Start Chromium once for the whole session."""
    chrome = Chrome(make_chromium_options())
    browser = event_loop.run_until_complete(chrome.__aenter__())
    event_loop.run_until_complete(browser.start())
    yield browser
    event_loop.run_until_complete(browser.__aexit__(None, None, None))


@pytest.fixture
def tab(event_loop, browser):
    """Provide a fresh browser context + tab for each test."""
    context_id = event_loop.run_until_complete(browser.create_browser_context())
    tab = event_loop.run_until_complete(browser.new_tab(browser_context_id=context_id))
    yield tab
    event_loop.run_until_complete(browser.delete_browser_context(context_id))


@pytest.fixture
def run(event_loop):
    """Helper to run async coroutines easily inside tests."""
    return event_loop.run_until_complete


async def wait_for_url(
    tab, expected_url: str, timeout: float = 5.0, interval: float = 0.05
):
    """Wait until the tab navigates to expected_url."""
    deadline = asyncio.get_event_loop().time() + timeout
    while True:
        current_url = await tab.current_url
        if current_url == expected_url:
            return
        if asyncio.get_event_loop().time() > deadline:
            raise TimeoutError(
                f"Timed out waiting for URL {expected_url}, last seen {current_url}"
            )
        await asyncio.sleep(interval)
