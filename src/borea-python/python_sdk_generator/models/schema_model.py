from typing import Dict, Any
from pydantic import BaseModel


class SchemaPyJinja(BaseModel):
    schema_name: str
    schema_data: Dict[str, Any]
    models_filename: str
    description: str = ""
