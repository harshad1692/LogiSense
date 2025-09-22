# log_storage.py
class LogStorage:
    def __init__(self, db_type="sqlite", db_path="logs.db"):
        self.db_type = db_type
        self.db_path = db_path
        # TODO: initialize DB connection

    def save(self, parsed_log):
        """
        Save parsed log into storage
        """
        # TODO: implement save logic
        pass

    def bulk_save(self, parsed_logs):
        for log in parsed_logs:
            self.save(log)
