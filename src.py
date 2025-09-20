from typing import Any
import httpx
import logging
import asyncio
from mcp.server.fastmcp import FastMCP
import os
from dotenv import load_dotenv
load_dotenv()


logging.basicConfig(level=logging.INFO)

PORT=os.environ.get("PORT")
AD_ACCOUNT_ID=os.environ.get("META_APP_ID")
APP_SECRET=os.environ.get("META_APP_SECRET")
ACCESS_TOKEN = os.environ.get("META_ACCESS_TOKEN")
META_API_BASE="https://graph.facebook.com/v21.0"

mcp = FastMCP("MyMetaAdsServer", host="0.0.0.0", port=PORT)
# How to get access token : login into meta app, required action, tools and give permisssion.
# how i get this acount details : curl "https://graph.facebook.com/v20.0/me/adaccounts?access_token=<ACCESS_TOKEN>"
# {
#     "data":
#     [
#         {
#             "account_id":"111111111111111",
#             "id":"act_111111111111111" //this one use for login
#         }
#     ],
#     "paging":
#     {
#         "cursors":
#         {
#             "before":"",
#         }
#     }
# }
# For long live token :
# GET https://graph.facebook.com/v20.0/oauth/access_token?grant_type=fb_exchange_token&client_id=<client_id>&client_secret=<secret>&fb_exchange_token=<accesstoken>



@mcp.tool()
async def account_info() -> dict | None:
    url = f"{META_API_BASE}/me/adaccounts"
    params = {
        "access_token": ACCESS_TOKEN,
        "fields": "id, name, status, created_time, insights{impressions, clicks, spend}"
    }
    # async client make api call asynchronous
    logging.info("calling to api")
    async with httpx.AsyncClient() as client:
        try: 
            response = await client.get(url, params=params)
            response.raise_for_status()
            logging.info(f"response : {response.text}")
            return response.json()
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            return None
        

if __name__ == "__main__":
    # start mcp server and transport is comunication method, stdio is standard input/output
    mcp.run(transport="streamable-http")

