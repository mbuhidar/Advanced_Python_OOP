from house import Bill, Roommate
from reports import PdfReport


def main():

    amount = float(input("Hey user, enter the bill amount: "))
    period = input("What is the bill period? e.g. December 2020: ")

    name1 = input("What is your name? ")
    days_in_house1 = int(input(f"How many days did {name1} stay in the house during the bill period? "))

    name2 = input("What is the name of the other roommate? ")
    days_in_house2 = int(input(f"How many days did {name2} stay in the house during the bill period? "))

    the_bill = Bill(amount, period)

    roommate1 = Roommate(name1, days_in_house1)
    roommate2 = Roommate(name2, days_in_house2)

    print(f"{roommate1.name} pays: ", roommate1.pays(the_bill, roommate2))
    print(f"{roommate2.name} pays: ", roommate2.pays(the_bill, roommate1))

    pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
    pdf_report.generate(roommate1, roommate2, the_bill)

if __name__ == '__main__':
    main()
