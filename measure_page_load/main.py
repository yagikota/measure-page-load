from selenium import webdriver
from browsermobproxy import Server

if __name__ == "__main__":
    proxy_path = "/Users/kota/sandbox_python/measure_page_load/browsermob-proxy-2.1.4/browsermob-rest-2.1.4-javadoc.jar"
    server = Server(proxy_path)
    server.start()
    proxy = server.create_proxy()

    profile = webdriver.FirefoxProfile()
    profile.set_proxy(proxy.selenium_proxy())
    driver = webdriver.Firefox(firefox_profile=profile)
    proxy.new_har("google")
    driver.get("http://www.google.com")
    har = proxy.har  # returns a HAR JSON blob
    print(har)
    server.stop()
    driver.quit()

# from browsermobproxy import Server
# from selenium import webdriver
# import json
# from pathlib import Path
# import time


# class GetWebPageHar:
#     proxy_path = "browsermob-proxy-2.1.4/bin/browsermob-proxy"

#     def __init__(self):
#         self.server = Server(str(Path(self.proxy_path).absolute()))
#         self.server.start()
#         self.proxy = self.server.create_proxy()

#     def get_har(self, url, output_filename):
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_argument("--proxy-server={0}".format(self.proxy.proxy))
#         chrome_options.add_argument("--ignore-certificate-errors")
#         chrome_options.add_argument("--incognito")
#         driver = webdriver.Chrome(chrome_options=chrome_options)

#         self.proxy.new_har("google")
#         driver.get(url)
#         time.sleep(10)
#         har_json = json.dumps(self.proxy.har, indent=4, ensure_ascii=False)
#         with open(output_filename, "w") as f:
#             f.write(har_json)
#         driver.quit()

#     def stop(self):
#         self.server.stop()


# if __name__ == "__main__":
#     getter = GetWebPageHar()
#     getter.get_har("https://www.google.com", "test_har.json")
#     getter.stop()


# from selenium import webdriver
# from browsermobproxy import Server
# from selenium.webdriver.chrome.options import Options
# import json

# # Firefoxドライバーを起動
# options = Options()
# # options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-gpu')
# options.add_argument('--ignore-certificate-errors')
# driver = webdriver.Chrome(options=options)

# # browsermob-proxyを起動
# proxy_path = "/Users/kota/sandbox_python/measure_page_load/browsermob-proxy-2.1.4/bin/browsermob-proxy"
# server = Server(proxy_path)
# server.start(options={'port': 50000})
# proxy = server.create_proxy()

# # ブラウザをプロキシサーバーに接続
# proxy.new_har("page")
# driver.get("https://www.example.com")

# # HARファイルを取得
# har = proxy.har

# # ブラウザを終了し、プロキシサーバーを停止
# driver.quit()
# server.stop()

# # HARファイルを保存
# with open("example.har", "w") as har_file:
#     har_file.write(json.dumps(har, indent=4))


# from selenium import webdriver

# # Configure the browser with the desired options
# options = webdriver.ChromeOptions()
# options.add_argument("--disable-extensions")
# options.add_argument("--disable-popup-blocking")
# options.add_argument("--disable-infobars")

# # Start the browser and navigate to the target URL
# browser = webdriver.Chrome(chrome_options=options)
# browser.get("https://www.youtube.com/")

# # Collect the HAR file
# har = browser.execute_cdp_cmd("Network.enable", {})
# result = browser.execute_cdp_cmd("Network.getAllCookies", {})
# print(result["cookies"])
# result = browser.execute_cdp_cmd("Network.getResponseBody", {"requestId": "xyz"})
# print(result["body"])
# result = browser.execute_cdp_cmd("Network.disable", {})
# print(har)

# # https://www.selenium.dev/ja/documentation/webdriver/bidirectional/chrome_devtools/#collect-performance-metrics
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get('https://www.youtube.com/')
# driver.execute_cdp_cmd('Performance.enable', {})
# # driver.execute_cdp_cmd('PerformanceTimeline.enable', {})
# # driver.execute_cdp_cmd("Network.enable", {})
# # rr = driver.execute_cdp_cmd("Network.getResponseBody", {})
# # m = driver.execute_cdp_cmd('Performance.metrics', {})
# t = driver.execute_cdp_cmd('Performance.getMetrics', {})
# print(t)
# driver.quit()
