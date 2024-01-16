# Must do pattern problems before starting DSA

# first pattern --> https://www.codingninjas.com/studio/problems/n-forest_6570177?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems

# my approach
def nForest(n:int) ->None:
    for i in range(n):
        print('* '*n)

# striver's approach
def nForest(n:int) ->None:
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()

# second pattern --> https://www.codingninjas.com/studio/problems/n-2-forest_6570178?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&leftPanelTabValue=SUBMISSION
        
# my approach --> faster 
def nForest(n:int) ->None:
    # Write your solution here.
    for i in range(1, n+1):
        print('* '*i)

# third pattern --> https://www.codingninjas.com/studio/problems/n-triangles_6573689?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems

def nTriangle(n:int) ->None:
    # Write your solution here.
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

# fourth pattern -->  https://www.codingninjas.com/studio/problems/triangle_6573690?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&leftPanelTabValue=SUBMISSION

def triangle( n:int) ->None:
    # Write your solution here.
    for i in range(1, n+1):
        print('{} '.format(i)*i)

# fifth pattern --> https://www.codingninjas.com/studio/problems/seeding_6581892?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&leftPanelTabValue=SUBMISSION
        
def seeding(n: int) -> None:
    # Write your solution here.
    for i in range(n, -1, -1):
        print('* '*i)

# sixth pattern --> https://www.codingninjas.com/studio/problems/reverse-number-triangle_6581889?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&leftPanelTabValue=SUBMISSION
        
def nNumberTriangle(n: int) -> None:
    # Write your solution here.
    for i in range(n, 0, -1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

# seventh pattern --> https://www.codingninjas.com/studio/problems/star-triangle_6573671?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&leftPanelTabValue=SUBMISSION
        
def nStarTriangle(n: int) -> None:
    # Write your code here.
    stars = 1
    while n > 0:
        spaces = n - 1
        print(spaces*' ' + stars*'*' + spaces*' ')
        n-=1
        stars += 2

# eigth pattern -->   

