import json
from string import Formatter

def read_json(file):
    file_name = file if file.endswith('.json') else file + '.json'
    with open(file_name, 'r') as f:
        return json.load(f)
    
def write_json(file, content):
    file_name = file if file.endswith('.json') else file + '.json'
    with open(file_name, 'w') as f:
        try:
            json.dump(content, f)
            return True
        except:
            return False
        
def fstring_keys(fstring):
    keys = [part[1] for part in Formatter().parse(fstring) if part[1] is not None]
    return keys

def format_xpath(fstring, vals):
    fstring_len = len(fstring_keys(fstring))
    if isinstance(vals, (str, list, tuple)):
        if isinstance(vals, str) or len(vals) < fstring_len :
            list_of_vals = [vals] if isinstance(vals, str) else [*vals]
            difference = fstring_len - len(list_of_vals)
            values = list_of_vals + ['' for _ in range(difference)]
        elif len(vals) > fstring_len:
            values = [*vals][:fstring_len]
        else:
            values = [*vals]
        return fstring.format(*values)
    else:
        raise TypeError('Must be a string, a list or a tuple')