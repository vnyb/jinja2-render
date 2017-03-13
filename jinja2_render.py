"""
Load variables from YAML-formatted file(s) to render a jinja2 template
"""

import argparse
import jinja2
import sys
import yaml

def load_filters(env, filters):
    """
    Load extra Jinja2 filters
    """

    module = __import__(filters)
    env.filters.update(module.FILTERS)

def render(env, template_file, data_file, extra_filters=None):
    """
    Load data from 'data_file' to render 'template_file'
    """

    template = env.from_string(template_file.read())

    data = {}
    for i in data_file:
        data.update(yaml.load(i))

    return template.render(data)

def main():
    """
    Load variables from YAML-formatted files to render a jinja2 template
    """

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        '-p', '--extra-path',
        type=str,
        help='add extra python path',
    )
    parser.add_argument(
        '-f', '--filters',
        type=str,
        help='import extra filters from module'
    )
    parser.add_argument(
        'template_file',
        type=argparse.FileType('r'),
        help='jinja2-formatted template file',
    )
    parser.add_argument(
        'data_file',
        nargs='+',
        type=argparse.FileType('r'),
        help='YAML-formatted data file',
    )

    args = parser.parse_args()
    env = jinja2.Environment(
        autoescape=False,
        trim_blocks=False,
    )

    if args.extra_path:
        sys.path.append(args.extra_path)
    if args.filters:
        load_filters(env, args.filters)

    print(render(env, args.template_file, args.data_file))


if __name__ == '__main__':
    main()
