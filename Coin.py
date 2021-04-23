playagain = "yes"
while playagain.lower() == "yes":
    coin = ["Head","Tails"]
    import random

    toss = random.choice(coin)
    guess = input("Enter Head or Tails:")
    if guess == toss:
        print("WE WON")
    else:
        print("WE LOSE")
    playagain = input("Do You Want To Play Again?"





































