def sortList(list):
    for i in range(0, len(list)):
        for j in range(i + 1, len(list)):
            if list[i] >= list[j]:
                list[i], list[j] = list[j], list[i]

    print("Sorted List: ", list)


def main():
    while True:
        qtyElements = int(input("How many elements you would like to insert (qty less than 4 is not allowed)? "))
        if qtyElements < 4:
            print("Qty must not be less than 4")
        elif qtyElements % 2 != 0:
            print("Qty must be odd")
        else:
            userInput = input("Enter elements of list using space between them (Ex: 1 23 21 45): ")

            userList = list(map(int,userInput.split()))

            if len(userList) != qtyElements:
                print("Please insert correct qty of elements")

            else:
                sortList(userList)

                break