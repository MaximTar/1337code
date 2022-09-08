from collections import Counter


class Solution:
    # 1
    def getHint(self, secret: str, guess: str) -> str:
        bulls = {str(x): 0 for x in range(10)}
        for s, g in zip(secret, guess):
            if s == g:
                bulls[s] += 1

        return f'{sum(bulls.values())}A{sum(((Counter(secret) & Counter(guess)) - Counter(bulls)).values())}B'

    # 2 Simplified
    def getHint(self, secret: str, guess: str) -> str:
        # First, we count the number of bulls
        # That is, indices on which the digits in the secret and guess strings match
        bulls = 0
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1

        # To count cows, you can use Counter from collections - a subclass of dict to count hashable objects
        # Counter(secret) will return us a dictionary-like structure
        # containing numbers (in string format) as keys and the digits of times they occur in the secret string
        # Similarly, for the guess string
        # I specifically pointed out that this structure is similar to a dictionary,
        # because it allows us to use the ampersand operator (&),
        # which will return us the intersection of these structures
        # For example, if secret = "1123" and guess = "0111",
        # then Counter(secret) is Counter({'1': 2, '2': 1, '3': 1}),
        # respectively Counter(guess) is Counter({'0': 1, '1': 3})
        # and Counter(secret) & Counter(guess) is Counter({'1': 2})
        # The example shows that in order to get the number of cows,
        # it remains to subtract the number of bulls from the resulting result
        return f'{bulls}A{sum((Counter(secret) & Counter(guess)).values()) - bulls}B'
