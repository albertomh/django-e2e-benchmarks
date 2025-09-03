from .conftest import BASE_URL


def test_home_title(tab, run):
    run(tab.go_to(BASE_URL))
    res = run(tab.execute_script("return document.title"))
    title = res.get("result", {}).get("result", {}).get("value", "")
    assert "Home | " in title
