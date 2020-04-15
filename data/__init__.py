import json

__title__ = 'safety-db'
__version__ = '2020.4.14'
__author__ = 'Justin Womersley <support@pyup.io>'
__copyright__ = '2016-2017 PyUp'
__license__ = 'Attribution-NonCommercial-ShareAlike 4.0 International'
__all__ = (
    'INSECURE',
    'INSECURE_FULL',
)

with open("data/insecure.json") as __f:
    try:
        INSECURE = json.loads(__f.read())
    except ValueError as e:
        INSECURE = []


with open("data/insecure_full.json") as __f:
    try:
        INSECURE_FULL = json.loads(__f.read())
    except ValueError as e:
        INSECURE_FULL = []
