import requests


class SlackDriver:

    def __init__(self, _token):
        self._token = _token  # api_token
        self._headers = {'Content-Type': 'application/json'}

    def send_message(self, message, channel, thread_ts=None):
        if thread_ts is None:
            params = {"token": self._token, "channel": channel, "text": message}
        else:
            params = {"token": self._token, "channel": channel, "text": message, "thread_ts": thread_ts}

        r = requests.post('https://slack.com/api/chat.postMessage',
                          headers=self._headers,
                          params=params)
        print("return ", r.json())
        ts = r.json()['ts']  # get thread id of sent message
        print(ts)

    def send_image(self, file_path, message, channel):
        files = {'file': open(file_path, 'rb')}
        params = {"token": self._token, 'channels': channel, 'initial_comment': message}
        # headers = {'Content-Type': 'multipart/form-data'}  # invalid_form_data if you use headers

        r = requests.post('https://slack.com/api/files.upload',
                          params=params,
                          files=files)
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
    # slack.send_image("image.png", "This is the comment of the image", "#random")
    # slack.get_channel_history("xxxxx")  # channel should be ID not name
