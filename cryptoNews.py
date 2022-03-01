from random import randrange #randomiser

#the speculative question
spec = ["Could", "Will", "Does","Evidence suggests that"]

#both the actors and the recipients of the action
actors = ["Satoshi Nakamoto", "China", "Central Banks", "Elon Musk","the Fed", "Bitcoin Miners","El Salvador", "Environmentalists", "Janet Yellen", "Donald Trump", "Joe Biden", "the Bank of England", "the SEC", "HMRC", "MicroStrategy", "Jack Dorsey", "Twitter", "Bitcoin Whales", "the Queen", "Ripple", "Binance", "technical analysts", "Youtubers", "Tik tok creators",]

#the action that is causing the worry
causes = ["buying", "mining", "burning", "selling", "taxing", "hacking", "rugging", "hodling", "trading",]

#the thing that is at the centre of the controversy
assets = ["fiat money", "Bitcoin", "Ethereum", "DogeCoin", "Gold", "the dollar", "XRP holders", "cash", "CBDCs", "Litecoin", "Trumpcoin", "Shiba Inu", "candlestick charts",]

#what might happen
effects = ["destroy", "give cancer to", "crash", "melt", "burn", "enslave", "wipe out", "sabotage", "swallow up", "ravish", "liquidate", "bolster", "make millionaires of", "launch", "support", "cushion", "enrich", "enhance",]

while True:
  print(spec[randrange(0,len(spec)-1)] +" "+ actors[randrange(0,len(actors)-1)] + " " + causes[randrange(0,len(causes)-1)] + " " + 
   assets[randrange(0,len(assets)-1)] + " " +
   effects[randrange(0,len(effects)-1)] + " " +
   actors[randrange(0,len(actors)-1)] + "?"
  )
  break
