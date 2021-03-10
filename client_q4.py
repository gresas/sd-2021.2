import rpyc, time
import sys
 

if len(sys.argv) < 2:
   exit("Usage {} SERVER".format(sys.argv[0]))
 
server = sys.argv[1]
n = 10000
# n = int(input())

start = time.time() 
conn = rpyc.connect(server,18861)

arr = [i for i in range(n)]

print(conn.root.sum_array_timed(arr))
end = time.time() 

print(end-start)