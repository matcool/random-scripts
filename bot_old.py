import discord
import asyncio
import base64
import random
import string
import hashlib
import urllib.request
import requests
import XORPython
import math
import MatStuff
import datetime
import json
import inspect
import textwrap

description = 'a super hyper mega doing nothing bot'

client = discord.Client()

@client.event
async def on_ready():
    configfile = open('botconfig.txt', 'r+')
    conflines = configfile.readlines()
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    Pstatus = conflines[0][5:]
    Pstatus = Pstatus.replace("%numberofservers%", str(len(client.servers)))
    await client.change_presence(game=discord.Game(name=Pstatus[:-1]))
    print('Playing {}'.format(Pstatus[:-1]))
    print('------')

tmpvar = ""
@client.event
async def on_message(message): 
    sendmess = client.send_message
    channelmess = message.channel
    stwi = message.content.startswith
    editmess = client.edit_message
    contentmess = message.content
    durma = asyncio.sleep
    authormess = message.author
    addreaction = client.add_reaction
    if message.author.id == '83010416610906112':
        if stwi('Ata é o que você vai falar quando chupar a cabeça da minha rola, seu filha da puta'):
            await sendmess(channelmess, 'cala boca nightbot')
    if message.author.id == '191233808601841665':
        if message.content.startswith('sakuješ'):
            tmp = discord.utils.get(client.get_all_emojis(), name='tru')
            await client.send_message(channelmess, "very very VeRY {}".format(str(tmp)))
        elif stwi('!myass'):
            await sendmess(channelmess, 'heres a pic of my ass: \nhttps://cdn.discordapp.com/attachments/295953725271572481/298505198366883841/gc2.png'
        elif stwi('edit test'):
            tmp = await sendmess(channelmess, 'test')
            await asyncio.sleep(4)
            await editmess(tmp, 'haha u fool')
        elif stwi('^version'):
            tmp = await sendmess(channelmess, 'Getting version info...')
            await durma(1)
            await editmess(tmp, 'MatBot Version '+str(matversion))
        elif stwi('lenny'):
            tmp2 = '( ͡° ͜ʖ ͡°)'
            tmp = await sendmess(channelmess, tmp2)
            for i in range(100):
                await durma(0.2)
                tmp2 += ' ( ͡° ͜ʖ ͡°)'
                await editmess(tmp, tmp2)
        elif stwi('embed test'):
            tmp = discord.Embed(title='Commands', description='My Embed Content.', colour=0xDEADBF)
            tmp.set_author(name='Someone', icon_url=client.user.default_avatar_url)
            await client.send_message(message.channel, embed=tmp)
        elif stwi('going to sleep'):
            await sendmess(channelmess, 'good night mat i love you <3 <3')
        elif stwi('^say '):
            await client.delete_message(message)
            await sendmess(channelmess, contentmess[5:])
        elif stwi('^saytts '):
            await client.delete_message(message)
            await sendmess(channelmess, contentmess[8:], tts=True)
        elif stwi('^repeat'):
            tmp = contentmess[8:].split("|")
            for i in range(int(tmp[1])):
                tmp2 = tmp[0].replace("%number%", str(i + 1))
                if str(i + 1)[-1:] == "1" and str(i + 1)[-2:-1] != "1":
                    tmp2 = tmp2.replace("%enunumber%", str(i + 1)+"st")
                elif str(i + 1)[-1:] == "2" and str(i + 1)[-2:-1] != "1":
                    tmp2 = tmp2.replace("%enunumber%", str(i + 1)+"nd")
                elif str(i + 1)[-1:] == "3" and str(i + 1)[-2:-1] != "1":
                    tmp2 = tmp2.replace("%enunumber%", str(i + 1)+"rd")
                else:
                    tmp2 = tmp2.replace("%enunumber%", str(i + 1)+"th")
                await sendmess(channelmess, tmp2)
        elif stwi("^sendallemojis"):
            tmp = ""
            for i in client.get_all_emojis():
                tmp += " "+str(i)
            tmp2 = tmp.split(" ")
            tmp3 = ["", ""]
            tmp4 = 0
            for i in range(len(tmp2)):
                if len(tmp3) < tmp4 + 1:
                    tmp3[tmp4] = ""
                if len(tmp3[tmp4]) < 2000 and len(tmp2[i - 1]) < 2000 - len(tmp3[tmp4]):
                    tmp3[tmp4] += tmp2[i - 1]
                else:
                    tmp4 += 1
            for arraaaw in tmp3:
                await sendmess(channelmess, arraaaw)
        elif stwi("^updstatus"):
            if contentmess[11:] != "":
                tmp = contentmess[11:]
                tmp = tmp.replace("%numberofservers%", str(len(client.servers)))
                await client.change_presence(game=discord.Game(name=tmp))
            else:
                tmp = open('botconfig.txt', 'r+')
                tmp2 = tmp.readlines()
                tmp3 = tmp2[0][5:]
                tmp3 = tmp3.replace("%numberofservers%", str(len(client.servers)))
                await client.change_presence(game=discord.Game(name=tmp3))
                tmp.close()
            await client.delete_message(message)
        elif stwi("!stalk"):
            tmp = open("ohcool.txt", "w+")
            tmp2 = ""
            for member in message.server.members:
                tmp2 += str(member)+" \n"
            tmp.write(str(tmp2))
            tmp.close()
        elif stwi("!changeavatar "):
            tmp = contentmess[14:]
            tmp2 = open(tmp, "rb")
            await client.edit_profile(avatar=tmp2.read())
        elif stwi("^exec"):
            env = {
            'client': client,
            'channelmess': message.channel,
            'authormess': message.author,
            'sendmess': client.send_message,
            'message': message
            }
            env.update(globals())
            to_compile = 'async def func():\n%s' % textwrap.indent(message.content.strip('^exec'), '  ')
            try:
                exec(to_compile, env)
            except SyntaxError as e:
                return await client.send_message(message.channel, get_syntax_error(e))
            func = env['func']
            try:
                await func()
            except Exception as e:
                await client.send_message(message.channel, "{}:{}".format(type(e).__name__, e))
        elif stwi("^somebody"):
            allstar = open("bot_allstarlyrics.txt", "r")
            tmp = allstar.readlines()
            tmp3 = ""
            tmp2 = await sendmess(channelmess, tmp3+".")
            for line in tmp:
                tmp3 += line
                await editmess(tmp2, tmp3)
                await durma(0.8)
        
    if message.author.id == '181848101777047562':
        if stwi('maybe'):
            await sendmess(channelmess, 'shut up dhl')
    if message.author.id != '295956628690173952':
        if message.content.startswith("^embed "):
            tmp = message.content[7:].split("|")
            tmp2 = discord.Embed(title=tmp[0], description=tmp[1], colour=int(tmp[2], 16))
            tmp2.set_author(name=message.author, icon_url=message.author.avatar_url)
            await sendmess(channelmess, embed=tmp2)
        if stwi('^test '):
            if message.content[6:] == '1':
                await sendmess(channelmess, 'you chooose option 1')
            elif message.content[6:] == 'wow':
                await sendmess(channelmess, 'oh wow')
        elif message.content == '^test' :
            await sendmess(channelmess, 'u chose nothing')
        if stwi('^encode'):
            if message.content[8:15]=="base64 ":
                tmp = message.content[15:]
                tmp2 = base64.b64encode(bytes(tmp, 'utf-8')).decode('utf-8')
                await sendmess(channelmess, tmp2)
                #thanks to fluffy
            elif contentmess[8:12] == "gjp ":
                tmp = contentmess[12:]
                await sendmess(channelmess, XORPython.encode(tmp, "37526"))
            elif contentmess[8:12]=="md5 ":
                tmp = contentmess[12:].encode('utf-8')
                await sendmess(channelmess, hashlib.md5(tmp).hexdigest())
            elif contentmess[8:13]=="sha1 ":
                tmp = contentmess[13:].encode('utf-8')
                await sendmess(channelmess, hashlib.sha1(tmp).hexdigest())
            elif contentmess[8:12]=="dog ":
                tmp3 = ["bork", "bark", "woof", "borky"]
                tmp2 = ""
                for i in range(random.randint(1,5)):
                    tmp = random.choice(tmp3)
                    tmp2 += tmp+" "
                await sendmess(channelmess, tmp2)
            elif contentmess[8:13]=="dog2 ":
                await sendmess(channelmess, MatStuff.DogEnc(contentmess[13:]))
            elif contentmess[8:13]=="lenny":
                tmp = random.randint(0,5)
                tmp2 = "( ͡° ͜ʖ ͡°)"
                for i in range(tmp):
                    tmp2 += " ( ͡° ͜ʖ ͡°)"
                await sendmess(channelmess, tmp2)
            elif contentmess[8:12]=="ednp":
                tmp = random.randint(0,5)
                tmp2 = "ednaldo pereira"
                for i in range(tmp):
                    tmp2 += " ednaldo pereira"
                await sendmess(channelmess, tmp2)
            elif contentmess[8:13]=="kappa":
                if contentmess[14:]!="kappa":
                    tmp = random.randint(0,9)
                    tmp2 = "<:kappa:277576162199339008>"
                    for i in range(tmp):
                        tmp2 += "<:kappa:277576162199339008>"
                    await sendmess(channelmess, tmp2)
                elif contentmess[14:]=="kappa":
                    await sendmess(channelmess, "<:kappa:277576162199339008>")
            elif contentmess[8:11]=="cat":
                await sendmess(channelmess, "i cant speak cat im a doge you maincra")
            elif contentmess[8:]=="some body":
                await sendmess(channelmess, "once told me")
            elif contentmess[8:12]=="mmbb":
                tmp = random.randint(0,5)
                tmp2 = "me me big boy"
                for i in range(tmp):
                    tmp2 += " me me big boy"
                await sendmess(channelmess, tmp2)
            else:
                await sendmess(channelmess, 'Usage : ^encode md5/base64/sha1/cat/dog/lenny/kappa/ednp/mmbb *message*')
        elif stwi('^decode'):
            if message.content[8:15]=="base64 ":
                tmp = message.content[15:]
                die = ''
                try:
                    tmp2 = base64.b64decode(bytes(tmp, 'utf-8')).decode('utf-8')
                except binascii.Error:
                    die = 'die'
                    pass
                if die == 'die':
                    await sendmess(channelmess, tmp2)
                #thanks to fluffy
            elif contentmess[8:12] == "gjp ":
                tmp = contentmess[12:]
                await sendmess(channelmess, XORPython.decode(tmp, "37526"))
            elif contentmess[8:13]=="dog2 ":
                await sendmess(channelmess, MatStuff.DogDec(contentmess[13:]))
        elif stwi('^calc '):
            tmp = contentmess[6:].find("+")
            tmp2 = contentmess[6:].split("+")
            if tmp != -1:
                await sendmess(channelmess, str(int(tmp2[0])+int(tmp2[1])))
            else:
                tmp = contentmess[6:].find("-")
                tmp2 = contentmess[6:].split("-")
                if tmp != -1:
                    await sendmess(channelmess, str(int(tmp2[0]) - int(tmp2[1])))
                else:
                    tmp = contentmess[6:].find("*")
                    tmp2 = contentmess[6:].split("*")
                    if tmp != -1:
                        await sendmess(channelmess, str(int(tmp2[0]) * int(tmp2[1])))
        elif stwi('^delete'):
            await sendmess(channelmess, "okdone deleted "+str(message.clean_content[8:]))
            await client.delete_message(message)
        elif stwi('^help'):
            file = open("bothelp.txt", "r")
            tmp = discord.Embed(title="Matbot commands", description=file.read() , colour=0x000011)
            if contentmess[6:] != "-h":
                await sendmess(message.author, embed=tmp)
            else:
                await sendmess(channelmess, embed=tmp)
        elif stwi('^love'):
            tmp = contentmess[6:]
            await sendmess(channelmess, "<3 {} <3".format(tmp))
        elif stwi('^hate'):
            tmp = contentmess[6:]
            await sendmess(channelmess, ":thumbsdown: {} :thumbsdown: >:(".format(tmp))
        elif stwi('^bee'):
            file = open("beemovie.txt", "r")
            tmp = file.readlines()
            if contentmess[5:] == "random":
                await sendmess(channelmess, random.choice(tmp))
            else:
                tmp2 = int(contentmess[5:]) - 1
                await sendmess(channelmess, tmp[tmp2])
        elif stwi('^corgi'):
            file = open("dogpic.txt", "r")
            tmp = file.readlines()
            await sendmess(channelmess, random.choice(tmp))
        elif stwi('^maltese'):
            file = open("cvoltondog.txt", "r")
            tmp = file.readlines()
            await sendmess(channelmess, random.choice(tmp))
        elif stwi('^randomsent '):
            tmp = ""
            tmp2 = 0
            words = []
            file = open("beemovie.txt", "r")
            lines = file.readlines()
            for line in lines:
                tmp3 = line.split()
                for i in range(len(line.split())):
                    if tmp2 > len(line):
                        tmp2 = 0
                    tmp4 = tmp3[tmp2]
                    words.append(tmp4)
                    tmp2 += 1
                tmp2 = 0
            wordcount = contentmess[12:]
            for x in range(int(wordcount)):
                tmp += "{} ".format(random.choice(words))
            await sendmess(channelmess, tmp)
        elif stwi('!songtest '):
            tmp = contentmess[10:]
            tmp2 = requests.post("http://pi.michaelbrabec.cz:9010/a/getGJSongInfo.php", data={'songID':tmp})
            tmp3 = tmp2.text.split("~|~")
            tmp4 = ""
            tmp5 = tmp3[0]
            if tmp5[int(len(tmp5) - 2):len(tmp5)] == "-1":
                await sendmess(channelmess, "that song dont exist m8")
            else:
                tmp4 += "**Song Name :** {} \n".format(tmp3[3])
                tmp4 += "**Song Author :** {} \n".format(tmp3[7])
                tmp4 += "**Song Size :** {} MB \n".format(tmp3[9])
                tmp4 += "**Song Link :** {} \n".format(tmp3[13])
                await sendmess(channelmess, urllib.parse.unquote(tmp4))
        elif stwi('^spcfy '):
            await sendmess(channelmess, " ".join(contentmess[7:]))
        elif stwi('^sakuješ'):
            await client.add_reaction(message, '\N{Regional Indicator Symbol Letter S}')
            await client.add_reaction(message, '\N{Regional Indicator Symbol Letter A}')
            await client.add_reaction(message, '\N{Regional Indicator Symbol Letter K}')
            await client.add_reaction(message, '\N{Regional Indicator Symbol Letter U}')
            await client.add_reaction(message, '\N{Regional Indicator Symbol Letter J}')
            await client.add_reaction(message, '\N{Regional Indicator Symbol Letter E}')
            await client.add_reaction(message, '\N{Heavy Dollar Sign}')
        elif stwi('^prank1'):
            await client.delete_message(message)
            tmp = await sendmess(channelmess, "React on this message with :a:")
            tmp2 = await client.wait_for_reaction(['\N{Negative Squared Latin Capital Letter A}'], message=tmp)
            await editmess(tmp, "{0.user} is gey kthx".format(tmp2))
            await client.clear_reactions(tmp)
        elif stwi('!ban '):
            await sendmess(channelmess, "Banned {} Successfully.".format(contentmess[5:]))
        elif stwi('^reactwithallemojis'):
            for i in client.get_all_emojis():
                await addreaction(message, i)
        elif stwi("!sendemoji "):
            tmp = discord.utils.get(client.get_all_emojis(), name=contentmess[11:])
            await sendmess(channelmess, tmp)
        elif stwi("^invite"):
            await sendmess(channelmess, "https://discordapp.com/oauth2/authorize?client_id=295963237927878656&scope=bot&permissions=8192")
        elif stwi("^fap"):
            await sendmess(channelmess, "no porn for u "+message.author.name)
        elif stwi("^get "):
            tmp = contentmess[5:]
            if tmp[:3] == "pfp":
                if contentmess[9:] != "":
                    tmp = contentmess[9:]
                    tmp2 = discord.utils.get(message.server.members, id=tmp)
                    if tmp2.avatar_url.find(".webp") != -1:
                        tmp3 = tmp2.avatar_url.find(".webp")
                        await sendmess(channelmess, tmp2.avatar_url[:tmp3]+".png")
                    else:
                        await sendmess(channelmess, tmp2.avatar_url)
                else:
                    tmp2 = message.author
                    if tmp2.avatar_url.find(".webp") != -1:
                        tmp3 = tmp2.avatar_url.find(".webp")
                        await sendmess(channelmess, tmp2.avatar_url[:tmp3]+".png")
                    else:
                        await sendmess(channelmess, tmp2.avatar_url)
            elif tmp[:10] == "servericon":
                tmp = message.server.icon_url
                if tmp.find(".jpg") != -1:
                    await sendmess(channelmess, tmp.replace(".jpg", ".png"))
                else:
                    await sendmess(channelmess, tmp)
        elif stwi('^google '):
            await sendmess(channelmess, "http://google.com/search?q="+contentmess[8:])
        elif stwi("^ping"):
            tmp = datetime.datetime.now()
            tmp2 = await sendmess(channelmess, ":clock:")
            tmp3 = datetime.datetime.now()
            tmp4 = tmp3 - tmp
            await editmess(tmp2, "Took **{}ms**".format(str(int(tmp4.total_seconds() * 1000))))
        elif stwi('^pi'):
            await sendmess(channelmess, str(math.pi))
        elif stwi("^give "):
            with open('bot_itemsid.json', 'r') as file:
                data = json.load(file)
            stuff = contentmess[6:].split(':')
            itemname = ""
            amount = 1
            tmp = stuff[0].find('x')
            itemid = stuff[0]
            if len(stuff) > 1:
                itemmeta = stuff[1]
            if stuff[0].find('x') != -1 and len(stuff) == 1:
                amount = stuff[0][tmp + 1:]
                itemid = str(stuff[0][:tmp])
                itemid = itemid.replace(" ", '')
            if len(stuff) != 1 and stuff[1].find('x') != -1:
                tmp = stuff[1].find('x')
                amount = stuff[1][tmp + 1:]
                itemmeta = str(int(stuff[1][:tmp]))
            print("id({}) meta() stuff({})".format(itemid, stuff))
            for i in data:
                if len(stuff) == 1:
                    if str(i['type']) == itemid or i['text_type'] == itemid or "minecraft:"+i['text_type'] == 'minecraft'+itemid:
                        itemname = str(i['name'])
                        break
                else:
                    if str(i['meta']) == itemmeta and (str(i['type']) == itemid or i['text_type'] == itemid or "minecraft:"+i['text_type'] == 'minecraft'+itemid):
                        itemname = str(i['name'])
                        break
            if itemname != "":
                await sendmess(channelmess, "Given [{}] x {} to {}".format(itemname, str(amount), authormess.name))
            else:
                await sendmess(channelmess, "invalid id")
        elif stwi('^weirdfy '):
            await sendmess(channelmess, MatStuff.uppLetters(contentmess[9:]))
        elif stwi('^db64xtimes '):
            string = contentmess[12:]
            Decode = True
            while Decode:
                try:
                    string = base64.b64decode(bytes(string, 'utf-8')).decode('utf-8')
                except Exception as e:
                    Decode = False
                    pass
            await sendmess(channelmess, string)














        elif stwi(''):
            tmp = open('botconfig.txt', 'r+')
            tmp2 = tmp.readlines()
            tmp3 = tmp2[1][10:]
            tmp4 = tmp2[2][8:]
            if tmp4[:-1] == message.channel.id and tmp3[:-1] == "on":
                await client.add_reaction(message, '\N{Aubergine}')
            tmp.close()
            





client.run('aaaaaaaaa')
