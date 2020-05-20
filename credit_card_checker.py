while True:
    # Takes card number as string input, removes any spaces and converts to and int
    num = int(input("Number: ").replace(" ", ""))

    # Possible length of amex, mastercard and visa cards, stores values in list
    AM_len = [15]
    MA_len = [16]
    VI_len = [13, 16]
    # Possible starting numbers for amex, mastercard and visa cards, stores values in list
    AM_start = [34, 37]
    MA_start = [51, 52, 53, 54, 55]
    VI_start = [4]

    # Function that uses Luhn's algorithm to calulate whether a card is syntactically valid and prints either the card type, or invalid
    def num_checker(cardtype, num):
        if len(str(num)) % 2 == 0:
            listnum = [int(x) for x in str(num)]

            list1 = [x * 2 for x in listnum[0::2]]
            sumoflist1 = sum(list1)

            list2 = listnum[1::2]
            sumoflist2 = sum(list2)

            final_num = sumoflist1 + sumoflist2

            if str(final_num)[-1]:
                print(cardtype)
            else:
                print("INVALID")

        elif len(str(num)) % 2 == 1:
            listnum = [int(x) for x in str(num)]

            list1 = [x * 2 for x in listnum[1::2]]
            sumoflist1 = sum(list1)

            list2 = listnum[0::2]
            sumoflist2 = sum(list2)

            final_num = sumoflist1 + sumoflist2

            if str(final_num)[-1]:
                print(cardtype)
            else:
                print("INVALID")
    # checks the length of numebr and what it starts with to find out what kind of card it is,
    # then calls num_checker function to check if the number is a valid number
    if (len(str(num)) in AM_len) and (int(str(num)[0:2]) in AM_start):
        cardtype = "AMEX"
        num_checker(cardtype, num)
    elif (len(str(num)) in MA_len) and (int(str(num)[0:2]) in MA_start):
        cardtype = "MASTERCARD"
        num_checker(cardtype, num)
    elif (len(str(num)) in VI_len) and (int(str(num)[0:1]) in VI_start):
        cardtype = "VISA"
        num_checker(cardtype, num)
    else:
        print("INVALID")
