import typing

from Models.Workshop import Workshop
from Service.WorkshopService import WorkshopService


class WorkshopHelper:
    @staticmethod
    def retrieve_workshop(index: str) -> typing.List[Workshop]:
        return[Workshop(w.id, w.state, w.score) for w in WorkshopService.get_workshops(index)]
