
import pytest

from pages.verticals.customapp import customApp
from pages.verticals.fintech import fintech
from pages.verticals.healthcare import healthcare
from pages.verticals.retail import retail
from pages.verticals.verticalpage import vertical


    
#trading object
@pytest.mark.smoke
def test_trading(page):
    v1=vertical(page)
    v1.trading()
    
#Reatil and Ecommerce Object
@pytest.mark.smoke
def test_retailSubMenu(page):
    obj_retail=retail(page)
    obj_retail.retailSubMenu()

#healthcare Object
@pytest.mark.smoke
def test_healthcareSubMenu(page):
    obj_health=healthcare(page)
    obj_health.healthcareSubMenu()

# #fintech Object
@pytest.mark.smoke
def test_fintechSubMenu(page):
    obj_fintech=fintech(page)
    obj_fintech.fintechSubMenu()

# #customApp Object
@pytest.mark.smoke
def test_customAppSubMenu(page):
    obj_customApp=customApp(page)
    obj_customApp.customAppSubMenu()
