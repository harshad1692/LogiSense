# log_alerts.py
class LogAlerts:
    def __init__(self, rules):
        self.rules = rules  # e.g., {"ERROR": 100 per min}

    def check_alerts(self, logs):
        """
        Check logs against alert rules
        Returns list of triggered alerts
        """
        alerts = []
        # TODO: implement alert logic
        return alerts

    def notify(self, alert):
        """
        Send notification (email, slack, etc.)
        """
        # TODO: implement notification logic
        print(f"ALERT: {alert}")
