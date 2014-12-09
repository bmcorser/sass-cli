import os
import click
import sass

def compile_write(scsspath, csspath):
    'Call libsass wrapper with the scsspath, (create and) write to csspath'
    cssdir = os.path.dirname(csspath)
    if not os.path.exists(cssdir):
        os.makedirs(cssdir)
    with open(csspath, 'w') as cssfile:
        css = sass.compile_file(bytes(scsspath, 'utf-8')).decode('utf-8')
        cssfile.write(css)


def css_ext(path):
    'Rename a *.* path to *.css'
    return ''.join([os.path.splitext(path)[0], '.css'])


def directories(inpath, outpath):
    'Walk and compile, write *.[scss,sass] files to their css couterparts'
    for root, _, scssnames in os.walk(inpath):
        for scssname in scssnames:
            scsspath = os.path.join(root, scssname)
            csspath = css_ext(scsspath.replace(inpath, outpath))
            compile_write(scsspath, csspath)

@click.command()
@click.argument('inpath', type=click.Path(exists=True))
@click.argument('outpath', type=click.Path())
def run(inpath, outpath):
    'Check if we have been called with directories or filenames'
    if os.path.isdir(inpath) and os.path.isdir(inpath):
        return directories(inpath, outpath)
    if os.path.isfile(inpath) and os.path.isfile(inpath):
        return compile_write(inpath, outpath)
    click.echo('This CLI only works with a pair of directories or a pair of files')
