from aiohttp import web

from bumblebot.services.google import GoogleClient
from bumblebot.services.logger import Logger


class FacebookController:
    _google: GoogleClient = None

    def __init__(self, google: GoogleClient = None):
        self._google = google

    async def get(self, request):
        logger = Logger.get('main.controllers.facebook')
        logger.debug([request, self._google])
        return web.Response(text="Wololooo")
