import unittest
from reportsystembot import report
from reportsystembot.report import FormatText
from reportsystembot.report import Command


class TestReport(unittest.TestCase):
    """
    Classe de teste para obter os comandos
    """
    
    def test_get_command_df(self):
        """
        Testa o retorno do comando df
        """
        self.assertEqual(report.get_command('df'), 'df -kh')
 
class TestCommand(unittest.TestCase):
    """
    Classe para teste do formatador da saida
    """
    def test_command_2_mais_2(self):
        """
        Testa a execução do comando echo $((2+2))
        """
        comando = Command('echo $((2+2))')
        self.assertEqual([b'4\n'], comando.execute())

    def test_command_echo_duas_linhas(self):
        """
        Testa a execução do comando echo "Teste\nNova Linha"
        """
        comando = Command('echo "Teste\nNova Linha"')
        self.assertEqual([b'Teste\n',b'Nova Linha\n'], comando.execute())        
        
class TestReporFormatText(unittest.TestCase):
    """
    Classe para teste do formatador da saida
    """
    def test_format_command_2_mais_2(self):
        """
        Testa a formatacao do retorno do comando echo $((2+2))
        """
        dois_mais_dois = Command('echo $((2+2))').execute()
        self.assertEqual('4',FormatText(dois_mais_dois).format())
        
    def test_format_command_echo_duas_linhas(self):
        """
        Testa a formatacao do retorno do comando echo "Teste\nNova Linha"
        """
        duas_linhas = Command('echo "Teste\nNova Linha"').execute()
        self.assertEqual('Teste\nNova Linha',FormatText(duas_linhas).format())        

if __name__ == '__main__':
    unittest.main()
