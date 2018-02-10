import itchat
from wechat.tuling import getResponse

state = "on"


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    info = getResponse(msg["Text"])["text"]
    print(msg["User"]["NickName"] + " 对你说：" + msg["Text"])
    print("图灵机器人帮你回复了：" + info)
    realmsg = info + "\n～By:机器人图图"
    return realmsg


# 获取群的ID
def group_id(name):
    df = itchat.search_chatrooms(name=name)
    return df[0]["UserName"]


# 对某一个微信进行自动回复
@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def group_text_reply(msg):
    # 如果只想针对被@的人才回复，可以设置if msg["isAt"]:
    item1 = group_id(u"图灵机器人测试群")  # 需要设置为群的名称
    if msg["FromUserName"] == item1:
        global state
        print(msg["FromUserName"])
        print(item1)
        print(state + msg["ActualNickName"])
        print(msg["isAt"])
        print("闭嘴" in msg["Text"])
        # 自己一时觉得好玩增加了管理员权限，只有管理员@了机器人并说闭嘴，程序才不会接着回复消息
        if state == "on":
            if msg["ActualNickName"] == "管理员" and msg["isAt"] and "闭嘴" in msg["Text"]:
                itchat.send("好的，机器人已关闭", msg["FromUserName"])
                state = "off"
                print("好的，机器人已关闭")
            else:
                info = getResponse(msg["Text"])["text"]
                itchat.send(info, msg["FromUserName"])
        else:
            if msg["ActualNickName"] == "管理员" and msg["isAt"] and "说话" in msg["Text"]:
                itchat.send("终于可以说话了，憋死我了", msg["FromUserName"])
                state = "on"
                print("终于可以说话了，憋死我了")


itchat.auto_login()
itchat.run()
