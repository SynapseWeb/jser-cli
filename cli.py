#!/usr/bin/env python
"""Command line interface to interact with jser files."""


import sys
from pathlib import Path
from funcs import *


def jser_commands(args):
    """Commands to work with jser files."""

    jser = Path(args[2])
    subcommand = args[1]

    if jser.suffix != ".jser" or not jser.exists():
        print("Please point to valid jser file.")
        sys.exit(1)
    
    data = load_jser(args[2])
    
    match subcommand:

        case "objects":

            print_objects(data)

        case "alignments":

            print_alignments(data)

        case "groups":

            print_groups(data)

        case "add-to-group":

            group = args[3]
            objs = args[4:]
            add_to_groups(data, group, objs)

        case "src_dir":

            print_src_dir(data)

        case "test":
            
            print("test!")

        case _:

            print(f"Subcommand \"{subcommand}\" not valid on jsers.")
            print_jser_subcommands()


def dir_commands(args):
    """Commands to work with directories."""

    directory = Path(args[2])
    subcommand = args[1]

    match subcommand:

        case "recent":

            get_recent_jser(directory)

        case _:

            print(f"Subcommand \"{subcommand}\" not valid on jsers.")
            print_dir_subcommands()
            

def main():

    args = sys.argv

    if len(args) == 1:
        
        print_usage()
        sys.exit(0)

    elif len(args) < 3:

        print("Please provide at least 2 arguments.")
        print_example()
        sys.exit(1)

    path_provided = Path(args[2])

    if path_provided.is_file():

        jser_commands(args)

    elif path_provided.exists():

        dir_commands(args)

    else:

        print("Please provide a valid path as an argument")
        print_example()
        sys.exit()


if __name__ == "__main__":

    main()
