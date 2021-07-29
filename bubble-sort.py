def sort(arr):
     if arr is None:
        print("Array is invalid")
        return
     elif not arr:
        print("Array is empty")
        return
     elif len(arr) == 1:
        print("One element array")
        return
     else:
        print("We are in business or dead")
        print("\n")
        print("\n")
        print("\n")
        len1=len(arr)
        for i in range(len1-1):
            print(f'outer i {i}')

            swapped = False
            for j in range(len1 - 1 - i):
                print(f'  inner j {j}')
                prev = arr[j];
                next = arr[j+1]
                if prev > next:
                    arr[j] = next
                    arr[j+1] = prev
                    swapped = True
                print("\n")
            #if swapped == False:
               # break;

        print(arr)
        return

x=[9,6]
y=[5]
z=[4]
zz=[5,6]
#arr1=[100,2,45,8,22,15,9,3]
arr2=[2, 3, 8, 9, 15, 22, 45, 100]
arr1=[200, 3, 8, 9, 15, 22, 45, 100]
sort(x)
sort(y)
sort(z)
sort(zz)
sort(arr1)
#sort(arr2)


