class Solution:
    def NumberOf1(self, n):
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            n = n & (n - 1)
            count += 1
            
        return count


if __name__ == "__main__":
    print(Solution().NumberOf1(-1))

