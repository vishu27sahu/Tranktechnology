import pytest

from pages.technologies import mobileapp
from pages.technologies.ecom import ecom

@pytest.mark.smoke
def test_ecommerce(page):
    obj_ecom=ecom(page)
    obj_ecom.ecomSubMenu()

@pytest.mark.smoke
def test_mobileapp(page):
    obj_mobileapp=mobileapp(page)
    obj_mobileapp.mobileAppSubMenu()

# @pytest.mark.smoke
# def test_AI(page):
#     obj_AI=AI(page)
#     obj_ecom.ecommerceSubMenu()
#     obj_mobileapp=mobileapp(page)
#     obj_mobileapp.mobileAppSubMenu()