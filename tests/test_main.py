import os
from sass_cli import main


def stripall(chars):
    return chars.replace('\n', '').replace(' ', '')


def test_directories(output_dir):
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
