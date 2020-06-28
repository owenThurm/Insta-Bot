import random
import math

def randomCommentText():
    comments = ["It’s a vibe! shoot @genuineaesthetic a dm when you can",
                "It’s a vibe! dm @genuineaesthetic when you can ",
                "It’s a vibe! when you get the chance shoot @genuineaesthetic a dm",
                "It’s a vibe! when you get the chance shoot a dm to @genuineaesthetic ",
                "It’s a vibe! shoot a dm to @genuineaesthetic when you can",
                "It’s a vibe! when you’re free shoot a dm to @genuineaesthetic ",
                "It’s a vibe! dm @genuineaesthetic whenever you’re free",
                "It’s a vibe! whenever you get a minute dm @genuineaesthetic ",
                "It’s a vibe! whenever you get a minute shoot @genuineaesthetic a dm",
                "It’s a vibe! when you get a minute dm @genuineaesthetic",
                "It’s a vibe! when you’re free shoot a dm to @genuineaesthetic ",
                "It’s a vibe! dm @genuineaesthetic when you can",
                "It’s a vibe! whenever you’re free dm @genuineaesthetic",
                "Dope shot! dm @genuineaesthetic when you can",
                "Dope shot! dm @genuineaesthetic when you can",
                "Dope shot! dm @genuineaesthetic whenever you get the chance!",
                "Dope shot! dm @genuineaesthetic when you get the chance",
                "Dope shot! when you get the chance shoot a dm to @genuineaesthetic",
                "Dope shot! when you’re free shoot a dm to @genuineaesthetic",
                "Dope shot! when you’re free dm @genuineaesthetic!",
                "Dope shot! dm @genuineaesthetic whenever you’re free!"]
    return comments[math.floor(random.random()*len(comments))]


if __name__ == '__main__':
    comments = ["It’s a vibe🙌 shoot @genuineaesthetic a dm when you can🙏",
                "It’s a vibe🙌 dm @genuineaesthetic when you can🙏 ",
                "It’s a vibe👌 when you get the chance shoot @genuineaesthetic a dm🙏",
                "It’s a vibe🤟when you get the chance shoot a dm to @genuineaesthetic 🙏",
                "It’s a vibe🤟shoot a dm to @genuineaesthetic when you can🙌",
                "It’s a vibe👌when you’re free shoot a dm to @genuineaesthetic 🤟",
                "It’s a vibe🙌 dm @genuineaesthetic whenever you’re free🙏",
                "It’s a vibe🙏 whenever you get a minute dm @genuineaesthetic 🙌",
                "It’s a vibe🙌 whenever you get a minute shoot @genuineaesthetic a dm🙏",
                "It’s a vibe🙌 when you get a minute dm @genuineaesthetic 🙏",
                "It’s a vibe🙏 when you’re free shoot a dm to @genuineaesthetic 🙏",
                "It’s a vibe👌 dm @genuineaesthetic when you can🙏",
                "It’s a vibe🙌 whenever you’re free dm @genuineaesthetic🤟",
                "Dope shot🤟 dm @genuineaesthetic when you can🙌",
                "Dope shot🙏 dm @genuineaesthetic when you can🙌",
                "Dope shot👌 dm @genuineaesthetic whenever you get the chance🙏",
                "Dope shot🙌 dm @genuineaesthetic when you get the chance",
                "Dope shot🤟 when you get the chance shoot a dm to @genuineaesthetic 🙏",
                "Dope shot🙌 when you’re free shoot a dm to @genuineaesthetic👌",
                "Dope shot🙏 when you’re free dm @genuineaesthetic🙌",
                "Dope shot🙌 dm @genuineaesthetic whenever you’re free🙏"]
    print(randomCommentText(comments))    