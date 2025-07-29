from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload


class CRUDBase:
    """Базовый CRUD."""

    def __init__(self, model) -> None:
        self.model = model

    async def create(self, session: AsyncSession, obj_in: dict):
        obj = self.model(**obj_in)
        session.add(obj)
        await session.commit()
        await session.refresh(obj)
        return obj

    async def get_all(self, session: AsyncSession):
        result = await session.execute(
            select(self.model).options(selectinload(self.model.movies))
        )
        return result.scalars().all()

    async def get_multi(self, session: AsyncSession, skip: int = 0, limit: int = 100):
        result = await session.execute(select(self.model).offset(skip).limit(limit))
        return result.scalars().all()

    async def _fetch_one(self, condition, session):
        stmt = select(self.model).where(condition)
        result = await session.execute(stmt)
        return result.scalars().first()

    async def get_by_attr(self, attr_name, attr_value, session):
        attr = getattr(self.model, attr_name)
        return await self._fetch_one(attr == attr_value, session)

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
