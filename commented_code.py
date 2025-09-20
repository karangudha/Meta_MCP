# from typing import Any
# import httpx
# import logging
# import asyncio
# from mcp.server.fastmcp import FastMCP
# import os
# from dotenv import load_dotenv


# mcp = FastMCP("MyMetaAdsServer")
# logging.basicConfig(level=logging.INFO)
# load_dotenv()

# AD_ACCOUNT_ID=os.environ.get("META_APP_ID")
# APP_SECRET=os.environ.get("META_APP_SECRET")
# ACCESS_TOKEN = os.environ.get("META_ACCESS_TOKEN")
# META_API_BASE="https://graph.facebook.com/v21.0"
# # ACCESS_TOKEN="EAAXysYZBkedQBPXkKyNxQEaOs50ADs4ws2NUlOziQT15cRcMyeOyvjmOI7kiGJIXpDE5L3easXFR28kOpvKEcF7b70UStQLZCD5A6jpmfbyzSeFLxPobZBjZAhr46kpX3Xw8F2Rhs1AQlRnOb8T2rSOvwSPDpn5JZCyABhgqZCIlFoeYxZCDUGLO96nZC7IAGUjdM4i2VJzOIeagXi7SbHpMvZBLHLvpkO3B4a8QC3VWNUQZDZD"

# # How to get access token : login into meta app, required action, tools and give permisssion.
# # how i get this acount details : curl "https://graph.facebook.com/v20.0/me/adaccounts?access_token=<ACCESS_TOKEN>"
# # {
# #     "data":
# #     [
# #         {
# #             "account_id":"680771925065811",
# #             "id":"act_680771925065811" //this one i have to use for login
# #         }
# #     ],
# #     "paging":
# #     {
# #         "cursors":
# #         {
# #             "before":"MTIwMjMzODUzOTgwODYwMjMz",
# #         }
# #     }
# # }
# # For long live token :
# # GET https://graph.facebook.com/v20.0/oauth/access_token?grant_type=fb_exchange_token&client_id=act_680771925065811&client_secret=2478aa77a3b354c524ab667bd9cc7537&fb_exchange_token=EAAXysYZBkedQBPefTpvHe5vhJaoQxkvifzSpIRNHhdRYnr4goEWhN1wcfovcBu3rivPmfaBAzJcf4Vaf5R6hTSTpU6D9C6lZCacEqyNpCam3ek3A0vfTUh4NTxQy3AauRzjLBEQZAnABFFhIEPXoZAfhiOAuScZCyXZBu2u1c9b1JM82QW2KanX6GRq3EQZBM9ADeFVGghlVrOnA6nsrR9rHvLxK9xwl4AIiUC6jj4urwZDZD



# @mcp.tool()
# async def account_info() -> dict | None:
#     url = f"{META_API_BASE}/me/adaccounts"
#     params = {
#         "access_token": ACCESS_TOKEN,
#         "fields": "id, name, status, created_time, insights{impressions, clicks, spend}"
#     }
#     # async client make api call asynchronous
#     logging.info("calling to api")
#     async with httpx.AsyncClient() as client:
#         try: 
#             response = await client.get(url, params=params)
#             response.raise_for_status()
#             logging.info(f"response : {response.text}")
#             return response.json()
#         except Exception as e:
#             logging.error(f"Unexpected error: {e}")
#             return None
        
# # right now im working on just ot get info of user account, 
# # for this user dont need to send any thing any 
# # 
# # async def main():
# #     result = await account_info()
#     # logging.info(f"respone: " {result.text})
# if __name__ == "__main__":
#     # start mcp server and transport is comunication method, stdio is standard input/output
#     # mcp.run(transport='stdio')
#     # asyncio.run(main())

