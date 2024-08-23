import numpy as np

if __name__ == '__main__':
    arr = np.array([1, 0, 9, 6, 8, 3, 2, 5])
    print('Before sorted: ', arr)

    sorted_arr = np.sort(arr)
    print('After sorted: ', sorted_arr)
