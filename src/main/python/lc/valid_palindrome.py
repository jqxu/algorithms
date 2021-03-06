class Solution:
	# @param s, a string
	# @return a boolean
	def isPalindrome(self, s):
		start = 0
		end = len(s) - 1

		while start <= end:
			while start < end and not s[start].isalnum():
				start += 1
			while start < end and not s[end].isalnum():
				end -= 1
			if s[start].lower() != s[end].lower():
				return False
			start += 1
			end -= 1

		return True

if __name__ == '__main__':
	s = Solution()
	st = " "
	print(s.isPalindrome(st))
