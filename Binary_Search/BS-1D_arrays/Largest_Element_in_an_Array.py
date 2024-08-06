def largest(arr,n):
    maximum = max(arr)
    return maximum


if __name__ == "__main__":
    n = int(input())
    arr = [int(x) for x in input().strip().split()]
    print(f"largest elements of the array are {largest(arr,n)}")
    