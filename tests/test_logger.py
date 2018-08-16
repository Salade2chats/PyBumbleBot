import unittest

from bumblebot.services.logger import Logger


class TestLogger(unittest.TestCase):
    def test_prepare(self):
        logger = Logger.prepare('root_name', 10)
        assert logger.getEffectiveLevel() == 10

    def test_get(self):
        Logger.prepare('root_name', 10)
        logger = Logger.get('root_name.sub_name')
        assert logger.getEffectiveLevel() == 10
