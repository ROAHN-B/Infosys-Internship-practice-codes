# python -m pip install "dask[complete] -> "dask[array], dask[dataframe], dask[bag], dask[delayed]""

import pandas as pd
import dask.array as da
import dask.dataframe as dd

x = da.array([1, 2, 3, 4])
print(x.compute())

y = x + 10

print(y.compute())

a = da.random.random((10000, 10000), chunks=(1000, 1000))
print(a)
b = a.mean()
print(b.compute())

# rows=10000 / 1000 = 10
# cols=10000 / 1000 = 10
# chunk_size=(1000,1000)

# rows*cols = 10 * 10 = 100

z = da.arange(20, chunks=5)
print(z)
print(z.compute())

# data[frame]

# data[frame] -> CSV or excel -> partitions ->lazy-> operations (Execution)

# Data[frame] -> tables
#  read_csv("file name.csv") -> in pandas

# partitions -> smaller pandas dataframes

# 6 rows
# 1p = 1-2rows
# 2p=3-4 rows -------


data = {
    "order_id": [1, 2, 3, 4, 5, 6],
    "city": ["Nagpur", "Delhi", "mumbai", "pune", "lucknow", "chandigarh"],
    "amount": [250, 320, 150, 620, 450, 550],
    "product": ["laptop", "mobile", "fridge", "monitor", "fan", "table"],
}

pdf = pd.DataFrame(data)
print("panda Dataframe: ")
pdf.to_csv("sales.csv", index=True)
print("CSV file succesfully created")
