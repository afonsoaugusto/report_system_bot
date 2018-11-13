import unittest
from reportsystembot import report


class TestReport(unittest.TestCase):
    """
    Classe de test para obter os comandos
    """
    
    def test_get_command_df(self):
        """
        Testa o retorno do comando df
        """
        self.assertEqual(report.get_command('df'), 'df -kh')

if __name__ == '__main__':
    unittest.main()
