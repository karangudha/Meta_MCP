# Meta Ads MCP Server

This project integrates the **Meta Marketing API** with the **Model Context Protocol (MCP)** so you can fetch ad account data (impressions, clicks, spend, etc.) and use it with LLMs like **Claude**.

---

## ⚡ Features

* Connects to **Meta Ads Graph API** using an access token.
* Exposes a **Model Context Protocol (MCP)** server for seamless LLM integration.
* Fetches Ad Accounts and Insights (impressions, clicks, spend).
* Environment variable support with `.env`.

---
## Miro Link: https://miro.com/app/board/uXjVJGMa9ZQ=/


## 📦 Requirements

* Python 3.9+
* Meta Ads Access Token (from [Meta for Developers](https://developers.facebook.com/))

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Setup

1. Clone the repo:

   ```bash
   git clone https://github.com/karangudha/Meta_MCP.git
   cd Meta_MCP
   ```

2. Create a `.env` file in the project root:

   ```ini
   META_APP_ID=your_app_id
   META_APP_SECRET=your_app_secret
   META_ACCESS_TOKEN=your_long_lived_access_token
   ```

3. Run the server:

   ```bash
   python3 src.py
   ```

---

## 🛠 Usage

Once the server is running.
You’ll then add your servers in the mcpServers key. The MCP UI elements will only show up in Claude for Desktop if at least one server is properly configured.

```json
{
  "mcpServers": {
    "MyMetaAdsServer": {
      "command": "/ABSOLUTE/PATH/TO/PARENT/FOLDER/.venv/bin/python3",
      "args": [
        "/ABSOLUTE/PATH/TO/PARENT/FOLDER/src.py"
      ]
    }
  }
}
```

---

## 📂 Project Structure

```
.
├── src.py           # Main server script
├── requirements.txt # Python dependencies
├── .env             # Environment variables
└── README.md        # Documentation
```

---

## 🔑 Notes

* Ensure your **access token** has the required permissions (`ads_read`, `ads_management`).
* If using with Claude (or another MCP client), configure it to connect to this server via `stdio`.

---

## 📜 License

MIT License.
