def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

def main():
    # Example usage
    arr = [12, 4, 5, 6, 7, 3, 1, 15]
    sorted_arr = quick_sort(arr)
    print("Original Array:", arr)
    print("Sorted Array:", sorted_arr)

if __name__ == "__main__":
    main()
