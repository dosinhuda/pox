#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import irange,dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import RemoteController

import argparse
import sys
import time


class ClosTopo(Topo):

    def __init__(self, fanout, cores, **opts):
        # Initialize topology and default options
        Topo.__init__(self, **opts)
       
        "Set up Core and Aggregate level, Connection Core - Aggregation level"
        for c in irange(1, cores):
            self.addSwitch('full_node%s' %c)
            for a in irange(1, cores*fanout):
                self.addSwitch('agw%s' %(a+cores))
                self.addLink('agw%s' %(a+cores), 'full_node%s' %c)

        counter = cores + (cores*fanout) #to deal with mininet numberings

        "Set up Edge level, Connection Aggregation - Edge level "
        for a in irange(1, cores*fanout):
            for e in irange(1, cores*(fanout**2)):
                self.addSwitch('homegw%s' %(e+counter))
                self.addLink('homegw%s' %(e+counter), 'agw%s' %(a+cores))
        
        "Set up Host level, Connection Edge - Host level "
        host_pod_offset = 0 #offset per pod accessed by edge switch
        for e in irange(1, cores*(fanout**2)):
            for h in irange(1, fanout):
                self.addHost('sta%s' %(host_pod_offset+h))
                self.addLink('homegw%s' %(e+counter), 'sta%s' %(host_pod_offset+h))
            host_pod_offset = host_pod_offset + fanout
	

def setup_clos_topo(fanout=2, cores=2):
    "Create and test a simple clos network"
    assert(fanout>0)
    assert(cores>0)
    topo = ClosTopo(fanout, cores)
    net = Mininet(topo=topo, controller=lambda name: RemoteController('c0', "127.0.0.1"), autoSetMacs=True, link=TCLink)
    net.start()
    time.sleep(20) #wait 20 sec for routing to converge
    #net.pingAll()  #test all to all ping and learn the ARP info over this process
    CLI(net)       #invoke the mininet CLI to test your own commands
    net.stop()     #stop the emulation (in practice Ctrl-C from the CLI 
                   #and then sudo mn -c will be performed by programmer)

    
def main(argv):
    parser = argparse.ArgumentParser(description="Parse input information for mininet Clos network")
    parser.add_argument('--num_of_core_switches', '-c', dest='cores', type=int, help='number of core switches')
    parser.add_argument('--fanout', '-f', dest='fanout', type=int, help='network fanout')
    args = parser.parse_args(argv)
    setLogLevel('info')
    setup_clos_topo(args.fanout, args.cores)


if __name__ == '__main__':
    main(sys.argv[1:])
