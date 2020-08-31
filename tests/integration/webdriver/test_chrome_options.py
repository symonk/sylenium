import os

from assertpy import assert_that

from sylenium import Configuration


def test_chrome_options_headless_standalone(headless_session):
    assert_that(headless_session.get_driver())


def test_service_options_log(sy_session, tmpdir):
    with sy_session(
        configuration=Configuration(
            chrome_service_log_path=f"{tmpdir}{os.path.sep}sylenium.log",
            headless=False,
            browser_position="0x0",
        )
    ) as session:
        session.get_driver()
