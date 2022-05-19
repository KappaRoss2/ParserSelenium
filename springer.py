import init_parser as ip
from selenium.webdriver.common.by import By


class springer(ip.parser):
    def parse_page(self):
        self.driver.get(self.url)
        blocks = self.driver.find_element(By.CLASS_NAME, "content-item-list")
        self.posts = blocks.find_elements(By.TAG_NAME, "li")
        for post in self.posts:
            self.parse_block(post)


    def parse_block(self, post):
        reference = post.find_element(By.TAG_NAME, "h2").find_element(By.TAG_NAME, "a").get_attribute("href")

        article = post.find_element(By.TAG_NAME, "h2").find_element(By.TAG_NAME, "a").text

        access = "No-Access"
        try:
            post.find_element(By.CLASS_NAME, "no-access-message")
        except:
            access = "Free"

        authors_list = post.find_element(By.CLASS_NAME, "meta").find_elements(By.CLASS_NAME, "authors")
        authors = ""
        for el in authors_list:
            authors += el.text

        self.result.append(ip.ParseResult(
            Article = article,
            Reference = reference,
            Access = access,
            Authors = authors,
        ))
