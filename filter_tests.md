# Section 3: Network Traffic Filtering Lab Log

This log documents the iptables configuration rules applied to protect the central student records server and records the tests conducted to verify network security behavior.

## 1. Applied Firewall Rules

The following rules were configured in the laboratory environment to restrict access to the student records server:

```bash
# Set default policies to drop incoming traffic
iptables -P INPUT DROP
iptables -P FORWARD DROP

# a. Block guest network access to the student records server (Assuming Guest Subnet: 192.168.50.0/24)
iptables -A INPUT -s 192.168.50.0/24 -j DROP

# b. Permit authorised staff network access to the specified service (Assuming Staff Subnet: 10.0.10.0/24, Service Port: 443 HTTPS)
iptables -A INPUT -s 10.0.10.0/24 -p tcp --dport 443 -j ACCEPT

# c. Block other inbound access to that service
iptables -A INPUT -p tcp --dport 443 -j DROP

# Allow loopback traffic and established connections for stability
iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
```

---

## 2. Firewall Verification Tests

### Test 1: Authorised Staff Connection (Permitted)
* **Command:** `curl -k https://10.0.10.5` (Executed from Staff PC: `10.0.10.25`)
* **Expected Outcome:** Connection successful; returns the web page content or server response.
* **Actual Result:** `HTTP/1.1 200 OK` received. Traffic permitted as intended.

### Test 2: Guest Network Connection (Blocked)
* **Command:** `curl -k --connect-timeout 5 https://10.0.10.5` (Executed from Guest PC: `192.168.50.12`)
* **Expected Outcome:** Connection drops or times out completely due to the DROP rule.
* **Actual Result:** `curl: (28) Connection timed out`. Access explicitly blocked.

### Test 3: Unauthorised External Network Connection (Blocked)
* **Command:** `curl -k --connect-timeout 5 https://10.0.10.5` (Executed from Unauthorised External IP: `203.0.113.88`)
* **Expected Outcome:** Connection drops silently due to default fallback policies or specific service restrictions.
* **Actual Result:** `curl: (28) Connection timed out`. Access denied.
