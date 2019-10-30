import os
import string

import termcolor

from interfaces.repository import ConsoleRepository
from entity import user


class Console(ConsoleRepository):
    def __init__(self, user_name='') -> None:
        self.user_name = user_name
        self.template_file = get_template_dir_path()

    def view(self, file_name, color, message, isEnd=False):
        while True:
            full_path = os.path.join(self.template_file, file_name)
            template = get_template(full_path, color)

            if isEnd:
                print(template.substitute(message))
                break

            user_name = input(template.substitute(message))
            if user_name:
                self.user_name = user_name.title()
                break

    def find_user_name(self):
        return self.user_name


def get_template_dir_path():

    import settings

    template_dir_path = None
    if settings.TEMPLATE_PATH:
        template_dir_path = settings.TEMPLATE_PATH

    if not template_dir_path:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        template_dir_path = os.path.join(base_dir, 'templates')

    return template_dir_path


def get_template(template, color):
    with open(template, 'r', encoding='utf-8') as template_file:
        contents = template_file.read()
        contents = contents.rstrip(os.linesep)
        contents = '{splitter}{sep}{contents}{sep}{splitter}{sep}'.format(
            contents=contents, splitter="=" * 60, sep=os.linesep)
        contents = termcolor.colored(contents, color)
        return string.Template(contents)
