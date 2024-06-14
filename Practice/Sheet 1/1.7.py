def count_water_vol(n, arr):
    first = arr[0]
    last = arr[n - 1]
    sum_water_vol = 0
    i = 1
    while i < n - 1:
        if arr[i] < first or arr[i] < last:
            sum_water_vol += 