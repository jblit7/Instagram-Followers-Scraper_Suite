Instagram Graph API helper

Overview

This repository includes a small helper module at modules/IG_Graph.py to access the Instagram Graph API (official, compliant). Use it to fetch basic account metadata (followers_count, media_count, username, name).

Requirements

- An Instagram Business or Creator account connected to a Facebook Page
- A Facebook Graph API access token with instagram_basic (and other required) permissions
- The numeric IG user ID for the Instagram account (see below)

Quick start

1. Set environment variables (preferred):

   export IG_ACCESS_TOKEN="<YOUR_ACCESS_TOKEN>"
   export IG_USER_ID="<IG_USER_ID>"

2. In the repo root run:

   python3 -c "from modules.IG_Graph import print_account_summary; print_account_summary()"

This will print a short summary (username, followers, media count). The helper raises clear errors if credentials are missing.

Notes

- The Instagram Graph API is the legitimate way to access account metrics and perform approved automation for business/creator accounts. It does not support creating followers (that would be disallowed).
- To obtain an access token and IG user ID, follow Facebook's documentation for the Graph API and Instagram Basic Display / Instagram Graph API depending on your use case.

Security

Never commit access tokens to the repository. Use environment variables or a secrets manager.
