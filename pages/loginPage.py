class loginPage():
    def __init__(self, driver):
        driver
        # LOCATORS
        self.userName_textbox    =  driver.find_element_by_name('User')
        self.password_textbox    =  driver.find_element_by_name('Password')
        self.login_button        =  driver.find_element_by_class_name ('btn-success')
    

    def enter_username(self, username):
        self.userName_textbox.clear()
        self.userName_textbox.send_keys(username)
        return self

    def enter_password(self, password):
        self.password_textbox.clear()
        self.password_textbox.send_keys(password)
        return self

    def click_login(self):
        self.login_button.click()
