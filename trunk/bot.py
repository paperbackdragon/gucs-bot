import threading
import Input
import Output 
from Irc.irc import Irc

# Settings
CHANNEL = "##GUCS"

irc = Irc()
irc.connect("irc.freenode.net") 
irc.set_info("tehCat", "George the Cat")

irc.join(CHANNEL)
irc.me(CHANNEL, "purrs")

Input.Input(irc).start()
Output.Output(irc).start()
