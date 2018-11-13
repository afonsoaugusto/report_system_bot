import unittest
from reportsystembot.reportso import ReportSO

class TestReportSO(unittest.TestCase):
    """
    Classe de test dos relatótios
    """

    def test_arch(self):
        """
        Primeiro Testesss
        """
        rso = ReportSO()
        self.assertEqual(rso.get_arch(), '64bit')


if __name__ == '__main__':
    unittest.main()
