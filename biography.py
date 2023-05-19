from RPA.Browser.Selenium import Selenium
from selenium.webdriver.common.by import By

import datetime

br = Selenium()

class Biography:
    def __init__(self, name):
        self.name = name
        self.wiki_url = "en.wikipedia.org/wiki/" + name
        self.bday = None
        self.death = None
        self.summary = None

        self.populate_bio(self.wiki_url)

        self.age = self.calc_age(self.bday, self.death)

    # remove surrounding parens around date
    def clean_date(self, date_string):
        cleaned_death_date = date_string.removeprefix("(")
        cleaned_death_date = cleaned_death_date.removesuffix(")")
        return cleaned_death_date

    # convert string to date object
    def create_date(self, date_string):
        date_array = date_string.split('-')
        year = int(date_array[0])
        month = int(date_array[1])
        day = int(date_array[2])
        return datetime.date(year, month, day)

    # calculate age using birth and death dates
    def calc_age(self, birth, death):
        lifespan = death - birth
        return lifespan.days//365

    # populate attributes by extracting from DOM elements
    def populate_bio(self, webpage):
        br.open_available_browser(webpage)

        # populate birth date
        bday_element = br.driver.find_element(By.CLASS_NAME, "bday")
        self.bday = self.create_date(bday_element.get_attribute("textContent"))

        # populate date of death
        death_element = br.driver.find_element(By.XPATH, "//table[@class='infobox biography vcard']/tbody/tr[4]/td[@class='infobox-data']/span")

        # this date string comes with parens around the date - must be removed before translating to date datatype
        cleaned_death_date = self.clean_date(death_element.get_attribute("textContent"))
        death_date = self.create_date(cleaned_death_date)

        # cover edge case where date of death is actually in following row of table due to multiple names for individual
        if death_date == self.bday:
            death_element = br.driver.find_element(By.XPATH, "//table[@class='infobox biography vcard']/tbody/tr[5]/td[@class='infobox-data']/span")
            cleaned_death_date = self.clean_date(death_element.get_attribute("textContent"))
            death_date = self.create_date(cleaned_death_date)
        self.death = death_date

        # retrieve first paragraph in wiki bio - may be either 2nd or 3rd p element depending on whether disambiguation text is present
        overview_element = br.driver.find_element(By.XPATH, "//div[@id='bodyContent']/div[@id='mw-content-text']/div[@class='mw-parser-output']/p[2]")
        summary = overview_element.get_attribute("textContent")
        if summary == '\n\n':
            next_overview_element = br.driver.find_element(By.XPATH, "//div[@id='bodyContent']/div[@id='mw-content-text']/div[@class='mw-parser-output']/p[3]")
            summary = next_overview_element.get_attribute("textContent")
        self.summary = summary

