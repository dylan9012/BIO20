ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	
def initialise(plan, output, chosen, length):
	if len(plan) > 0:
		for i in ALPHABET:
			if i not in plan and i not in chosen:
				output.append([i,plan[0]])
				chosen.append(i)
				plan.pop(0)
				return initialise(plan, output, chosen, length)
	else:
		rest = ALPHABET[0:length]
		remaining = []
		for j in rest:
			if j not in chosen:
				remaining.append(j)
		output.append(remaining)	
		return output	
	
def move(spy, dict, rooms, p):
	position = 0
	while p > 0:
		if dict[spy[-1]] % 2 == 0:
			possible = False
			for i in rooms[ALPHABET.index(spy[-1])]:
				if dict[i] % 2 != 0: # Checking for oddly visited room
					position = rooms[ALPHABET.index(spy[-1])].index(i) # nth room	
					if i == rooms[ALPHABET.index(spy[-1])][-1]: #check for last room?
						spy.append(i)
						possible = True
					break					
			if possible: # it is the last room
				dict[spy[-1]] += 1
				p -= 1
				continue
			else: #choosing next room
				if len(rooms[ALPHABET.index(spy[-1])]) == 1 or len(rooms[ALPHABET.index(spy[-1])]) == position + 1: #if only one in list
					adjacent = rooms[ALPHABET.index(spy[-1])][0]
				else:
					adjacent = rooms[ALPHABET.index(spy[-1])][position+1]
				spy.append(adjacent)
				dict[spy[-1]] += 1
				p-=1
				continue
		else:
			next = rooms[ALPHABET.index(spy[-1])][0]
			spy.append(next)
			dict[spy[-1]] += 1
			p-=1
			continue
	return spy[-1]
	
def Alpha(plan, p, q):
	connections = initialise(list(plan), [], [], len(plan)+2)
	rooms = []
	for i in range(0,len(plan)+2):
		letter = ALPHABET[i]
		connected = []
		for j in connections:
			if j[0] == letter:
				connected.append(j[1])
			elif j[1] == letter:
				connected.append(j[0])
		rooms.append(sorted(connected))		
	# moving
	dict = {i: 0 for i in ALPHABET[0:len(plan)+2]}
	dict['A'] += 1
	spy = ['A']
	for j in rooms:
		print(''.join(j))	
		
	if p >= q:
		spy1 = move(spy, dict, rooms, q)
		spy2 = move(spy, dict, rooms, p-q)
		print(spy2 + spy1)
	else:
		spy1 = move(spy, dict, rooms, p)
		spy2 = move(spy, dict, rooms, q-p)
		print(spy1+spy2)

			

plan = input("Plan: ")
p = int(input("P = "))
q = int(input("Q = "))
Alpha(plan, p, q)
