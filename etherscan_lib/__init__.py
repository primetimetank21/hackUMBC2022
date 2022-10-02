"""
Library for detecting potential exploiters
"""
# HEIST_URL = "https://etherscan.io/accounts/label/heist"
import requests
from bs4 import BeautifulSoup as BS

from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem


def get_labels(address: str):
    """Get labels deeming untrusworthiness (if any)"""
    url = f"https://etherscan.io/address/{address}"

    software_names = [SoftwareName.CHROME.value]
    operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
    user_agent_rotator = UserAgent(
        software_names=software_names, operating_systems=operating_systems, limit=100
    )
    user_agent = user_agent_rotator.get_random_user_agent()
    headers = {"User-Agent": user_agent}
    req = requests.get(url, headers=headers, timeout=15)
    # print(req.headers)
    soup = BS(req.text, "html.parser")
    a_tags = soup.find_all("a", href=True)
    with open("user.txt", "w", encoding="utf-8") as f:
        f.write(str(a_tags))
    labels = []
    for a_tag in a_tags:
        if "/accounts/label" in a_tag["href"]:
            label = a_tag["href"].split("/")[-1]
            labels.append(label)
    return labels
