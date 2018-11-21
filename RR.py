
process=[]
readyQ=[]
bursttime=[]
rem_btime=[]
arrivaltime=[]
completetime=[]
turnaroundtime=[]

n = 0
time_q = 0
a = "p0"
b = 1
c = 2
inp = open("Input.txt","r")
for line in inp:
	a,b,c=line.split()
	process.append(a)
	arrivaltime.append(int(b))
	bursttime.append(int(c))
	turnaroundtime.append(0)

n = len(process)
print("Input read from file: ")
print("Process: "+str(process))
print("Arrival: "+str(arrivaltime))
print("BurstT:  "+str(bursttime))
print("")

print ("Enter Time Quantum : ")
time_q = int(input())

clock = 0
temparrt=[]

execution_complete = 'false'
while(execution_complete == 'false'):
	execution_complete = 'true'
	k=0
	for j in range( 0,len(process) ):
		if(arrivaltime[j] != -1):
			if(arrivaltime[j] <= clock):
				readyQ.append(bursttime[j])		
				rem_btime.append(bursttime[j])
				temparrt.append(arrivaltime[j])
				completetime.append(0)
				arrivaltime[j]=-1	
				if(k == 0):
					k=j
	for i in range( k,len(readyQ) ):
		if(rem_btime[i] > 0):
			execution_complete = 'false'
			if(rem_btime[i] > time_q):
				clock = clock + time_q
				rem_btime[i] = rem_btime[i]-time_q
			else:
				clock = clock + rem_btime[i]
				completetime[i] = clock
				rem_btime[i] = 0


for i in range(0,len(readyQ)):
	turnaroundtime[i] = completetime[i] - temparrt[i]

sum_waiting = 0.0
sum_turnaroundtime = 0.0

for i in range(0,n): 
        sum_turnaroundtime = sum_turnaroundtime + turnaroundtime[i]
	print("Turnaround time of " + str(process[i]) + " = " + str(turnaroundtime[i]))
	print("")
  
print("Average Turnaround time = " + str(float(float(sum_turnaroundtime) / n)))
