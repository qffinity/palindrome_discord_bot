import discord, os, math
TOKEN = 'ODMzNDEyODQ2NTYxNjU2ODMy.YHx-Mg.w7k7Thamt4CYdi2FvIvvHXXhi8A'
#PUT YOUR TOKEN HERE




def palindrome_check(num):
    palindrome = True
    string = str(num)
    for i in range(math.ceil(len(string) / 2)):
        if string[i] != string[-(i + 1)]:
            palindrome = False
    return palindrome


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if palindrome_check(message.content):
        await message.channel.send('**Palindrome alert!**')

client.run(TOKEN)