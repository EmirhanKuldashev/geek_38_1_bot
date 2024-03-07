import requests
from parsel import Selector


class NewsScraper:
    PLUS_URL = "https://knews.kg/"
    URL = "https://knews.kg/"
    HEADERS = {
        "Accept-Language":
            "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0"
    }

    LINK_XPATH = '//div[@class="td-block-span4"]/div[@class="td_module_mx4 td_module_wrap td-animation-stack"]/h3[@class="entry-title td-module-title"]/a/@href'

    def scrape_data(self):
        response = requests.request(method="GET", url=self.URL, headers=self.HEADERS)
        tree = Selector(text=response.text)
        links = tree.xpath(self.LINK_XPATH).getall()

        for link in links:
            print(link)

        return links


if __name__ == "__main__":
    scraper = NewsScraper()
    scraper.scrape_data()

