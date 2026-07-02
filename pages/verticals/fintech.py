class fintech:
    def __init__(self,page):
        self.page=page
        self.verticals=page.locator("(//a[text()='Verticals'])[1]")
        self.fintech=page.locator("//strong[text()='Fintech']")
        self.possd=page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.crypto=page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')

    def fintechSubMenu(self):
        fintechList=[self.possd,self.crypto]
        for i in fintechList:
            self.verticals.hover()
            self.page.wait_for_timeout(1000)
            self.fintech.hover()
            self.page.wait_for_timeout(1000)
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
            self.page.wait_for_load_state("load")