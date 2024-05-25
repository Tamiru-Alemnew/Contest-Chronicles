import math

def min_screens(t, test_cases):
    results = []
    
    for x, y in test_cases:
        # Calculate screens needed for 2x2 icons
        screens_for_2x2 = (y + 1) // 2
        
        # Calculate remaining 1x1 icons after using screens for 2x2
        remaining_1x1_icons = x - screens_for_2x2 * 7
        if remaining_1x1_icons < 0:
            remaining_1x1_icons = 0
        
        # Calculate additional screens for remaining 1x1 icons
        screens_for_1x1 = (remaining_1x1_icons + 14) // 15
        
        total_screens = screens_for_2x2 + screens_for_1x1
        results.append(total_screens)
    
    return results

# Input reading and processing
import sys
input = sys.stdin.read
data = input().split()
t = int(data[0])
test_cases = [(int(data[i*2+1]), int(data[i*2+2])) for i in range(t)]
results = min_screens(t, test_cases)

for result in results:
    print(result)
