# Printing patterns examples
def print_stars(n):
    print("*"*n)   
print_stars(10)

def print_stars_using_loop(n):
    for i in range(n):
        print("*", end=" ")
        
print_stars_using_loop(10)
print("="*20)

# increasing triangle
def print_stars_insquare_using_loop(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print()
        
print_stars_insquare_using_loop(10)
print("="*20)

# Decreasing triangle
def print_stars_insquare_using_loop(n):
    for i in range(n):
        for j in range(i, n):
            print(i, end=" ")
        print()
        
print_stars_insquare_using_loop(10)


# prits combined triangles
def print_patterns(n):
    for i in range(n):
        for j in range(i+1):
            print(" ", end=" ")
        
        for j in range(i, n-1):
            print("*", end=" ")
            
        for j in range(i, n):
            print("#", end=" ")
            
        print("")
        
print_patterns(5)