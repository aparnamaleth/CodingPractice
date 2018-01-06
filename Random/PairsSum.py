def CheckPairSum(Arr, Total):
        n = len(Arr)
        dict_of_numbers = [0] * 1000
#       print("Start of loop")
        for i in range (n):
                difference = Total - Arr[i]
#               print difference
                if dict_of_numbers[difference] == 1:
                        print("The pair is", Arr[i], "and", difference)
                dict_of_numbers[Arr[i]] = 1

Arr = [1,2,4,5,7,8,10,-1,6]
Total = 9
CheckPairSum(Arr, Total)

