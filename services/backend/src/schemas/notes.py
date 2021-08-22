from typing import Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.databse.models import Notes


NoteInSchema = pydantic_model_creator(
  Notes, name="Notein", exclude=["author_id"], exclude_readonly=True
)
NoteOutSchema = pydantic_model_creator(
  Notes, name="Note", exclude=[
    "modified_at", "author.password", "author.created_at", "author.modified_at"
  ]
)

class UpdateNote(BaseModel):
  title: Optional[str]
  content: Optional[str]