#!/usr/bin/python

"""
Setting the position of Nodes (only for Stations and Access Points) and providing mobility using mobility models.

"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.node import CPULimitedHost
from mininet.link import Link, Intf, TCLink
from mininet.util import irange,dumpNodeConnections
from mininet.log import setLogLevel, info
from mininet.node import Controller, RemoteController



def topology():

    "Create a network."
    net = Mininet(controller=Controller, link=TCLink)
   
    print "*** Creating nodes"
    sta1 = net.addHost( 'sta1' )
    sta2 = net.addHost( 'sta2' )
    sta3 = net.addHost( 'sta3')
    sta4 = net.addHost( 'sta4' )
    sta5 = net.addHost( 'sta5')
    sta6 = net.addHost( 'sta6')
    sta7 = net.addHost( 'sta7' )
    sta8 = net.addHost( 'sta8' )
    sta9 = net.addHost( 'sta9'  )
    sta10 = net.addHost( 'sta10' )
    sta11 = net.addHost( 'sta11' )
    sta12 = net.addHost( 'sta12')
    sta13 = net.addHost( 'sta13')
    sta14 = net.addHost( 'sta14' )
    sta15 = net.addHost( 'sta15')
    sta16 = net.addHost( 'sta16')
     

     
    
    full_node1 = net.addSwitch( 'Full-Node1')
    full_node2 = net.addSwitch( 'Full-Node2') 
    agw1 = net.addSwitch( 'AGW1')
    agw2 = net.addSwitch( 'AGW2')
    agw3 = net.addSwitch( 'AGW3')
    agw4 = net.addSwitch( 'AGW4')
    hgw1 = net.addSwitch( 'HomeGW1')
    hgw2 = net.addSwitch( 'HomeGW2')
    hgw3 = net.addSwitch( 'HomeGW3')
    hgw4 = net.addSwitch( 'HomeGW4')
    hgw5 = net.addSwitch( 'HomeGW5')
    hgw6 = net.addSwitch( 'HomeGW6')
    hgw7 = net.addSwitch( 'HomeGW7')
    hgw8 = net.addSwitch( 'HomeGW8')

    c1 = net.addController( 'c1', controller=RemoteController, ip='127.0.0.1', port=6633 )

    
    print "*** Associating and Creating links"
    #net.addLink(full_node1, full_node2, delay ='0.002')
  
    net.addLink(full_node1, agw1) 
    net.addLink(full_node1, agw2) 
    net.addLink(full_node1, agw3) 
    net.addLink(full_node1, agw4, bw=100, delay ='0.02ms', loss=0) 

    net.addLink(full_node2, agw1, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(full_node2, agw2, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(full_node2, agw3, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(full_node2, agw4, bw=100, delay ='0.02ms', loss=0) 


    net.addLink(agw1, hgw1, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(agw1, hgw2, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(agw1, hgw3, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(agw1, hgw4, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(agw1, hgw5, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(agw1, hgw6, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(agw1, hgw7, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(agw1, hgw8, bw=100, delay ='0.02ms', loss=0)

    net.addLink(agw2, hgw1, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(agw2, hgw2, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(agw2, hgw3, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(agw2, hgw4, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(agw2, hgw5, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(agw2, hgw6, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(agw2, hgw7, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(agw2, hgw8, bw=100, delay ='0.02ms', loss=0)

    net.addLink(agw3, hgw1, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(agw3, hgw2, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(agw3, hgw3, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(agw3, hgw4, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(agw3, hgw5, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(agw3, hgw6, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(agw3, hgw7, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(agw3, hgw8, bw=100, delay ='0.02ms', loss=0)
     
    net.addLink(agw4, hgw1, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(agw4, hgw2, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(agw4, hgw3, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(agw4, hgw4, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(agw4, hgw5, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(agw4, hgw6, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(agw4, hgw7, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(agw4, hgw8, bw=100, delay ='0.02ms', loss=0)
     

    net.addLink(hgw1, sta1, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(hgw1, sta2, bw=100, delay ='0.02ms', loss=0)

    net.addLink(hgw2, sta3, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(hgw2, sta4, bw=100, delay ='0.02ms', loss=0)

    net.addLink(hgw3, sta5, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(hgw3, sta6, bw=100, delay ='0.02ms', loss=0)

    net.addLink(hgw4, sta7, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(hgw4, sta8, bw=100, delay ='0.02ms', loss=0)

    net.addLink(hgw5, sta9, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(hgw5, sta10, bw=100, delay ='0.02ms', loss=0)

    net.addLink(hgw6, sta11, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(hgw6, sta12, bw=100, delay ='0.02ms', loss=0)

    net.addLink(hgw7, sta13, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(hgw7, sta14, bw=100, delay ='0.02ms', loss=0)

    net.addLink(hgw8, sta15, bw=100, delay ='0.02ms', loss=0) 
    net.addLink(hgw8, sta16, bw=100, delay ='0.02ms', loss=0)




    print "*** Starting network"
    net.build()
    c1.start()
    
    
    full_node1.start( [c1] )
    full_node2.start( [c1] )

    agw1.start( [c1] )
    agw2.start( [c1] )
    agw3.start( [c1] )
    agw4.start( [c1] )

    hgw1.start( [c1] )
    hgw2.start( [c1] )
    hgw3.start( [c1] )
    hgw4.start( [c1] )
    hgw5.start( [c1] )
    hgw6.start( [c1] )
    hgw7.start( [c1] )
    hgw8.start( [c1] )
   



 
   
    print "*** Running CLI"
    CLI( net )

    print "*** Stopping network"
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    topology()
