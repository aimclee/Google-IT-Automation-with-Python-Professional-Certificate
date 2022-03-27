import re

def rearrrange_names(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    i
    return "{} {}".format(result[2],result[1])