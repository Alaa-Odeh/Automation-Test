import re
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from datetime import date
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



class HomePage:
    FORWARD_BUTTON='(//android.widget.ImageView[@content-desc="Image"])[2]'
    BACKWORD_BUTTON='(//android.widget.ImageView[@content-desc="Image"])[1]'
    CURRENT_WEEK='com.claudivan.taskagenda:id/tvVisor'
    MENU_BUTTON='com.claudivan.taskagenda:id/hamburguer'
    WEEK_OPTIONS='//android.widget.TextView[@text="Week"]'
    CALENDER_OPTIONS='//android.widget.TextView[@text="Calendar"]'
    ADD_EVENT_BUTTON='com.claudivan.taskagenda:id/btNovoEvento'
    SETTING='com.claudivan.taskagenda:id/btAjustes'
    CALENDER_EVENT_MARKER='com.claudivan.taskagenda:id/item_background'
    COLOR='//android.widget.LinearLayout[@resource-id="com.claudivan.taskagenda:id/container_cores"]/android.widget.LinearLayout[3]/android.view.View[4]'
    CALENDER_OPTION_DATE="com.claudivan.taskagenda:id/tvVisor"
    ADD_EVENT_TIME='//android.widget.TextView[@resource-id="android:id/text1" and @text="'
    EVENT_NAME='com.claudivan.taskagenda:id/etTitulo'
    SAVE_EVENT='com.claudivan.taskagenda:id/item_salvar'
    PENDING_EVENTS='com.claudivan.taskagenda:id/btEventosSemana'
    TODAY_PENDING_EVENT='//android.widget.TextView[@resource-id="com.claudivan.taskagenda:id/tvTitulo"]'
    TOMORROW_PENDING_EVENT='//android.widget.TextView[@resource-id="com.claudivan.taskagenda:id/tvTitulo"]'
    EVENT_DATE='//android.view.View[@content-desc='
    OK_EVENT='android:id/button1'
    OTHER_PENDING_EVENTS='//android.widget.TextView[@resource-id="com.claudivan.taskagenda:id/tvTitulo"]'
    ALLOW_NOTIFICATION='com.android.permissioncontroller:id/permission_allow_button'
    EVENT_CHECKBOX='com.claudivan.taskagenda:id/cbEventoConcluido'
    BACK_EVENT_BUTTON='//android.widget.ImageButton[@content-desc="Navigate up"]'
    NO_PENDING_EVENT='com.claudivan.taskagenda:id/btEventosSemana'
    ALARMS_AND_NOTIFICATION='com.claudivan.taskagenda:id/itemNotificacoes'
    DURATION='com.claudivan.taskagenda:id/tvValorDuracaoAlarmeEvento'


    def __init__(self, driver):
        self.driver=driver
        self.forward_button=self.driver.find_element(by=AppiumBy.XPATH, value=self.FORWARD_BUTTON)
        self.backward_button=self.driver.find_element(by=AppiumBy.XPATH, value=self.BACKWORD_BUTTON)
        self.menu_button=self.driver.find_element(by=AppiumBy.ID, value=self.MENU_BUTTON)
        self.week_option=self.driver.find_element(by=AppiumBy.XPATH, value=self.WEEK_OPTIONS)
        self.add_event_button = self.driver.find_element(by=AppiumBy.ID, value=self.ADD_EVENT_BUTTON)
        self.calender_option = self.driver.find_element(by=AppiumBy.XPATH, value=self.CALENDER_OPTIONS)
        self.pending_events=self.driver.find_element(by=AppiumBy.ID, value=self.PENDING_EVENTS)
        today = date.today()
        self.day = today.strftime("%d")
        self.month = today.strftime("%B")
        self.year = today.strftime("%Y")

    def click_on_menu_button(self):
        self.menu_button.click()
        self.settings_button=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID,self.SETTING)))

    def click_on_settings_button(self):
        self.settings_button.click()
        self.alarms_and_notifications_button=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID,self.ALARMS_AND_NOTIFICATION)))

    def click_on_alarms_and_notifications_button(self):
        self.alarms_and_notifications_button.click()
        self.duration=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID,self.DURATION)))

    def click_on_duration_button(self):
        self.duration.click()

    def choose_duration_time(self,duration_time):
        self.duration_time=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,f'//android.widget.TextView[@resource-id="android:id/text1" and @text="{duration_time} seconds"]')))
        self.duration_time.click()


    def set_duration_time_flow(self,duration_time):
        self.click_on_menu_button()
        self.click_on_settings_button()
        self.click_on_alarms_and_notifications_button()
        self.click_on_duration_button()
        self.choose_duration_time(duration_time)



    def click_next_week_button(self):
        self.forward_button.click()

    def get_next_week(self):
        self.click_next_week_button()
        self.week_text=self.driver.find_element(by=AppiumBy.ID, value=self.CURRENT_WEEK)
        weektext=self.week_text.text
        self.week_day = re.findall(r"(\d+)/", weektext)
        self.week_month = re.findall("/(.*?) ", weektext)


    def get_last_week(self):
        self.backward_button.click()
        self.week_text=self.driver.find_element(by=AppiumBy.ID, value=self.CURRENT_WEEK)
        weektext=self.week_text.text
        self.week_day=re.findall(r"(\d+)/",weektext )
        self.week_month=weektext.split("-")
        self.last_week_month=re.findall("/(.*)", self.week_month[1])


    def choose_calender_option(self):
        self.calender_option.click()
        self.calender_option_date=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, self.CALENDER_OPTION_DATE)))
        self.calender_month=self.calender_option_date.text.split(" ")[0]
        self.calender_year =self.calender_option_date.text.split(" ")[1]

    def click_on_add_event(self):
        self.add_event_button.click()
        self.add_event_today=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.ADD_EVENT_TIME+'Today"]')))
        self.add_event_tomorrow=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.ADD_EVENT_TIME+'Tomorrow"]')))
        self.add_event_other=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.ADD_EVENT_TIME+'Other"]')))

    def click_on_add_event_today(self):
        self.add_event_today.click()
        self.event_name_input=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, self.EVENT_NAME)))

    def click_on_add_event_tomorrow(self):
        self.add_event_tomorrow.click()
        self.event_name_input=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, self.EVENT_NAME)))

    def click_on_add_event_other(self,date='"14 March 2024"'):
        self.add_event_other.click()
        self.event_date = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.EVENT_DATE+date+']')))

    def click_on_event_date(self):
        self.event_date.click()
        self.ok_date = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, self.OK_EVENT)))
    def click_ok_on_event_date(self):
        self.ok_date.click()
        self.event_name_input=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, self.EVENT_NAME)))

    def enter_new_event_name(self,event_name):
        self.event_name_input.send_keys(event_name)
        self.save_event=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, self.SAVE_EVENT)))

    def click_on_save_event(self):
        self.save_event.click()

    def click_on_pending_events(self):
        self.pending_events.click()

    def click_allow_notification(self):
        self.allow_notification=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, self.ALLOW_NOTIFICATION)))
        self.allow_notification.click()
    def get_today_pending_event_text(self):
        self.today_pending_event=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.TODAY_PENDING_EVENT)))
        return self.today_pending_event.text
    def get_tomorrow_pending_event_text(self):
        self.tomorrow_pending_event=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.TOMORROW_PENDING_EVENT)))
        return self.tomorrow_pending_event.text

    def get_other_pending_event(self):
        self.other_pending_event=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.OTHER_PENDING_EVENTS)))
        self.checkbox_for_pending_event=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, self.EVENT_CHECKBOX)))

    def click_checkbox_for_pending_event(self):
        self.checkbox_for_pending_event.click()
        self.back_event_button=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.BACK_EVENT_BUTTON)))

    def get_no_pending_event(self):
        self.back_event_button.click()
        self.no_peneding_event_button=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, self.NO_PENDING_EVENT)))
    def adding_event_today_flow(self,event_name):
        self.click_on_add_event()
        self.click_on_add_event_today()
        self.enter_new_event_name(event_name)
        self.click_on_save_event()
        self.click_on_pending_events()
        self.click_allow_notification()
        return self.get_today_pending_event_text()

    def adding_event_tomorrow_flow(self,event_name):
        self.click_on_add_event()
        self.click_on_add_event_tomorrow()
        self.enter_new_event_name(event_name)
        self.click_on_save_event()
        self.click_on_pending_events()
        self.click_allow_notification()
        return self.get_tomorrow_pending_event_text()

    def adding_event_other(self,event_name,date):
        self.click_on_add_event()
        self.click_on_add_event_other(date)
        self.click_on_event_date()
        self.click_ok_on_event_date()
        self.enter_new_event_name(event_name)
        self.click_on_save_event()

    def get_pending_other_event(self):
        self.click_next_week_button()
        self.click_on_pending_events()
        self.click_allow_notification()
        self.get_other_pending_event()
    def adding_event_other_flow(self,event_name,date):
        self.adding_event_other(event_name,date)
        self.get_pending_other_event()
        return self.other_pending_event.text


    def complete_event_flow(self,event_name,date):
        self.adding_event_other(event_name,date)
        self.get_pending_other_event()
        self.click_checkbox_for_pending_event()
        self.get_no_pending_event()
        return self.no_peneding_event_button.text
