import argparse

from . import __version__


def main():
    parser = argparse.ArgumentParser(prog="granpost", description="Granpost CLI (MVP)")
    parser.add_argument("-v", "--version", action="version", version=__version__)
    parser.parse_args()
