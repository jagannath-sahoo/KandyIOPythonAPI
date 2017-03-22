import json as JSON
import requests

import Constants

class Groups:
    api_key = ''
    group_id = ''

    def __init__(self, api_key, group_id):
        self.api_key = api_key
        self.group_id = group_id

    def get_all_groups(self, give_json=False):

    def create_group(self, group_name, group_image, give_json=False):

    def get_group_by_id(self, give_json=False):

    def destory_group(self, give_json=False):

    def update_group(self, give_json=False):

    def add_members_to_group(self, members, give_json=False):

    def remove_members_from_group(self, give_json=False):

    def leave_group(self, give_json=False):

    def mute_unmute_group(self, mute, give_json=False):

    def mute_unmute_members(self, mute, give_json=False):

    def send_message(self, UUID, text, give_json=False):

    def group_chat_protocol_sending_message()