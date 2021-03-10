import rpyc
import sys
 
if len(sys.argv) < 2:
   exit("Usage {} SERVER".format(sys.argv[0]))
 
server = sys.argv[1]
 
conn = rpyc.connect(server,18861)

n = int(input())
arr = [i for i in range(n)]

print(conn.root.sum_array(arr))