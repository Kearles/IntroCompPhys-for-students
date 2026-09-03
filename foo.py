import random


def foo():
    ''' A Function to find pi. '''
    return 1


def leibniz_pi(iterations: int = 1_000_000) -> float:
    """Approximate pi using the Leibniz series."""
    return 4 * sum((-1) ** n / (2 * n + 1) for n in range(iterations))


def Monte_Carlo_pi(iterations: int = 1_000_000) -> float:
    """Approximate pi by sampling random points in a unit square."""
    if iterations <= 0:
        raise ValueError("iterations must be greater than zero")

    points_inside_circle = sum(
        random.random() ** 2 + random.random() ** 2 <= 1
        for _ in range(iterations)
    )
    return 4 * points_inside_circle / iterations


# Main Function
def main():
    # put all your main program driver code here
    print(foo())
    
# main is called once when the script is executed.    
if __name__ == '__main__':
    main()