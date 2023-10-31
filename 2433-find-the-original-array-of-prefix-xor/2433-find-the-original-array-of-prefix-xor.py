class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        n = len(pref)
        for i in range(n-1,0,-1):
            pref[i] = pref[i]^pref[i-1]
        return pref