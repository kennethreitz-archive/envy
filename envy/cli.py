# -*- coding: utf-8 -*-

"""
envy.cli
~~~~~~~~

This module contains the CLI for Envy.
"""

import sys

from .version import __version__
from .packages.clint import args
from .packages.clint.textui import colored, puts

class Command(object):
    COMMANDS = {}
    SHORT_MAP = {}

    @classmethod
    def register(klass, command):
        klass.COMMANDS[command.name] = command
        if command.short:
            for short in command.short:
                klass.SHORT_MAP[short] = command

    @classmethod
    def lookup(klass, name):
        if name in klass.SHORT_MAP:
            return klass.SHORT_MAP[name]
        if name in klass.COMMANDS:
            return klass.COMMANDS[name]
        else:
            return None

    @classmethod
    def all_commands(klass):
        return sorted(klass.COMMANDS.values(),
                      key=lambda cmd: cmd.name)

    def __init__(self, name=None, short=None, fn=None, usage=None, help=None):
        self.name = name
        self.short = short
        self.fn = fn
        self.usage = usage
        self.help = help

    def __call__(self, *args, **kw_args):
        return self.fn(*args, **kw_args)


def def_cmd(name=None, short=None, fn=None, usage=None, help=None):
    command = Command(name=name, short=short, fn=fn, usage=usage, help=help)
    Command.register(command)

def display_help():
    """Displays Legit help."""

    display_info()


def display_version():
    """Displays Legit version/release."""


    puts('{0} v{1}'.format(
        colored.yellow('envy'),
        __version__
    ))


def display_info():
    puts('{0}. {1}\n'.format(
        colored.yellow('envy'),
        'A Kenneth Reitz Project'
    ))


def show_error(msg):
    sys.stdout.flush()
    sys.stderr.write(msg + '\n')

def dispatch():
    command = Command.lookup(args.get(0))
    if command:
        arg = args.get(0)
        args.remove(arg)

        command.__call__(args)
        sys.exit()

    elif args.contains(('-h', '--help')):
        display_help()
        sys.exit(1)

    elif args.contains(('-v', '--version')):
        display_version()
        sys.exit(1)

    else:
        git_args = list(sys.argv)

        show_error(colored.red('Unknown command {0}'.format(args.get(0))))
        display_info()
        sys.exit(1)

def cmd_init(args):
    print 'init!'

def_cmd(
    name='init',
    fn=cmd_init,
    usage='init',
    help='Get a nice pretty list of branches.')

def main():
    dispatch()
