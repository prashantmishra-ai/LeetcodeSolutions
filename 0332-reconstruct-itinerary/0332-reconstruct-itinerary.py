class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(airport):
            while graph[airport]:
                # The pop() method ensures that the ticket is "used up"
                dfs(graph[airport].pop(0))
            # Add the airport to the result once all its outgoing tickets are used up.
            itinerary.append(airport)

        # Step 1: Create the adjacency list (with sorted destinations)
        graph = defaultdict(list)
        for src, dest in sorted(tickets):
            graph[src].append(dest)

        itinerary = []
        dfs("JFK")

        # The itinerary is constructed in reverse, so we return its reverse.
        return itinerary[::-1]
