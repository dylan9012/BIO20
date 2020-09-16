ways = []
output = []

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def arrangments(constructor, letters, r):
	if len(constructor) != r:
		for i in letters:
			arrangments(constructor+i, letters, r)
	else:
		ways.append(constructor)
			
def verify(plan, q):
	count = 1
	for k in range(len(plan)):				
		if k == len(plan) - 2:
			if plan[k] == plan[k+1]:
				count += 1
			if count <= q:
				output.append(plan)
			break	
		else:
			if plan[k] == plan[k+1]:
				count += 1
				if count > q:
					break
			else:
				count = 1
	
def plans(p,q,r,n):
	letters = (ALPHABET[0:p])
	for i in letters:
		arrangments(i, letters, r)
	if len(ways) > 1 and q > 1:
		for j in ways:
			verify(j, q)
		print(output[n-1])
	else:
		print(ways[n-1])										
	
p = int(input("P: "))
q = int(input("Q: "))
r = int(input("R: "))
n = int(input("N: "))

plans(p,q,r,n)
