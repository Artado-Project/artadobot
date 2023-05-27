from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey

from core.model import Model
from helpers.constants import TableNames



class PageLinks(Model):
    __tablename__ = TableNames.PageLinks
    id = Column("id", Integer, primary_key=True, nullable=False)
    page_id = Column("page_id", Integer, ForeignKey(f"{TableNames.Pages}.id"), nullable=False)
    link_url = Column("link_url", String, nullable=False)
    link_type = Column("link_type", String, nullable=False)
    last_modified_at = Column("last_modified_at", Date, nullable=False)

    def __init__(self, id, page_id, link_url, link_type, last_modified_at):
        self.id = id
        self.page_id = page_id
        self.link_url = link_url
        self.link_type = link_type
        self.last_modified_at = last_modified_at
