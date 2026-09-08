class Solution(object):
    def countPrimes(self, n):
        if n <= 2: return 0
        if n == 3: return 1
        is_prime = [True] * n
        is_prime[0] = is_prime[1]=False

        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                step = i
                start = i*i
                is_prime[start:n:step] = [False] * (((n-1-start)//step)+1)
        return sum(is_prime)        
        """
        :type n: int
        :rtype: int
        """
        