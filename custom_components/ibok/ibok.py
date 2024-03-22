"""
iBOK API
login url: ibok.puwis.pl/?JSTest=ok&user=[numer_kontrahenta]&pass=[hasło]&login=Zaloguj
"""

from __future__ import annotations

import aiohttp
import logging

from typing import Any, final
from datetime import date
from enum import IntFlag, unique

iBOK_API_URL: final = "https://ibok.puwis.pl/?"
iBOK_LOGIN: final = "JSTest=ok&"
ARISTON_REMOTE: final = "remote"
ARISTON_PLANTS: final = "plants"
ARISTON_LITE: final = "lite"
ARISTON_DATA_ITEMS: final = "dataItems"
ARISTON_ZONES: final = "zones"
ARISTON_PLANT_DATA: final = "plantData"
ARISTON_REPORTS: final = "reports"
ARISTON_TIME_PROGS: final = "timeProgs"

_LOGGER = logging.getLogger(__name__)

class iBOK_API:
    """iBOK API class"""

    def __init__(self, username: str, password: str) -> None:
        """Constructor for iBOK API."""
        self.__username = username
        self.__password = password
        self.__token = ""
      
    async def async_connect(self) -> bool:
        """Login to ariston cloud and get token"""

        response = await self.post(
            f"{iBOK_API_URL}{iBOK_LOGIN}user={self.__username}&pass={self.__password}&login=Zaloguj",
        )

        if response is None:
            return False

        self.__token = response["token"]

        return True
  
