import time
import pytest


class ResultsCollector:
    def __init__(self):
        self.reports = []
        self.passed = 0
        self.failed = 0
        self.total_duration = 0

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_makereport(self):
        outcome = yield
        report = outcome.get_result()
        if report.when == 'call':
            self.reports.append(report)

    def pytest_terminal_summary(self, terminalreporter, exitstatus):
        for report in self.reports:
            self.passed += 1 if report.outcome == "passed" else 0
            self.failed += 1 if report.outcome == "failed" else 0
        self.total_duration = time.time() - terminalreporter._sessionstarttime
