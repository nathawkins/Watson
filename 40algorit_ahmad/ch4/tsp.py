"""
Possible solutions to the travelling salesman problem
"""

# Imports ---------------------------------------------------------------------
from argparse import ArgumentParser
from itertools import permutations
from numpy import inf
import matplotlib.pyplot as plt
import random
import time

# Functions -------------------------------------------------------------------
def constructCommandLineArguments():
    # Create ArgumentParser object
    parser = ArgumentParser()

    # Add command line input for number of cities
    parser.add_argument("-N", "--num", 
                        help = "Number of cities to use in simulation. Default: 5",
                        default = 5,
                        type = int)
    
    # Add command line input for triggering timing
    parser.add_argument("-t", "--time",
                        help = "If passed, the simulation will be timed.",
                        action = "store_true")
    
    # Add command line input for method to use
    parser.add_argument("-m", "--method",
                        help = "Method to use for solving the problem. Accepted inputs 'brute' for brute force or 'greedy' for greedy algorithm. Default: 'brute'.",
                        default = 'brute')
    
    # Return parser
    return parser

def generateCities(N,
                   confines = [300, 500],
                   seed = 8675309):
    # Set random seed
    random.seed(N+seed)

    # Generate N points in confines of box
    return [[random.randint(0, confines[0]), random.randint(0, confines[1])] for _ in range(N)]


def calculateDistance(A, B):
    # Euclidean distance
    return ((A[0] - B[0])**2 + (A[1] - B[1])**2)**(1/2)

def totalDistance(city_order,
                  cities):
    # Initialize total distance
    total_distance = 0

    # Loop through city_order. Each element is an index
    # corresponding to a given city in the cities list
    for i in range(1, len(cities)):
        city_A = cities[city_order[i-1]]
        city_B = cities[city_order[i]]

        total_distance += calculateDistance(city_A, city_B)

    # Finally, compute the distance from the endpoint back to the beginning
    total_distance += calculateDistance(cities[-1], cities[0])

    return total_distance

def bruteForceSolution(cities, **kwargs):
    # See if we need to time the experiment
    if kwargs.get('time'):
        start_ = time.time()

    # Define best solution and best total distance
    best_route = None
    best_distance = inf

    # Iterate through all possible solutions to find the best
    for route in permutations(range(len(cities))):
        distance = totalDistance(route, cities)

        if distance < best_distance:
            best_route    = route
            best_distance = distance

    # End timing if applicable
    if kwargs.get('time'):
        print(f"Execution Time: {round(time.time() - start_, 3)}")
    
    return {"Route": best_route, "Distance": best_distance}

def greedySolution(cities, 
                   start = 0,
                   **kwargs):
    # Time algorithm if specified
    if kwargs.get('time'):
        start_ = time.time()

    # Initialize the route
    route = [start]

    # Get current city
    current_city = cities[start]

    # Establish remaining cities (minus the one we are at now)
    remaining_cities = [x for x in cities if x != current_city]

    # Iterate through remaining cities until none are left
    while len(remaining_cities) > 0:
        # Find nearest city
        nearest_neighbor = findNearestNeighbor(current_city, remaining_cities)

        # Get index of neighbor in total list of cities
        nearest_neighbor_index = cities.index(nearest_neighbor)

        # Add to route
        route.append(nearest_neighbor_index)

        # Update current city
        current_city = nearest_neighbor

        # Remove new current city from list of possible cities remaining
        remaining_cities.remove(nearest_neighbor)

    # End timing if applicable
    if kwargs.get('time'):
        print(f"Execution Time: {round(time.time() - start_, 3)}")
    
    return {'Route': route}

def findNearestNeighbor(city, cities):
    # Find C in list of cities that minimizes the distance between
    # the input city and the list of available cities
    return min(cities, key = lambda C: calculateDistance(city, C))

def plotSolution(route, cities):
    # Create figure
    plt.figure(figsize = (12,7))

    # Plot lines connecting cities first so points can be 
    # overlaid on top
    # Connect end of route to starting point
    city_A = cities[route[-1]]
    city_B = cities[route[0]]

    plt.plot([city_A[0], city_B[0]],
             [city_A[1], city_B[1]],
             "b-")
    
    # Iterate through path
    for i in range(1, len(route)):
        city_A = cities[route[i-1]]
        city_B = cities[route[i]]

        plt.plot([city_A[0], city_B[0]],
                 [city_A[1], city_B[1]],
                 "b-")
        
    # Plot points on the graph corresponding to cities
    for city in cities:
        plt.scatter(city[0], city[1], s = 50, c = "k")

    # Show plot
    plt.show()
    

# Main ------------------------------------------------------------------------
def main():
    # Construct command line arguments
    parser = constructCommandLineArguments()

    # Get command line arguments
    args = parser.parse_args()

    # Generate city
    cities = generateCities(args.num)

    # Solve TSP
    if args.method == 'brute':
        solution = bruteForceSolution(cities, time = args.time)

    if args.method == 'greedy':
        solution = greedySolution(cities, time = args.time)

        
    # Plot route
    plotSolution(solution['Route'], cities)
    

if __name__ == '__main__':
    main()