import os
import re
from typing import Any


def read_contents_from_file(project_root: str, filename: str):
    path = '{}/{}'.format(project_root, filename)
    content = None
    with open(path, 'r') as f:
        content = f.read()
    return content


def build_names_and_indents(file_contents: str):
    names = []
    is_after_heading = False
    is_after_symbol = False
    heading = 'Directory Tree Schema'
    symbol = '```'

    contents_list = file_contents.split('\n')

    for element in contents_list:

        if heading in element:
            is_after_heading = True

        elif symbol in element and is_after_heading:
            if is_after_symbol:
                is_after_symbol = False
                is_after_heading = False
            else:
                is_after_symbol = True
            
        elif is_after_symbol:
            names.append(element)
    
    names = names[1:]
    names_and_indents = []

    for name in names:
        indent = re.search('\S', name).start()
        name = name[2 + indent:]

        name_and_indent = (name, indent)
        names_and_indents.append(name_and_indent)

    return names_and_indents


def build_paths(project_root: str, names_and_indents: list[tuple[str, int]]):
    paths = [project_root]

    for i in range(len(names_and_indents)):
        name, indent = names_and_indents[i]

        if indent == 0:
            paths.append(name)
            continue
        
        parent_directory_name = project_root

        for name2, indent2 in names_and_indents[:i]:
            if indent == indent2 + 2 and name2 != parent_directory_name:
                parent_directory_name = name2
        
        full_parent_directory_name = [x for x in paths if x.endswith(parent_directory_name)][0]
        path = '{}/{}'.format(full_parent_directory_name, name)

        paths.append(path)
    
    return paths


def create_files_and_directories(paths: list[str]):
    file_extensions = [
        '.txt',
        '.md',
        '.py',
        '.gitignore',
        '.html',
        '.scss',
        '.css',
        '.sass',
        '.js',
        '.jsx'
    ]
    paths_and_file_or_dir_values = []

    for path in paths:
        file_or_dir = 'dir'
        for ext in file_extensions:
            if ext in path:
                file_or_dir = 'file'

        paths_and_file_or_dir_values.append((path, file_or_dir))


    for path, file_or_dir in paths_and_file_or_dir_values:
        
        if file_or_dir == 'dir':
            if os.path.isdir(path):
                continue
            else:
                os.mkdir(path)
            
        if file_or_dir == 'file':
            if os.path.isfile(path):
                continue
            else:
                f = open(path, 'x')
                f.close()


def build_project(project_root: str):
    contents = read_contents_from_file(project_root, 'README.md')
    names = build_names_and_indents(contents)
    paths = build_paths(project_root, names)
    create_files_and_directories(paths)
    