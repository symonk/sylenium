.. image:: .github/banner.png
  :class: with-border
  :width: 1280

========
Overview :flags:
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs:
      - |docs|
    * - tests:
      - | |travis| |codecov|
    * - package:
      - | |version|
    * - infra:
      - | |github-actions|

.. |docs| image:: https://readthedocs.org/projects/sylenium/badge/?style=flat
    :target: https://sylenium.readthedocs.io/en/latest/
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/symonk/sylenium.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/symonk/sylenium

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/symonk/sylenium?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/symonk/sylenium

.. |codecov| image:: https://codecov.io/gh/symonk/sylenium/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/symonk/sylenium

.. |version| image:: https://img.shields.io/pypi/v/sylenium.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/sylenium

.. |wheel| image:: https://img.shields.io/pypi/wheel/sylenium.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/sylenium

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/sylenium.svg
    :alt: Supported versions
    :target: https://pypi.org/project/sylenium

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/sylenium.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/sylenium

.. |github-actions| image:: https://github.com/symonk/sylenium/workflows/Release%20Sylenium/badge.svg
    :alt: Automated Releasing
    :target: https://github.com/symonk/sylenium/workflows/Release%20Sylenium/badge.svg


.. end-badges

========
What is Sylenium? :flags:
========

The goal of sylenium is to create a test framework agnostic browser (selenium wrapper) automation library to help
development teams write end to end tests for their web applications without all the necessary boilerplate that is
required to achieve stability with selenium.


=============
Official Documentation :flags:
=============

https://sylenium.readthedocs.io/

==============
Configuring Sylenium :flags:
==============

Sylenium uses a smart default configuration for most use cases, however the customisation options are endless.  Managing
the 'global' configuration can be achieved as outlined below:

.. code-block:: python

    from sylenium import Configuration
    from sylenium import configure
    configure(Configuration(headless=False, remote=True, explicit_waiting=15.00))
    # Now all drivers will use this 'global configuration'
    go("https://www.google.com")


On the fly per driver configurations?

.. code-block:: python

    with get_driver(Configuration(headless=True, polling_interval=2.50, default_selector='ID')):
        go('https://www.google.com')


==============
Quick Start :flags:
==============

Here is a simple way to get going for a standalone simple library script that requires some browser interaction:

.. code-block:: python

    import sylenium import *

    def main():
        # google search => No setup at all, just install sylenium with pip
        with get_driver():
            go("https://www.bing.com")
            find(ById("sb_form_q")).set_text("Hello World").clear().set_text("My Search").press_enter()
            find(ById("b_results")).should_be(Visible).should_contain(Text("My Search"))

==============
Sylenium-pytest :flags:
==============

Plugin (coming soon)
