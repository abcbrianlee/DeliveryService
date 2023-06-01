# Parcel Delivery Service

# Overview
The Parcel Delivery Service is an application created using Python. It efficiently manages the delivery of parcels by reading data from a CSV file containing information about various addresses. By utilizing the Greedy's algorithm and a hash table for package ID retrieval, the service ensures quick and efficient delivery routes.

# Features

- **Greedy's Algorithm:** The application utilizes the Greedy's algorithm to optimize the delivery routes, ensuring speedy and efficient parcel delivery.

- **Hash Table:** A hash table is used to store and retrieve package IDs, enabling fast access to package information during the delivery process.

- **Package Criteria and Delivery Requirements:** Each package has specific criteria and delivery requirements, which are taken into account when planning the delivery routes.

- **Text-Based Menu Interface:** The application provides a command-line interface (CLI) with a text-based menu. Users can interact with the program by selecting options presented in the menu, allowing them to perform various actions.

- **Print All Package Status:** Users can select an option to print the status of all packages. This feature provides an overview of the current status of each package.

- **Get a Single Package by ID and Time:** Users can input the ID of a package and a specific time to retrieve the status of that package at the given time. This feature allows users to track the progress and location of individual packages.

- **Get All Package Status by Time:** Users can enter a specific time to retrieve the status of all packages at that time. This feature provides a snapshot of the status of all packages at a particular moment.

- **Calculate Total Mileage:** The application includes an option to calculate the total mileage covered by the trucks during the delivery process. This feature helps monitor and analyze the distance traveled by the trucks.


# Assumptions
The Parcel Delivery Service is designed based on the following assumptions:

- Each truck can carry a maximum of 16 packages.
- Trucks travel at an average speed of 18 miles per hour.
- Trucks have an infinite gas supply and do not require any refueling stops.
- Drivers leave the hub at 8am with the trucks loaded and can return to the hub for additional packages if needed.
- The day is over when all packages have arrived at their destination

## Special Note
Package #9 has the wrong delivery address, and a correction will be made at 10:20 am. This special note ensures that the package is delivered to the correct address at the designated time.

# Getting Started
1. Clone the repository
2. Set main.py located at root as entry point of program

## Contribution
Contributions to the Parcel Delivery Service project are welcome! If you find any bugs, have feature requests, or would like to make improvements, please open an issue or submit a pull request.
