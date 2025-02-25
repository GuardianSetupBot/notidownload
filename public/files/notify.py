import urllib.request
import json
from datetime import datetime

def send_discord_notification():
    webhook_url = "https://discord.com/api/webhooks/1340649381006807144/5QGYa6F1SSM86g_6YnUz15C56edl3cjM-hIjcTbtKfh1O7pZhjB1b51-igoWXP7N-Sno"
    
    # Create the message data
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        "content": f"Script was executed at {current_time}",
        "username": "Notification Bot"
    }
    
    # Convert data to JSON and encode as bytes
    json_data = json.dumps(data).encode('utf-8')
    
    # Create the request
    req = urllib.request.Request(
        webhook_url,
        data=json_data,
        headers={
            'Content-Type': 'application/json',
            'User-Agent': 'Python/DiscordWebhook'
        },
        method='POST'
    )
    
    # Send the request
    try:
        print("Attempting to send notification...")
        with urllib.request.urlopen(req) as response:
            print(f"Response status: {response.status}")
            if response.status == 204:
                print("Notification sent successfully!")
            else:
                response_data = response.read()
                print(f"Failed to send notification. Status code: {response.status}")
                print(f"Response: {response_data.decode('utf-8')}")
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
        print(f"Response: {e.read().decode('utf-8')}")
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
    except Exception as e:
        print(f"Error sending notification: {str(e)}")

if __name__ == "__main__":
    print("Starting notification script...")
    send_discord_notification()
    print("Script finished.")