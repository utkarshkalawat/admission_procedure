import csv
def admissionprocdure(name,marks,documents,seat,fee,cutoff):
    if marks >= cutoff:
        print("eligible for admission: ")
        if documents.lower() == "yes":
            if seat.lower() == "yes":
                if fee.lower() == "yes":
                    print("admission confirmed")
                else:
                    print("admission pending (fee not paid)")

            else:
                print("added to waiting list")
        else:
            print("admission rejected(invaild documents)")

    else:
        print("adimission rejected (not eligible)")

    print("process completed")
    
with open('student.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        admissionprocdure(row['name'], int(row['marks']), row['documents'], row['seat'], row['fee'],60)