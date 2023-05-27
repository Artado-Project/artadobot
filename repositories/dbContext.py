from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine
from typing import List, TypeVar, Generic, Type
from models.webSites import WebSites
from core.model import Model



class DbContext:
    def __init__(self, db_url:str, model_class):
        self.__model_class = model_class
        self.__engine = create_engine(db_url, echo=True)
        self.__Session: sessionmaker = sessionmaker(bind=self.__engine)

    def Create(self, obj):
        try:
            session = self.__Session()
            session.add(obj)
            session.commit()
            session.close()
            return obj
        except Exception as e:
            print(e)

    def Update(self, obj):
        try:
            session = self.__Session()
            session.merge(obj)
            session.commit()
            session.close()
            return obj
        except Exception as e:
            print(e)

    def Delete(self, id: int):
        try:
            session = self.__Session()
            obj = session.query(self.__model_class).get(id)
            session.delete(obj)
            session.commit()
            session.close()
        except Exception as e:
            print(e)

    def GetById(self, id: int):
        try:

            session = self.__Session()
            obj = session.query(self.__model_class).get(id)
            session.close()
            return obj
        except Exception as e:
            print(e)

    def GetAll(self) -> List:
        try:
            session = self.__Session()
            objects = session.query(self.__model_class).all()
            session.close()
            return [entity for entity in objects]
        except Exception as e:
            print(e)

    def GetObjectsWithCondition(self, expression) -> List:
        try:
            session = self.__Session()
            objects = session.query(self.__model_class).filter(expression).all()
            session.close()
            return objects
        except Exception as e:
            print(e)
    def __createTable(self):
        session = self.Session()
        WebSites.__table__.create(bind=self.engine)
        session.close()