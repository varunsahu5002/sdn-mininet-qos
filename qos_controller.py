from pox.core import core
import pox.openflow.libopenflow_01 as of
import pox.lib.packet as pkt

log = core.getLogger()

class QoSController(object):
    def __init__(self, connection):
        self.connection = connection
        connection.addListeners(self)

    def _handle_PacketIn(self, event):
        packet = event.parsed

        if not packet.parsed:
            return

        ip = packet.find('ipv4')

        # BLOCK: h1 (10.0.0.1) → h3 (10.0.0.3)
        if ip and ip.srcip == "10.0.0.1" and ip.dstip == "10.0.0.3":
            log.info("BLOCKED: h1 -> h3 traffic")
            return  # Drop packet

        # QoS classification logs
        if ip:
            if ip.protocol == 1:
                log.info("HIGH PRIORITY: ICMP packet")
            elif ip.protocol == 6:
                log.info("LOW PRIORITY: TCP packet")

        # Normal forwarding
        msg = of.ofp_packet_out()
        msg.data = event.ofp
        msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
        self.connection.send(msg)

def launch():
    def start_switch(event):
        log.info("Switch connected")
        QoSController(event.connection)

    core.openflow.addListenerByName("ConnectionUp", start_switch)
