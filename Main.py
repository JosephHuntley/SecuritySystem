from Notifications import send_notification 
import argparse

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Send a Pushover message.')
    # parser.add_argument('--config', default='config.ini', help='Path to the configuration file')
    parser.add_argument('--message', required=True, help='Message to be sent via Pushover')

    # Parse the command-line arguments
    args = parser.parse_args()


res = send_notification(args.message, "test", 1)

print(res.text)