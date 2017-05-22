#!/usr/bin/env python
import os
from configparser import ConfigParser
import argparse

GREEN = "\033[0;32m"
RESET = "\033[0;0m"


class Awsps(object):

    def __init__(self):
        self.user_home = os.path.expanduser('~')
        self.aws_credentials_file = os.path.join(
            self.user_home, '.aws/credentials')
        self.config = ConfigParser()
        self.config.read(self.aws_credentials_file)

    def clone_default_profile(self):
        profiles = self.config

        if 'default_awsps' not in self.config.sections():
            profiles['default_awsps'] = profiles['default']
            return profiles

        return profiles

    def list_profiles(self):
        print(GREEN + 'Available Profiles:')
        for i, item in enumerate(self.config.sections()):
            if i != 0:
                print(GREEN + '{}) {}'. format(i, item))
        print(RESET)
        return

    def get_current_profile(self):
        for item in self.config.sections():
            if (
                item != 'default' and
                self.config[item]['aws_access_key_id'] ==
                self.config['default']['aws_access_key_id'] and
                self.config[item]['aws_secret_access_key'] ==
                self.config['default']['aws_secret_access_key']
            ):
                print(GREEN + 'The current AWS profile is {}'.format(item))
        print(RESET)
        return

    def get_new_profile(self):
        temp = []
        for i, item in enumerate(self.config.sections()):
            if i != 0:
                temp.append(item)
                print(GREEN + '{}) {}'.format(i, item))
        idx = int(input("\nEnter profile to select: "))
        return temp[idx]

    def switch_profile(self, profile):
        content = self.clone_default_profile()
        content['default'] = content[profile]
        with open(self.aws_credentials_file, 'w') as confile:
            content.write(confile)
        print('\nProfile switched to {}'.format(profile))
        print(RESET)
        return


def main():
    parser = argparse.ArgumentParser(description='AWS Profile Switcher')
    parser.add_argument('-ls', '--list', action='store_true',
                        help='List available Profiles')
    parser.add_argument('-cp', '--current', action='store_true',
                        help='Get Current Profile')
    parser.add_argument('-sp', '--switch', action='store_true',
                        help='Switch AWS Profile')

    args = parser.parse_args()
    print(RESET)
    aps = Awsps()

    if args.list:
        aps.list_profiles()
    elif args.current:
        aps.get_current_profile()
    elif args.switch:
        aps.switch_profile(aps.get_new_profile())
    else:
        parser.parse_args(['-h'])


if __name__ == '__main__':
    main()
