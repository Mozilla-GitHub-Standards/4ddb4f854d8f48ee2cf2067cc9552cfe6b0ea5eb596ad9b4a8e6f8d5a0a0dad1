from marionette_driver.marionette import Marionette
from time import sleep


def test_load_vapid_page():
    client = Marionette("localhost", port=2828)
    client.start_session()
    url = "https://jrconlin.github.io/Webpush_QA/"
    expected_url = "https://jrconlin.github.io/Webpush_QA/success.html"
    client.navigate(url)
    sleep(5)

    assert expected_url in client.get_url()
