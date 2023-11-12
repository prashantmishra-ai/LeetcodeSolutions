from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0

        adj_list = defaultdict(list)
        # Create a map from the bus stop to all the routes that include this stop.
        for route_index, route in enumerate(routes):
            for stop in route:
                adj_list[stop].append(route_index)

        q = deque()
        visited = set()
        # Insert all the routes in the queue that have the source stop.
        for route in adj_list[source]:
            q.append(route)
            visited.add(route)

        bus_count = 1
        while q:
            size = len(q)
            for _ in range(size):
                route = q.popleft()
                # Iterate over the stops in the current route.
                for stop in routes[route]:
                    # Return the current count if the target is found.
                    if stop == target:
                        return bus_count
                    # Iterate over the next possible routes from the current stop.
                    for next_route in adj_list[stop]:
                        if next_route not in visited:
                            visited.add(next_route)
                            q.append(next_route)
            bus_count += 1

        return -1

# Example usage:
# sol = Solution()
# print(sol.numBusesToDestination(routes=[[1, 2, 7], [3, 6, 7]], source=1, target=6))  # Should return the number of buses needed
