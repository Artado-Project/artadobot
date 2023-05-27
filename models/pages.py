from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey

from core.model import Model
from helpers.constants import TableNames


class Pages(Model):
    __tablename__ = TableNames.Pages
    id = Column("id", Integer, primary_key=True, nullable=False, unique=True)
    domain_id = Column("domain_id", Integer, ForeignKey(f"{TableNames.WebSites}.id"), nullable=False)
    url = Column("url", String, nullable=False)
    is_allowed = Column("is_allowed", Boolean, nullable=False)
    crawled_at = Column("crawled_at", Date, nullable=True)

    def __init__(self, id, domain_id, url, is_allowed, crawled_at):
        self.id = id
        self.domain_id = domain_id
        self.url = url
        self.is_allowed = is_allowed
        self.crawled_at = crawled_at
