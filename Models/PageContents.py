from Core import Model
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from Helpers import Contants


class PageContents(Model):
    __tablename__ = Contants.TableNames.PAGECONTENTS
    id = Column("id", Integer, primary_key=True, nullable=False)
    page_id = Column("page_id", Integer, ForeignKey(f"{Contants.TableNames.PAGES}.id"),nullable=False)
    title = Column("title", String, nullable=False)
    keywords = Column("keywords", String, nullable=False)
    content_type = Column("content_type", String, nullable=False)
    last_modified_at = Column("last_modified_at", Date, nullable=False)

    def __init__(self, id, page_id, title, keywords, content_type, last_modified_at):
        self.id = id
        self.page_id = page_id
        self.title = title
        self.keywords = keywords
        self.content_type = content_type
        self.last_modified_at = last_modified_at
