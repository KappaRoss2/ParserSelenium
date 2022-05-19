import init_parser as ip
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class elsiever(ip.parser):

    def parse_page(self):
        self.driver.get(self.url)
        wait = WebDriverWait(self.driver, 2)
        try:
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-result-wrapper")))
            blocks = self.driver.find_element(By.CLASS_NAME, "search-result-wrapper")
        except:
            return
        self.posts = blocks.find_elements(By.CLASS_NAME, "ResultItem")
        for post in self.posts:
            self.parse_block(post)

    def parse_block(self, post):
        reference = post.find_element(By.TAG_NAME, "h2").find_element(By.TAG_NAME, "a").get_attribute("href")

        article = post.find_element(By.TAG_NAME, "h2").find_element(By.TAG_NAME, "a").text

        access = "Free"
        try:
            post.find_element(By.CLASS_NAME, "access-indicator")
        except:
            access = "No-Access"

        authors_list = post.find_element(By.CLASS_NAME, "Authors").find_elements(By.TAG_NAME, "li")

        authors = ""
        for el in authors_list:
            authors += el.text + ", "
        authors = authors[:len(authors) - 2:]

        self.result.append(ip.ParseResult(
            Article = article,
            Reference = reference,
            Access = access,
            Authors = authors,
        ))

