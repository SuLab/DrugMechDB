import os as _os
import numpy as _np
import subprocess as _subprocess

__all__ = ['head']


def head(file_name, n_lines=20, print_out=True, line_nums=False):
    """Get the first n_lines lines of a file. Print if print_out=True, else return as list. Works on UNIX systems"""

    assert type(n_lines) == int
    n_lines = str(n_lines)

    if _os.path.splitext(file_name)[-1] in ['.gz', '.zip']:
        zcat_p = _subprocess.Popen(['zcat', file_name], stdout=_subprocess.PIPE)
        head_p = _subprocess.Popen(['head', '-n', n_lines], stdin=zcat_p.stdout, stdout=_subprocess.PIPE)
        zcat_p.stdout.close()
        output = head_p.communicate()[0].decode('utf-8')
    else:
        output = _subprocess.Popen(['head', '-n', n_lines, file_name], stdout=_subprocess.PIPE).stdout.read().decode('utf-8')

    if not print_out:
        return output

    if line_nums:
        pad = int(_np.log10(int(n_lines)))+1
        fmt_str = '{:' + '{}'.format(pad) + '.0f}:'

        split_out = output.rstrip('\n').split('\n')
        for i, line in enumerate(split_out):
            print(fmt_str.format(i), line)
    else:
        print(output)


