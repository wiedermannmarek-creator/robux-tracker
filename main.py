import os
import requests
from playwright.sync_api import sync_playwright

URL = "https://www.eldorado.gg/buy-robux/og/10664367-9c80-4640-abf2-08de89a1b9dd?offerSortingCriterion=Cheapest"
WEBHOOK = os.getenv("WEBHOOK")

def send(msg):
    requests.post(WEBHOOK, json={"content": msg})

def check():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(URL, timeout=60000)

        page.wait_for_timeout(5000)

        content = page.content()

        # ⚠️ jednoduchý hack parsing (funguje i bez přesných selectorů)
        text = page.inner_text("body")

        # pokus o extrakci čísel (zjednodušené)
        if "0.04" in text or "0.03" in text:
            send(f"🚨 POTENCIÁLNÍ DEAL!\n{URL}")

        browser.close()

if __name__ == "__main__":
    check()
