import shodan

API_KEY = "your_shodan_API_here"
api = shodan.Shodan(API_KEY)

# Prompt user for input file location
file_path = input("Enter the path to the file containing IPs/CIDR ranges: ")

try:
    with open(file_path, "r") as file:
        ip_ranges = [line.strip() for line in file if line.strip()]
except FileNotFoundError:
    print("Error: File not found. Please check the path and try again.")
    exit()

# Prompt user for output file location
output_file_path = input("Enter the path to save the results (e.g., shodan_results.txt): ")

# Open output file to save results
with open(output_file_path, "w") as output_file:
    for target in ip_ranges:
        query = f'net:"{target}"'
        try:
            results = api.search(query)
            output_file.write(f"\nResults for {target}:\n")
            print(f"\nResults for {target}:")  # Print to console

            for result in results['matches']:
                ip = result['ip_str']
                port = result.get('port', 'Unknown')
                service = result.get('product', 'Unknown Service')
                version = result.get('version', 'Unknown Version')
                vulns = result.get('vulns', {})

                # Process vulnerabilities
                if vulns:
                    for cve, details in vulns.items():
                        verified = details.get('verified', False)
                        status = 'Verified' if verified else 'Unverified'
                        line = f"IP: {ip} | Port: {port} | Service: {service} | Version: {version} | Vulnerability: {cve} | Status: {status}\n"
                        print(line.strip())  # Print to console
                        output_file.write(line)  # Save to file
                else:
                    line = f"IP: {ip} | Port: {port} | Service: {service} | Version: {version} | Vulnerabilities: None\n"
                    print(line.strip())  # Print to console
                    output_file.write(line)  # Save to file

        except shodan.APIError as e:
            error_msg = f"Error fetching {target}: {e}\n"
            print(error_msg.strip())  # Print to console
            output_file.write(error_msg)  # Save to file

print(f"\nResults saved to {output_file_path}")
