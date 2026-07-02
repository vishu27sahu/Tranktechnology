from conftest import page


class healthcare:
    def __init__(self,page):
        self.page=page
        self.verticals=page.locator("(//a[text()='Verticals'])[1]")
        self.healthcare=page.locator("//strong[text()='Healthcare']")
        self.diet=page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.heatlttrackapp=page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')

    def healthcareSubMenu(self):
        healthcareList=[self.diet,self.heatlttrackapp]
        for i in healthcareList:
            self.verticals.hover()
            self.page.wait_for_load_state(state="load")
            self.healthcare.hover()
            self.page.wait_for_load_state(state="load")
            i.click()
            #self.page.wait_for_load_state("load")
            self.page.wait_for_load_state(state="load")
            self.page.go_back()
            self.page.wait_for_load_state("load")