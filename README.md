-- in English --
# co-operater

Bot who calls me when I'm working alone
For example, if you put a linux command on slack, if it is a dangerous command
There is a thing calling out "Please be careful!"

-- in Japanese --
一人運用作業をしている時に声をかけてくれるBot
例えばlinuxコマンドをslackに貼ったとすると、危ないコマンドなら
「気をつけてね！」と声をかけてくれる事がある。


# リファレンス
## How to develop Slack RTM Bot
[Try making secretary bot with Real Time Messaging API : Real Time Messaging APIで秘書botを作ってみる](http://techblog.adish.co.jp/entry/2016/12/14/Real_TIme_Messaging_APIで秘書botを作ってみる)

## How to deploy Heroku
[python3でslackbotの作成\(その6:デプロイ編\) \- Qiita](https://qiita.com/thimi0412/items/aa0b0f28896fe4d364b3#_reference-8e53d2e60b9037be0a3d)

[python3でslackbotの作成\(その5:Heroku設定編\) \- Qiita](https://qiita.com/thimi0412/items/852ee9bbfd8b1dd3c072)

`heroku ps:scale python_bot=1`
