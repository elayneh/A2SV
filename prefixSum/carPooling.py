#!/usr/bin/python3

"""
There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

"""
class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        pchange = [0] * 1001
        for trip in trips:
            noPass, start, end = trip
            pchange[start] += noPass
            pchange[end] -= noPass

        currPass = 0
        for i in range(1001):
            currPass += pchange[i]
            if currPass > capacity:
                return False

        return True
