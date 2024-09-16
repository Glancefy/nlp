import json
from typing import List, Dict


class DataScrapper:
    """
    Base class for data scrapper classes

    Attributes:
    article_urls: List of article urls
    articles: List of article dictionaries
    """

    def __init__(self, save_dir: str, verbose: bool):
        self.article_urls: List[str] = []
        self.articles: List[Dict[str, str]] = []
        self.save_dir: str = save_dir
        self.verbose = verbose

    def save_articles_to_json(self, filename):
        if self.verbose:
            print(f"Saving articles to file {filename}")
        with open(filename, "w") as file:
            json.dump(self.articles, file)

    def save_article_urls_to_json(self, filename, pretty=False):
        if self.verbose:
            print(f"Saving article urls to file {filename}")
        with open(filename, "w") as file:
            json.dump(self.article_urls, file, indent=4 if pretty else None)

    def load_articles_from_json(self, filename):
        if self.verbose:
            print(f"Loading articles from file {filename}")
        try:
            with open(filename, "r") as file:
                self.articles = json.load(file)
        except FileNotFoundError:
            print(f"File {filename} not found")

    def load_article_urls_from_json(self, filename):
        if self.verbose:
            print(f"Loading article urls from file {filename}")
        try:
            with open(filename, "r") as file:
                self.article_urls = json.load(file)
        except FileNotFoundError:
            print(f"File {filename} not found")

    def get_articles(self):
        return self.articles

    def get_article_urls(self):
        return self.article_urls
