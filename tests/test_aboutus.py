import pytest

from pages.aboutus import aboutus


@pytest.mark.smoke
def test_aboutus(page):
    obj_about=aboutus(page)
   #obj_about.aboutUsSUbPage()
    obj_about.aboutUsArrow()