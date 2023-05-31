from lib.solutions.CHK import checkout_solution


class TestCHK():
    def test_sum(self):
        assert checkout_solution.checkout("AAAAAAAABBBCDDEEFFF") == 525
        assert checkout_solution.checkout("EEEBFF") == 140
        assert checkout_solution.checkout("EEEEBB") == 160
        assert checkout_solution.checkout("EE") == 80
        assert checkout_solution.checkout("F") == 10
        assert checkout_solution.checkout("FF") == 20
        assert checkout_solution.checkout("FFF") == 20
        assert checkout_solution.checkout("FFFFF") == 40
        assert checkout_solution.checkout("FFFFFF") == 40
        assert checkout_solution.checkout("FFFFFFF") == 50

