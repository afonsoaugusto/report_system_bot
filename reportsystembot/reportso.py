import platform
import subprocess


class ReportSO:

    def __init__(self):
        self.os_name='uname -v | awk {\'print$1\'} | cut -f2 -d\'-\''
        self.upt='uptime | awk {\'print$3\'} | cut -f1 -d\',\''
        self.ip_add='ifconfig | grep "inet addr" | head -2 | tail -1 | awk {\'print$2\'} | cut -f2 -d:'
        self.num_proc='ps -ef | wc -l'
        self.root_fs_pc='df -h /dev/sda1 | tail -1 | awk \'{print$5}\''
        self.root_fs_pc_numeric='df -h /dev/sda1 | tail -1 | awk \'{print$5}\' | cut -f1 -d\'%\''
        self.total_root_size='df -h /dev/sda1 | tail -1 | awk \'{print$2}\''
        self.load_avg='cat /proc/loadavg  | awk {\'print$1,$2,$3\'}'
        self.ram_usage='free -m | head -2 | tail -1 | awk {\'print$3\'}'
        self.ram_total='free -m | head -2 | tail -1 | awk {\'print$2\'}'
        self.ram_pc='echo "scale=2; $ram_usage / $ram_total * 100" | bc | cut -f1 -d \'.\''
        self.inode='df -i / | head -2 | tail -1 | awk {\'print$5\'}'
        self.inode_numeric='df -i / | head -2 | tail -1 | awk {\'print$5\'} | cut -f1 -d \'%\''
        self.os_version='uname -v | cut -f2 -d\'~\' | awk {\'print$1\'} | cut -f1 -d\'-\' | cut -c 1-5'
        self.num_users='w | head -1 | awk \'{print$4}\''
        self.cpu_free='top b -n1 | head -5 | head -3 | tail -1 | awk \'{print$8}\' | cut -f1 -d \',\''
        self.last_reboot='who -b | awk \'{print$3, $4}\''
        self.df='df -kh'

    def get_arch(self):
        return platform.architecture()[0]

    def get_load_average(self):
        return_command = self.execute_comand('w | grep "load average" | awk \'{print $6 " "$7" " $10}\'')
        return return_command[0].decode("utf-8")

    def get_uptime(self):
        return_command = self.execute_comand('uptime')
        return format_return(return_command)

    def get_free(self):
        return_command = self.execute_comand('free -m')
        return format_return(return_command)

    def get_uname(self):
        return_command = self.execute_comand('uname -a')
        return format_return(return_command)

    def get_filesystems(self):
        return self.execute_comand('df -kh')

    def execute_comand(self, command):
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return p.stdout.readlines()

    def format_return(self, text):
        return text[0].decode("utf-8")
