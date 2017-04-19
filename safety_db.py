import json

__title__ = 'safety-db'
__version__ = '2017.4.19'
__author__ = 'Jannis Gebauer <support@pyup.io>'
__copyright__ = '2016-2017 Jannis Gebauer'
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
