import os
import unittest
from reportsystembot.command import Command
from reportsystembot.command import CommandList
from test.support import EnvironmentVarGuard



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
    def setUp(self):
        absFilePath = os.path.abspath(__file__)                # Absolute Path of the module
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

if __name__ == '__main__':
    unittest.main()
