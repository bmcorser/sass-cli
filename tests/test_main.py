import os
from sass_cli import main


def stripall(chars):
    'Whitespace is not so relevant'
    return chars.replace('\n', '').replace(' ', '')


def test_directories(output_dir):
    'Works as expected when a pair of dirnames are passed'
    input_dir = 'tests/scss'
    expected_root = 'tests/css'
    main.directories(input_dir, output_dir)
    for root, _, cssnames in os.walk(output_dir):
        for cssname in cssnames:
            csspath = os.path.join(root, cssname)
            expected_csspath = csspath.replace(output_dir, expected_root)
            print("in:      {0}".format(csspath))
            print("out:     {0}".format(expected_csspath))
            css = stripall(open(csspath, 'r').read())
            expected_css = stripall(open(expected_csspath, 'r').read())
            assert css == expected_css
            print("success: {0}".format(cssname))
            print('---')


def test_files(output_dir):
    'Works as expected when a pair of filenames are passed'
    input_file = 'tests/scss/specific/c.scss'
    output_file = os.path.join(output_dir, 'output.css')
    expected_output_file = 'tests/css/specific/c.css'
    main.compile_write(input_file, output_file)
    css = stripall(open(output_file, 'r').read())
    expected_css = stripall(open(expected_output_file, 'r').read())
    assert css == expected_css
