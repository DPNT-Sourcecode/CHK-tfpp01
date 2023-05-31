from lib.solutions.CHK import checkout_solution


class TestCHK():
    def test_sum(self):
        assert checkout_solution.checkout("AAAAAAAABBBCDDEE") == 535
        assert checkout_solution.checkout("EEEB") == 150
        assert checkout_solution.checkout("EEEEBB") == 205


