class Solution(object):
    def largestVariance(self, s):
        counter = [0] * 26
        for ch in s:
            counter[ord(ch) - ord('a')] += 1
        globalMax = 0
        
        for i in range(26):
            for j in range(26):
                # major and minor cannot be the same, and both must appear in s.
                if i == j or counter[i] == 0 or counter[j] == 0:
                    continue
                
                # Find the maximum variance of major - minor.        
                major = chr(ord('a') + i)
                minor = chr(ord('a') + j)
                majorCount = 0
                minorCount = 0
                
                # The remaining minor in the rest of s.
                restMinor = counter[j]
                
                for ch in s:    
                    if ch == major:
                        majorCount += 1
                    if ch == minor:
                        minorCount += 1
                        restMinor -= 1
                    
                    # Only update the variance (local_max) if there is at least one minor.
                    if minorCount > 0:
                        globalMax = max(globalMax, majorCount - minorCount)
                    
                    # We can discard the previous string if there is at least one remaining minor
                    if majorCount < minorCount and restMinor > 0:
                        majorCount = 0
                        minorCount = 0
        
        return globalMax
