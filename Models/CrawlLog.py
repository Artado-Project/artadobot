from Core import Model
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from Helpers import Contants


class CrawlLog(Model):
    __tablename__ = Contants.TableNames.CrawLog
    id = Column("id", Integer, primary_key=True, nullable=False, unique=True)
    page_id = Column("page_id", Integer, ForeignKey(f"{Contants.TableNames.Pages}.id"), nullable=False)
    rule_id = Column("rule_id", Integer, ForeignKey(f"{Contants.TableNames.CrawRules}.id"), nullable=False)
    status_code = Column("status_code", Integer, nullable=False)
    response_time = Column("response_time", Integer, nullable=False)
    error_message = Column("error_message", String, nullable=True)
    success_message = Column("success_message", String, nullable=True)
    is_allowed = Column("is_allowed", Boolean, nullable=False)

    def __init__(self,
                 id,
                 page_id,
                 rule_id,
                 status_code,
                 response_time,
                 error_message=None,
                 success_message=None,
                 is_allowed=True):
        self.id = id
        self.page_id = page_id
        self.rule_id = rule_id
        self.status_code = status_code
        self.response_time = response_time
        self.error_message = error_message
        self.success_message = success_message
        self.is_allowed = is_allowed
