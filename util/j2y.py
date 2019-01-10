#!/usr/bin/env python3
import yaml
import json
import sys
import os


def main():
    json_path = sys.argv[1]
    with open(json_path) as json_fp:
        file_name_without_ext = os.path.split(json_fp.name)[-1].split('.')[0]
        d = json.load(json_fp)
        with open(file_name_without_ext + '.yaml', 'w') as yaml_fp:
            yaml.dump(d, yaml_fp)


if __name__ == '__main__':
    main()