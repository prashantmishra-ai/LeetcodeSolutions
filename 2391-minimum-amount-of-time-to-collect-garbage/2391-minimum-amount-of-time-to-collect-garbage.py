class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # Initialize the total time for each truck
        total_time = {'M': 0, 'P': 0, 'G': 0}

        # Track the last house where each type of garbage was found
        last_house = {'M': -1, 'P': -1, 'G': -1}

        # Iterate over each house
        for i, g in enumerate(garbage):
            # Update the last house for each type of garbage
            for garbage_type in 'MPG':
                if garbage_type in g:
                    last_house[garbage_type] = i
                    total_time[garbage_type] += len([x for x in g if x == garbage_type])

        # Calculate the total travel time for each truck
        for garbage_type in 'MPG':
            if last_house[garbage_type] != -1:
                total_time[garbage_type] += sum(travel[:last_house[garbage_type]])

        # The total time is the sum of times for each truck
        return sum(total_time.values())