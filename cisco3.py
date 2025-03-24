def funcDrop(xCoordinate, yCoordinate):
    # Create a list of points from the coordinates
    # Create a list of points by pairing x and y coordinates
    


def main():
    # Input for xCoordinate
    xCoordinate = []
    xCoordinate_size = int(input())
    xCoordinate = list(map(int, input().split()))
    
    # Input for yCoordinate
    yCoordinate = []
    yCoordinate_size = int(input())
    yCoordinate = list(map(int, input().split()))
    
    result = funcDrop(xCoordinate, yCoordinate)
    print(result)

if __name__ == "__main__":
    main()