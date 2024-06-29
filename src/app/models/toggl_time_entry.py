
import os
import urllib
from datetime import datetime
from typing import Optional, Iterator, List

import requests
from pydantic import BaseModel, par

class TogglTimeEntry(BaseModel):
    """TogglTimeEntry model."""
    id: int
    workspace_id: int
    user_id: int
    project_id: int
    task_id: Optional[int]
    billable: bool
    at: datetime
    description: str
    start: datetime
    stop: Optional[datetime]
    duration: int
    tags: Optional[List[str]]

    @property
    def initiative(self) -> str:
        """Returns the initiative part of the description."""
        return self.description.split(":")[0]
