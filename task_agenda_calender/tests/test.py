import re
import unittest
from infra.android_wrapper import AndroidWrapper
from logic.home_page import HomePage
from datetime import date


class TestAppium(unittest.TestCase):
    def setUp(self):
        self.android=AndroidWrapper()
        self._driver=self.android._driver
        self.home_page=HomePage(self._driver)

    def tearDown(self) :
        self._driver.quit()


    def test_next_week_text(self):
        self.home_page.get_next_week()
        self.assertIn(self.home_page.week_month[0],self.home_page.month)
        self.assertGreaterEqual(int(self.home_page.day)+7,int(self.home_page.week_day[0]))

    def test_last_week_text(self):
        self.home_page.get_last_week()
        self.assertIn(self.home_page.last_week_month[0],self.home_page.month)
        self.assertLessEqual(int(self.home_page.day)-7,int(self.home_page.week_day[1]))

    def test_calender_option_date(self):
        self.home_page.choose_calender_option()
        self.assertEqual(self.home_page.calender_month,self.home_page.month)
        self.assertEqual(self.home_page.calender_year,self.home_page.year)

    def test_add_event_today(self,event_name="project today"):
        event_name_in_pending=self.home_page.adding_event_today_flow(event_name)
        self.assertEqual(event_name_in_pending, event_name)

    def test_add_event_tomorrow(self,event_name="project tomorrow"):
        event_name_in_pending=self.home_page.adding_event_tomorrow_flow(event_name)
        self.assertEqual(event_name_in_pending, event_name)

    def test_add_event_other(self,event_name="project other",event_date='"14 March 2024"'):
        event_name_in_pending = self.home_page.adding_event_other_flow(event_name,event_date)
        self.assertEqual(event_name_in_pending, event_name)

    def test_complete_event(self,event_name="project other",event_date='"14 March 2024"'):
        get_no_pending_events=self.home_page.complete_event_flow(event_name,event_date)
        self.assertEqual(get_no_pending_events,"NO PENDING EVENT")


    def test_setting_duration_time_alarm(self,duration_time=15):
        self.home_page.set_duration_time_flow(duration_time)
        self.assertIn(str(duration_time),self.home_page.duration.text)