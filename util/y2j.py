#!/usr/bin/env python3
import yaml
import json
import sys
import os


def main():
    yaml_path = sys.argv[1]
    with open(yaml_path) as yaml_fp:
        file_name_without_ext = os.path.split(yaml_fp.name)[-1].split('.')[0]
        d = yaml.load(yaml_fp)
        with open(file_name_without_ext + '.json', 'w') as json_fp:
            json.dump(d, json_fp)


if __name__ == '__main__':
    main()