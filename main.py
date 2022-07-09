import requests


def generateMail(count: int = 1) -> list[str]:
    mails = requests.get("https://1secmail.com/api/v1/?action=genRandomMailbox&count={}".format(str(count))).json()
    return mails


def getMessages(email: str) -> list[str]:
    login = email[:email.find("@")]
    domain = email[email.find("@") + 1:]
    messages = requests.get(
        "https://1secmail.com/api/v1/?action=getMessages&login={}&domain={}".format(login, domain)).json()
    return messages


if __name__ == '__main__':
    # print(generateMail(1)[0])
    mail = "7fybf8@dcctb.com"
    print("mail: ", mail)
    messages = getMessages(mail)
    print("messages: ", messages)

    twitterVCode = messages[0]['subject'].split()[0]
    print("twitter v code: ", twitterVCode)
