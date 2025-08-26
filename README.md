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

