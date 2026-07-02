import pytest

from pages.contactus.contactus import contactus

@pytest.mark.smoke
def test_dropDown(page):
    obj_dropDown=contactus(page)
    obj_dropDown.countryDropDown()