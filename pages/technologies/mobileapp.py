class mobileApp:
    def __init__(self, page):
        self.page = page
        self.technologies=page.locator('//li[@class="drop_down"]//a[text()="Technologies"]')
        self.mobile_app=self.mobile_app=page.locator('//li[@data-id="mobileApp"]')

        #mobile App developement
        self.react_native=page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.enterprise_mobile=page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.xamarin_App=page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.kotlin_mobile=page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.flutter_mobile=page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.ionic_app=page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        
    
    def mobileAppSubMenu(self):
        self.mobile_app_list=[self.react_native,self.enterprise_mobile,self.xamarin_App,self.kotlin_mobile,self.flutter_mobile,self.ionic_app]
        for i in self.mobile_app_list:
            self.technologies.hover()
            self.mobile_app.hover()
            self.page.wait_for_load_state("load")
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
          
          

    #print("mobile_app_list is clicked succesffully",{len(self.mobile_app_list)})
