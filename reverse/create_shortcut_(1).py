from win32com.client import Dispatch
from pathlib import Path
import os


def create_shortcut(file_name: str, target: str, work_dir: str, arguments: str = ''):
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(file_name)
    shortcut.TargetPath = target
    shortcut.Arguments = arguments
    shortcut.WorkingDirectory = work_dir
    shortcut.save()


abs_file_name = os.getcwd() + "\\start.bat"
path = Path(abs_file_name)
name = 'start.bat'
print(path)

create_shortcut(
    file_name=f"{name}.lnk",
    target=str(path),
    work_dir=str(path.parent),
    arguments='/cmd {%s} -new_console' % name,
)
