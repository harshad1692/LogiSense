# main.py
from log_ingestor import LogIngestor
from log_parser import LogParser
from log_storage import LogStorage
from log_query import LogQuery
from log_analyser import LogAnalyser
from log_alerts import LogAlerts
from log_dashboard import LogDashboard

def main():
    sources = ["app.log"]  # example log sources
    ingestor = LogIngestor(sources)
    raw_logs = ingestor.read_logs()

    parser = LogParser()
    parsed_logs = [parser.parse(log) for log in raw_logs]

    storage = LogStorage()
    storage.bulk_save(parsed_logs)

    analyser = LogAnalyser(storage)
    dashboard = LogDashboard(analyser)
    dashboard.show_summary()

    alerts = LogAlerts(rules={"ERROR": 10})
    triggered = alerts.check_alerts(parsed_logs)
    for alert in triggered:
        alerts.notify(alert)

if __name__ == "__main__":
    main()
