from os.path import dirname, join
from setuptools import find_packages, setup

KEYWORDS = []
CLASSIFIERS = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Natural Language :: French',
    'Operating System :: Unix',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: Implementation :: CPython',
    'Programming Language :: Python',
    'Topic :: Communications',
    'Topic :: Communications :: Chat',
]
INSTALL_REQUIRES = [
    'aiohttp==3.3.*',
    'click==6.7.*',
    'colorama==0.3.*',
    'coverage==4.5.*',
    'python-dotenv==0.8.*',
    'requests==2.19.*',
]

PROJECT_DIR = dirname(__file__)
README_FILE = join(PROJECT_DIR, 'README.md')
ABOUT_FILE = join(PROJECT_DIR, 'src', 'bumblebot', '__about__.py')


def get_readme():
    with open(README_FILE) as fileobj:
        return fileobj.read()


def get_about():
    about = {}
    with open(ABOUT_FILE) as fileobj:
        exec(fileobj.read(), about)
    return about


ABOUT = get_about()

setup(
    name=ABOUT['__title__'],
    version=ABOUT['__version__'],
    description=ABOUT['__summary__'],
    long_description=get_readme(),
    author=ABOUT['__author__'],
    author_email=ABOUT['__email__'],
    url=ABOUT['__uri__'],
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    entry_points={
        'console_scripts': [
            'bumblebot=bumblebot.__main__:main',
        ],
    },
    install_requires=INSTALL_REQUIRES,
    python_requires='>=3.7',
    zip_safe=False
)
