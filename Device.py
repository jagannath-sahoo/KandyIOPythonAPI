import Constants
import User
import requests
import json as JSON


class Device:
    device_id = None
    user_access_token = None

    def __init__(self, user_access_token, device_id):
        self.user_access_token = user_access_token
        self.device_id = device_id

    def upload_a_device_addressbook(self, contacts, give_json=False):
        """
        Upload a device address book
        :param contacts: Array of contacts information in json format
        :param give_json:Returns json object as in-built if true else Returns Json object as string
        :return:json response string or Object determined by give_json parameter to the method
        """
        url = Constants.BASE_URL + 'devices/addressbooks'
        requestbody = JSON.dumps({
            "device_id": self.device_id,
            "contacts": []
        })

        data = JSON.loads(requestbody)
        data["contacts"].append(contacts)
        requestbody = JSON.dumps(data)
        response = requests.post(url=url,
                                 params={'key': self.user_access_token, 'device_id': self.device_id}, json=requestbody)
        #print(respone)
        if give_json:
            return response.json()
        else:
            return response.text

    def get_device_addressbook(self, give_json=False):
        """
        Get address book of device with hints
        :param give_json:Returns json object as in-built if true else Returns Json object as string
        :return:json response string or Object determined by give_json parameter to the method
        """

        url = Constants.BASE_URL + 'devices/addressbooks'
        response = requests.get(url=url,
                                params={'key': self.user_access_token, 'device_id': self.device_id})

        if give_json:
            return response.json()
        else:
            return response.text

    def delete_device_addressbook(self, give_json=False):
        """
        Delete an address book of device
        :param give_json:Returns json object as in-built if true else Returns Json object as string
        :return:json response string or Object determined by give_json parameter to the method
        """

        url = Constants.BASE_URL + 'devices/addressbooks'
        response = requests.delete(url=url,
                                   params={'key': self.user_access_token, 'device_id': self.device_id})

        if give_json:
            return response.json()
        else:
            return response.text

    def get_hints_for_device_addressbook(self, give_json=False):
        """
        Get only hints from an address book of a device
        :param give_json:Returns json object as in-built if true else Returns Json object as string
        :return:json response string or Object determined by give_json parameter to the method
        """

        url = Constants.BASE_URL + 'devices/addressbooks/hints'
        response = requests.get(url=url,
                                params={'key': self.user_access_token, 'device_id': self.device_id})

        if give_json:
            return response.json()
        else:
            return response.text


Obj = User.User('DAK681759e27de4495f9085468bc44e6118', 'DASb0c21ef306f44f02912354b71627de9e')

respone = Obj.get_user_access_token('user1', True)

#respone["result"]["user_access_token"]

dev = Device(user_access_token=respone["result"]["user_access_token"],device_id='3d405f6dfd9842a981a90daaf0da08fa')

contact = {
      "firstName": "John",
      "lastName": "Doe",
      "numbers": ["+14055671234"]
    }

Resp = dev.upload_a_device_addressbook(contacts=contact)

{'result': {'user_access_token': 'UATabb5d109cccc493e8c8430a415c91c8c'},
 'message': 'success',
 'status': 0,
 'status_description': {'code': 2000, 'message': 'The request completed successfully'}
}
