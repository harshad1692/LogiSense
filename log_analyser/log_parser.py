# log_parser.py
import re

class LogParser:
    def __init__(self, rules=None):
        """
        rules: dict of parsing rules or regex patterns
        """
        self.rules = rules or {}

    def parse(self, raw_log):
        """
        Convert raw log line into structured dict.
        Example: {timestamp, level, service, message}
        """
        parsed_log = {}
        # TODO: implement parsing logic
        return parsed_log
