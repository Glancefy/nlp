from bs4 import BeautifulSoup
import requests
from scrapper_src.data_scrapper import DataScrapper


class BBC_scrapper(DataScrapper):
    """
    Class for scraping BBC news articles

    Attributes:
    article_urls: List of article urls
    articles: List of article dictionaries
    """

    def __init__(
        self,
        save_dir="data",
        save_file="bbc_articles.jsonl",
        save_urls_file="bbc_article_urls.jsonl",
        verbose=False,
    ):
        super().__init__(save_dir, verbose)
        self.save_file = f"{save_dir}/{save_file}"
        self.save_urls_file = f"{save_dir}/{save_urls_file}"

    def scrape_article_urls(self, from_file=False):
        """
        Get article urls from BBC news website
        """
        url = "https://www.bbc.com/news"

        if from_file:
            self.load_article_urls_from_json(self.save_urls_file)
            if self.article_urls:
                return

        if self.verbose:
            print(f"Scraping article urls from {url}")
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        for link in soup.find_all("a"):
            if (link_val := link.get("href")) and link_val.startswith(
                "/news/articles/"
            ):
                self.article_urls.append(f"https://www.bbc.com{link_val}")

    def _scrape_article(self, url):
        """
        Get article from url
        """
        return {"text": f"This is a test article for {url}"}

    def scrape_articles(self):
        """
        Get articles from article urls
        """
        for url in self.article_urls[0]:
            self.articles.append({"url": url, **self._scrape_article(url)})
        return self.articles


if __name__ == "__main__":
    scrapper = BBC_scrapper()
    scrapper.save_articles_to_json("bbc_articles.json")
