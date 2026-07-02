class customApp:
    def __init__(self,page):
        self.page=page
        self.verticals=page.locator("(//a[text()='Verticals'])[1]")
        self.custom_App=page.locator("//strong[text()='Custom App']")
        self.desktop_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.crm=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
        self.hrm=page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
        self.erp=page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
        self.travel=page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
        self.elearn=page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
        self.dating=page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
        self.realestate=page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]')
        self.crmDevUsa=page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')
    
    def customAppSubMenu(self):
        customAppList=[self.desktop_dev, self.crm,self.hrm,self.erp,self.travel, self.elearn,self.dating,self.realestate,self.crmDevUsa]
        for i in customAppList:
            self.verticals.hover()
            self.page.wait_for_timeout(1000)
            self.custom_App.hover()
            self.page.wait_for_timeout(1000)
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
            self.page.wait_for_load_state("load")