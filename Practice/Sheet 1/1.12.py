import numpy as np

"""
***Pari nai***
"""


def check_required_stations(arr, dep):
    req_stations = 1
    j = 0
    while j < len(dep) - 1:
        if dep[j] < arr[j + 1]:
            pass
        elif dep[j] > arr[j + 1]:
            req_stations += 1
        j += 1
    return req_stations


arr1 = np.array([900, 940, 950, 1100, 1500, 1800])
dep1 = [910, 1200, 1120, 1130, 1900, 2000]
print(check_required_stations(arr1, dep1))
arr2 = [900, 1100, 1235]
dep2 = [1000, 1200, 1240]
print(check_required_stations(arr2, dep2))