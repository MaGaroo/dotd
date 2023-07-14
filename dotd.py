#!/usr/bin/env python
import argparse
from pathlib import Path
import sys


def main():
    args = parse_args(sys.argv)

    file_address = Path(args.filename)
    if args.directory:
        directory_address = Path(args.directory)
    else:
        directory_address = Path(args.filename + ".d")

    if not directory_address.exists():
        print("Error: directory does not exist {directory_address}", file=sys.stderr)

    if not directory_address.is_dir():
        print("Error: {directory_address} is not a directory")

    with file_address.open("w") as target_file:
        append_from_dir(target_file, directory_address, recursive=args.recursive)

    return 0


def parse_args(args):
    parser = argparse.ArgumentParser(
        prog="dotd",
        description="Merge files in whatever.d directory into whatever file",
    )
    parser.add_argument("filename")
    parser.add_argument("-d", "--directory", action="store", type=str)
    parser.add_argument("-r", "--recursive", action="store_true", type=bool)
    return parser.parse_args()


def append_from_dir(target_file, directory: Path, recursive: bool = False):
    for child in sorted(directory.glob("*")):
        if child.is_dir() and recursive:
            append_from_dir(target_file, child, recursive)
        elif child.is_file():
            append_from_file(target_file, child)


def append_from_file(target_file, source_path: Path):
    with source_path.open("r") as source_file:
        content = source_file.read()
        if not content.endswith("\n"):
            content += "\n"
        print(content, end="", file=target_file)


if __name__ == "__main__":
    sys.exit(main())