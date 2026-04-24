# import pandas library
import pandas as pd

#Create Dictionary
data = {
    "id": [1, 2, 3],
    "name": ["A", "B", "C"],
    "age": [10, 20, 30]
}

# convert to tabular format
df = pd.DataFrame(data)

# show data
print(df)