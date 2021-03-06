#!/usr/bin/env python3
#
# Script to identify unused Java classes in a project
#

import sys, glob


def main():
    try:
        project_directory = sys.argv[1]
    except IndexError:
        print("Usage: %s [PROJECT DIRECTORY]" % sys.argv[0])
        sys.exit(1)

    java_file_paths = glob.glob(
        '%s/**/src/main/java/**/*.java' % project_directory,
        recursive=True)
    class_names = (f.split('/')[-1][:-5] for f in java_file_paths)

    for class_name in class_names:
        usage_found = False
        for path in java_file_paths:
            if class_name == path.split('/')[-1][:-5]:
                # Don't count self as usage
                continue
            with open(path) as fp:
                if class_name in fp.read():
                    usage_found = True
                    break
        if not usage_found:
            print("Candidate: %s" % class_name, flush=True)

if __name__ == '__main__':
    main()
