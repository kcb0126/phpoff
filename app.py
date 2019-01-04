import requests

payload = (
  ("utf8", "✓"),
  ("_method", "patch"),
  ("authenticity_token", "Q2cj4QPQd78IOXPGxyLQpULC2jZkt4J4a6n1lAc2NeI="),
  ("order[terms_and_conditions]", "yes"),
#  ("order[terms_and_conditions]", "yes"),
  ("commit", "Save+and+Continue")
)
r = requests.post(
  "https://www.off---white.com/en/IT/checkout/update/address",
  headers={
#    "Cache-Control": "max-age=0",
#    "Origin": "https://www.off---white.com",
#    "Upgrade-Insecure-Requests": "1",
#    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#    "Referer": "https://www.off---white.com/en/IT/checkout/address",
#    "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
#    "Cookie": "__cfduid=dd732fb1c2a3c0634608e0480c89767ed1545601344; __uzmb=1545601345; __uzma=5411639220101131938; guest_token=IktmaXJhUFlvd1RaamhaMlc0Tlg3ekEi--250673f2248c8d93b69b4e71b9422802a2e89699; dismiss_cookie_law=true; __riskifiedBeaconSessionId=ffbbb48d-20fe5ec5-43d2e532-e487ef76-787a2864-9c5f0606; remember_spree_user_token=W1sxMTY0NjFdLCJ6enZEaUdpMnM2amF4ejgzUzFHZCIsIjE1NDU2MDEzNjkuMDQ1MDYyNSJd--823ea3168f68e96cdb83f1a0bafbe49438e29a79; __uzmd=1546456834; __uzmc=21117192493355; _hs_session_v4=MHpEdE1ka0hIUUhUZ0h3WkYxM3BaSmFTUElYQ3pINFk4N1pqY09sZFpzN3MvVHdxV3NaQkZmdDBDUkNXbU1YTyt3SWMveEhPUzdyMlk0QzFmRkJIb1BUc3BEYUx6UWpDck8weEUwRjRWMVc1a2MyRkN0Vm5ZOU1ESm5KTG9DQ1dCL0lnMU5SbkcrWmFCVU1nU0h6dmxqM3ZiSXRCUnp0bVZLTmFTK210OU8yUFNEbVdrWHVtNktVUGpMemRuaVNBWlQwcG5ZNkJIamdOL0hpK3FzS0VYaHRxL3VpK05EUG92cFI2L3pLaWticVZ2djIyekxpRGdHTUZpOG1BMFNDb1F2dTVNK1k3c2dqVkJkb1F6RElpbit3b09KSVdJWlNHRlQ2bHF2czV6R3VveUZiQUhSeHlBbHhGQ2pOMG9qemFoR3Q3OGhCT2tXbUF2UVlPMyttRHlNVWhTRXhMYStyYWpxdlU2eitUVG8xdUtrem45MUI2Y21JRm41K05iUFZyUHF5TFNxczllajJTMSttM3JHcFY3RURSUmtaZnAvbUJMMEY2bGk2MXgvVjhmT2pFT1prWWhkWmplRVBTVE9xS1E4eklsOVdTRTk1bmpFTm1HLzhXOTZ4azhDakFBbTU1WEg0UytVR3lvMytEbVoxbzFIdXlrYW9maCtEWUFrcCs5MDZqRWpNdWNnb011UU11a29TZTZBMmZHbVNrZ0hDanlQajJmTk5ENFhsWFU4RmJnUEk5cWZrdHpiQlZvV3NKRTkzaTVTK3RNWXR1U2taMU9LZU4xR1VwV01sSS96RHpFUjBxb0lXdHdlRmRCa0Nad0pTakovU2pkT0dKYzBGZFhXN29BdVFnbW9WUXBPaFk2Myswd1EwaGQ0OUZNWUhUeXMrckcyalVGWVlYM2VoaUJkMG5NSGE1RWxiTFd1eWlYaVFoeVBPcWJQUkdzcnE5L0dEL3B6THNETzR5eHhNRWtxMnZsc0taVWM1U3BFbnhaY2pPQk9uNFZzRm12WXVYeDRQQXhMRmQ1cnM2N3diblBYN0JNclczdkU3cTYrOXNPZEFidGdCRklPK3M3SGpoekVaYnloZDdNZzlWVXF0TURTVlBmTVYxMDFEUjRyN0VuYnlHc1M2MDQxdzVPcXd6SWhwUzAyWE8xdU1DcXY0V2lHdzZ5ZDM5OThkclVqZDAwdC9jMGFmejBPb29pYjMvRk1VNkI1bTc1Z0dxdW50VDE1NFZONm0vb3dCdWlQSnJpdkd0bzNuTHlEZXpTYTc0MytJUTIvcGtyeDJTblNQNVFKdHJFYkp6TnBwdVJ6dllON3ZJMnVpUlVtOVFBeW1tYVc0OXhjRUdlRHF5bEFsaWRsMjJtOHZEdFhWc0NGRWM2MW5JakR0SFNSZk1USGNXUU8xTndIME9hY2UvWnB2c0x6WXFQOWI2dS83b0t4RmpkdHRyS2pqQWVtdVVva21PZitPcENZMGtLdnNuZmowR2x6WUJXdGZNVGtnSmNNRFFmOGZpT285MTYxM1Y1Y0ZZS3h1Z1E5ZmNHRkZrN0lIUmtoUzRxcks3dWJGaVdlZ3ZoeFk5c283UkpzeHY4anVlSHg5ZzNFNHZBODRSRFVDa2xqc1QxQU1iMkltamRlL0Uyenh0YlE9PS0tYjRGM2htMDUvczQxOEM5WERlWlVMdz09--32a4d60e6aa9511e2d04326c496bda0e145bcb24"
  },
  data=payload
)

f = open("output.html", "w")
f.write(r.text)
f.close()
