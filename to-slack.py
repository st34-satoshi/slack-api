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


if __name__ == '__main__':
    token = ''  # TODO your token.
    slack = SlackDriver(token)
    slack.send_message("Hello World! from python", "#random")
