#User function Template for python3

class Solution:
	def binaryToDecimal(self, b):
		# Code here
		ans = 0
		for ch in b:
		    ans = ans * 2 + int(ch)
		return ans