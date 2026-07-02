class retail:
    def __init__(self,page):
        self.page=page
        #Retail and Ecommerce
        self.verticals=page.locator("(//a[text()='Verticals'])[1]")
        self.ret_ecomm=page.locator("//strong[text()='Retail and Ecommerce']")
        self.ecom_website=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[1]')
        self.ecom_app=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')

    def retailSubMenu(self):
        retailList=[self.ecom_website,self.ecom_app]
        for i in retailList:
            self.verticals.hover()
            self.page.wait_for_load_state(state="load")
            self.ret_ecomm.hover()
            self.page.wait_for_load_state(state="load")
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
            self.page.wait_for_load_state("load")