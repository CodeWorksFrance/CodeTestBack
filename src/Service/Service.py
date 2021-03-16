from abc import ABC

from db_config import DBConfig


class Service(ABC):
    @property
    def _type(self):
        raise NotImplementedError

    def get(self, index: str = None) -> [_type]:
        session = DBConfig().get_session()
        if index is None:
            query_result = session.query(self._type)
            session.close()
            return query_result

        query_result = session.query(self._type).filter_by(id=index)
        session.close()
        return query_result

    def create(self, element: _type) -> _type:
        session = DBConfig().get_session()
        session.add(element)
        session.commit()
        element_id = str(element.id)
        session.close()

        return self.get(element_id).first()

    def update(self, index: str, instruction: dict):
        session = DBConfig().get_session()
        session.query(self._type).filter(self._type.id == index).update(instruction)
        session.commit()
        session.close()
