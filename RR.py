def sort():
	for i in range(0,n):
	       	sorted_queue.append([arrival_time[i],burst_time[i],process[i]])
	sorted_queue.sort()
	for i in range(0,n):
		arrival_time[i] = sorted_queue[i][0]
		burst_time[i] = sorted_queue[i][1]
		process[i] = sorted_queue[i][2]
	print(" ")

def not_complete():
	done = 0
	for i in range(0,n):
		if(sorted_queue[i][1]<=0):
			done = done + 1
	if(done == n):
		return 'false'
	else:
		return 'true'

process=[]
ready_queue=[]
sorted_queue=[]
burst_time=[]
arrival_time=[]
turnaroundtime=[]

n = 0
a = "p0"
b = 1
c = 2

time_q = 0
inp = open("Input.txt","r")
for line in inp:
	a,b,c=line.split()
	process.append(a)
	arrival_time.append(int(b))
	burst_time.append(int(c))
	turnaroundtime.append(0)

n = len(process)
print("Input read from file: ")
print("Process: "+str(process))
print("Arrival: "+str(arrival_time))
print("BurstT:  "+str(burst_time))
print("")

print ("Enter Time Quantum : ")
time_q = int(input())

clock = 0
sort()

print("After Swapping: ")
print("Process: " , sorted_queue)

while(not_complete() == 'true'):
	k=0
	y=0
	count=0
	for i in range( 0,n ):
		if(arrival_time[i]>clock):
			count = count + 1
	if(count == n):
		clock = clock + 1
	else:
		for j in range( 0,n ):
			if(sorted_queue[j][0] != -1):
				if(sorted_queue[j][0] <= clock):
					ready_queue.append([sorted_queue[j][1],sorted_queue[2]])		
					sorted_queue[j][0] = -1
					if(k == 0):
						k = j
		for i in range( 0, n ):
			if(sorted_queue[i][0] == -1):
				if(sorted_queue[i][1] > 0):
					if(sorted_queue[i][1] > time_q):
						clock = clock + time_q
						sorted_queue[i][1] = sorted_queue[y][1] - time_q
					else:
						clock = clock + sorted_queue[i][1]
						turnaroundtime.insert(i,clock - arrival_time[i])
						sorted_queue[i][1] = 0

sum_waiting = 0.0
sum_turnaroundtime = 0.0

for i in range(0,n): 
        sum_turnaroundtime = sum_turnaroundtime + turnaroundtime[i]
	print("Turnaround time of " + str(sorted_queue[i][2]) + " = " + str(turnaroundtime[i]))
	print("")
  
print("Average Turnaround time = " + str(float(float(sum_turnaroundtime) / n)))
