from Notifications import send_notification 
from configparser import ConfigParser
import argparse

def load_config(file_path, section='credentials'):
    config = ConfigParser()
    config.read(file_path)
    return config[section]

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Send a Pushover message.')
    parser.add_argument('--config', default='config.ini', help='Path to the configuration file')
    parser.add_argument('--message', required=True, help='Message to be sent via Pushover')

    # Parse the command-line arguments
    args = parser.parse_args()

    config_data = load_config(file_path=args.config)

res = send_notification(config_data, args.message, "SecuritySystem", 1)

print(res.text)