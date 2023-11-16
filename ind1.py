#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from datetime import date


def main():
    # List of flights.
    flights = []

    # Organize an endless cycle of requesting commands.
    while True:
        # Request a command from the terminal.
        command = input(">>> ").lower()

        # Perform the action according to the command.
        if command == 'exit':
            break

        elif command == 'add':
            # Request flight details.
            destination = input("Destination name: ")
            aircraft_type = input("Aircraft type: ")
            flight_number = input("Flight number: ")

            # Create a dictionary.
            flight = {
                'destination': destination,
                'aircraft_type': aircraft_type,
                'flight_number': flight_number,
            }

            # Add a dictionary to the list.
            flights.append(flight)

            # Sort the list based on flight numbers.
            flights.sort(key=lambda item: item.get('flight_number', ''))

        elif command == 'list':
            # Table header.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 8
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                    "№",
                    "Destination",
                    "Aircraft type",
                    "Flight number"
                )
            )
            print(line)

            # Output data about all flights.
            for idx, flight in enumerate(flights, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                        idx,
                        flight.get('destination', ''),
                        flight.get('aircraft_type', ''),
                        flight.get('flight_number', '')
                    )
                )

            print(line)

        elif command.startswith('select '):
            # Get the destination name.
            destination_name = command.split(' ', maxsplit=1)[1].strip()

            # Display flight numbers and aircraft types for the given destination.
            display_flights_for_destination(flights, destination_name)

        elif command == 'help':
            # Output help about working with the program.
            print("List of commands:\n")
            print("add - add a flight;")
            print("list - display a list of flights;")
            print("select <destination> - display flight numbers and aircraft types for a destination;")
            print("help - display help;")
            print("exit - exit the program.")

        else:
            print(f"Unknown command {command}", file=sys.stderr)


def display_flights_for_destination(flights, destination_name):
    matching_flights = [flight for flight in flights if flight['destination'] == destination_name]

    if matching_flights:
        print(f"\nFlights to {destination_name}:")
        for flight in matching_flights:
            print(f"Flight Num: {flight['flight_number']}, Aircraft Type: {flight['aircraft_type']}")
    else:
        print(f"\nNo flights found to {destination_name}.")


if __name__ == '__main__':
    main()
