from lib.solutions.CHK import checkout_solution


class TestCHK():
    def test_sum(self):
        assert checkout_solution.checkout("AAAAAAAABBBCDDEEFFF") == 525
        assert checkout_solution.checkout("EEEBFF") == 130
        assert checkout_solution.checkout("EEEEBBFFFF") == 180
        assert checkout_solution.checkout("EEFFFFFFFFFF") == 130
        assert checkout_solution.checkout("F") == 10
        assert checkout_solution.checkout("FF") == 10
        assert checkout_solution.checkout("FFF") == 20
        assert checkout_solution.checkout("FFFFF") == 30

