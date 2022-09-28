import os
import shutil
import pytest
import random
import string

from test_runner_utils import ResultsCollector


def generate_random_str():
    letters = string.ascii_letters
    name = ''.join(random.choice(letters) for i in range(20))
    return name



class TestRunner:
    def __init__(self):
        self.dir_name = generate_random_str()

    def setup(self, code_path, test_path):
        # create temporary working dir
        os.mkdir(self.dir_name, mode=0o740)
        # copy code and test to the temporary working dir
        shutil.copyfile(code_path, os.path.join(self.dir_name, "user_code.py"))
        shutil.copyfile(test_path, os.path.join(self.dir_name, "test.py"))

    def run(self):
        try:
            collector = ResultsCollector()
            pytest.main([os.path.join(self.dir_name, "test.py")], plugins=[collector])

        except Exception as e:
            print("Error while trying to run test: ", e)

        total_tests_count = collector.passed + collector.failed
        if total_tests_count == 0:
            return 0

        return int(collector.passed * 100 / total_tests_count)

    def cleanup(self):
        shutil.rmtree(self.dir_name)
