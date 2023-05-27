from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey

from core.model import Model
from helpers.constants import TableNames



class PageImages(Model):
    __tablename__ = TableNames.PageImages
    id = Column("id", Integer, primary_key=True, nullable=False)
    page_id = Column("page_id", Integer, ForeignKey(f"{TableNames.Pages}.id"), nullable=False)
    alt_text = Column("alt_text", String, nullable=True)
    height = Column("height", Integer, nullable=True)
    width = Column("width", Integer, nullable=True)

    def __init__(self, id, page_id, alt_text=None, height=None, width=None):
        self.id = id
        self.page_id = page_id
        self.alt_text = alt_text
        self.height = height
        self.width = width