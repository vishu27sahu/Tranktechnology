class vertical:
    def __init__(self, page):
        self.page=page
        self.ver=page.locator("(//a[text()='Verticals'])[1]")

        self.Trading=page.locator("//strong[text()='Trading']")
        self.Retails_cmrce=page.locator("//strong[text()='Retail and Ecommerce']")
        self.healthcare=page.locator("//strong[text()='Healthcare']")
        self.fin_tech=page.locator("//strong[text()='Fintech']")

        #Trading
        self.stock_t=page.locator('(//a[text()="Stock Trading"])[1]')
        self.paper_t=page.locator('(//a[text()="Paper Trading"])[1]')
        self.cft_t=page.locator('(//a[text()="CFD Trading"])[1]')
        self.tradig_app=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        self.algo_t=page.locator('(//a[@href="https://www.tranktechnologies.com/algo-trading-app-development-company"])[1]')
        self.custom_t=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.web_t=page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')

        self.Trading_list=[self.stock_t,self.paper_t,self.cft_t,self.tradig_app,self.algo_t,self.custom_t,self.web_t]



    def mouse_hover(self):
        list=[self.Trading,self.Retails_cmrce,self.healthcare,self.fin_tech]
        for i in list:
            self.ver.hover()
            i.hover()
            self.page.wait_for_timeout(2000)

    def trading(self):

        #self.Trading_list=[self.stock_t,self.paper_t,self.cft_t,self.tradig_app,self.algo_t,self.custom_t,self.web_t]

        for i in self.Trading_list:

           self.ver.hover()
           self.Trading.hover()
           i.click()
           self.page.go_back()
           self.page.wait_for_timeout(2000)
       
    
        
       
    
        


