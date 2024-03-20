import requests
import json
import socket

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

def get_internal_ip():
    internal_ip = None
    try:
        internal_ip = socket.gethostbyname(socket.gethostname())
    except:
        internal_ip = "(내부 아이피를 가져올수 없습니다.)"
    return internal_ip

def display_ip_info(ip_info):
    if ip_info:
        if 'ip' in ip_info:
            print(f"공인 아이피: {ip_info['ip']}")
        if 'country_code' in ip_info:
            print(f"국가 코드: {ip_info['country_code']}")
    else:
        print("확인 가능한 IP 주소가 없습니다")
        
def how_to_join(ip_info):
    print('당신이 서버장이라면 localhost로 접속을 하시면 됩니다.')
    print('접속자가 같은 인터넷망 혹은 VPN(Hamachi etc...)을(를) 통한 같은 인터넷 사용시')
    print(f'{get_internal_ip()}:25565 로 접속하시면 됩니다.')
    print('접속자가 다른 인터넷망을 사용중이라면 먼저 25565로 포트포워딩을 해야합니다.')
    print(f'그다음 접속자는 서버를 {ip_info['ip']}:25565로 접속하면 됩니다.')

# Fetch IP information and display it
ipv4_info = get_ip_info(output_format='json')

print("IPv4 정보:")
display_ip_info(ipv4_info)

print('서버 접속방법:')
how_to_join(ipv4_info)

