from bs4 import BeautifulSoup
import requests


def fetch_webpage(url: str) -> str:
    requests.get(url=url)
