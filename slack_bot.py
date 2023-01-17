from datetime import datetime

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


channel_id="stock-auto"
message=''


def send_to_slack(channel_id, message):
    token="my_token"
    client = WebClient(token=token)

    now = datetime.now().strftime('[%Y/%m/%d %H:%M:%S] ')

    try :
        response = client.chat_postMessage(channel=channel_id, text=f'{now} - {message}')
    except SlackApiError as e:
        print(f'Error: {e.response.error}')


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="SlackBot")
    
    parser.add_argument("-c", "--channel_id", help="Enter the channel ID you want to send")
    parser.add_argument("-m", "--message", help="Enter the Message you want to send")
    
    args = parser.parse_args()

    send_to_slack(args.channel_id, args.message)
