
def tsp_dp(graph):
    # used for dp
    memo = {}
    INF = float('inf')
    n = len(graph)

    #recursive dynamic programming way
    def visit(visited, last):
        # if all cities visited return the cost to return to the starting city
        if visited == (1 << n) - 1:
            return graph[last][0]

        # if already visited return the saves result from memo with dp
        if (visited, last) in memo:
            return memo[(visited, last)]

        # set minimum cost to inf
        min_cost = INF
        for city in range(n):
            # if the city is not  visited
            if not visited & (1 << city):
                # Calculate the new visited city and the cost
                new_visited = visited | (1 << city)
                current_cost = graph[last][city] + visit(new_visited, city)
                min_cost = min(min_cost, current_cost)

        # store the result in the memo
        memo[(visited, last)] = min_cost
        return min_cost

    # start the recursive with city visited
    min_cost = visit(1, 0)

    # construct the path again
    path = []
    last = 0
    visited = 1
    for _ in range(n):
        path.append(last)
        next_city = min(
            range(n),
            key=lambda city: (INF if visited & (1 << city) else graph[last][city] + memo.get((visited | (1 << city), city), INF))
        )
        visited |= (1 << next_city)
        last = next_city
    path.append(0)

    return min_cost, path

# taking graph from user
def get_graph_from_user():
    while True:
        try:
            n = int(input("Enter number of cities: "))
            if n <= 1:
                raise ValueError("Cities should be more than 1.")
            print("Enter the cost matrix row by row (enter 'inf' for infinity):")
            graph = []
            for i in range(n):
                row = input(f"Enter costs for city {i}: ").split()
                if len(row) != n:
                    raise ValueError("Invalid input: Number of elements in each row must be equal to the number of cities.")
                row = [float(x) if x.lower() != 'inf' else float('inf') for x in row]
                if row[i] != 0:
                    raise ValueError(f"Invalid input: Diagonal element at index {i} is not zero.")
                graph.append(row)
            return graph
        except ValueError as e:
            print("Error:", e)
            print("Please enter the values again.\n")

# showing result to user
try:
    graph = get_graph_from_user()
    min_cost, best_path = tsp_dp(graph)
    print("\nMinimum cost:", min_cost)
    print("Best path:", best_path)
except KeyboardInterrupt:
    print("\nProgram terminated by user.")
except Exception as e:
    print("Error:", e)


def main():
    while True:
        try:
            n = int(input("Enter the number of cities (enter 0 to finish): "))

            if n == 0:
                print("Program finished.")
                break

            if n <= 0:
                raise ValueError("Number of cities must be positive.")

            graph = []

            print("Enter the indexes of matrix (space seperated):")
            for i in range(n):
                row = list(map(int, input().split()))
                if len(row) != n:
                    raise ValueError(f"Row {i} does not have {n} elements.")
                graph.append(row)

            #check diagonal elements are zero
            for i in range(n):
                if graph[i][i] != 0:
                    print(f"Warning: Diagonal element at ({i}, {i}) is not zero. Setting it to zero.")
                    graph[i][i] = 0

            # call tsp_dp function to compute the minimum cost and optimal tour
            min_cost, path = tsp_dp(graph)

            # show result
            print(f"Minimum cost to travel all cities and return home is: {min_cost}")
            print(f"Optimal tour (starting and ending at city 0): {' -> '.join(map(str, path))}")
            print()

        except ValueError as ve:
            print(f"Error: {ve}")
            print("Please provide valid input.")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")
            print("Please try again.")

if __name__ == "__main__":
    main()
