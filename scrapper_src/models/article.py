from typing import Optional, List


class Article:
    """
    Model for a news article that will be used for analysing political disposition, its factuality, summarized content and other features
    """

    def __init__(
        self,
        title: str,
        author: str,
        url: str,
        content: str,
        date: str,
        source: str,
        tags: Optional[List[str]] = None,
    ) -> None:
        self.title = title
        self.author = author
        self.url = url
        self.content = content
        self.date = date
        self.source = source
        self.summary = None
        self.factuality = None
        self.tags = tags

    def __str__(self) -> str:
        return """Title: {title}
Author: {author}
URL: {url}
Content: {content}
Date: {date}
Source: {source}
Summary: {summary}
Factuality: {factuality}
Tags: {tags}
""".format(
            title=self.title,
            author=self.author,
            url=self.url,
            content=self.content,
            date=self.date,
            source=self.source,
            summary=self.summary,
            factuality=self.factuality,
            tags=self.tags,
        )

    def set_summary(self, summary: str) -> None:
        self.summary = summary

    def set_factuality(self, factuality: str) -> None:
        self.factuality = factuality
