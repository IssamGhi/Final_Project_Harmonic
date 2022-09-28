import time
import pytest
from test_runner import TestRunner


class IssueToSolve:
    def __init__(self, user_id, issue_id, code_path, test_path):
        self.user_id = user_id
        self.issue_id = issue_id
        self.code_path = code_path
        self.test_path = test_path

# TODO: delete after developing get_issue_from_db()
issues = [IssueToSolve(1, 1, './tests/user_code.py', './tests/test.py')]


def run_test_on_issue():
    while True:
        print("Checking for new tests in DB")
        issue_to_solve = get_issue_from_db()
        if issue_to_solve is None:
            time.sleep(5)
            continue

        test_runner = TestRunner()
        test_runner.setup(issue_to_solve.code_path, issue_to_solve.test_path)
        result = test_runner.run()
        test_runner.cleanup()

        try:
            put_test_result_to_db(result, issue_to_solve.user_id, issue_to_solve.issue_id)
        except:
            print("Error while trying to put test result to DB")


def get_issue_from_db() -> IssueToSolve:
    if len(issues) > 0:
        return issues.pop(0)
    # TODO: get (user_id, issue_id, code_path, test_path) from DB


def run_test(path):
    result = pytest.main([path])
    if result.value == result.OK:
        print("Test passed")
    else:
        print("Test failed")


def put_test_result_to_db(test_result, user_id, issue_id):
    print(f"Saving test result {test_result} to DB for user_id={user_id}, issue_id={issue_id}")
    # TODO: save result to DB instead of just printing it


if __name__ == '__main__':
    run_test_on_issue()
