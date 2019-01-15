#!/usr/bin/env python3
import json
import sys

import yaml


def main():
    json_path = sys.argv[1]
    with open(json_path) as json_fp:
        d = json.load(json_fp)
        print(yaml.dump(d, default_flow_style=False))


if __name__ == '__main__':
    main()
