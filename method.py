def get_method():
  while True:
    try:
      user_method = int(input("Which method do you want to play, press 1 for infinity ♾️ , 2 for round 🏆: "))
      if user_method == 1:
        return 1
      elif user_method == 2:
        return 2
      else:
        print("please choose in-between mode 1 and 2")
    except ValueError:
      print("Please Choose Between Mode 1 and 2")