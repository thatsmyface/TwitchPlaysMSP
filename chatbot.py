import sys
import irc.bot
import requests
import time
import threading

import draw


class TwitchBot(irc.bot.SingleServerIRCBot):

    def __init__(self, username, client_id, token, channel):
        self.client_id = client_id
        self.token = token
        self.channel = '#' + channel
        self.curCol = "black"
        self.votesT = 0
        self.votesC = 0
        self.votesDict = {}
        self.running = False
        self.percent = 0
        # draw.randomThing()
        def checkTimer():
            if (self.percent >= 50):
                print("Still Good - Restarting")
                draw.save()
                draw.randomThing()
                self.votesDict = {}
                self.votesT = 0
                self.votesC = 0
                self.percent = recalc(self.votesT, self.votesC, self.t, "", "", self.running)
                self.t = threading.Timer(60, checkTimer)
                
            else:
                print("No longer good")
                self.t = threading.Timer(60, checkTimer)
            self.running = False

        self.t = threading.Timer(60, checkTimer)

        # Get the channel id, we will need this for v5 API calls
        url = 'https://api.twitch.tv/kraken/users?login=' + channel
        headers = {'Client-ID': client_id, 'Accept': 'application/vnd.twitchtv.v5+json'}
        r = requests.get(url, headers=headers).json()
        self.channel_id = r['users'][0]['_id']

        # Create IRC bot connection
        server = 'irc.chat.twitch.tv'
        port = 6667
        print 'Connecting to ' + server + ' on port ' + str(port) + '...'
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port, 'oauth:'+token)], username, username)
        

    def on_welcome(self, c, e):
        print 'Joining ' + self.channel

        # You must request specific capabilities before you can use them
        c.cap('REQ', ':twitch.tv/membership')
        c.cap('REQ', ':twitch.tv/tags')
        c.cap('REQ', ':twitch.tv/commands')
        c.join(self.channel)

    def on_pubmsg(self, c, e):

        # If a chat message starts with an exclamation point, try to run it as a command
        if e.arguments[0][:1] == '!':
            cmd = e.arguments[0].split(' ')[0][1:]
            self.do_command(e, cmd)
        return

    def do_command(self, e, cmd):
        c = self.connection

        if cmd == "draw":
            try:
                #get username of sent message
                messager = e.source.split('!')[0]

                #get chosen moveVals from message
                pos = e.arguments[0].split("draw ",1)[1]
                xModif = pos.split(" ",1)[0]
                yModif = pos.split(" ",1)[1]

                #log and do change
                print('Drawing from currentPos with deltax:'+xModif+" deltaY:"+yModif+" because of "+messager)
                draw.draw(xModif, yModif)

            except:
                c.privmsg(self.channel, "@" + messager + " used invalid syntax. Try \"!draw [xChange] [yChange]\"")

        elif cmd == "move":
            try:
                #get username of sent message
                messager = e.source.split('!')[0]

                #get chosen moveVals from message
                pos = e.arguments[0].split("move ",1)[1]
                xModif = pos.split(" ",1)[0]
                yModif = pos.split(" ",1)[1]

                #log and do change
                print('Drawing from currentPos with deltax:'+xModif+" deltaY:"+yModif+" because of "+messager)
                draw.draw(xModif, yModif)

            except:
                c.privmsg(self.channel, "@" + messager + " used invalid syntax. Try \"!draw [xChange] [yChange]\"")

        elif cmd == "drawfrom":
            try:
                #get username of sent message
                messager = e.source.split('!')[0]

                #get chosen moveVals from message
                argsString = e.arguments[0].split("drawfrom ",1)[1]
                args = argsString.split()

                xS = args[0]
                yS = args[1]
                xF = args[2]
                yF = args[3]

                #log and do change
                print('Drawing from ('+xS+", "+yS+") to ("+xF+","+yF+") because of "+messager)
                draw.drawStart(xS,yS,xF,yF)
            except:
                c.privmsg(self.channel, "@" + messager + " used invalid syntax. Try \"!drawfrom [xStart] [yStart] [xFinal] [yFinal]\"")

        elif cmd=="fill":
            try:
                #get username of sent message
                messager = e.source.split('!')[0]

                #get chosen moveVals from message
                argsString = e.arguments[0].split("fill ",1)[1]
                args = argsString.split()
                if (len(args)==3):
                    x = args[0]
                    y = args[1]
                    color = args[2]
                elif (len(args)==1):
                    x = 480
                    y = 293
                    color = args[0]

                draw.fill(x,y,color)
                print('Filled \"'+ str(color)+"\" @ ("+str(x)+","+str(y)+") because of "+str(messager))
                pColNum = draw.colToNum(self.curCol)
                draw.colorChangeAgain(pColNum)
            except:
                c.privmsg(self.channel, "@" + messager + " used invalid syntax. Unknown color? Try \"!fill [x] [y] [color]\"")
        
        elif cmd=="color":
            try:
                #get username of sent message
                messager = e.source.split('!')[0]

                #get chosen moveVals from message
                argsString = e.arguments[0].split("color ",1)[1]

                color = argsString
                draw.colorChange(draw.colToNum(str(color)))
                print('Changed color to \"'+color+"\" because of "+messager)
                self.curCol = str(color)
            except:
                c.privmsg(self.channel, "@" + messager + " used invalid syntax. Unknown color? Try \"!color [color]\"")
        
        elif cmd=="complete":
            messager = e.source.split('!')[0]

            try:
                if (self.votesDict[str(messager)] == "incomplete"):
                    self.votesC+=1
                    c.privmsg(self.channel, "@" + messager + ", your vote has been changed.")
                else:
                    c.privmsg(self.channel, "@" + messager + ", your vote has already been recorded.")
            except:
                self.votesT+=1
                self.votesC+=1
                c.privmsg(self.channel, "@" + messager + ", your vote has been recorded.")

            self.percent = recalc(self.votesT, self.votesC, self.t, c, self.channel, self.running)
            if (self.running == False):
                if (self.percent >= 50):
                    self.running=True
            self.votesDict[str(messager)] = "complete"

        elif cmd=="incomplete":
            messager = e.source.split('!')[0]
            
            try:
                if (self.votesDict[str(messager)] == "complete"):
                    self.votesC-=1
                    c.privmsg(self.channel, "@" + messager + ", your vote has been changed.")
                else:
                    c.privmsg(self.channel, "@" + messager + ", your vote has already been recorded.")                    
            except:
                self.votesT+=1
                c.privmsg(self.channel, "@" + messager + ", your vote has been recorded.")

            self.percent = recalc(self.votesT, self.votesC, self.t, c, self.channel, self.running)
            if (self.running == False):
                if (self.percent >= 50):
                    self.running=True
            self.votesDict[str(messager)] = "incomplete"

        elif cmd=="size":
            try:
                #get username of sent message
                messager = e.source.split('!')[0]

                #get chosen moveVals from message
                argsString = e.arguments[0].split("size ",1)[1]

                size = argsString
                draw.changeSize(size)
                print('Changed size to '+size+" because of "+messager)
            except:
                c.privmsg(self.channel, "@" + messager + " used invalid syntax. Try \"!size [1-4]\"")

        # The command was not recognized
        else:
            c.privmsg(self.channel, "Did not understand command: " + cmd)

def run(username, client_id, token, channel):
    bot = TwitchBot(username, client_id, token, channel)
    bot.start()


def recalc(total, complete, t, c, thing, running):
    try:
        percent = int(int(complete)/float(total)*100)
    except:
        percent = 0

    text_file = open("CSS-Pie-Chart-Timer-master/percent.txt", "w")
    text_file.write(str(percent))
    text_file.close()
    if (running == False):
        if (percent >= 50):
            t.start()
            running = True
            print("greater than 50 timer started")
            c.privmsg(thing, "Completion is greater than 50%. If it stays that way for more than 1 minute then the art will be saved and reset!")
        

    print("Completion: "+str(percent)+"%")
    return(percent)
