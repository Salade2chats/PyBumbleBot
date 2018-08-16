import os
from pathlib import Path

import click
from aiohttp import web
from dotenv import load_dotenv

from bumblebot.controllers import Route
from bumblebot.services.google import GoogleClient
from .__about__ import __version__
from .services.logger import Logger


@click.group(context_settings={'help_option_names': ['-h', '--help']})
@click.version_option(__version__)
@click.option('-q', '--quiet', is_flag=True, help="no output")
@click.option('-v', '--verbose', count=True, help="verbosity level")
def main(quiet, verbose):
    """Bumblebot is ur salve. Slap it. 🐟"""
    Logger.prepare('main', 1000 if quiet else 50 - verbose * 10)
    # configure app
    load_dotenv(dotenv_path=Path('.') / '.env')


@main.command()
def run():
    app = web.Application()
    routes = Route(
        google=GoogleClient(api_key=os.getenv('GOOGLE_API_KEY'))
    ).all()
    app.add_routes(routes)
    # app.add_routes([web.get('/', handle),
    #                web.get('/{name}', handle)])

    web.run_app(app)


if __name__ == '__main__':
    main()
