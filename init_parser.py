import collections
import csv
from selenium import webdriver
from selenium_stealth import stealth
import time

ParseResult = collections.namedtuple(
    'ParseResult',
    (
        'Article',
        'Reference',
        'Access',
        'Authors',

    )
)

HEADERS = (
    'Статья',
    'Ссылка',
    'Доступ',
    'Авторы',
)


class parser:

    def __init__(self, url):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        # options.add_argument("--headless")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Chrome(options=options, executable_path="chromedriver.exe")

        stealth(self.driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )
        self.url = url
        self.result = []

    def save_results(self):
        with open(self.filename,'w', encoding='utf-8') as f:
            writer = csv.writer(f, quoting= csv.QUOTE_MINIMAL)
            writer.writerow(HEADERS)
            for item in self.result:
                writer.writerow(item)

    def run(self, filename):
        self.filename = filename
        self.parse_page()
        self.save_results()
        self.driver.close()







