from ahkab import *
import warnings
from warnings import filterwarnings, showwarning
from exceptions import DeprecationWarning


filterwarnings("always", category=DeprecationWarning)

def _ahkab_warning(message, category = UserWarning, filename = '', lineno = -1):
    print "%s:\n\t%s" % (category.__name__, message)

warnings.showwarning = _ahkab_warning