from slackbot.bot import default_reply
import urllib.request
import urllib.parse
import os
import json

# vars(message) sample
# {'_client': <slackbot.slackclient.SlackClient object at 0x10558a048>,'_body': {'type': 'message', 'channel': 'GA1CL5LLR', 'user': 'U0GA72734', 'text': 'おはよう', 'ts': '1523000579.000223', 'source_team': 'T02D9RVN1', 'team': 'T02D9RVN1'}, '_plugins': <slackbot.manager.PluginsManager object at 0x106494b38>}

@default_reply()
def aitalk(message):
    url = "https://api.a3rt.recruit-tech.co.jp/talk/v1/smalltalk"
    method = "POST"
    api_key = os.environ["A3RT_TALK_API_KEY"]
    message_content = vars(message)
    query = message_content['_body']['text']

    data = urllib.parse.urlencode({'apikey': api_key, 'query': query}).encode('utf-8')
    request = urllib.request.Request(url, data)
    response = urllib.request.urlopen(request)

    # https://a3rt.recruit-tech.co.jp/product/talkAPI/#reference
    # {"status": 0, "message": "ok", "results": [{"perplexity": 1.9698981714810797, "reply": "\u79c1\u306e\u3067\u3059\u304b?\u79d8\u5bc6\u3067\u3059"}]});
    content = json.loads(response.read().decode('utf8'))
    status = content['status']

    if status == 200:
        print(content)
        for x in content['results']:
            reply_msg = x['reply']
            message.send(reply_msg)

        message.react('+1')
    elif status == 2000:
        message.react('+1')
    else:
        print(str(status))
        message.send("何か起きているの。確認してもらえる？ STATUS:"+str(status)+"\nhttps://a3rt.recruit-tech.co.jp/product/talkAPI/#reference")

