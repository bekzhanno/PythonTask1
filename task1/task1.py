from itertools import permutations  
def allPermutations(z):
       
     permList = permutations(z)
     for perm in list(permList):
         print (''.join(perm))
        
z = input("Enter the characters:")
print(z)
allPermutations(z)