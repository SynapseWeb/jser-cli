"""Functions to interact with jser files."""


import json


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
