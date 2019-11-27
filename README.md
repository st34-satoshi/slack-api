# slack-api
- slack apiをpythonでたたく
- slackからのメッセージを受信する([Events app][events-app])

<hr>
# slack apiをpythonでたたく

## Requirement
set your **token** in main.py.  
参考 [Slack API 推奨Tokenについて](https://qiita.com/ykhirao/items/3b19ee6a1458cfb4ba21)

## Usage
`python3 to-slack.py`

<hr>
# slackからメッセージを受信する
使い方などは参照
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