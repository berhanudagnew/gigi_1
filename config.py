"""
Music Player, Telegram Voice Chat Bot
Copyright (c) 2021-present Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

from os import getenv
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: int = int(getenv("API_ID", None))

        self.API_HASH: str = getenv("API_HASH", None)
        self.SESSION: str = getenv("SESSION", None)
        self.BOT_TOKEN: str = getenv("BOT_TOKEN", None)
        self.SUDOERS: list = [
            int(id) for id in getenv("SUDOERS", " ").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("ERROR: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.SPOTIFY: bool = False
        self.QUALITY: str = getenv("QUALITY", "high").lower()
        self.PREFIXES: list = getenv("PREFIX", "!").split()
        self.LANGUAGE: str = getenv("LANGUAGE", "en").lower()
        self.STREAM_MODE: str = (
            "audio"
            if (getenv("STREAM_MODE", "audio").lower() == "audio")
            else "video"
        )
        self.ADMINS_ONLY: bool = getenv("ADMINS_ONLY", False)
        self.SPOTIFY_CLIENT_ID: str = getenv("SPOTIFY_CLIENT_ID", None)
        self.SPOTIFY_CLIENT_SECRET: str = getenv("SPOTIFY_CLIENT_SECRET", None)
    


config = Config()
