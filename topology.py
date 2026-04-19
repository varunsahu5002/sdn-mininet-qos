from mininet.topo import Topo

class SingleSwitchTopo(Topo):
    def build(self):
        # Add switch
        s1 = self.addSwitch('s1')

        # Add hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')

        # Add links
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s1)

topos = {'mytopo': (lambda: SingleSwitchTopo())}

#used mininet custom topology " sudo mn --topo single,3 --controller=remote,ip=127.0.0.1,port=6633 "
#made a topology python file for completeness of github repo
