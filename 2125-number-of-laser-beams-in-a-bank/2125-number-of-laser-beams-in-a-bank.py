class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # Count the number of security devices in each row
        device_count_per_row = [row.count('1') for row in bank]

        total_beams = 0
        for i in range(len(device_count_per_row)):
            for j in range(i+1, len(device_count_per_row)):
                # Check if there are no devices in the rows between i and j
                if all(device_count_per_row[k] == 0 for k in range(i+1, j)):
                    total_beams += device_count_per_row[i] * device_count_per_row[j]

        return total_beams
