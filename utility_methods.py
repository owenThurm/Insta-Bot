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
                "It's a vibe! when you get some time shoot a dm to @genuineAesthetic",
                "It's a vibe! when you get some time dm @genuineaesthetic",
                "It's a vibe fr! when you get the time shoot a dm to @genuineaesthetic",
                "It's a vibe fr! when you get the chance shoot a dm to @genuineaesthetic",
                "It's a vibe fr! if you get the chance shoot a dm to @genuineaesthetic",
                "It's a vibe fr! Whenever you're free shoot a dm to @genuineaesthetic",
                "It's a vibe fr! When you get a chance dm @genuineaesthetic",
                "It's a vibe fr! dm @genuineaesthetic whenever you get the time",
                "It's a vibe fr! dm @genuineaesthetic whenever you get the chance",
                "It's a vibe fr! dm @genuineaesthetic whenever you get a chance",
                "It's a vibe fr! dm @genuineaesthetic when you get the time",
                "It's a vibe fr! dm @genuineaesthetic when you get the chance",
                "It's a vibe fr! dm @genuineaesthetic when you get a chance",
                "It's a vibe fr! dm @genuineaesthetic whenever you can",
                "Dope shot! dm @genuineaesthetic when you can",
                "Dope shot! dm @genuineaesthetic when you can",
                "Dope shot! dm @genuineaesthetic whenever you get the chance!",
                "Dope shot! dm @genuineaesthetic when you get the chance",
                "Dope shot! when you get the chance shoot a dm to @genuineaesthetic",
                "Dope shot! when you’re free shoot a dm to @genuineaesthetic",
                "Dope shot! when you’re free dm @genuineaesthetic!",
                "Dope shot! when you get some time shoot a dm to @genuineaesthetic",
                "Dope shot! shoot a dm to @genuineaesthetic when you get the time",
                "Dope shot! shoot a dm to @genuineaesthetic when you get a chance",
                "Dope shot! shoot a dm to @genuineaesthetic when you get the chance",
                "Dope shot fr! shoot a dm to @genuineaesthetic when you get the time",
                "Dope shot fr! shoot a dm to @genuineaesthetic whenever your get a chance",
                "Dope shot fr! whenever you're free shoot a dm to @genuineaesthetic",
                "Dope shot! dm @genuineaesthetic whenever you’re free!",
                "Vibes! shoot @genuineaesthetic a dm whenever you get the chance",
                "Vibes! when you get a chance shoot a dm to @genuineaesthetic",
                "Vibes! shoot a dm to @genuineaesthetic when you can",
                "Vibes! dm @genuineaesthetic whenever you get the time",
                "Vibes fr! dm @genuineaesthetic whenever you get the chance",
                "Vibes fr! dm @genuineaesthetic whenever you're free!",
                "Vibes fr! dm @genuineaesthetic when you find the time!",
                "Vibes! if you get a chance shoot a dm to @genuineaesthetic",
                "it's a vibe fr! dm @genuineaesthetic when you can",
                "vibes fr! dm @genuineaesthetic when you can",
                "Vibes! whenever you get the time shoot a dm to @genuineaesthetic",
                "Vibes! if you're free shoot a dm to @genuineaesthetic",
                "Vibes! shoot a dm to @genuineaesthetic if you're free",
                "Hope you're having a good day! when you get the chance shoot a dm to @genuineaesthetic",
                "Hope you're having a good day! when you're free shoot a dm to @genuineaesthetic",
                "Hope you're having a good day! if you get the time shoot a dm to @genuineaesthetic",
                "Hope you're having a good day! whenever you get a chance dm @genuineaesthetic",
                "Hope you're having a good day! dm @genuineaesthetic whenever you're free!",
                "Hope you're having a good day! if you have the time shoot a dm to @genuineaesthetic",
                "Hope you're having a good day! whenever you get the chance shoot a dm to @genuineaesthetic",
                "Hope you're having a good day! whenever you get a chance shoot a dm to @genuineaesthetic",
                "Hope you're having a good day! when you get a chance shoot a dm to @genuineaesthetic",
                "Hope you're having a good day! shoot a dm to @genuineaesthetic when you can!",
                "Hope you're having a good day! shoot a dm to @genuineaesthetic when you get a chance",
                "Hope you're having a good day! shoot a dm to @genuineaesthetic whenever you get a chance",
                "Hope you're having a good day! shoot a dm to @genuineaesthetic when you get the time",
                "Hope you're having a good day! shoot a dm to @genuineaesthetic whenever you're free!",
                "Dope style! shoot a dm to @genuineaesthetic when you can!",
                "Dope style! dm @genuineaesthetic when you get the chance!",
                "Dope style! dm @genuineaesthetic whenever you get the chance!",
                "Dope style! dm @genuineaesthetic when you get a chance",
                "Dope style! dm @genuineaesthetic when you get a chance!",
                "Dope style! dm @genuineaesthetic whenever you can",
                "Dope style! dm @genuineaesthetic whenever you get the time",
                "Dope style! whenever you get the time shoot a dm to @genuineaesthetic",
                "Dope style! whenever you can, shoot a dm to @genuineaesthetic",
                "Dope style! whenever you get a chance shoot a dm to @genuineaesthetic",
                "Dope style! whenever you get the chance, shoot a dm to @genuineaesthetic",
                "Dope style fr! dm @genuineaesthetic when you're free",
                "Dope style fr! if you get the chance, shoot a dm to @genuineaesthetic",
                "Dope style fr! whenever you get the time shoot a dm to @genuineaesthetic",
                "Dope style fr! whenever you're free shoot a dm to @genuineaesthetic",
                "Dope style fr! Whenever you're free dm @genuineaesthetic",
                "Dope style fr! Whenever you get the time dm @genuineaesthetic",
                "Dope style fr! Whenever you get a chance shoot a dm to @genuineaesthetic",
                "Dope style fr! Whenever you get the chance shoot a dm to @genuineaesthetic",
                "Dope style fr! Whenever you get the chance dm @genuineaesthetic",
                "Dope style fr! Whenever you get a chance dm @genuineaesthetic",
                "Dope style fr! shoot a dm to @genuineaesthetic whenever you get the chance!",
                "Dope style fr! shoot a dm to @genuineaesthetic whenever you can!",
                "Dope style fr! shoot a dm to @genuineaesthetic when you get the time!",
                "Dope style fr! shoot a dm to @genuineaesthetic whenever you get the time!",
                "Dope style fr! shoot a dm to @genuineaesthetic whenever you get a chance!",
                "That's whats up, if you get the chance shoot a dm to @genuineaesthetic",
                "That's whats up, when you get the chacne shoot a dm to @genuineaesthetic",
                "That's whats up, shoot a dm to @genuineaesthetic whenever you can",
                "That's whats up, when you get a chance dm @genuineaesthetic",
                "That's whats up, whenever you find the time shoot a dm to @genuineaesthetic",
                "That's whats up, if you get a chance dm @genuineaesthetic",
                "That's whats up, dm @genuineaesthetic when you can",
                "That's whats up, dm @genuineaesthetic whenever you get the chance to",
                "That's whats up, dm @genuineaesthetic if you have the time!",
                "That's whats up, dm @genuineaesthetic whenever you get the time!",
                "That's whats up, dm @genuineaesthetic whenever you're free!",
                "That's whats up, shoot a dm to @genuineaesthetic whenever you can!",
                "That's whats up, shoot a dm to @genuineaesthetic whenever you get the chance!",
                "That's whats up, shoot a dm to @genuineaesthetic when you get the chance!",
                "That's whats up, shoot a dm to @genuineaesthetic when you can!",
                "That's whats up, shoot a dm to @genuineaesthetic whenever you find the time!",
                "That's whats up, shoot a dm to @genuineaesthetic whenever you get the time!",
                "That's whats up, shoot a dm to @genuineaesthetic whenever you get a chance",
                "That's whats up, shoot a dm to @genuineaesthetic when you get the time!"]
    return comments[math.floor(random.random()*len(comments))]

def randomCommentTextMain():
    comments = ["It’s a vibe! shoot us a dm when you can",
                "It’s a vibe! dm us when you can ",
                "It’s a vibe! when you get the chance shoot us a dm",
                "It’s a vibe! when you get the chance shoot a dm to us ",
                "It’s a vibe! shoot a dm to us when you can",
                "It’s a vibe! when you’re free shoot a dm to us ",
                "It’s a vibe! dm us whenever you’re free",
                "It’s a vibe! whenever you get a minute dm us ",
                "It’s a vibe! whenever you get a minute shoot us a dm",
                "It’s a vibe! when you get a minute dm us",
                "It’s a vibe! when you’re free shoot a dm to us ",
                "It’s a vibe! dm us when you can",
                "It’s a vibe! whenever you’re free dm us",
                "It's a vibe! when you get some time shoot a dm to us",
                "It's a vibe! when you get some time dm us",
                "It's a vibe fr! when you get the time shoot a dm to us",
                "It's a vibe fr! when you get the chance shoot a dm to us",
                "It's a vibe fr! if you get the chance shoot a dm to us",
                "It's a vibe fr! Whenever you're free shoot a dm to us",
                "It's a vibe fr! When you get a chance dm us",
                "It's a vibe fr! dm us whenever you get the time",
                "It's a vibe fr! dm us whenever you get the chance",
                "It's a vibe fr! dm us whenever you get a chance",
                "It's a vibe fr! dm us when you get the time",
                "It's a vibe fr! dm us when you get the chance",
                "It's a vibe fr! dm us when you get a chance",
                "It's a vibe fr! dm us whenever you can"
                "Dope shot! dm us when you can",
                "Dope shot! dm us when you can",
                "Dope shot! dm us whenever you get the chance!",
                "Dope shot! dm us when you get the chance",
                "Dope shot! when you get the chance shoot a dm to us",
                "Dope shot! when you’re free shoot a dm to us",
                "Dope shot! when you’re free dm us!",
                "Dope shot! when you get some time shoot a dm to us",
                "Dope shot! shoot a dm to us when you get the time",
                "Dope shot! shoot a dm to us when you get a chance",
                "Dope shot! shoot a dm to us when you get the chance"
                "Dope shot fr! shoot a dm to us when you get the time",
                "Dope shot fr! shoot a dm to us whenever your get a chance",
                "Dope shot fr! whenever you're free shoot a dm to us",
                "Dope shot! dm us whenever you’re free!",
                "Vibes! shoot us a dm whenever you get the chance",
                "Vibes! when you get a chance shoot a dm to us",
                "Vibes! shoot a dm to us when you can",
                "Vibes! dm us whenever you get the time",
                "Vibes fr! dm us whenever you get the chance",
                "Vibes fr! dm us whenever you're free!",
                "Vibes fr! dm us when you find the time!",
                "Vibes! if you get a chance shoot a dm to us",
                "it's a vibe fr! dm us when you can",
                "vibes fr! dm us when you can",
                "Vibes! whenever you get the time shoot a dm to us",
                "Vibes! if you're free shoot a dm to us",
                "Vibes! shoot a dm to us if you're free",
                "Hope you're having a good day! when you get the chance shoot a dm to us",
                "Hope you're having a good day! when you're free shoot a dm to us",
                "Hope you're having a good day! if you get the time shoot a dm to us",
                "Hope you're having a good day! whenever you get a chance dm us",
                "Hope you're having a good day! dm us whenever you're free!",
                "Hope you're having a good day! if you have the time shoot a dm to us",
                "Hope you're having a good day! whenever you get the chance shoot a dm to us",
                "Hope you're having a good day! whenever you get a chance shoot a dm to us",
                "Hope you're having a good day! when you get a chance shoot a dm to us",
                "Hope you're having a good day! shoot a dm to us when you can!",
                "Hope you're having a good day! shoot a dm to us when you get a chance",
                "Hope you're having a good day! shoot a dm to us whenever you get a chance",
                "Hope you're having a good day! shoot a dm to us when you get the time",
                "Hope you're having a good day! shoot a dm to us whenever you're free!",
                "Dope style! shoot a dm to us when you can!",
                "Dope style! dm us when you get the chance!",
                "Dope style! dm us whenever you get the chance!",
                "Dope style! dm us when you get a chance",
                "Dope style! dm us when you get a chance!",
                "Dope style! dm us whenever you can",
                "Dope style! dm us whenever you get the time",
                "Dope style! whenever you get the time shoot a dm to us",
                "Dope style! whenever you can, shoot a dm to us",
                "Dope style! whenever you get a chance shoot a dm to us",
                "Dope style! whenever you get the chance, shoot a dm to us",
                "Dope style fr! dm us when you're free",
                "Dope style fr! if you get the chance, shoot a dm to us",
                "Dope style fr! whenever you get the time shoot a dm to us",
                "Dope style fr! whenever you're free shoot a dm to us",
                "Dope style fr! Whenever you're free dm us",
                "Dope style fr! Whenever you get the time dm us",
                "Dope style fr! Whenever you get a chance shoot a dm to us",
                "Dope style fr! Whenever you get the chance shoot a dm to us",
                "Dope style fr! Whenever you get the chance dm us",
                "Dope style fr! Whenever you get a chance dm us",
                "Dope style fr! shoot a dm to us whenever you get the chance!",
                "Dope style fr! shoot a dm to us whenever you can!",
                "Dope style fr! shoot a dm to us when you get the time!",
                "Dope style fr! shoot a dm to us whenever you get the time!",
                "Dope style fr! shoot a dm to us whenever you get a chance!",
                "That's whats up, if you get the chance shoot a dm to us",
                "That's whats up, when you get the chacne shoot a dm to us",
                "That's whats up, shoot a dm to us whenever you can",
                "That's whats up, when you get a chance dm us",
                "That's whats up, whenever you find the time shoot a dm to us",
                "That's whats up, if you get a chance dm us",
                "That's whats up, dm us when you can",
                "That's whats up, dm us whenever you get the chance to",
                "That's whats up, dm us if you have the time!",
                "That's whats up, dm us whenever you get the time!",
                "That's whats up, dm us whenever you're free!",
                "That's whats up, shoot a dm to us whenever you can!",
                "That's whats up, shoot a dm to us whenever you get the chance!",
                "That's whats up, shoot a dm to us when you get the chance!",
                "That's whats up, shoot a dm to us when you can!",
                "That's whats up, shoot a dm to us whenever you find the time!",
                "That's whats up, shoot a dm to us whenever you get the time!",
                "That's whats up, shoot a dm to us whenever you get a chance",
                "That's whats up, shoot a dm to us when you get the time!"]
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
