from lib.solutions.CHK import checkout_solution


class TestCHK():
    def test_sum(self):
        assert checkout_solution.checkout("AAABBCCDD") == 245

