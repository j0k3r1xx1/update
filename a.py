import asyncio
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from pyppeteer import launch

async def run_pyppeteer(url):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)
    await page.screenshot({'path': 'screenshot.png'})
    await browser.close()

app = QApplication([])
window = QMainWindow()

webview = QWebEngineView(window)
webview.loadFinished.connect(lambda: asyncio.ensure_future(run_pyppeteer(webview.url().toString())))

window.setCentralWidget(webview)
window.show()

webview.load('https://www.google.com')

app.exec_()
