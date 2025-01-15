from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession


class AbstractRepository(ABC):
    @abstractmethod
    def __init__(self, session):
        raise NotImplementedError

    @abstractmethod
    async def add(self, data: dict):
        return NotImplementedError

    @abstractmethod
    async def get_by_id(self, id):
        return NotImplementedError

    @abstractmethod
    async def find_all(self):
        return NotImplementedError

    @abstractmethod
    async def delete(self, data):
        return NotImplementedError


