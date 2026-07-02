class blog:
    def __init__(self, page):
        self.page = page
        self.blog=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/"])[1]')
        self.app_dev=page.locator('//a[@href="/blog/category/app-development/"]')
        self.web_Dev=page.locator('//a[@href="/blog/category/web-development/"]')
        self.soft_dev=page.locator('//a[@href="/blog/category/software-development/"]')
        self.digital_m=page.locator('//a[@href="/blog/category/digital-marketing/"]')
        self.email_m=page.locator('//a[@href="/blog/category/email-marketing/"]')
        self.Ai=page.locator('//a[@href="/blog/category/artificial-intelligence/"]')
        self.uiuxDesignb=page.locator('//a[@href="/blog/category/ui-ux-design/"]')
        self.appdev01=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/app-development/"])[2]')
        self.ai01=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/artificial-intelligence/"]')
        self.contmark01=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/content-marketing/"]')
        self.crmDev01=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/crm-development/"]')
        self.digmark01=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/digital-marketing/"]')
        self.ecommdev01=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ecommerce-development/"])[5]')
        self.emaimark01=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/email-marketing/"]')
        self.grapdesig01=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/graphic-design/"])[3]')
        self.softItcmp01=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/software-it-company/"]')
        self.softdev01=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/software-development/"]')
        self.uiux01=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ui-ux-design/"])[5]')
        self.webDevelop01=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/web-development/"])[5]')
    
    def blogSubMenu(self):
        self.blog_list=[self.app_dev,self.web_Dev,self.soft_dev,self.email_m,self.Ai,self.uiuxDesignb,self.contmark01,self.crmDev01,self.digmark01,self.ecommdev01,self.emaimark01,self.grapdesig01,self.softItcmp01,self.softdev01,self.uiux01,self.webDevelop01]
        self.blog.click()

        def _click_and_handle(locator):
            try:
                locator.click()
            except Exception:
                locator.scroll_into_view_if_needed()
                locator.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
            self.page.wait_for_load_state("load")

        for locator in self.blog_list:
            _click_and_handle(locator)
        self.page.wait_for_load_state('load')
        print("loaded page", locator)