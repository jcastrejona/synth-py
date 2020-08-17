from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time 
import keyboard
import sys
sys.path.append('../pages')
from loginPage import loginPage
from menuBar import menuBar



class TestMenus:
    def setup_method(self):
        self.vars = {}

        # #REMOTE
        capabilities = DesiredCapabilities.CHROME 
        self.driver = webdriver.Remote(command_executor='http://10.0.213.243:4444/wd/hub', desired_capabilities=capabilities)  

        #LOCAL
        #self.driver = webdriver.Chrome()

        self.driver.get("https://coelens.digitalcoedevops.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
        loginPage(self.driver).enter_username('marcos.zaragoza').enter_password('admin').click_login()

    
    def teardown_method(self):
        self.driver.quit()



    # method for waiting for a new tab
    def wait_for_window(self, timeout = 2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    # #3 botones arriba ------------------------------------------------------------------
    def test_notificaciones(self):
        menuBar(self.driver).click_notificaciones()

    def test_opciones(self):
        menuBar(self.driver).click_opciones()
    
    def test_logout(self):
        menuBar(self.driver).click_logout()

    # # COE --------------------------------------------------------------------------------
    def test_visualize(self):
        menuBar(self.driver).click_visualize()
        assert self.driver.find_element_by_link_text('Current Engagements').is_displayed

    def test_analyze(self):
        menuBar(self.driver).click_analyze()
        assert self.driver.find_element_by_link_text('Profile analysis').is_displayed
    
    # # General -------------------------------------------------------------------------------
    def test_projects(self):
        menuBar(self.driver).click_projects()
        assert self.driver.find_element_by_xpath('/html/body/div[2]/main/div/div[1]/div/h3').is_displayed

    def test_community(self):
        menuBar(self.driver).click_community()
        assert self.driver.find_element_by_link_text('All Community').is_displayed and \
               self.driver.find_element_by_link_text('Register New Badge').is_displayed and \
               self.driver.find_element_by_class_name('fa-anchor').is_displayed
    
    def test_collaborators(self):
        menuBar(self.driver).click_collaborators()
        assert self.driver.find_element_by_link_text('All Collaborators').is_displayed and \
               self.driver.find_element_by_link_text('Platforms').is_displayed and \
               self.driver.find_element_by_link_text('Certifications').is_displayed and \
               self.driver.find_element_by_link_text('OnBoarding').is_displayed and \
               self.driver.find_element_by_class_name('fa-door-open').is_displayed and \
               self.driver.find_element_by_link_text('Trainings').is_displayed 
    
    def test_gdcs(self):
        menuBar(self.driver).click_gdcs()
        assert self.driver.find_element_by_link_text('Update GDCs').is_displayed and \
               self.driver.find_element_by_class_name('fa-building').is_displayed 

    def test_dashboards(self):
        menuBar(self.driver).click_dashboards()
        assert self.driver.find_element_by_link_text('Word Cloud: Tools').is_displayed and \
               self.driver.find_element_by_link_text('FDT: Tools All Centers').is_displayed and \
               self.driver.find_element_by_link_text('Force directed tree: Projects').is_displayed 
    
    def test_grafana(self):
        self.vars["window_handles"] = self.driver.window_handles
        menuBar(self.driver).click_grafana()
        self.vars["win9010"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win9010"])
        assert self.driver.title == "Grafana" 


        
