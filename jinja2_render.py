"""
Load variables from YAML-formatted file(s) to render a jinja2 template
"""

import argparse
import jinja2
import yaml

def render(template_file, data_file, extra_filters=None):
    """
    Load data from 'data_file' to render 'template_file'
    """

    # Prepare environment
    env = jinja2.Environment(
        autoescape=False,
        trim_blocks=False,
    )
    if extra_filters:
        module = __import__(extra_filters)
        env.filters.update(module.FILTERS)

    # Load template
    template = env.from_string(template_file.read())

    # Load data
    data = {}
    for i in data_file:
        data.update(yaml.load(i))

    # Render
    return template.render(data)

def main():
    """
    Load variables from YAML-formatted files to render a jinja2 template
    """

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
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
    print(render(args.template_file, args.data_file, args.filters))


if __name__ == '__main__':
    main()
