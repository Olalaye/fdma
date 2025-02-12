#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
import os
import time
import argparse

def calculate_md5(file_path):
    """
    Calculate the md5 hash of a file.

    Args:
        file_path (_type_): _description_

    Returns:
        _type_: _description_
    """
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def add_file_info(file_path, deps, desc, info_file='file_info.txt'):
    """
    Add file information to a file.

    Args:
        file_path (_type_): _description_
        deps (_type_): _description_
        desc (_type_): _description_
        info_file (str, optional): _description_. Defaults to 'file_info.txt'.
    """
    md5_hash = calculate_md5(file_path)
    name = os.path.basename(file_path)
    
    with open(info_file, 'a', encoding='utf-8') as f:
        info = f"Name: {name}\nmd5: {md5_hash}\nDeps: {', '.join(deps)}\nDesc: {desc}\nTime: {time.strftime('%Y-%m-%d %H:%M:%S')}\n"
        f.write(info)
        f.write("----\n")
        print("Appended the following info:")
        print(info)

def visualize_info(info_file='file_info.txt'):
    """
    Visualize file information.

    Args:
        info_file (str, optional): _description_. Defaults to 'file_info.txt'.
    """
    with open(info_file, 'r', encoding='utf-8') as f:
        content = f.read()
    print(content)

def main():
    """
    Main function to run the program.
    """
    parser = argparse.ArgumentParser(description='File Description Management Assistant')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add file description')
    add_parser.add_argument('file_path', type=str, help='Path to the file')
    add_parser.add_argument('deps', type=str, nargs='+', help='List of dependencies')
    add_parser.add_argument('desc', type=str, help='Description of the file')

    vis_parser = subparsers.add_parser('visualize', help='Visualize file descriptions')

    args = parser.parse_args()

    if args.command == 'add':
        add_file_info(args.file_path, args.deps, args.desc)
    elif args.command == 'visualize':
        visualize_info()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
