import pytest

from pages.contactus.contactus import contactus

@pytest.mark.smoke
def contactus(page):
    obj_contactus=contactus(page)
    obj_contactus.contactusForm()