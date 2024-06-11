"""Functions to interact with jser files."""


import json
from pathlib import Path


## Functions to print help #########################################################################


def print_example():

    print("Example call: jser <subcommand> <jser file>")
    

def print_jser_subcommands():

    print("Possible subcommands include: objects, alignments, add-to-group, test")


def print_dir_subcommands():

    print("Possible subcommands include: recent")


def print_usage():

    print(f"KH lab jser cli: {__doc__}")
    print()
    print_example()


## Functions to return dir data ####################################################################


def get_recent_jser(directory: Path):

    jsers = sorted(directory.glob("traces/*.jser"))
    print(jsers[-1])
    

## Functions to return jser data ###################################################################
    
def load_jser(filepath):

    with open(filepath, "r") as fp:
        data = json.load(fp)

    return data


def print_objects(data):

    contours = set()

    for section in data["sections"]:
        for contour, _ in section["contours"].items():
            contours.add(contour)

    objects = list(contours)
    objects.sort()

    for obj in objects:
        print(obj)


def print_alignments(data):

    current_alignment = data["series"]["alignment"]

    tforms = data["sections"][0]["tforms"]
    alignments = ["no-alignment"] + list(tforms.keys())

    alignments = [e + "*" if e == current_alignment else e for e in alignments]

    for alignment in alignments:
        print(alignment)


def print_groups(data):

    groups = list(data["series"]["object_groups"].keys())
    groups.sort()

    for group in groups:
        print(group)


def add_to_groups(data, group, objs):

    obj_groups = data["series"]["object_groups"]
    existing = obj_groups.get(group, None)
    
    if not existing:
        
        data["series"]["object_groups"][group] = objs
        
    else:
        
        new_objs = set(existing)

        for obj in objs:
            new_objs.add(obj)
            
        data["series"]["object_groups"][group] = new_objs

    print(json.dumps(data))

        
def print_src_dir(data):

    src_dir = data["series"]["src_dir"]
    print(src_dir)
