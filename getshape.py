
import pandas as pd
import numpy as np

def get_clean_shape(df_cleaned):
    temp = df_cleaned.groupby(["Year", "shape"]).count()["Time_clean"].reset_index()
    temp_ = [temp["Year"].values, temp["shape"].values]
    temp2 = pd.Series(temp["Time_clean"].values, index=temp_)

    shapes = df_cleaned["shape"].unique()
    shape_zero = np.zeros(shapes.size)
    shape_dict_zero = dict(zip(shapes, shape_zero))
    Years = df_cleaned["Year"].unique()

    dic = {}
    for i, j in zip(temp["Year"].values, temp["shape"].values):
        if i in dic.keys():
            dic[i][j] += temp2[(i, j)]
        else:
            if i == 1906:
                dic[i] = shape_dict_zero.copy()
                dic[i][j] += temp2[(i, j)]
                year = i
            else:
                dic[i] = dic[year].copy()
                dic[i][j] += temp2[(i, j)]
                year = i

    temp3 = []
    for key, value in dic.items():
        temp3.append(list(value.values()))
    temp3 = np.array(temp3)
    temp3 = pd.DataFrame(temp3, columns=[list(dic[1906].keys())])
    temp3["Year"] = list(dic.keys())
    Shape_ = temp3

    return Shape_