# SDN Mininet Project – Traffic Classification and Control

## Problem Statement

The objective of this project is to implement an SDN-based solution using Mininet and a POX controller to demonstrate traffic handling, flow rule behavior, and basic traffic control. The system differentiates traffic behavior and demonstrates allowed versus blocked communication between hosts.

---

## Objectives

* Establish controller–switch interaction using OpenFlow
* Observe packet handling and flow rule installation
* Perform traffic analysis using ping and iperf
* Demonstrate allowed versus blocked traffic behavior

---

## Tools Used

* Mininet
* POX Controller
* Open vSwitch (OVS)
* ping
* iperf

---

## Network Topology

* 1 Switch (s1)
* 3 Hosts (h1, h2, h3)
* Remote controller (POX)

---

## Setup and Execution

### Start POX Controller

```bash
cd ~/pox
./pox.py forwarding.l2_learning
```

### Start Mininet

```bash
sudo mn -c
sudo mn --topo single,3 --controller=remote,ip=127.0.0.1,port=6633
```

---

## Testing and Results

### Test 1: Allowed Traffic (Ping)

```bash
h1 ping -c 5 h2
```

**Observation:**

* Successful communication
* 0% packet loss
* Demonstrates normal forwarding behavior

---

### Test 2: Throughput (iperf)

```bash
h2 iperf -s
h1 iperf -c h2
```

**Observation:**

* Successful TCP communication
* High throughput observed due to virtual environment

---

### Test 3: Blocked Traffic

```bash
h1 iptables -A OUTPUT -d 10.0.0.3 -j DROP
h1 ping -c 5 h3
```

**Observation:**

* 100% packet loss
* Traffic from h1 to h3 is blocked
* Demonstrates traffic control behavior

---

### Flow Table Inspection

```bash
dpctl dump-flows
```

**Observation:**

* Flow entries appear after traffic generation
* Confirms match–action rule behavior

---

## Key Observations

* Controller successfully manages traffic forwarding
* Flow rules are installed dynamically
* Allowed traffic is forwarded successfully
* Specific traffic can be blocked based on defined rules
* Demonstrates SDN-based traffic control principles

---

## Conclusion

The project successfully demonstrates SDN concepts using Mininet and POX. Controller–switch interaction, traffic forwarding, and flow rule behavior were observed. The implementation also shows how specific traffic can be controlled, illustrating the flexibility of SDN.

---

## Proof of Execution

Include screenshots of:

* Controller running with switch connection
* Ping results (allowed traffic)
* iperf results (throughput)
* Blocked ping result showing 100% packet loss
* Flow table output

---

## Future Scope

* Implement QoS-based prioritization using controllers
* Use advanced controllers such as Ryu for improved stability
* Extend to larger and more complex network topologies
