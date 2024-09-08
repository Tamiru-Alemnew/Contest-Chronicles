def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        s = data[index]
        index += 1
        
        # When length is odd, we may need to delete one character to make it even.
        # Let's handle both even and odd length cases.

        # Even indexed characters: s[0], s[2], s[4], ...
        # Odd indexed characters: s[1], s[3], s[5], ...
        from collections import Counter

        even_count = Counter(s[i] for i in range(0, n, 2))
        odd_count = Counter(s[i] for i in range(1, n, 2))
        
        # Maximum frequency characters in even and odd positions
        max_even_freq = max(even_count.values(), default=0)
        max_odd_freq = max(odd_count.values(), default=0)
        
        if n % 2 == 0:
            # If length is even, no deletion is needed.
            min_operations = (n // 2 - max_even_freq) + (n // 2 - max_odd_freq)
        else:
            # If length is odd, we may consider one deletion.
            # Case 1: Delete a character from even positions
            min_operations = (n // 2 - max_even_freq) + (n // 2 + 1 - max_odd_freq)
            # Case 2: Delete a character from odd positions
            min_operations = min(min_operations, (n // 2 + 1 - max_even_freq) + (n // 2 - max_odd_freq))
            # Case 3: We can do one replacement to match both counts
            min_operations = min(min_operations, 1 + (n // 2 - max_even_freq) + (n // 2 - max_odd_freq))
        
        results.append(str(min_operations))
    
    print('\n'.join(results))

solve()
