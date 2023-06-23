from core.model import Model
from sqlalchemy import Column, Integer, String, Boolean, Date, Text, ForeignKey
from helpers.constants import TableNames


class CrawlRules(Model):
    __tablename__ = TableNames.CrawRules.value

    id = Column("id", Integer, primary_key=True, nullable=False)
    domain_id = Column("domain_id", Integer, ForeignKey(f"{TableNames.WebSites.value}.id"), nullable=False)
    rules = Column("rules", Text, nullable=False)

    def __init__(self, id, domain_id, rules):
        self.id = id
        self.domain_id = domain_id
        self.rules = rules
