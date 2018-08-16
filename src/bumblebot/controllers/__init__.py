from aiohttp import web

from bumblebot.controllers.facebook import FacebookController
from bumblebot.services.google import GoogleClient


class Route:
    routes: [] = []

    def __init__(self, google: GoogleClient = None):
        controller = FacebookController(
            google=google
        )
        self._add(web.RouteDef(
            method='GET',
            path='/',
            handler=controller.get,
            kwargs={}
        ))
        pass

    def all(self):
        return self.routes

    def _add(self, route):
        self.routes.append(route)
