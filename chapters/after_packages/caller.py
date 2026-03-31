from importlib import reload

import main.business_logic.weekly

reload(main.business_logic.weekly)
mb = main.business_logic
print(vars(mb).keys())
import sys

print(list(k for k in sys.modules if "main" in k))
