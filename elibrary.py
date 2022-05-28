import selenium.webdriver.remote.webelement as WebElement
import init_parser as ip
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class elibrary(ip.parser):

    def parse_page(self):
        self.driver.get("https://www.elibrary.ru/defaultx.asp")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "left-panel")))

        input_element = self.driver.find_element(By.CLASS_NAME, "left-panel").find_element(By.CLASS_NAME, "formfr").find_element(By.ID, "ftext")
        input_element.send_keys(self.url)
        input_element.send_keys(Keys.ENTER)

        handler = self.driver.current_window_handle
        self.driver.switch_to.window(handler)
        time.sleep(1)
        try:
            blocks = self.driver.find_element(By.ID, "restab")
        except:
            return

        self.posts = blocks.find_elements(By.XPATH, "//tr[@id]")
        for post in self.posts:
            self.parse_block(post)
            self.driver.execute_script("window.scrollTo(0, window.scrollY + 60)")

    def parse_block(self, post: WebElement):
        tags = post.find_elements(By.TAG_NAME, "td")

        reference = tags[1].find_element(By.TAG_NAME, "a").get_attribute("href")

        article = tags[1].find_element(By.TAG_NAME, "a").text

        try:
            authors = tags[1].find_element(By.TAG_NAME, "i").text
        except:
            authors = ""

        try:
            access = tags[0].find_element(By.TAG_NAME, "img").get_attribute("title")
        except:
            access = "Полный текст документа отсутствует в НЭБ"

        if access == 'Доступ к полному тексту открыт' or access == 'Полный текст доступен на внешнем сайте':
            access = "Free"
        else:
            access = "No-Access"

        self.result.append(ip.ParseResult(
            Article=article,
            Reference=reference,
            Access=access,
            Authors=authors,
        ))




