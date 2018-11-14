import platform
import subprocess


def get_command(command_name):
    return get_commands()[command_name]
    
def get_commands():
    return {'os_name'				:	'uname -a | awk {\'print$1\'} | cut -f2 -d\'-\'',\
            'upt'					:	'uptime | awk {\'print$3\'} | cut -f1 -d\',\'',\
            'ip_add'				:	'ifconfig | grep "inet addr" | head -2 | tail -1 | awk {\'print$2\'} | cut -f2 -d:',\
            'num_proc'			    :	'ps -ef | wc -l',\
            'root_fs_pc'			:	'df -h /dev/sda1 | tail -1 | awk \'{print$5}\'',\
            'root_fs_pc_numeric'	:	'df -h /dev/sda1 | tail -1 | awk \'{print$5}\' | cut -f1 -d\'%\'',\
            'total_root_size'		:	'df -h /dev/sda1 | tail -1 | awk \'{print$2}\'',\
            'load_avg'			    :	'cat /proc/loadavg  | awk {\'print$1,$2,$3\'}',\
            'ram_usage'			    :	'free -m | head -2 | tail -1 | awk {\'print$3\'}',\
            'ram_total'			    :	'free -m | head -2 | tail -1 | awk {\'print$2\'}',\
            'ram_pc'				:	'echo "scale:2; $ram_usage / $ram_total * 100" | bc | cut -f1 -d \'.\'',\
            'inode'				    :	'df -i / | head -2 | tail -1 | awk {\'print$5\'}',\
            'inode_numeric'		    :	'df -i / | head -2 | tail -1 | awk {\'print$5\'} | cut -f1 -d \'%\'',\
            'os_version'			:	'uname -v | cut -f2 -d\'~\' | awk {\'print$1\'} | cut -f1 -d\'-\' | cut -c 1-5',\
            'num_users'			    :	'w | head -1 | awk \'{print$4}\'',\
            'cpu_free'			    :	'top b -n1 | head -5 | head -3 | tail -1 | awk \'{print$8}\' | cut -f1 -d \',\'',\
            'last_reboot'			:	'who -b | awk \'{print$3, $4}\'',\
            'df'					:	'df -kh' }

class ReportSO:

    def __init__(self):
        pass

    def get_arch(self):
        return platform.architecture()[0]
        
    def get_return_command(self,command):
        return_command = Command(command).execute()
        return FormatText(return_command).format()
        
    def get_load_average(self):
        return self.get_return_command(get_command('load_avg'))

    def get_uptime(self):
        return self.get_return_command(get_command('upt'))


class Command:
    def __init__(self, command):
        self.command = command
        
    def execute(self):
        p = subprocess.Popen(self.command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return p.stdout.readlines()

class FormatText:
    
    def __init__(self,text):
        self.text = text
        
    def format(self):
        if len(self.text) == 0:
            return ''
        elif len(self.text) == 1:
            return self.text[0].decode("utf-8").replace('\n','')
        else:
            re_text = []
            for phrase in self.text:
                re_text.append(phrase .decode("utf-8"))
            re_text[len(re_text)-1] = re_text[len(re_text)-1].replace('\n','')
            return ''.join(re_text)