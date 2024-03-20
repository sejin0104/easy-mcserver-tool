import requests

def get_latest_stable_build(project, minecraft_version):
    api_url = f"https://api.papermc.io/v2/projects/{project}/versions/{minecraft_version}/builds"
    response = requests.get(api_url)
    response_json = response.json()
    builds = response_json.get('builds', [])
    if builds:
        stable_builds = [build['build'] for build in builds if build['channel'] == 'default']
        if stable_builds:
            return stable_builds[-1]
    return None

def download_latest_stable_build(project, minecraft_version):
    latest_version_url = f"https://api.papermc.io/v2/projects/{project}"
    latest_build_url = f"https://api.papermc.io/v2/projects/{project}/versions/{minecraft_version}/builds"
    
    latest_version_response = requests.get(latest_version_url)
    latest_version = latest_version_response.json().get('versions', [])[-1]
    
    latest_build_response = requests.get(latest_build_url)
    latest_builds = latest_build_response.json().get('builds', [])
    
    stable_build = None
    for build in latest_builds:
        if build['channel'] == 'default':
            stable_build = build['build']
            break
    
    if stable_build:
        jar_name = f"{project}-{latest_version}-{stable_build}.jar"
        papermc_url = f"https://api.papermc.io/v2/projects/{project}/versions/{latest_version}/builds/{stable_build}/downloads/{jar_name}"
        
        with open("server.jar", "wb") as f:
            response = requests.get(papermc_url)
            f.write(response.content)
        
        print("다운로드가 완료됐습니다.")
    else:
        print("빌드를 찾을 수 없습니다.")

# Example usage
PROJECT = "paper"
MINECRAFT_VERSION = "1.20.2"

latest_stable_build = get_latest_stable_build(PROJECT, MINECRAFT_VERSION)
if latest_stable_build:
    print(f"{PROJECT} 프로젝트의 마인크래프트 버전 {MINECRAFT_VERSION}의 마지막 빌드인 {latest_stable_build}를 다운로드 중입니다.")
    download_latest_stable_build(PROJECT, MINECRAFT_VERSION)
else:
    print("빌드를 찾을 수 없습니다.")