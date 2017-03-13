"""
Load variables from a YAML-formatted file to render jinja2 templates
"""

import argparse
import jinja2
import yaml

def render(template_file, data_file):
    """
    Load data from 'data_file' to render 'template_file'
    """
    env = jinja2.Environment(
        autoescape=False,
        trim_blocks=False,
    )
    template = env.from_string(template_file.read())
    data = yaml.load(data_file)
    return template.render(data)

def main():
    """
    Load variables from a YAML-formatted file to render jinja2 templates
    """

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        'template_file',
        type=argparse.FileType('r'),
        help='jinja2-formatted template file',
    )
    parser.add_argument(
        'data_file',
        type=argparse.FileType('r'),
        help='YAML-formatted data file',
    )

    args = parser.parse_args()
    print(render(args.template_file, args.data_file))


if __name__ == '__main__':
    main()
