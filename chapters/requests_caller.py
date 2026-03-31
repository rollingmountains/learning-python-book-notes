import sys

import requests.adapters

# filter to just requests-related
print(sys.modules.get("requests.adapters"))
del sys.modules["requests.adapters"]
del sys.modules["requests"]
del requests.adapters
del requests

print(sys.path)
sys.path.append("/Users/balapaudel/programming/learning-python/")
import chapters.requests.adapters as cra

print(cra.DEFAULT_POOLBLOCK)
