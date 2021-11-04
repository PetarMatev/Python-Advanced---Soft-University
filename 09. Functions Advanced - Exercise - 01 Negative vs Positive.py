# 01. Negative vs Positive:
def negative_vs_positive(numbers, positive=0, negative=0):
    if not numbers:
        if abs(negative) > positive:
            return f"{negative}", f"{positive}", "The negatives are stronger than the positives"
        else:
            return f"{negative}", f"{positive}", "The positives are stronger than the negatives"

    if numbers[0] < 0:
        return negative_vs_positive(numbers[1:], positive, negative + numbers[0])
    return negative_vs_positive(numbers[1:], positive + numbers[0], negative)


print("\n".join(negative_vs_positive(list(map(int, input().split())))))
