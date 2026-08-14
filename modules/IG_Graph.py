import os
import requests


def get_account_info(access_token: str = None, ig_user_id: str = None, fields: str = None) -> dict:
    """Fetch Instagram Business/Creator account info via the Instagram Graph API.

    Requires a valid Facebook Graph API access token with the instagram_basic permission
    and the IG user ID (numeric) for the Instagram Business/Creator account.

    The function prefers environment variables IG_ACCESS_TOKEN and IG_USER_ID when
    parameters are omitted.

    Returns the parsed JSON response as a dict.
    Raises ValueError when required credentials are missing and requests.HTTPError for HTTP errors.
    """
    access_token = access_token or os.getenv("IG_ACCESS_TOKEN")
    ig_user_id = ig_user_id or os.getenv("IG_USER_ID")

    if not access_token or not ig_user_id:
        raise ValueError("IG_ACCESS_TOKEN and IG_USER_ID must be provided as parameters or env vars")

    if not fields:
        fields = "id,username,name,followers_count,media_count"

    url = f"https://graph.facebook.com/v17.0/{ig_user_id}"
    params = {"fields": fields, "access_token": access_token}

    resp = requests.get(url, params=params, timeout=15)
    resp.raise_for_status()
    return resp.json()


def print_account_summary(access_token: str = None, ig_user_id: str = None) -> None:
    """Convenience function to print a one-line summary about the IG account."""
    try:
        info = get_account_info(access_token, ig_user_id)
    except Exception as e:
        print(f"Error fetching account info: {e}")
        return

    username = info.get("username")
    name = info.get("name")
    followers = info.get("followers_count")
    media_count = info.get("media_count")

    print(f"Instagram account: {username} ({name})")
    print(f"Followers: {followers}")
    print(f"Media count: {media_count}")


if __name__ == "__main__":
    # Run as a small CLI: prints account summary using env vars if present
    print_account_summary()
