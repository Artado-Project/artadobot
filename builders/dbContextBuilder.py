from typing import Type
from repositories.dbContext import DbContext


class DbContextBuilder:
    @staticmethod
    def Build(url, model_class):
        return DbContext(url, model_class)