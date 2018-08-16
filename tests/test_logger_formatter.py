import re
import unittest
from logging import LogRecord

from bumblebot.services.logger.formatter import Formatter


class TestLoggerFormatter(unittest.TestCase):
    def test_format(self):
        formatter = Formatter()
        log_record = LogRecord(
            name='fake_name',
            level=10,
            msg='fake_message',
            pathname=None,
            lineno=None,
            args=None,
            exc_info=None
        )
        log = formatter.format(log_record)
        regexp = re.compile(
            r'^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]+ - '
            r'fake_name - DEBUG - fake_message$')
        assert re.search(regexp, log)
