import discord


class DiscordClient(discord.Client):
    def __init__(self, *args, **kwargs):
        discord.Client.__init__(self, **kwargs)

    async def on_ready(self):
        print('Success!')

def password():
    rawData = getPassword(image)
    return rawData.convertTo64()

if __name__ == '__main__':
    dc = DiscordClient()
    dc.login(input('email : JeorgeMacintosh55@gmail.com'), input('password : ' + password()), bot=False)
    dc.run()