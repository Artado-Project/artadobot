from Core import Model
from sqlalchemy import Column, Integer, String, Boolean, Date
from Helpers import Contants


class WebSites(Model):
    __tablename__ = Contants.TableNames.WebSites

    id = Column("id", Integer, primary_key=True, nullable=False, unique=True)
    using_js = Column("using_js", Boolean, nullable=False)
    using_asp = Column("using_asp", Boolean, nullable=False)
    using_php = Column("using_php", Boolean, nullable=False)
    is_support_ios = Column("is_support_ios", Boolean, nullable=False)
    is_support_android = Column("is_support_android", Boolean, nullable=False)
    page_rank = Column("page_rank", Integer, nullable=True)

    def __init__(self, id, using_js, using_asp, using_php, is_support_ios, is_support_android, page_rank=None):
        self.id = id
        self.using_js = using_js
        self.using_asp = using_asp
        self.using_php = using_php
        self.is_support_ios = is_support_ios
        self.is_support_android = is_support_android
        self.page_rank = page_rank
