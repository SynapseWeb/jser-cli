#!/usr/bin/env python
"""Command line interface to interact with jser files."""

import sys
from pathlib import Path
from funcs import *

def print_example():

    print("Example call: kh-cli <subcommand> <jser file>")
    
def print_usage():
    
    print(f"KH lab jser cli: {__doc__}")
    print_example()

def print_subcommands():
    print("Possible subcommands include: objects, alignments, add-to-group, test")

if __name__ == "__main__":

    args = sys.argv

    if len(args) == 1:
        
        print_usage()
        sys.exit(0)

    elif len(args) < 3:

        print("Please provide at least 2 arguments to this command.")
        print_example()
        sys.exit(1)

    # check if jser exists

    jser = Path(args[2])

    if not jser.exists():

        print("Provided jser does not exist. Please provide a filepath to a valid jser file.")
        print_example()
        sys.exit(1)

    data = load_jser(jser)

    match args[1]:

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

            print(f"Subcommand \"{args[1]}\" not recognized.")
            print_subcommands()

