from marionette_driver import By
from marionette_driver.marionette import HTMLElement, Marionette
from time import sleep


def test_load_vapid_page():
    client = Marionette('localhost', port=2828)
    client.start_session()
    url = 'https://jrconlin.github.io/Webpush_QA/'
    client.navigate(url)
    sleep(5)

    # Loop through each expected test element and make sure we have our unicode check mark
    field_ids = ['pre', 'reg', 'sub', 'gen', 'vap', 'enc', 'snd', 'rcv', 'dec']
    command = "return window.getComputedStyle(document.querySelector('li#{0}.done.undone'),':before').getPropertyValue('content')"

    for field_id in field_ids:
        resp = client.execute_script(command.format(field_id))
        assert resp == u'"\u2611"'

