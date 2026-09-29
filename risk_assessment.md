# Risk Assessment and Project Setup

## a. Assets, Vulnerabilities, and Consequences

### Identified Assets
* **Student Records Database:** The sensitive personal, academic, and administrative data stored centrally.
* **Central Records Server:** The physical or virtual infrastructure hosting the database.
* **Inter-Campus Network Infrastructure:** The communication channels used to transmit files between the two campuses.


### Identified Vulnerabilities and Consequences
1. **Weak Staff Passwords**
   * **Consequence:** An attacker could easily brute-force or guess a staff member's password, leading to unauthorized access to the system and data theft.
2. **Unencrypted Inter-Campus File Transfers**
   * **Consequence:** Attackers on the network can intercept transmissions (man-in-the-middle attack) to read or alter student records while they are moving between campuses.
3. **Guest Network Access to the Records Server**
   * **Consequence:** Anyone sitting in the campus lobby or parking lot connected to the guest Wi-Fi could directly scan, attack, or exploit the central server.
  

## b. Risk Ranking and Justification

1. **Risk 1: Weak Staff Passwords**
   * **Likelihood:** High: The IT team has already observed repeated external connection attempts, meaning attackers are actively trying to gain entry.
   * **Impact:** High: If a credential is compromised, the attacker can fully access, modify, or steal confidential student database records.

2. **Risk 2: Guest Network Access to the Records Server**
   * **Likelihood:** Medium: It requires a malicious actor to physically be within range of the campus guest Wi-Fi or breach it remotely.
   * **Impact:** High: Direct server access bypasses external firewalls, allowing a local attacker to attempt exploits directly against the core system hosting data.

3. **Risk 3: Unencrypted Inter-Campus File Transfers**
   * **Likelihood:** Medium: An attacker must be positioned along the specific network path between the two campuses to intercept traffic.
   * **Impact:** Medium: While it exposes files mid-transit, it does not give the attacker a direct doorway into the entire underlying server infrastructure.


## c. Recommended Controls

1. **Control for Weak Staff Passwords:** Implement a strict password complexity policy requiring strong passwords, combined with mandatory **Multi-Factor Authentication (MFA)** for all staff accounts.
2. **Control for Guest Network Access:** Configure strict **Network Segmentation** and firewall traffic filtering rules to completely isolate the guest network from the internal server zone.
3. **Control for Unencrypted File Transfers:** Mandate the use of secure cryptographic transfer protocols like **SFTP (SSH File Transfer Protocol)** or establish a secure **VPN tunnel** between the two campuses to encrypt all transit data.
