from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class CRUDBase:
    def __init__(self, model) -> None:
        self.model = model

    async def create(self, session: AsyncSession, obj_in: dict):
        obj = self.model(**obj_in)
        session.add(obj)
        await session.commit()
        await session.refresh(obj)
        return obj

    async def read(self, session: AsyncSession, obj_id: int):
        result = await session.execute(
            select(self.model).where(self.model.id == obj_id)
        )
        return result.scalar_one_or_none()

    async def update(self, session: AsyncSession, obj_id: int, obj_in: dict):
        result = await session.execute(
            select(self.model).where(self.model.id == obj_id)
        )
        obj = result.scalar_one_or_none()
        if obj is None:
            return None
        for key, value in obj_in.items():
            setattr(obj, key, value)
        await session.commit()
        await session.refresh(obj)
        return obj

    async def delete(self, session: AsyncSession, obj_id: int):
        result = await session.execute(
            select(self.model).where(self.model.id == obj_id)
        )
        obj = result.scalar_one_or_none()
        if obj is None:
            return None
        await session.delete(obj)
        await session.commit()
        return obj
