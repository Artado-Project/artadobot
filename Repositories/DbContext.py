from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase as Base
from typing import List, TypeVar, Generic

T = TypeVar('T', bound=Base)


class DbContext(Generic[T]):

    def __init__(self, db_url):
        self.__engine = create_engine(db_url, echo=True)
        self.__Session: sessionmaker = sessionmaker(bind=self.__engine)

    def Create(self, obj: T):
        try:
            session = self.__Session()
            session.add(obj)
            session.commit()
            session.close()
        except Exception as e:
            print(e)

    def Update(self, obj: T):
        try:
            session = self.__Session()
            session.merge(obj)
            session.commit()
            session.close()
        except Exception as e:
            print(e)

    def Delete(self, id: int):
        try:
            session = self.__Session()
            obj = session.query(T).get(id)
            session.delete(obj)
            session.commit()
            session.close()
        except Exception as e:
            print(e)

    def GetById(self, id: int) -> T:
        try:

            session = self.__Session()
            obj: T = session.query(T).get(id)
            session.close()
            return obj
        except Exception as e:
            print(e)

    def GetAll(self) -> List:
        try:
            session = self.__Session()
            objects = session.query(T).all()
            session.close()
            return [entity for entity in objects]
        except Exception as e:
            print(e)

    def GetObjectsWithCondition(self, expression) -> List:
        try:
            session = self.__Session()
            objects = session.query(T).filter(expression).all()
            session.close()
            return objects
        except Exception as e:
            print(e)
