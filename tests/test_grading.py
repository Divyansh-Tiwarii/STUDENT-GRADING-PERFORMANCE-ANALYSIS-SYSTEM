import unittest, sys
sys.path.insert(0,'.')
from grading import result_status, calculate_total, calculate_average, grade_from_average

class TestGrading(unittest.TestCase):
    def test_pass(self): self.assertEqual(result_status([50,60,70]), 'PASS')
    def test_fail(self): self.assertEqual(result_status([50,49,70]), 'FAIL')
    def test_total_average(self):
        self.assertEqual(calculate_total([80,70,90]), 240)
        self.assertEqual(calculate_average([80,70,90]), 80)
    def test_grade(self): self.assertEqual(grade_from_average(95), ('A+',10))

if __name__ == '__main__': unittest.main()
