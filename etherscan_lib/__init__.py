"""
Library for detecting potential exploiters
"""
# Imports
import requests
from bs4 import BeautifulSoup as BS

from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

# Function declarations
def get_labels(address: str) -> list:
    """Get labels deeming untrusworthiness (if any)"""
    url = f"https://etherscan.io/address/{address}"

    # Create User-Agent header (to avoid getting blocked)
    software_names = [SoftwareName.CHROME.value]
    operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
    user_agent_rotator = UserAgent(
        software_names=software_names, operating_systems=operating_systems, limit=100
    )
    user_agent = user_agent_rotator.get_random_user_agent()

    headers = {"User-Agent": user_agent}
    res = requests.get(url, headers=headers, timeout=15)

    if res.status_code != 200:
        return []

    # Parse labels
    soup = BS(res.text, "html.parser")
    a_tags = soup.find_all("a", href=True)

    labels = []
    for a_tag in a_tags:
        if "/accounts/label" in a_tag["href"]:
            label = a_tag["href"].split("/")[-1]
            labels.append(label)

    return labels
