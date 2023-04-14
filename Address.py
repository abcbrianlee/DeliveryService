import csv

#Takes CVS file and appends each row into a List
def loadAddressData(addressData, addressCSV):
    with open(addressCSV, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            addressData.append(row[0])


addressData = []
addressCSV = 'Address_file.csv'
loadAddressData(addressData, addressCSV)

