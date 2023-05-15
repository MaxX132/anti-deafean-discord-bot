import discord
import time
import sys

prefix = "}"

TOKEN = "your-bot-token-here"

move = True

version = 0.9

guild_id = int("discord-server-id")

member_to_move_id = int("id-of-memeber-you-want-to-move")
move_to_channel_id = int("id-of-channel-you-want-people-to-get-moved-into")

bot_owner_id = int("your-discord-id")


def main():
    intents = discord.Intents.all()
    intents.voice_states = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print('logged as {0.user}'.format(client))

    @client.event
    async def on_voice_state_update(member, before, after):
        time.sleep(0.1)
        if move:
            try:
                after = str(after)
                guild = client.get_guild(guild_id)
                print(member)
                if "self_deaf=True" in after:
                    channel = client.get_channel(move_to_channel_id)
                    # channel now holds the channel you want to move people into

                    member_deafeaned = guild.get_member(member_to_move_id)
                    
                    #print(after)

                    if member_deafeaned == member:
                        #member now holds the user that you want to move

                        await member_deafeaned.move_to(channel=channel, reason='automated action (adam defeaned)')
                        print("adam system activated")
            except:
                print('err')
    
    @client.event
    async def on_message(message):
        global move
        guild = client.get_guild(guild_id)
        time.sleep(0.01)
        if message.content.startswith(prefix):
            mess = message.content.strip('}')
            if message.author == client.user:
                return
        
            if mess.startswith('help'):
                membr = guild.get_member(member_to_move_id)
                if message.author == membr:
                    await message.channel.send("Requires higher elevation of rights... Contact Admin")
                    return
                await message.channel.send("This bot prevents [REDACTED] from deafening in VC\n\n\n**Commands:**\n\n}help -> displays this message\n\n}stop -> stops moving [REDACTED]\n\n}start -> starts mobing [REDACTED]\n\n}kill -> terminates me (only 0x)\n\n}status -> checks my status")
                await message.channel.send("\n*made by 0x#3549*")

            if mess == ('stop'):
                membr = guild.get_member(member_to_move_id)
                if message.author == membr:
                    await message.channel.send("Requires higher elevation of rights... Contact Admin")
                    await message.channel.send("\n*made by 0x#3549*")
                    return
                move = False
                await message.channel.send("Disabled moving for [REDACTED]")
                await message.channel.send("\n*made by 0x#3549*")

            if mess == ('start'):
                membr = guild.get_member(member_to_move_id)
                if message.author == membr:
                    await message.channel.send("Requires higher elevation of rights... Contact Admin")
                    await message.channel.send("\n*made by 0x#3549*")
                    return
                move = True
                await message.channel.send("Enabled moving for [REDACTED]")
                await message.channel.send("\n*made by 0x#3549*")

            if mess == ('kill'):
                me = guild.get_member(bot_owner_id)
                if message.author != me:
                    await message.channel.send("Requires higher elevation of rights... Contact Admin")
                    await message.channel.send("\n*made by 0x#3549*")
                    return
                await message.channel.send("Terminating process with ID [REDACTED]...")
                time.sleep(1.2564)
                await message.channel.send("Successfully terminated [REDACTED]...")
                await message.channel.send("\n*made by 0x#3549*")
                sys.exit(1)
            
            if mess == ('status'):
                membr = guild.get_member(member_to_move_id)
                if message.author == membr:
                    await message.channel.send("Requires higher elevation of rights... Contact Admin")
                    await message.channel.send("\n*made by 0x#3549*")
                    return
                await message.channel.send("Process [REDACTED] is up and running on version v" + str(version))
                if move == True:
                    await message.channel.send("Status is now code 1 AKA enabled!")
                if move == False:
                    await message.channel.send("Status is now code 0 AKA disabled!")
                await message.channel.send("\n*made by 0x#3549*")
    
    

    client.run(TOKEN)


if __name__ == "__main__":
    main()
