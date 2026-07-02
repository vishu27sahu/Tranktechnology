class contactus:
    def __init__(self,page):
        self.page=page
        self.contactus=page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]')
        self.your_name=page.locator('(//input[@placeholder="Your Name"])[2]')
        self.your_email=page.locator('//input[@class="form-control email-input"]')
        self.your_company=page.locator('(//input[@placeholder="Your Company"])[2]')
        self.choose_service=page.locator('(//select[@class="form-control"])[2]')
        self.your_phone=page.locator('(//input[@placeholder="Your Phone"])[2]')
        self.text_area=page.locator('(//textarea[@placeholder="Message"])[2]')


           #Slect DropDown locators
        self.countryDropDownselect=page.locator('//select[@id="countrySelector"]')

    def contactusForm(self):
        self.contactus.click()
        self.page.wait_for_timeout(2000)
        self.contactus.fill("Vasundhara")
        self.page.wait_for_timeout(2000)
        self.page.wait_for_timeout(2000)
        self.your_name.fill("Vasundhara")
        self.page.wait_for_timeout(2000)
        self.your_email.fill("Vasundhara@gmal.com")
        self.page.wait_for_timeout(2000)
        self.your_company.fill("Zensar")
        self.page.wait_for_timeout(2000)
        self.choose_service.select_option("App Development")
        self.page.wait_for_timeout(2000)
        self.your_phone.fill("9588439463")
        self.page.wait_for_timeout(2000)
        self.text_area.fill("Heelo vasundhara")
        self.page.wait_for_load_state("load")
        self.page.wait_for_timeout(2000)

    def countryDropDown(self):
        self.countryDropDownselect.select_option('India')
        self.page.wait_for_load_state(state="load")
        self.countryDropDownselect.select_option('USA')
        self.page.wait_for_load_state("load")
        self.countryDropDownselect.select_option('UAE')
        self.page.wait_for_load_state("load")
        