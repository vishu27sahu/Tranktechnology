class ecom:
    def __init__(self, page):
        self.page=page
        self.technologies=page.locator('//li[@class="drop_down"]//a[text()="Technologies"]')
        self.ecommerce_dev=page.locator('//li[@data-id="ecomm"]')

        #ecommerce-options
        self.magent0_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')
        self.codeigniter_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')
        self.big_comm=page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')
        self.cs_cart=page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')
        self.open_cart=page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
        self.word_press=page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
        self.shopify_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
        self.Node_Js=page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')

    def ecomSubMenu(self):
        self.ecommerce_list=[self.magent0_dev,self.codeigniter_dev,self.big_comm,self.cs_cart,self.open_cart,self.word_press,self.shopify_dev,self.Node_Js]
        for i in self.ecommerce_list:
            self.technologies.hover()
            self.page.wait_for_load_state("load")
            self.ecommerce_dev.hover()
            self.page.wait_for_load_state("load")
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
            self.page.wait_for_load_state("load")
         