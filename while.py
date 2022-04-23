results = [0,0,0]

while True:
    try:
        nb = input("Enter You\'r Number ? :  ").lower()
        if nb != 'done':
            results[0] += int(nb) #Total
            results[1] += 1 #Count
            results[2] = round(results[0] / results[1], 2) #Average
        elif nb == 'done':
            print("\n You\'r results.. ", "Total : ", results[0], '  Count : ', results[1], '  Average : ', results[2])
            print("\n Thank You & Goodbye \n")
            break
        else:
            print("Oops..., Something Went Wrong")
    except Exception as e:
        print("Invalid Input, Try Again .. ")
