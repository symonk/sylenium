import pytest
from assertpy import assert_that

from browzer.configuration.browzer_configuration import BrowzerConfiguration
from browzer.exceptions.exceptions import BrowzerConfigValueError


class BrowserSubclass(BrowzerConfiguration):
    def __init__(self, headless: bool):
        self.headless = headless


def test_browser_headless_on():
    assert_that(BrowserSubclass(headless=True).headless).is_true()


def test_browser_headless_off():
    assert_that(BrowserSubclass(headless=False).headless).is_false()


def test_browser_headless_type_checks():
    with pytest.raises(BrowzerConfigValueError):
        BrowserSubclass(headless="exception")
