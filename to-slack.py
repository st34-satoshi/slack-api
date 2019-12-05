import requests


class SlackDriver:

    def __init__(self, _token):
        self._token = _token  # api_token
        self._headers = {'Content-Type': 'application/json'}

    def send_message(self, message, channel):
        params = {"token": self._token, "channel": channel, "text": message}

        r = requests.get('https://slack.com/api/chat.postMessage',
                          headers=self._headers,
                          params=params)
        print("return ", r.json())

    def get_channel_history(self, channel):
        # you need to use 'OAuth Access Token' not 'Bot User OAuth Access Token'
        # channel should be 'id' not 'name'
        params = {"token": self._token, "channel": channel}
        header = {'Content-Type': 'application/x-www-form-urlencoded'}

        r = requests.get('https://slack.com/api/channels.history',
                         headers=header,
                         params=params)
        print("return ", r.json())


if __name__ == '__main__':
    token = ''  # TODO your token.
    slack = SlackDriver(token)
    slack.send_message("Hello World! from python", "#random")
    slack.get_channel_history("xxxxx")  # channel should be ID not name
