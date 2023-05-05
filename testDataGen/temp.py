
from pyDOE2 import *
import pandas as pd
levels = {"user_id_type":
              ["user_id", "union_id", "open_id"],
          "department_id_type": ["dep_id", "open_dep_id"],
          "int_type": [1, 2, 3],
          "eva_list": [5, 6]}
design = lhs(len(levels), samples=20)
design = pd.DataFrame(design, columns=levels.keys())
for var, levels in levels.items():
    design[var] = pd.Series(levels).astype("category").values[design[var].round().astype(int)]
    print(design)