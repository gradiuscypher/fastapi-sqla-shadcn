from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from models.examples import Example, ExampleOrm

router = APIRouter(prefix="/examples", tags=["examples"])


@router.get("/")
async def get_examples(db: Annotated[AsyncSession, Depends(get_db)]) -> list[Example]:
    examples =  await ExampleOrm.get_all(db)
    return [Example.model_validate(example) for example in examples]


@router.post("/")
async def create_example(db: Annotated[AsyncSession, Depends(get_db)], example: Example) -> Example:
    db_example = await ExampleOrm.create(db, example)
    return Example.model_validate(db_example)
