import logging
 
 #basic log
logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s -- %(levelname)s -- %(message)s"

)
logger=logging.getLogger()


#for ui

def last_log():
    try:
        with open("bot.log", "r") as f:
            lines = f.readlines()
            if lines:
                return lines[-1]
    except:
        return "No logs yet"