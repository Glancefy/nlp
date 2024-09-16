from scrapper_src.news_sources.bbc import BBC_scrapper

save_dir = "data"
article_urls_file = "bbc_article_urls.jsonl"
articles_file = "bbc_articles.jsonl"


def main():
    bbc_scrapper = BBC_scrapper(
        save_dir=f"{save_dir}/bbc",
        save_file=articles_file,
        save_urls_file=article_urls_file,
        verbose=True,
    )
    bbc_scrapper.scrape_article_urls(from_file=False)
    bbc_scrapper.save_article_urls_to_json(
        f"{save_dir}/bbc/{article_urls_file}", pretty=True
    )


if __name__ == "__main__":
    main()
