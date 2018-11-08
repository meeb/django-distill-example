#!/usr/bin/env python


import os
import sys


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demoblog.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError('Error importing django, is it installed?') from exc
    execute_from_command_line(sys.argv)
