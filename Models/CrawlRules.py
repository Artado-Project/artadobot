from Core import Model
from sqlalchemy import Column, Integer, String, Boolean, Date, Text, ForeignKey
from Helpers import Contants


class CrawlRules(Model):
    __table__name = Contants.TableNames.CRAWLRULES

    id = Column("id", Integer, primary_key=True, nullable=False)
    domain_id = Column("domain_id", Integer, ForeignKey(f"{Contants.TableNames.WEBSITES}.id"),nullable=False)
    rules = Column("rules", Text, nullable=False)

    def __init__(self, id, domain_id, rules):
        self.id = id
        self.domain_id = domain_id
        self.rules = rules
