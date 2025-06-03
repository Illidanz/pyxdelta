""" Python interface for xdelta. """

def run(*, infile: str, outfile: str, patchfile: str) -> bool:
    """ Create xdelta patch. """
    ...

def decode(*, infile: str, patchfile: str, outfile: str) -> bool:
    """ Decode xdelta patch. """
    ...
