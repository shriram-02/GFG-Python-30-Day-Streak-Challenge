class Solution:
    def firstOccurence(self,txt,pat):
        #code here
        n,m = len(txt),len(pat)
        for i in range(n - m + 1):
            if txt[i:i + m] == pat:
                return i 
        return - 1