
end_of_auction = False
while not end_of_auction:
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n"))
    other_person = input("Are there any other bidders? type 'yes or 'no'\n").lower()

    auction_details = []
    person_entry = {}
    person_entry[name] = bid
    auction_details.append(person_entry)
    if other_person == 'no':
        end_of_auction = True
        for x in range(0, len(auction_details)):
            highest = auction_details[x][name]
            n = name
            if auction_details[x][name] > highest:
                highest = auction_details[x][name]
                n = name
            print(f"{n} has a highest bid value of $:{highest}")




