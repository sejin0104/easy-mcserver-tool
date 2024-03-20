import requests
import json

def get_ip_info(ip_version='ipv4', output_format='json'):
    base_url = 'https://api.ip.pe.kr/'

    if ip_version == 'ipv4':
        endpoint = base_url + 'json/' if output_format == 'json' else base_url + 'xml/'
    elif ip_version == 'ipv6':
        endpoint = base_url + 'json/' if output_format == 'json' else base_url + 'xml/'
    else:
        print("Invalid IP version specified.")
        return

    response = requests.get(endpoint)
    
    if response.status_code == 200:
        data = response.json() if output_format == 'json' else response.text
        return data
    else:
        print("Failed to fetch IP information.")
        return None

def display_ip_info(ip_info):
    if ip_info:
        if 'ip' in ip_info:
            print(f"Your IP address: {ip_info['ip']}")
        if 'country_code' in ip_info:
            print(f"Country Code: {ip_info['country_code']}")
        if 'country_name' in ip_info:
            print("Country Name:")
            for lang, name in ip_info['country_name'].items():
                print(f"  - {lang}: {name}")
    else:
        print("No IP information available.")

# Fetch IP information and display it
ipv4_info = get_ip_info(ip_version='ipv4', output_format='json')
ipv6_info = get_ip_info(ip_version='ipv6', output_format='json')

print("IPv4 Information:")
display_ip_info(ipv4_info)

print("\nIPv6 Information:")
display_ip_info(ipv6_info)
