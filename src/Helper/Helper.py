from abc import ABC, abstractmethod

import typing


class Helper(ABC):
    @property
    def _type_dto(self) -> type:
        raise NotImplementedError

    @property
    def _type_model(self) -> type:
        raise NotImplementedError

    @property
    def _type_service(self) -> type:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def map(element_dto: _type_dto) -> _type_model:
        raise NotImplementedError

    def map_all(self, elements_dto: [_type_dto]):
        return [self.map(element_dto) for element_dto in elements_dto]

    def retrieve(self) -> typing.List[type(_type_model)]:
        return self.map_all(self._type_service().get())

    def retrieve_by_index(self, index: str) -> typing.Optional[type(_type_model)]:
        element = self._type_service().get(index).first()
        return None if element is None else self.map(element)
