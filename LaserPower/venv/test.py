import numpy as np
import pandas as pd

x = np.random.randint(2, size=(10, 10))
df = pd.DataFrame(x)
y = np.array(df)
lw = np.tril(df, k=-1)
dflw = pd.DataFrame(lw)
print(dflw)