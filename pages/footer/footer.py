# class footer:
#     def __init__(self,page):
#         self.page=page
#            ##FOOTER
#     ##WEB_DEVLOPMENT
#         self.CMS=page.locator("//a[text()='CMS Website Development']")
#         self.CWD=page.locator("//a[text()='Custom Web Portal Development']")

#     def footerwebdev(self):
#         self.WEB_LIST=[self.CMS,self.CWD]
#         for i in self.WEB_LIST:
#             i.click()
#             self.page.wait_for_load_state(state="load")
#             self.page.go_back()

#     #ecomdevelopment
   
#         self.ECOMD=self.page.locator('(//i[@class="fa fa-chevron-down text-red-2"])[1]')
#         self.WEDD=self.page.locator("//a[text()='Website Development']")    

#     def footerecomdev(self):

#         self.ECOMD_list=[self.ECOMD,self.WEDD]

#         for i in self.ECOMD_list:
#             i.click()
#             self.page.wait_for_load_state(state="load")
#             self.page.go_back()
#             self.page.wait_for_load_state(state="load")
        

#         ##UI/UX DESIGN
        
#         self.MAD=self.page.locator("//a[text()='Mobile App Design']")
#         self.RWD=self.page.locator("//a[text()='Responsive Web Design']")
#         self.BID=self.page.locator("//a[text()='Brand Identity Design']")

#     def footerUIUX(self):

#         self.UI_LIST=[self.MAD,self.RWD,self.BID]

#         for i in self.UI_LIST:
#             i.click()
#             self.page.wait_for_load_state(state="load")
#             self.page.go_back()

#         ##APP DEVELOPMENT
#         self.IOS=self.page.locator("//a[text()='iOS App Development']")
#         self.HMD=self.page.locator("//a[text()='Hybrid Mobile App Development']")
#         self.CAD=self.page.locator("//a[text()='Cross-Platform App Development']")
#         self.PWD=self.page.locator("//a[text()='Progressive Web App Development']")

#     def footerAppDev(self):
#         self.APP_LIST=[self.IOS,self.HMD,self.CAD,self.PWD]
#         for i in self.APP_LIST:
#             i.click()
#             self.page.wait_for_load_state(state="load")
#             self.page.go_back()

#     #android app development
#         self.AD=self.page.locator('(//i[@class="fa fa-chevron-down text-red-2"])[2]').click()
#         self.page.wait_for_load_state(state="load")

#         self.APD=self.page.locator("(//a[text()='Android App Development'])[1]")
#         self.AD=self.page.locator("(//a[text()='App Development'])[2]")
        
#     def footerAndroidAppDev(self):
#         self.AD_LIST=[self.APD,self.AD]
#         for i in self.AD_LIST:
#             i.click()
#             self.page.wait_for_load_state(state="load")
#             self.page.go_back()

#         ##GRAPHICS DESIGNING
#         self.LD=self.page.locator("//a[text()='Logo Design']")
#         self.BD=self.page.locator("//a[text()='Banner Design']")
#         self.PD=self.page.locator("//a[text()='Packaging Design']")
#         self.BCD=self.page.locator("//a[text()='Business cards Design']")

#     def footerGraphicsDesign(self):
            
#         self.GP_LIST=[self.LD,self.BD,self.PD,self.BCD]
#         for i in self.GP_LIST:
#             i.click()
#             self.page.wait_for_load_state(state="load")
#             self.page.go_back()
        
            