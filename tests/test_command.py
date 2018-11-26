import os
import unittest
from reportsystembot.command import Command
from reportsystembot.command import CommandList
from test.support import EnvironmentVarGuard


class TestCommandList(unittest.TestCase):
    """
    Classe de teste para obter os comandos
    """

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

    def test_is_command_valid(self):
        """
        Testa se comando eh valido
        """
        self.assertTrue(CommandList().is_command_valid('/simples'))
        self.assertTrue(CommandList().is_command_valid_without_parameters('simples'))
               
    def test_is_command_not_valid(self):
        """
        Testa se comando nao eh valido
        """
        self.assertFalse(CommandList().is_command_valid('/simples123'))
        self.assertFalse(CommandList().is_command_valid_without_parameters('simples123'))
        
    def test_is_command_valid_with_parameters(self):
        """
        Testa se comando eh valido
        """
        self.assertTrue(CommandList().is_command_valid('/simples_parametros','a  b  c'))
        self.assertTrue(CommandList().is_command_valid_with_parameters('simples_parametros','a  b  c'))               

class TestCommand(unittest.TestCase):
    """
    Classe para teste da execução de comandos no SO.
    """
    def setUp(self):
        fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
        parentDir = os.path.dirname(fileDir)                   # Directory of the Module directory
        path_scripts = os.path.join(parentDir, 'scripts_teste')   # Get the directory for StringFunction

        environ = EnvironmentVarGuard()
        current_path = environ.get('PATH')
        new_path = ':'.join([current_path,path_scripts])
        environ.set('PATH',new_path)

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

    def test_generate_command_name(self):
        """
        Testa a criação do comando a ser executado passando apenas o nome
        """
        command = Command('comando')
        self.assertEqual('comando', command.generate_command())

    def test_generate_command_name_one_parameter(self):
        """
        Testa a criação do comando a ser executado passando um parametro
        """
        command = Command('comando',parameters='-t tempo')
        self.assertEqual('comando -t tempo', command.generate_command())

    def test_generate_command_name_one_parameter_with_space(self):
        """
        Testa a criação do comando a ser executado passando um parametro com espaço
        """
        command = Command('comando',parameters='-t tempo ')
        self.assertEqual('comando -t tempo', command.generate_command())
        command = Command('comando',parameters=' -t tempo')
        self.assertEqual('comando -t tempo', command.generate_command())
        command = Command('comando',parameters=' -t tempo ')
        self.assertEqual('comando -t tempo', command.generate_command())

    def test_generate_command_name_two_parameter(self):
        """
        Testa a criação do comando a ser executado passando dois parametros
        """
        command = Command('comando',parameters='-t tempo -d data')
        self.assertEqual('comando -t tempo -d data', command.generate_command())

    def test_generate_command_name_two_parameter_with_spaces(self):
        """
        Testa a criação do comando a ser executado passando dois parametros com espaços
        """
        command = Command('comando',parameters='-t tempo -d data ')
        self.assertEqual('comando -t tempo -d data', command.generate_command())

    def test_generate_command_name_with_help(self):
        """
        Testa a criação do help do comando com espaços.
        """
        command = Command('comando',parameters='-t tempo -d data',desc_help='Comando de teste')
        self.assertEqual('/comando -t tempo -d data\n\t -Comando de teste', command.generate_command_help())
        command = Command('comando',parameters='-t tempo -d data ',desc_help='Comando de teste ')
        self.assertEqual('/comando -t tempo -d data\n\t -Comando de teste', command.generate_command_help())
        command = Command('comando',parameters='-t tempo -d data ',desc_help=' Comando de teste')
        self.assertEqual('/comando -t tempo -d data\n\t -Comando de teste', command.generate_command_help())
        command = Command('comando',parameters='-t tempo -d data ',desc_help=' Comando de teste ')
        self.assertEqual('/comando -t tempo -d data\n\t -Comando de teste', command.generate_command_help())

if __name__ == '__main__':
    unittest.main()
