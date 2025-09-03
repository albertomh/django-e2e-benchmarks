import random
import string

from .conftest import BASE_URL, wait_for_url


class AuthTest:
    @classmethod
    def setup_class(cls):
        cls.user_email = "user@example.com"
        cls.user_password = "password"
        cls.login_url = f"{BASE_URL}/accounts/login/"
        cls.signup_url = f"{BASE_URL}/accounts/signup/"


class TestSignUp(AuthTest):
    def test_sign_up_navigation(self, tab, run):
        run(tab.go_to(BASE_URL))

        btn_signup = run(tab.find(text="Sign up"))
        run(btn_signup.click())
        run(wait_for_url(tab, self.signup_url))

    def test_sign_up(self, tab, run):
        run(tab.go_to(self.signup_url))

        btn_signup = run(tab.find(text="Sign up"))
        run(btn_signup.click())
        run(wait_for_url(tab, f"{BASE_URL}/accounts/signup/"))

        email = f"{''.join(random.choices(string.ascii_lowercase, k=6))}@example.com"
        in_email = run(tab.find(id="id_email"))
        run(in_email.click())
        run(in_email.insert_text(email))

        password = "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
        in_pwd = run(tab.find(id="id_password1"))
        run(in_pwd.click())
        run(in_pwd.insert_text(password))

        btn_sub = run(tab.find(tag_name="button", type="submit"))
        run(btn_sub.click())

        run(wait_for_url(tab, f"{BASE_URL}/"))

        txt = run(run(tab.query(expression="//header/nav/ul")).text)
        assert email in txt, "should be logged in"


class TestLogInPage(AuthTest):
    def test_log_in_as_a_regular_user(self, tab, run):
        run(tab.go_to(self.login_url))

        in_email = run(tab.find(id="id_login"))
        run(in_email.click())
        run(in_email.insert_text(self.user_email))

        in_pwd = run(tab.find(id="id_password"))
        run(in_pwd.click())
        run(in_pwd.insert_text(self.user_password))

        btn_sub = run(tab.find(tag_name="button", type="submit"))
        run(btn_sub.click())

        run(wait_for_url(tab, f"{BASE_URL}/"))

        txt = run(run(tab.query(expression="//header/nav/ul")).text)
        assert txt.startswith(self.user_email)

    def test_log_in_requires_email_address(self, tab, run):
        run(tab.go_to(self.login_url))

        in_email = run(tab.find(id="id_login"))
        run(in_email.click())
        run(in_email.insert_text(self.user_email))

        btn_sub = run(tab.find(tag_name="button", type="submit"))
        run(btn_sub.click())

        # expect that the page does NOT navigate: wait_for_url should time out
        try:
            run(wait_for_url(tab, f"{BASE_URL}/", timeout=1.0))
        except TimeoutError:
            return
        raise AssertionError(
            f"The page navigated away from '{self.login_url}' unexpectedly!"
        )

    def test_forgot_password_link_on_log_in_page(self, tab, run):
        run(tab.go_to(self.login_url))

        forgot_link = run(tab.find(tag_name="a", text="Forgot your password?"))
        run(forgot_link.click())

        run(wait_for_url(tab, f"{BASE_URL}/accounts/password/reset/"))


class TestLogOut(AuthTest):
    def test_log_out(self, tab, run):
        run(tab.go_to(self.login_url))

        in_email = run(tab.find(id="id_login"))
        run(in_email.click())
        run(in_email.insert_text(self.user_email))

        in_pwd = run(tab.find(id="id_password"))
        run(in_pwd.click())
        run(in_pwd.insert_text(self.user_password))

        btn_sub = run(tab.find(tag_name="button", type="submit"))
        run(btn_sub.click())
        run(wait_for_url(tab, f"{BASE_URL}/"))

        user_menu = run(tab.find(tag_name="li", text=self.user_email))
        run(user_menu.click())
        logout_link = run(tab.find(tag_name="a", text="Sign out"))
        run(logout_link.click())

        run(wait_for_url(tab, f"{BASE_URL}/accounts/logout/"))

        btn_logout = run(tab.find(tag_name="button", type="submit"))
        run(btn_logout.click())

        run(wait_for_url(tab, f"{BASE_URL}/"))
