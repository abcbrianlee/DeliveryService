### Brian Lee
### 010698043
### C950 WGUPS PA

import csv
import datetime

import Truck
from Address import addressData, loadAddressData

from HashTable import CreateHashMap
from Packages import Package

with open("Distance_file.csv") as csvfile1:
    CSV_Distance = csv.reader(csvfile1)
    CSV_Distance = list(CSV_Distance)

with open("Package_file.csv") as csvfile3:
    CSV_Package = csv.reader(csvfile3)
    CSV_Package = list(CSV_Package)

#Takes package CVS file and appends each row into a list, creating a new object for each row of packages and their respective attributes
#Loads all entries into a hashtable, with its ID being the key.
def load_package(filename, package_hash_table):
    with open(filename) as package_data:
        package_data = csv.reader(package_data)
        for package in package_data:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZipcode = package[4]
            pDeadline_time = package[5]
            pWeight = package[6]
            pStatus = "At Hub"
            pDeparture_Time = None


            pObject = Package(pID, pAddress, pCity, pState, pZipcode, pDeadline_time, pWeight, pStatus, pDeparture_Time)

            package_hash_table.insert(pID, pObject)

#Appends each row in distance CSV to a list
def loadDistanceData(distanceData, distanceCSV):
    with open(distanceCSV, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            distanceData.append(row[1:])

#Takes two addresses searches addressData to return an index. Then it uses [i][j] to find the distance in a 2-array list
def distanceBetween(address1, address2):
    return float(distanceData[addressData.index(address1)][addressData.index(address2)])

#
def minDistanceFrom(fromAddress, truckPackages, visitedAddresses, visitedID):
    minDistance = 2000
    minAddress = None
    for address in truckPackages: #Loops through each package that is loaded in it's respective truck
        p = package_hash_table.lookup(address)
        if p.address not in visitedAddresses or p.ID not in visitedID:#Continues to find the distance as long as the packageID and packageAddress has not been visited.

            distance = distanceBetween(fromAddress, p.address)#Loops through all the packages to find which package has the closest distance
            if distance < minDistance:
                minDistance = distance
                minAddress = address

    return minDistance, minAddress#Returns the closest distance and its package ID

def truckDeliverPackages(truck):

    truckTotalMileage = 0 #Sets the trucks mileage to 0, where it will be updated frequently
    deliveryTime = truck.depart_time # Sets Delivery Time to trucks departure time
    for package in truck.packages: #loops through each package in respective truck and sets status to 'en route' and its departure time
        pS = package_hash_table.lookup(package)
        pS.status = 'En Route'
        pS.departure_time = truck.depart_time



    for package in truck.packages:
        addressChange = datetime.timedelta(hours=10, minutes=20, seconds=0)
        if deliveryTime >= addressChange and package_hash_table.lookup(9).status == 'En Route':#package 9 address gets modified and make sure it only happens once
            pNew = Package(9, '410 S State St', 'Salt Lake City', 'UT', '84111', 'EOD', '2 Kilos', 'En Route', truck.depart_time)
            package_hash_table.insert(9, pNew)#inserts modified package

        distance, pAddress = minDistanceFrom(truck.address, truck.packages, visitedAddresses, visitedID)
        #finds the minimum Distance to travel to

        timeToDeliver = distance / 18.0
        time_obj = datetime.timedelta(hours=int(timeToDeliver), minutes = int((timeToDeliver % 1)*60), seconds = int(((timeToDeliver % 1)*60)%1 * 60))

        truckTotalMileage += distance #updates truck mileage
        deliveryTime += time_obj # updates time

        p = package_hash_table.lookup(pAddress)

        p.status='Delivered'
        p.delivery_time = deliveryTime
        truck.address = p.address
        visitedAddresses[p.address] = True #adds address and ID to dictionary so that repeptitive visits won't occur
        visitedID[p.ID] = True

    return(round(truckTotalMileage, 2), deliveryTime)

#Manually loads all 3 trucks.
truck1 = Truck.Truck(16, 18, None, [1, 13, 14, 15, 16, 19, 20, 21, 22, 24, 26, 29, 31, 33, 34, 40], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=8));
truck2 = Truck.Truck(16, 18, None, [3, 18, 23, 27, 30, 35, 36, 37, 38, 39], 0.0,
                     "4001 South 700 East", datetime.timedelta(hours=8))
truck3 = Truck.Truck(16, 18, None, [2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 17, 25, 28, 32], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=9, minutes=8))


package_hash_table = CreateHashMap()

distanceData = []
addressData = []
visited_locations = []
visitedID = {}
visitedAddresses = {}

distanceCSV = 'Distance_file.csv'
loadDistanceData(distanceData, distanceCSV)
load_package("Package_file.csv", package_hash_table)

addressCSV = 'Address_file.csv'
loadAddressData(addressData, addressCSV)



truck1Result1, truck1Result2 = truckDeliverPackages(truck1)
truck2Result1, truck2Result2 = truckDeliverPackages(truck2)
truck3Result1, truck3Result2 = truckDeliverPackages(truck3)

class Main:
    #while loop
    print('Welcome to WGUPS Routing Program!')
    print('Please select an option below!')

    print('1. Print All Package Status and Total Mileage')
    print('2. Get a Single Package Status with a Time')
    print('3. Get All Package Status with a Time')
    print('4. Exit the Program')

    user_input = input('Please select from 1 -4: ')
    #while loop
    if user_input == '1':
        for num in range(1, 41):
            user_package = package_hash_table.lookup(num)
            print(user_package)
        print("The total mileage for Truck 1 was", truck1Result1, "miles with a finished time at", truck1Result2)
        print("The total mileage for Truck 2 was", truck2Result1, "miles with a finished time at", truck2Result2)
        print("The total mileage for Truck 3 was", truck3Result1, "miles with a finished time at", truck3Result2)


    if user_input == '2':
        package_input = int(input('Please enter a package number 1-40: '))
        user_package = package_hash_table.lookup(package_input)
        user_time = input('Please enter a time (HH:MM:SS): ')
        (hrs, mins, secs) = user_time.split(':')
        convert_user_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds = int(secs))

        if convert_user_time >= user_package.delivery_time:
            print(user_package.ID, ",",
                  user_package.address, ",",
                  user_package.city, ",",
                  user_package.state, ",",
                  user_package.zipcode, ",",
                  user_package.Deadline_time, ",",
                  user_package.weight, ",",
                  "Package Delivered", ",",
                  "Delivery time/Expected delivery time", user_package.delivery_time)

        if convert_user_time < user_package.delivery_time and convert_user_time <= user_package.departure_time:
            print(user_package.ID, ",",
                      user_package.address, ",",
                      user_package.city, ",",
                      user_package.state, ",",
                      user_package.zipcode, ",",
                      user_package.Deadline_time, ",",
                      user_package.weight, ",",
                      "Package at Hub", ",",
                      "Delivery time/Expected delivery time" , user_package.delivery_time)

        if convert_user_time < user_package.delivery_time and convert_user_time > user_package.departure_time:
            print(user_package.ID, ",",
                  user_package.address, ",",
                  user_package.city, ",",
                  user_package.state, ",",
                  user_package.zipcode, ",",
                  user_package.Deadline_time, ",",
                  user_package.weight, ",",
                  "Package En Route", ",",
                  "Delivery time/Expected delivery time", user_package.delivery_time)


    if user_input =='3':
        user_time = input('Please enter a time (HH:MM:SS): ')
        (hrs, mins, secs) = user_time.split(':')
        convert_user_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))

        for num in range(1, 41):
            user_package = package_hash_table.lookup(num)
            if convert_user_time >= user_package.delivery_time:
                print(user_package.ID, ",",
                      user_package.address, ",",
                      user_package.city, ",",
                      user_package.state, ",",
                      user_package.zipcode, ",",
                      user_package.Deadline_time, ",",
                      user_package.weight, ",",
                      "Package Delivered", ",",
                      "Delivery time/Expected delivery time" , user_package.delivery_time)

            if convert_user_time <= user_package.delivery_time and convert_user_time <= user_package.departure_time:
                print(user_package.ID, ",",
                      user_package.address, ",",
                      user_package.city, ",",
                      user_package.state, ",",
                      user_package.zipcode, ",",
                      user_package.Deadline_time, ",",
                      user_package.weight, ",",
                      "Package at Hub", ",",
                      "Delivery time/Expected delivery time" , user_package.delivery_time)

            if convert_user_time < user_package.delivery_time and convert_user_time > user_package.departure_time:
                print(user_package.ID, ",",
                      user_package.address, ",",
                      user_package.city, ",",
                      user_package.state, ",",
                      user_package.zipcode, ",",
                      user_package.Deadline_time, ",",
                      user_package.weight, ",",
                      "Package En Route", ",",
                      "Delivery time/Expected delivery time" , user_package.delivery_time)

    if user_input == '4':
        print('Exiting Program')
        exit()

