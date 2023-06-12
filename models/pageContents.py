from sqlalchemy import Column, Integer, VARCHAR, Boolean, Date, ForeignKey

from core.model import Model
from helpers.constants import TableNames


class PageContents(Model):
    __tablename__ = TableNames.PageContents.value
    id = Column("id", Integer, primary_key=True, nullable=False)
    page_id = Column("page_id", Integer, ForeignKey(f"{TableNames.Pages.value}.id"), nullable=False)
    title = Column("title", VARCHAR(50), nullable=False)
    description = Column("description", VARCHAR(50), nullable=False)
    keywords = Column("keywords", VARCHAR(50), nullable=False)
    content_type = Column("content_type", VARCHAR(50), nullable=False)
    last_modified_at = Column("last_modified_at", Date, nullable=False)

    def __init__(self, id, page_id, title, keywords, description, content_type, last_modified_at):
        self.id = id
        self.page_id = page_id
        self.title = title
        self.description = description
        self.keywords = keywords
        self.content_type = content_type
        self.last_modified_at = last_modified_at
