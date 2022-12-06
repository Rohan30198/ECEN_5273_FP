#Creating network topology using mininet

from mininet.cli import CLI
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.term import makeTerm

if '__main__' == __name__:
    #adding controller as remote
    net = Mininet(controller=RemoteController)

    c0 = net.addController('c0', port=6633)

    #adding switches
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')
    #adding hosts
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    h3 = net.addHost('h3')
    #adding links between switches and hosts
    net.addLink(s1, h1)
    net.addLink(s2, h2)
    net.addLink(s3, h3)
    net.addLink(s1, s2)
    net.addLink(s2, s3)
    net.addLink(s3, s1)

    net.build()
    # starting the controller 
    c0.start()
    #connecting the switches to the controller
    s1.start([c0])
    s2.start([c0])
    s3.start([c0])
    
    net.startTerms()
    CLI(net)
    net.stop()
