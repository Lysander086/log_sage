from .core import hmm
import os
import urllib
import requests
from typing import List, Iterator
from datetime import datetime
from app.models.toggl_time_entry import TogglTimeEntry


class TogglService:
    """Service for interacting with the TimeEntries API."""

    def __init__(self, api_token: str) -> None:
        self.api_token = api_token

    @classmethod
    def from_environment(cls) -> "TogglService":
        """Creates a new `TogglService` instance from the `TOGGL_API_TOKEN` environment variable."""
        if "TOGGL_API_TOKEN" not in os.environ:
            raise Exception(
                "TOGGL_API_TOKEN environment variable not found. "
                "Please set it to your Toggl Track API token."
            )
        return cls(api_token=os.environ["TOGGL_API_TOKEN"])

    def list_time_entries(self, start_date: datetime, end_date: datetime, description: str = None, project_ids: List[int] = []) -> Iterator[TogglTimeEntry]:
        """Fetches the time entries between `start_date` and `end_date` dates.

        Time Entries API v9
        https://developers.track.toggl.com/docs/api/time_entries
        """
        params = dict(
            start_date=start_date.isoformat() + "Z",
            end_date=end_date.isoformat() + "Z",
        )

        url = (
            "https://api.track.toggl.com/api/v9/me/time_entries?"
            + urllib.parse.urlencode(params)
        )

        resp = requests.get(url, auth=(self.api_token, "api_token"))
        if resp.status_code != 200:
            raise Exception(resp.text)

        # it looks like the API doesn't support filtering, so I suppose
        # we have to do it ourselves
        entries = [TogglTimeEntry(**entry) for entry in resp.json()]

        if description:
            entries = filter(
                lambda entry: description in entry.initiative, entries)

        if project_ids:
            entries = filter(
                lambda entry: entry.project_id in project_ids, entries)

        return entries
