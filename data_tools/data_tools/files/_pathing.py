import os as _os

__all__ = ['parse_unix_path']

def parse_unix_path(path):
    """Parse a unix path with relative and/or home directory markers"""
    out_path = path
    if '~' in out_path:
        out_path = _os.path.expanduser(out_path)
    if '.' in out_path:
        out_path = _os.path.realpath(_os.path.abspath(out_path))
    else:
        out_path = _os.path.abspath(out_path)
    return out_path

