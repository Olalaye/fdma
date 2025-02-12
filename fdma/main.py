#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
import os
import argparse

def calculate_md5(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb', encoding='utf-8') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def add_file_info(file_path, deps, desc, info_file='file_info.txt'):
    md5_hash = calculate_md5(file_path)
    name = os.path.basename(file_path)
    
    with open(info_file, 'a', encoding='utf-8') as f:
        f.write(f"Name: {name}\n")
        f.write(f"md5: {md5_hash}\n")
        f.write(f"Deps: {', '.join(deps)}\n")
        f.write(f"Desc: {desc}\n")
        f.write("----\n")

def visualize_info(info_file='file_info.txt'):
    with open(info_file, 'r', encoding='utf-8') as f:
        content = f.read()
    print(content)

def main():
    parser = argparse.ArgumentParser(description='File Description Management Assistant')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add file description')
    add_parser.add_argument('file_path', type=str, help='Path to the file')
    add_parser.add_argument('deps', type=str, nargs='+', help='List of dependencies')
    add_parser.add_argument('desc', type=str, help='Description of the file')

    vis_praser = subparsers.add_parser('visualize', help='Visualize file descriptions')

    args = parser.parse_args()

    if args.command == 'add':
        add_file_info(args.file_path, args.deps, args.desc)
    elif args.command == 'visualize':
        visualize_info()

if __name__ == '__main__':
    main()
