import unittest
from reportsystembot import report
from reportsystembot.report import FormatText
from reportsystembot.report import Command
from reportsystembot.report import CommandList
from reportsystembot.report import ReportSO



class TestCommandList(unittest.TestCase):
    """
    Classe de teste para obter os comandos
    """

    def test_get_command_df(self):
        """
        Testa o retorno do comando df
        """
        self.assertEqual(CommandList().get_command('df'), 'df -kh')
        self.assertEqual(CommandList().get_command('/df'), 'df -kh')

    def test__clear_command_sem_barra(self):
        """
        Testa sem o uso de barras no comando.
        """
        self.assertEqual(CommandList().clear_command('uname'), 'uname')

    def test__clear_command_com_barras(self):
        """
        Testa com o uso de barras no comando.
        """
        self.assertEqual(CommandList().clear_command('/df -h'), 'df -h')
        self.assertEqual(CommandList().clear_command('/df -h /dev/sda1'), 'df -h /dev/sda1')

    def test_get_command_com_barra(self):
        """
        Testa o uso de barras nos comandos.
        """
        self.assertEqual(CommandList().get_command('/uname'), 'uname -a')




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

class TesteRportSO(unittest.TestCase):
    """
    Classe para teste do Report de Comandos.
    """

    def test_get_return_command_teste(self):
        """
        Testa a execução do comando teste
        """
        self.assertEqual('Testes', ReportSO().get_return_command('teste'))


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
