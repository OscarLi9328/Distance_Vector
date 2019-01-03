from utils import TRACE, YES, NO, Rtpkt, tolayer2


class DistanceTable:
    costs = [[999 for j in range(4)] for i in range(4)]

dt = DistanceTable()

# students to write the following two routines, and maybe some others

# modify this statement for different node
edges = [7, 999, 2, 0]
cost = [7, 999, 2, 0]
node_id = 3

def rtinit3():
    for i in range(4):
        if i == node_id:
        	continue
        dt.costs[i][i] = edges[i]

    printdt3(dt)
    tolayer2(Rtpkt(node_id, 0, edges))
    tolayer2(Rtpkt(node_id, 2, edges))


def rtupdate3(rcvdpkt):
	change = False
	srcid = rcvdpkt.sourceid
	table = rcvdpkt.mincost

	for i in range(4):
		tmp = edges[srcid] + table[i]
		dt.costs[i][srcid] = min(dt.costs[i][srcid], tmp)
		if tmp < cost[i]:
			change = True
			cost[i] = tmp

	printdt3(dt)
	if change:
		tolayer2(Rtpkt(node_id, 0, cost))
		tolayer2(Rtpkt(node_id, 2, cost))


def printdt3(dtptr):
    print("             via     \n")
    print("   D3 |    0     2 \n")
    print("  ----|-----------\n")
    print("     0|  %3d   %3d\n" % (dtptr.costs[0][0], dtptr.costs[0][2]))
    print("dest 1|  %3d   %3d\n" % (dtptr.costs[1][0], dtptr.costs[1][2]))
    print("     2|  %3d   %3d\n" % (dtptr.costs[2][0], dtptr.costs[2][2]))

# rtinit3()
# printdt3(dt)