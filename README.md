# 🔍 Shodan Network Scanner

A Python script that automates querying the [Shodan](https://www.shodan.io/) API for a list of IP addresses or CIDR ranges.  
It retrieves details about open ports, detected services, versions, and known vulnerabilities (CVEs), then saves the results to a file.

---

## ✨ Features

- Reads IPs/CIDRs from a file  
- Queries Shodan using its API  
- Extracts IP, port, service, version, and vulnerabilities  
- Saves results to a text file while also printing to console  
- Handles errors gracefully  

---

## 📦 Requirements

- Python 3.7+  
- [Shodan Python library](https://pypi.org/project/shodan/)  

Install dependencies with:

```bash
pip install shodan
```

---

## ⚙️ Setup

Clone this repository:

```bash
git clone https://github.com/Dextan-solutions/shodan_network_scanner.git
cd shodan-network-scanner
```

Replace the placeholder with your Shodan API key inside the script:

```python
API_KEY = "your_API_key_here"
```

Prepare a file (e.g., `targets.txt`) with one IP address or CIDR range per line:

```
8.8.8.8
1.1.1.0/24
```

---

## 🚀 Usage

Run the script:

```bash
python shodan_network_scanner.py
```

You will be prompted for:
- The input file (list of IPs/CIDRs)
- The output file (where results will be saved)

---

## 📄 Example

**Input (`targets.txt`):**
```
8.8.8.8
1.1.1.1
```

**Output (`shodan_results.txt`):**
```
Results for 8.8.8.8:
IP: 8.8.8.8 | Port: 53 | Service: Unknown Service | Version: Unknown Version | Vulnerabilities: None

Results for 1.1.1.1:
IP: 1.1.1.1 | Port: 80 | Service: nginx | Version: 1.18.0 | Vulnerability: CVE-2021-23017 | Status: Verified
```

---

## ⚠️ Disclaimer

This tool is for educational and authorized security testing only.  
Unauthorized scanning of networks without permission may be illegal.  
**Always ensure you have explicit authorization before running this tool.**
