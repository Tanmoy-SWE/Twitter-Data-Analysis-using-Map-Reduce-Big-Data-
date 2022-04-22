import  numpy as np

arr = np.array(
    [
        [1,2,3],
        [11, 12, 13],
        [111,222,333]
    ]
)

for x in arr[:, 0]:
    print(x)