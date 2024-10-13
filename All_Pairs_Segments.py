def join(v, delimiter):
    """Joins a list of strings with the given delimiter."""
    return delimiter.join(v)

def process_test_case(n, q, x, queries):
    freq = {}

    # Calculate the number of segments that cover each point
    for c in range(1, n + 1):
        # Points on x[c] have coverage based on segments ending or starting at x[c]
        k_p = (c - 1) * (n - c + 1) + (n - c)
        freq[k_p] = freq.get(k_p, 0) + 1

        # Handle the gaps between consecutive points
        if c < n:
            delta = x[c] - x[c - 1] - 1
            if delta > 0:
                k_between = c * (n - c)
                freq[k_between] = freq.get(k_between, 0) + delta

    # Prepare answers for queries
    answers = []
    for ki in queries:
        answers.append(str(freq.get(ki, 0)))

    return join(answers, " ")

def main():
    t = int(input())
    results = []

    for _ in range(t):
        n, q = map(int, input().split())
        x = list(map(int, input().split()))
        queries = list(map(int, input().split()))
        
        result = process_test_case(n, q, x, queries)
        results.append(result)

    print(join(results, "\n"))

if __name__ == "__main__":
    main()
