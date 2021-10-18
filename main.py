from os import system, name
from colors import Colors as c
import random, json
from os import path, listdir
import getkey

x = 0
y = 0
items = 0
depth = 1
def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')
def waiting():
  input("Pressez ENTER pour continuer")
  clear()
n = input("Hello. Bienvenue sur MINER. \n S'il vous plait, tapez votre pseudo \n si vous avez sauvegardé votre partie, tapez le même pseudo et d - charger\n")
gem = 0;
gold = 0;
iron = 0;
money = 0;
pickaxeLevel = 1;
backpackLevel = 1;
auraLevel = 1;
pickUpCost = 100;
backUpCost = 100;
auraUpCost = 140;
pickaxeHealth = pickaxeLevel * 20
field = [
  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
  ["0", "0", "0", "0", "#", "0", "0", "0", "0", "0"],
  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
]
counterX = 0
counterY = 0
for line in field:
  counterY += 1
  counterX = 0
  for item in line:
    counterX += 1
    a = random.randint(1,100)
    color = c.white
    if field[counterY - 1][counterX - 1] == "#":
      color = c.red
    elif a <= 10:
      color = c.magenta
    elif a >= 11 and a <= 40:
      color = c.bright_yellow
    field[counterY - 1][counterX - 1] = f"{color}{field[counterY - 1][counterX - 1]}{c.r}"
def newDepth():
  counterX = 0
  counterY = 0
  for line in field:
    counterY += 1
    counterX = 0
    for item in line:
      counterX += 1
      a = random.randint(1,100)
      color = c.white
      if field[counterY - 1][counterX - 1] == "#":
        color = c.red
      elif a <= 10:
        color = c.magenta
      elif a >= 11 and a <= 40:
        color = c.bright_yellow
      if field[counterY - 1][counterX - 1] == "#":
        field[counterY - 1][counterX - 1] = f"{color}#{c.r}"
      else:
        field[counterY - 1][counterX - 1] = f"{color}0{c.r}"
def out(f):
      for line in f:
        counter = 0
        for item in line:
          counter += 1
          if (counter != 10):
            print(f"{item} ", end="", flush=True)
          else:
            print(f"{item} ")
def start():
  print(f"Bienvenue dans LA VIE DE {n.upper()}! le but de ce jeu est de réaliser une carrière de mineur. Vous devez miner des minerais, améliorer votre équipement et essayer d'avoir le meilleur score.")
  waiting()
def findPos():
  global x, y
  for Y in range(len(field)):
    for X in range(len(field[Y])):
      if item == "#":
        x = X
        y = Y
        break
def atCoordinateMine(xCoord, yCoord):
  global iron, gem, gold, pickaxeHealth
  it = field[yCoord - 1][xCoord - 1]
  if it == f"{c.white}0{c.r}":
    iron += 1
    pickaxeHealth -= 1
    op = 1
  elif it == f"{c.bright_yellow}0{c.r}":
    gold += 1
    pickaxeHealth -= 3
    op = 1
  elif it == f"{c.magenta}0{c.r}":
    gem += 1
    pickaxeHealth -= 5
    op = 1
  else:
    op = 0
  return op
def shop():
  global money, pickaxeLevel, pickaxeHealth, backpackLevel, auraLevel, pickUpCost, backUpCost, auraUpCost, iron, gold, gem
  while True:
    print(f"niveau de la pioche: {pickaxeLevel}     taille du sac: {backpackLevel}      multiplieur de bonnes affaires: {auraLevel}      Monnaie: {money}\n ")
    while True:
      sel = input(f"Choisissez votre action: \nA: vendre tout mes minerais\nB: améliorer ma pioche: {pickUpCost}\nC: améliorer la taille du sac: {backUpCost}\nD: avoir de meilleurs prix sur les minerais: {auraUpCost}\nE: quitter la boutique.\n")
      sel = sel.lower()
      if sel not in ["a", "b", "c", "d", "e"]:
        clear()
        shop()
      else:
        break
    if sel == "a":

      clear()
      amountSold = round((iron * 1 + gold * 3 + gem * 9) * (1 + auraLevel * 0.3)) 
      iron = 0
      gold = 0
      gem = 0
      money += amountSold
      print(f"Vous vendu tout vos minerais pour{amountSold}. Vous avez désormais {money} d'argent")
      waiting()
      clear()
      shop()
    if sel == 'b':
      if money < pickUpCost:
        print(f"Vous n'avez pas assez d'argent pour améliorer votre pioche qui coûte {pickUpCost}. Minez encore un peu et revenez plus tard !")
        waiting()
        clear()
        shop()
      else:
        money -= pickUpCost
        pickaxeLevel += 1
        pickaxeHealth = 20 * pickaxeLevel
        pickUpCost *= (1 + (pickaxeLevel - 1) * 0.5)
        pickUpCost = round(pickUpCost)
        print(f"Vous avez amélioré votre pioche au niveau {pickaxeLevel}")
        waiting()
        clear()
        shop()
    if sel == "c":
      if money < backUpCost:
        print(f"Vous n'avez pas assez d'argent pour améliorer votre sac à dos, ce qui coûte {backUpCost}.  Minez encore un peu et revenez plus tard !")
        waiting()
        clear()
        shop()
      else:
        money -= backUpCost
        backpackLevel += 1
        backUpCost *= (1 + (backpackLevel - 1) * 0.5)
        backUpCost = round(backUpCost)
        print(f"Vous avez amélioré votre sac au niveau{backpackLevel}")
        waiting()
        clear()
        shop()
    if sel == "d":
      if money < auraUpCost:
        print(f"Vous n'avez pas assez d'argent pour mettre à niveau vos skill en négociation, ce qui coûte {auraUpCost}.  Minez encore un peu et revenez plus tard !")
        waiting()
        clear()
        shop()
      else:
        money -= auraUpCost
        auraLevel += 1
        auraUpCost *= (1 + (auraLevel - 1) * 0.5)
        auraUpCost = round(auraUpCost)
        print(f"Vous avez augmenté vos skill en négociation au niveau {auraLevel}")
        waiting()
        clear()
        shop()
    if sel == "e":
      clear()
      mine()


def mining():
  global x, y, items, depth, pickaxeHealth, pickaxeLevel

  while True:
    clear()
    print(f"Gem: {gem}     or: {gold}      Fer: {iron}         sac: {items}/{backpackLevel * 10}     Durabilité de la pioche: {pickaxeHealth}/{pickaxeLevel * 20}")
    out(field)
    current = getkey.getkey()
    current = current.lower()
    if current.lower() in ['w', 'a', 's', 'd']:
      prev_y = y
      prev_x = x
      if current == "w":
        if y != 1:
          put = atCoordinateMine(x, y - 1)
          if put == 1:
            items += 1
          y -= 1
        else:
          clear()
          mining()
      if current == "s":
        if y != 10:
          put = atCoordinateMine(x, y + 1)
          if put == 1:
            items += 1
          y += 1
        else:
          clear()
          mining()
      if current == "a":
        if x != 1:
          put = atCoordinateMine(x - 1, y)
          if put == 1:
            items += 1
          x -= 1
        else:
          clear()
          mining()
      if current == "d":
        if x != 10:
          put = atCoordinateMine(x + 1, y)
          if put == 1:
            items += 1
          x += 1
        else:
          clear()
          mining()
      yy = 0
      xx = 0
      for line in field:
        yy += 1
        xx = 0;
        for item in line:
          xx += 1
          if xx == x and yy == y:
            field[yy - 1][xx - 1] = f"{c.red}#{c.r}"
          elif xx == prev_x and yy == prev_y:
            field[yy - 1][xx - 1] = " "
          else:
            field[yy - 1][xx - 1] = field[yy - 1][xx - 1]
      if items >= backpackLevel * 10:
        clear()
        pickaxeHealth = pickaxeLevel * 20
        newDepth()
        mine()
      if pickaxeHealth <= 0:
        clear()
        pickaxeHealth = pickaxeLevel * 20
        newDepth()
        mine()
      if items < backpackLevel * 10 and items > 99 * depth:
        depth += 1
        newDepth()

      clear()
def mine():
  global x, y, items, n, field, gem, gold, iron, money, pickUpCost, backUpCost, auraUpCost, pickaxeLevel, backpackLevel, auraLevel, pickaxeHealth
  while True:
    print(f"Bienvenue à nouveau sur LIFE OF {n.upper()}!\n choisissez la lettre pour faire votre action:\nA: Miner\nB: aller à la boutique\nC: sauvgarder \nD: charger\nE: Tableau des leaders\nF: crédit")
    selection = input()
    selection = selection.lower()
    if selection in ["a", "b", "c", "d", "e", "f"]:
      break
    else:
      clear()
  clear()
  if selection == "a":
    field[5][4] = f"{c.red}#{c.r}"
    x = 5
    y = 6
    print("Bienvenue à la mine.")
    items = 0
    mining()
  elif selection == "b":
    print("bienvenue dans la boutique.")
    shop()
  elif selection == "c":
    with open(f"file/{n}.json", "w") as F:
      jsonFile = {"name": n, "field": field, "gem": gem, "gold": gold, "iron": iron, "money": money, "pickUp": pickUpCost, "backUp": backUpCost, "auraUp": auraUpCost, "pickLevel": pickaxeLevel, "backLevel": backpackLevel, "auraLevel": auraLevel, "pickHealth": pickaxeHealth}
      json.dump(jsonFile, F)
    print("JEU SAUVÉ")
    mine()
  elif selection == "d":
    if path.exists(f"file/{n}.json"):
      with open(f"file/{n}.json", "r") as ff:
        data = json.load(ff)
        n = data["name"]
        field = data["field"]
        gem = data["gem"]
        gold = data["gold"]
        iron = data["iron"]
        money = data['money']
        pickUpCost = data["pickUp"]
        backUpCost = data['backUp']
        auraUpCost = data['auraUp']
        pickaxeLevel = data['pickLevel']
        backpackLevel = data['backLevel']
        auraLevel = data['auraLevel']
        pickaxeHealth = data['pickHealth']
        ff.close()
      print("JEU CHARGÉ")
      mine()
    else:
      print("LE FICHIER À VOTRE NOM N'EXISTE PAS")
      mine()

  elif selection == "f":
      print(" jeu originalement crée par: aguy11")
      print("traduction en fr par: valvo_fluttershy")
      print("-------------")
      print("game created by: aguy11")
      print("tranlated in franch by: valvo_fluttershy \n")
      mine()

  elif selection == "e":
    users = []
    orderedUsers = []
    high = 0
    for filename in listdir("file"):
      print(filename)
      us = open(f"file/{filename}", 'r')
      d = us.read()
      data = json.loads(d)
      users.append([data["name"], data["money"]])
      us.close()
    for user in users:
      if high <= user[1]:
        orderedUsers.insert(0, user)
        high = user[1]
      else:
        if len(orderedUsers) == 0:
          orderedUsers.insert(0, user)
        else:
          counter = 0
          for use in orderedUsers:
            if user[1] >= use[1]:
              orderedUsers.insert(counter, user)
            else:
              if counter == len(orderedUsers) - 1:
                orderedUsers.append(user)
              else:
                continue
            counter += 1
      clear()
      print("LEADERBOARD")
      counter = 0
      for u in orderedUsers:
        counter += 1
        if counter <= 5:
          print(f"{counter}) {u[0]}........{u[1]}")
          print("\nj'ai pu aprercevoir le problème du leaderboard chez aguy11, le créateur du jeu. La seul solution pour le moment est que vous me dites en commantaire vos stats. je les ajouterai au jeu toutes les semaines. SVP n'utilisez pas le compte des autres!")
        else:
          break

      waiting()
      clear()
      mine()

    



    
start()
mine()
