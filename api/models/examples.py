from pydantic import BaseModel, ConfigDict
from sqlalchemy import Column, Integer, String, select
from sqlalchemy.ext.asyncio import AsyncSession

from database import Base


class Example(BaseModel):
    id: int
    name: str
    description: str
    model_config = ConfigDict(from_attributes=True)


class ExampleCreate(BaseModel):
    name: str
    description: str


class ExampleOrm(Base):
    __tablename__ = "examples"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)


    @classmethod
    async def create(cls, db: AsyncSession, example: ExampleCreate) -> "ExampleOrm":
        db_example = ExampleOrm(name=example.name, description=example.description)
        db.add(db_example)
        await db.commit()
        await db.refresh(db_example)
        return db_example

    @classmethod
    async def get_all(cls, db: AsyncSession) -> list["ExampleOrm"]:
        result = await db.execute(select(cls))
        return result.scalars().all()
