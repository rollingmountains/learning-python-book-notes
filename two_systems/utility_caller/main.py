from system2.utilities import var  # absolute import, importing an external package. this direclty scans sys.path lookinf for the folder system2 that has utitlites module

from .test import var as tv  # relative import importing a #intrapackage or module file. this doens't look at sys.path, it first #cheks relative to the directory main.py, import main.py's sibling #named test.py


print(tv)

print(var)
