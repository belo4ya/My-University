# shell hAck

import subprocess
import shlex
import sys
import os
import cmd
from subprocess import CompletedProcess
from pathlib import Path
from typing import Tuple, List

from config import *


class CrossPlatformFileManager(cmd.Cmd):
    intro = "Welcome to a simple cross-platform file manager. Type help or ? to list commands.\n"

    def __init__(self, completekey='tab', stdin=None, stdout=None):
        super(CrossPlatformFileManager, self).__init__(completekey, stdin, stdout)
        self.platform = sys.platform
        self.posix = self.platform != WIN
        self.help_cmd = HELP_CMD[self.platform]

        self.root = get_root()
        cwd = os.getcwd()
        self.prompt = cwd[cwd.find(self.root.name):] + "::-> "

    def preloop(self) -> None:
        if sys.platform not in HELP_CMD.keys():
            raise NotImplementedError(f"The current platform is not supported: {sys.platform}."
                                      f"You can add support for your platform by editing config.py")

    def precmd(self, line: str) -> str:
        line = line.split()
        if line:
            line[0] = line[0].lower()
            return " ".join(line)

        return ""

    def postcmd(self, stop: bool, line: str) -> bool:
        cwd = os.getcwd()
        self.prompt = cwd[cwd.find(self.root.name):] + "::-> "
        return stop

    def do_root(self, args) -> None:
        """
        Returns to the root directory.
        For more details use: root [--help, /?].
        """
        cmd_, args, shell = self.parse(self.lastcmd, args)
        if self.help_cmd["--help"] in args:
            print("Returns to the root directory.")
            return

        os.chdir(self.root)

    def do_cd(self, args) -> None:
        """
        Change the working directory.
        For more details use: cd [--help, /?].
        """
        cmd_, args, shell = self.parse(self.lastcmd, args)
        answer = execute_cmd(cmd_, args, shell)

        if args and self.help_cmd["--help"] not in args:
            target = get_abspath(args[0])
            if self.root in target.parents and target != self.root.joinpath(".."):
                try:
                    os.chdir(target)
                except OSError:
                    pass
            else:
                print("Attempt to exit the workspace.")
                return

        msg = get_msg(answer)

        print(msg)

    def do_pwd(self, args) -> None:
        """
        Print the name of the current working directory.
        For more details use: pwd [--help, /?].
        """
        self.execute(args)

    def do_ls(self, args) -> None:
        """
        List information about the FILEs (the current directory by default).
        For more details use: ls [--help, /?].
        """
        self.execute(args)

    def do_mkd(self, args) -> None:
        """
        Create the DIRECTORY(ies), if they do not already exist.
        For more details use: mkd [--help, /?].
        """
        self.execute(args)

    def do_mkf(self, args) -> None:
        """
        Creates an empty FILE(s), if they do not already exist.
        For more details use: mkf [--help, /?].
        """
        self.execute(args)

    def do_rmd(self, args) -> None:
        """
        Remove the DIRECTORY(ies).
        For more details use: rmd [--help, /?].
        """
        self.execute(args)

    def do_rmf(self, args) -> None:
        """
        Remove (unlink) the FILE(s).
        For more details use: rmf [--help, /?].
        """
        self.execute(args)

    def do_echo(self, args) -> None:
        """
        Display a line of text.
        For more details use: echo [--help, /?].
        """
        self.execute(args)

    def do_dog(self, args) -> None:
        """
        Concatenate FILE(s) to standard output.
        For more details use: dog [--help, /?].
        """
        self.execute(args)

    def do_cp(self, args) -> None:
        """
        Copy SOURCE to DEST, or multiple SOURCE(s) to DIRECTORY.
        For more details use: cp [--help, /?].
        """
        self.execute(args)

    def do_mv(self, args) -> None:
        """
        Move SOURCE(s) to DIRECTORY.
        For more details use: mv [--help, /?].
        """
        self.execute(args)

    def do_rn(self, args) -> None:
        """
        Rename SOURCE to DEST.
        For more details use: rn [--help, /?].
        """
        self.execute(args)

    def do_exit(self, args) -> bool:
        """
        Exit the shell.
        For more details use: exit [--help, /?].
        """
        print("Thank you for using me. Bye!")
        return True

    def execute(self, args: str) -> None:
        cmd_, args, shell = self.parse(self.lastcmd, args)
        answer = execute_cmd(cmd_, args, shell)
        msg = get_msg(answer)

        print(msg)

    def parse(self, line, args) -> Tuple[str, List[str], bool]:
        cmd_ = line.split()[0]
        cmd_list = COMMANDS[cmd_][self.platform][ALIAS].split()
        cmd_alias = cmd_list[0]

        args = [*cmd_list[1:], *shlex.split(args, posix=self.posix)]
        param_prefix = self.help_cmd["--help"][0]
        args_alias = [
            COMMANDS[cmd_][self.platform][ARGS].get(arg) or
            arg if arg.startswith(param_prefix) else get_abspath(arg)
            for arg in args
        ]

        shell = COMMANDS[cmd_][self.platform][SHELL]

        return cmd_alias, args_alias, shell


def execute_cmd(cmd_: str, args: List[str], shell) -> CompletedProcess:
    return subprocess.run([cmd_, *args], shell=shell, capture_output=True, encoding="cp866")


def get_msg(answer: CompletedProcess) -> str:
    code = answer.returncode
    if code == 1 or code == 0:
        msg = answer.stdout or answer.stderr
    else:
        msg = f"Return code: {code}. Stdout: {answer.stdout}. Stderr: {answer.stderr}"

    return msg


def get_abspath(path: str):
    return Path(path).absolute()


def get_root():
    return get_abspath(os.getcwd())


if __name__ == '__main__':
    CrossPlatformFileManager().cmdloop()
