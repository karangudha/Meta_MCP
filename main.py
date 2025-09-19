from mcp.server.fastmcp import FastMCP
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from dotenv import load_dotenv
import os
import asyncio


mcp = FastMCP("meta_ads_sdk")
load_dotenv()

APP_ID=os.environ.get("META_APP_ID")
APP_SECRET=os.environ.get("META_APP_SECRET")
ACCESS_TOKEN = os.environ.get("META_ACCESS_TOKEN")
FacebookAdsApi.init(app_id=APP_ID, app_secret=APP_SECRET, access_token=ACCESS_TOKEN)

@mcp.tool()
async def get_account():
    """find details of meta ad account using meta sdk"""
    try:
        accounts = AdAccount.get_my_account(fields=['id', 'name', 'account_status'])
        results = []
        for account in accounts:
            results.append({
                "id": account.get("id"),
                "name": account.get("name"),
                "status": account.get("account_status")
            })
        print(results)
        return results
    except Exception as e:
        return {"error": str(e)}

async def main():
    result = await get_account()
    print(result)

if __name__ == "__main__":
    # mcp.run(transport="stdio")
    asyncio.run(main())
