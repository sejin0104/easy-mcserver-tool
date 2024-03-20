import requests
import json

def get_ip_info(output_format='json'):
    try:
        base_url = 'https://api.ip.pe.kr/'
        endpoint = base_url + 'json/' if output_format == 'json' else base_url + 'xml/'

        response = requests.get(endpoint)
    
        if response.status_code == 200:
            data = response.json() if output_format == 'json' else response.text
            return data
        else:
            print("Failed to fetch IP information.")
            return None
    except Exception as e:
        print("예상치 못한 오류가 발생했습니다, 개발자에게 문의해주세요.")

def display_ip_info(ip_info):
    if ip_info:
        if 'ip' in ip_info:
            print(f"Your IP address: {ip_info['ip']}")
        if 'country_code' in ip_info:
            print(f"국가 코드: {ip_info['country_code']}")
    else:
        print("확인 가능한 IP 주소가 없습니다")

# Fetch IP information and display it
ipv4_info = get_ip_info(output_format='json')

print("IPv4 정보:")
display_ip_info(ipv4_info)

