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
        page.goto(URL)

        page.wait_for_timeout(5000)

        text = page.inner_text("body")

        # 🔥 DEBUG: pošli část textu na Discord
        send("🔍 DEBUG START")
        send(text[:1500])  # první část stránky

        if "0.04" in text or "0.03" in text:
            send("🚨 DEAL FOUND!")

        browser.close()

check()
