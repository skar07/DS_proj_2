import config


class userAct:
    def userView(self):
        for x in config.members:
            for i, j in x.items():
                print("{} : {}".format(i, j))
