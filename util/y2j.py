#!/usr/bin/env python3
import json
import sys

import yaml


def main():
    yaml_path = sys.argv[1]
    with open(yaml_path) as yaml_fp:
        d = yaml.load(yaml_fp)
        print(json.dumps(d))


if __name__ == '__main__':
    main()
