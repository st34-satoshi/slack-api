# slack-api
- Slack API using python
    - send messages to slack
    - receive messages from slack ([Events app][events-app])

# send messages to slack

## Requirement
set your **token** in to-slack.py.  
ref: [Slack API 推奨Tokenについて](https://qiita.com/ykhirao/items/3b19ee6a1458cfb4ba21)

get your token from [https://api.slack.com/apps](https://api.slack.com/apps)
OAuth & Permissions -> Bot User OAuth Token


## Usage
`python3 to-slack.py`

# receive messages from slack
## Requirement
`pip install -r requirements.txt`

## Usage
`python3 from-slack.py`

<hr>

## Reference
- [chat.postMessage api](https://api.slack.com/methods/chat.postMessage)
- [Slack API 推奨Tokenについて](https://qiita.com/ykhirao/items/3b19ee6a1458cfb4ba21)
- [Slackにpythonからメッセージを送信する](https://qiita.com/stu345/items/24790710abc571aae3ea)
- [Events app][events-app]


[events-app]: https://api.slack.com/events-api
