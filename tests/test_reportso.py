import unittest
from reportsystembot.command import Command
from reportsystembot.report import FormatText
from reportsystembot.report import ReportSO


class TesteRportSO(unittest.TestCase):
    """
    Classe para teste do Report de Comandos.
    """

    def test_get_return_command_teste(self):
        """
        Testa a execução do comando teste
        """
        self.assertEqual(ReportSO().get_return_command('teste'),'Testes')

    def test_get_return_command_simples(self):
        """
        Testa a execução do comando simples
        """
        self.assertEqual('simples', ReportSO().report('/simples'))

class TestReporFormatText(unittest.TestCase):
    """
    Classe para teste do formatador da saida
    """

    def test_format_command_2_mais_2(self):
        """
        Testa a formatacao do retorno do comando echo $((2+2))
        """
        dois_mais_dois = Command('echo $((2+2))').execute()
        self.assertEqual(FormatText(dois_mais_dois).format(),'4')

    def test_format_command_echo_duas_linhas(self):
        """
        Testa a formatacao do retorno do comando echo "Teste\nNova Linha"
        """
        duas_linhas = Command('echo "Teste\nNova Linha"').execute()
        self.assertEqual(FormatText(duas_linhas).format(),'Teste\nNova Linha')

if __name__ == '__main__':
    unittest.main()