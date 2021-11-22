import os
import sys
import httpx
import asyncio
import logging
from tasksio import TaskPool

logging.basicConfig(
    level=logging.INFO,
    format="\u001b[36;1m[\u001b[0m%(asctime)s\u001b[36;1m]\u001b[0m %(message)s\u001b[0m",
    datefmt="%H:%M:%S"
)

class TikTok(object):

    def __init__(self):
        if sys.platform == "linux":
            os.system("clear")
        else:
            os.system("cls && title [TikTok Autoclaimer] github.com/dropout1337")

        self.attempts = 0
        self.checking = True
        self.first_req = True

        self.webhook = input("\u001b[36;1m[\u001b[0m?\u001b[36;1m]\u001b[0m Webhook \u001b[36;1m->\u001b[0m ")
        self.nickname = input("\u001b[36;1m[\u001b[0m?\u001b[36;1m]\u001b[0m Nickname \u001b[36;1m->\u001b[0m ")
        self.signature = input("\u001b[36;1m[\u001b[0m?\u001b[36;1m]\u001b[0m Signature \u001b[36;1m->\u001b[0m ")

        self.target = input("\u001b[36;1m[\u001b[0m?\u001b[36;1m]\u001b[0m Target \u001b[36;1m->\u001b[0m ")
        self.session_id = input("\u001b[36;1m[\u001b[0m?\u001b[36;1m]\u001b[0m Session ID \u001b[36;1m->\u001b[0m ")
        self.x_token = input("\u001b[36;1m[\u001b[0m?\u001b[36;1m]\u001b[0m X-Token \u001b[36;1m->\u001b[0m ")
        self.threads = int(input("\u001b[36;1m[\u001b[0m?\u001b[36;1m]\u001b[0m Threads \u001b[36;1m->\u001b[0m "))

        print()

    async def _webhook(self):
        payload = {
        "username": "TikTok Autoclaimer",
        "avatar_url": "https://lf16-tiktok-common.ibytedtos.com/obj/tiktok-web-common-sg/mtact/static/images/share_img.png",
        "embeds": [
            {
                "description": "Successfully claimed %s after %s requests" % (self.target, self.attempts),
                "color": 0xf62b52,
                "thumbnail": {
                    "url": "https://i.pinimg.com/originals/20/4e/29/204e292ca1547703c2af07bdfd893ab6.png"
                }
                }
            ]
        }
        if not self.webhook == "":
            try:
                async with httpx.AsyncClient() as client:
                    await client.post(self.webhook, json=payload)
            except Exception:
                pass

    async def _update(self):
        query = {
            "iid":"7025240856680744710",
            "device_id":"6906478625937278469",
            "ac":"wifi",
            "channel":"googleplay",
            "aid":"1233",
            "app_name":"musical_ly",
            "version_code":"210605",
            "version_name":"21.6.5",
            "device_platform":"android",
            "ab_version":"21.6.5",
            "ssmix":"a",
            "device_type":"A5010",
            "device_brand":"OnePlus",
            "language":"en",
            "os_api":"25",
            "os_version":"7.1.2",
            "openudid":"c0575264c704f9c6",
            "manifest_version_code":"2022106050",
            "resolution":"1280*720",
            "dpi":"240",
            "update_version_code":"2022106050",
            "_rticket":"1635699028787",
            "current_region":"US",
            "app_type":"normal",
            "sys_region":"US",
            "mcc_mnc":"31031",
            "timezone_name":"Asia/Shanghai",
            "residence":"US",
            "ts":"1635699032",
            "timezone_offset":"28800",
            "build_number":"21.6.5",
            "region":"US",
            "uoo":"0",
            "app_language":"en",
            "carrier_region":"US",
            "locale":"en",
            "op_region":"US",
            "ac2":"wifi",
            "cdid":"c7486e9b-720c-4c53-b01e-b48e1627212c",
            "support_webview":"1",
            "okhttp_version":"4.0.61.8-tiktok"
        }
        payload = "signature=%s&nickname=%s&confirmed=0&uid=7026441925374657583&page_from=0" % (self.signature, self.nickname)
        headers = {
            "x-ss-stub": "42DC863028F620DC41672CD338EB44A4",
            "accept-encoding": "gzip",
            "passport-sdk-version": "19",
            "sdk-version": "2",
            "x-tt-multi-sids": "7025753269597127726%3Adfcf3163978d7473f4265b7985a97c8b%7C6878277293988398082%3A244ead388a50153c26ac6fc1acc952cf%7C6798526938606273542%3A22ffb97374208354f611434830978268%7C7026142094618723374%3A2ba5159cd3831bb558b0d2b9e6956d2d%7C7026413601490617390%3A0baebad63036d3d61d7299db3e405ca5%7C7026419283280331822%3A2b9d3689fc25bdd2a31eb5f9986895c0",
            "x-tt-token": self.x_token,
            "multi_login": "1",
            "x-ss-req-ticket": "1635969272581",
            "x-bd-client-key": "#Rzymagg36Y5cBIsrKQVP4afsyk58gCfUIKoRifwyk0hpXouT5vJYFruOdYbI34RHdv8dom3KGjMPJCRQ",
            "x-bd-kmsv": "0",
            "x-vc-bdturing-sdk-version": "2.1.0.i18n",
            "x-tt-dm-status": "login=1;ct=1rt=1",
            "x-tt-cmpl-token": "AgQQAPNSF-RPsLG8NbvG090XxbkkhHRO_4fZYMOUng",
            "x-tt-store-idc": "maliva",
            "x-tt-store-region": "us",
            "x-tt-store-region-src": "uid",
            "user-agent": "com.zhiliaoapp.musically/2022107090 (Linux; U; Android 7.1.2; en_US; A5010; Build/N2G48H;tt-ok/3.10.0.2)",
            "cookie": "sessionid=%s" % (self.session_id),
            "x-tt-passport-csrf-token": self.session_id,
            "x-ladon": "cz9ecBKrtwxN1+X3z7aoUiUDuxNDEuj0RHFnT+JAHadKAF5K",
            "x-gorgon": "0404e0924005cc3f5647c07af65bfe3c96bebe12f47d79753870",
            "x-khronos": "1635969272",
            "x-argus": "TwNbYJjqKLgLkeAm4oPdfvHLyLQSIcmtbB/y68LCkl9UTFJ3OywZaUx5CQcv3fAwp7T7+wZIKs9z8LsJ3ss1ADanZj/BhytTS08tpkiOtm3JT7JExg9sMxI4cB5axU34IxuvI7HWrcqCt6xESX3tpr1SalM7iOyDyk7a4YVELtbxOsbixiYgc1OMQNJnF4ekmzcCHVBkzl4aXspjK3D5BPc/sWJ3FNj0vHUI8nv+rhLDPKD69YRbPAjLppF2FSw1u04RVCRN4vnWGKmhX0OQFScW+nas+noQH2Glr6etJwXus+5X+ahJMaq3n9NU+LHCaM5ZAvmD0DEvxtWN9TNRAynoShF6l2A+IXZUTvtU+UHYHw==",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "host": "api22-normal-c-useast1a.tiktokv.com",
            "connection": "Keep-Alive"
        }
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post("https://api22-normal-c-useast1a.tiktokv.com/aweme/v1/commit/user/", data=payload, headers=headers, params=query)
                if not "nickname" in response.text:
                    logging.error("Invalid session/x-token specified.")
                    sys.exit()
                else:
                    logging.info("Successfully logged into %s" % (response.json()["user"]["unique_id"]))
        except Exception:
            pass

    async def _claim(self):
        query = {
            "iid":"7025240856680744710",
            "device_id":"6906478625937278469",
            "ac":"wifi",
            "channel":"googleplay",
            "aid":"1233",
            "app_name":"musical_ly",
            "version_code":"210605",
            "version_name":"21.6.5",
            "device_platform":"android",
            "ab_version":"21.6.5",
            "ssmix":"a",
            "device_type":"A5010",
            "device_brand":"OnePlus",
            "language":"en",
            "os_api":"25",
            "os_version":"7.1.2",
            "openudid":"c0575264c704f9c6",
            "manifest_version_code":"2022106050",
            "resolution":"1280*720",
            "dpi":"240",
            "update_version_code":"2022106050",
            "_rticket":"1635699028787",
            "current_region":"US",
            "app_type":"normal",
            "sys_region":"US",
            "mcc_mnc":"31031",
            "timezone_name":"Asia/Shanghai",
            "residence":"US",
            "ts":"1635699032",
            "timezone_offset":"28800",
            "build_number":"21.6.5",
            "region":"US",
            "uoo":"0",
            "app_language":"en",
            "carrier_region":"US",
            "locale":"en",
            "op_region":"US",
            "ac2":"wifi",
            "cdid":"c7486e9b-720c-4c53-b01e-b48e1627212c",
            "support_webview":"1",
            "okhttp_version":"4.0.61.8-tiktok"
        }
        payload = "uid=7025085796388963374&login_name=%s&page_from=0" % (self.target)
        headers = {
            "x-ss-stub": "42DC863028F620DC41672CD338EB44A4",
            "accept-encoding": "gzip",
            "passport-sdk-version": "19",
            "sdk-version": "2",
            "x-tt-multi-sids": "7025753269597127726%3Adfcf3163978d7473f4265b7985a97c8b%7C6878277293988398082%3A244ead388a50153c26ac6fc1acc952cf%7C6798526938606273542%3A22ffb97374208354f611434830978268%7C7026142094618723374%3A2ba5159cd3831bb558b0d2b9e6956d2d%7C7026413601490617390%3A0baebad63036d3d61d7299db3e405ca5%7C7026419283280331822%3A2b9d3689fc25bdd2a31eb5f9986895c0",
            "x-tt-token": self.x_token,
            "multi_login": "1",
            "x-ss-req-ticket": "1635969272581",
            "x-bd-client-key": "#Rzymagg36Y5cBIsrKQVP4afsyk58gCfUIKoRifwyk0hpXouT5vJYFruOdYbI34RHdv8dom3KGjMPJCRQ",
            "x-bd-kmsv": "0",
            "x-vc-bdturing-sdk-version": "2.1.0.i18n",
            "x-tt-dm-status": "login=1;ct=1rt=1",
            "x-tt-cmpl-token": "AgQQAPNSF-RPsLG8NbvG090XxbkkhHRO_4fZYMOUng",
            "x-tt-store-idc": "maliva",
            "x-tt-store-region": "us",
            "x-tt-store-region-src": "uid",
            "user-agent": "com.zhiliaoapp.musically/2022107090 (Linux; U; Android 7.1.2; en_US; A5010; Build/N2G48H;tt-ok/3.10.0.2)",
            "cookie": "sessionid=%s" % (self.session_id),
            "x-tt-passport-csrf-token": self.session_id,
            "x-ladon": "cz9ecBKrtwxN1+X3z7aoUiUDuxNDEuj0RHFnT+JAHadKAF5K",
            "x-gorgon": "0404e0924005cc3f5647c07af65bfe3c96bebe12f47d79753870",
            "x-khronos": "1635969272",
            "x-argus": "TwNbYJjqKLgLkeAm4oPdfvHLyLQSIcmtbB/y68LCkl9UTFJ3OywZaUx5CQcv3fAwp7T7+wZIKs9z8LsJ3ss1ADanZj/BhytTS08tpkiOtm3JT7JExg9sMxI4cB5axU34IxuvI7HWrcqCt6xESX3tpr1SalM7iOyDyk7a4YVELtbxOsbixiYgc1OMQNJnF4ekmzcCHVBkzl4aXspjK3D5BPc/sWJ3FNj0vHUI8nv+rhLDPKD69YRbPAjLppF2FSw1u04RVCRN4vnWGKmhX0OQFScW+nas+noQH2Glr6etJwXus+5X+ahJMaq3n9NU+LHCaM5ZAvmD0DEvxtWN9TNRAynoShF6l2A+IXZUTvtU+UHYHw==",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "host": "api22-normal-c-useast1a.tiktokv.com",
            "connection": "Keep-Alive"
        }
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post("https://api22-normal-c-useast1a.tiktokv.com/passport/login_name/update/", data=payload, headers=headers, params=query)
                if "success" in response.text:
                    logging.info("Successfully claimed \u001b[36;1m(\u001b[0m%s\u001b[36;1m)\u001b[0m" % (self.target))
                    await self._webhook()
                    sys.exit()
                else:
                    logging.error("%s \u001b[36;1m(\u001b[0m%s\u001b[36;1m)\u001b[0m" % (response.json()["data"]["description"], self.target))
                    sys.exit()
        except Exception:
            logging.error("Unable to claim \u001b[36;1m(\u001b[0m%s\u001b[36;1m)\u001b[0m" % (self.target))
            sys.exit()

    async def _worker(self):
        while True:
            headers = {
                "Host": "api19-normal-c-useast1a.tiktokv.com",
                "Connection": "keep-alive",
                "x-Tt-Token": "012a6b6d6f0ca859868c920bed0fbc89de00dc324a56c811a80996dd798c7aa36503752930344e7b10db7fed42a72a4149da3907477f89775bfae0244a20fe48ef254133b42c049f24deb2121b9197cd17e8c-1.0.0",
                "sdk-version": "2",
                "User-Agent": "com.zhiliaoapp.musically/2022106020 (Linux; U; Android 7.1.2; en_US; Build/N2G48H;tt-ok/3.10.0.2)",
                "x-tt-store-idc": "alisg",
                "x-tt-store-region": "de",
                "Accept-Encoding": "gzip, deflate"
            }
            try:
                async with httpx.AsyncClient() as client:
                    response = await client.get("https://api19-normal-c-useast1a.tiktokv.com/aweme/v1/unique/id/check/?unique_id=%s&iid=7026260912928425734&device_id=7026260845073188357&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=210602&version_name=21.6.2&device_platform=android&ab_version=21.6.2&ssmix=a&device_type=SM-N975F&device_brand=samsung&language=en&os_api=25&os_version=7.1.2&openudid=f0bfccc997a123b5&manifest_version_code=2022106020&resolution=720*1280&dpi=240&update_version_code=2022106020&_rticket=1636035582804&current_region=NZ&app_type=normal&sys_region=US&mcc_mnc=53001&timezone_name=Asia Shanghai&residence=NZ&ts=1636035582&timezone_offset=28800&build_number=21.6.2&region=US&uoo=0&app_language=en&carrier_region=NZ&locale=en&op_region=NZ&ac2=wifi&cdid=8a438d2e-2dea-4dc4-b7a9-ffa83828570e" % (self.target), headers=headers, timeout=5)
                    self.attempts += 1
                    if not self.attempts % 100: logging.info("Sent %s request attempts" % (self.attempts))

                    if "is_valid" in response.text:
                        if response.json()["is_valid"]:
                            self.checking = False
                            return await self._claim()
            except Exception:
                pass

    async def start(self):
        logging.info("Starting autoclaimer!")
        await self._update()
        async with TaskPool(self.threads) as pool:
            while self.checking:
                await pool.put(self._worker())

if __name__ == "__main__":
    client = TikTok()
    asyncio.get_event_loop().run_until_complete(client.start())
