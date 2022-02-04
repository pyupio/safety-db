import json
from importlib.resources import read_text

__title__ = 'safety-db'
__version__ = '2021.7.17'
__author__ = 'Justin Womersley <support@pyup.io>'
__copyright__ = '2016-2017 PyUp'
__license__ = 'Attribution-NonCommercial-ShareAlike 4.0 International'
__all__ = (
    'INSECURE',
    'INSECURE_FULL',
)

try:
    INSECURE = json.loads(read_text(__package__, "insecure.json"))
except ValueError as e:
    INSECURE = []


try:
    INSECURE_FULL = json.loads(read_text(__package__, "insecure_full.json"))
except ValueError as e:
    INSECURE_FULL = []
