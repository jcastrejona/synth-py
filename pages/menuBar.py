class menuBar():
    def __init__(self, driver):
        self.driver = driver
        # LOCATORS
        self.notificaciones         =   driver.find_element_by_class_name('fa-bell')
        self.opciones               =   driver.find_element_by_class_name('fa-cog')
        self.logout                 =   driver.find_element_by_class_name ('fa-power-off')

        self.visualize              =   driver.find_element_by_link_text('Visualize')
        self.Analyze                =   driver.find_element_by_link_text('Analyze')
        self.Projects               =   driver.find_element_by_link_text('Projects')
        self.Community              =   driver.find_element_by_link_text('Community')
        self.Collaborators          =   driver.find_element_by_link_text('Collaborators')
        self.GDCs                   =   driver.find_element_by_link_text('GDCs')
        self.Dashboards             =   driver.find_element_by_link_text('Dashboards')
        self.Grafana                =   driver.find_element_by_link_text('Grafana')
    

    def click_notificaciones(self):
        self.notificaciones.click()  

    def click_opciones(self):
        self.opciones.click()
    
    def click_logout(self):
        self.logout.click()
    
    def click_visualize(self):
        self.visualize.click()

    def click_analyze(self):
        self.Analyze.click()

    def click_projects(self):
        self.Projects.click()

    def click_community(self):
        self.Community.click()
    
    def click_collaborators(self):
        self.Collaborators.click()

    def click_gdcs(self):
        self.GDCs.click()

    def click_dashboards(self):
        self.Dashboards.click()

    def click_grafana(self):
        self.Grafana.click()

        
        
