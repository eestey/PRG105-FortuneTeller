import random

aa = ("Maybe", "It seems so", "I am not sure", "Yes", "No", "Don't count on it", "The world may never know",
      "The odds are in your favor", "Try again", "Definitely", "Unlikely", "Not sure", "Perhaps", "Ask again later", "You'll be lucky", "Without a doubt", "Most likely")
answer_set = set([])
while True:
    choice = raw_input("Type 'Hello' to ask a question.")
    if choice == "Hello":
        raw_input("Please enter your question:\n")
        bb = random.randint(0, len(aa) - 1)
        answer = aa[bb]
        answer_set.add(answer)
        print answer
        raw_input()
    else:
        print "Error -- Try again\n"
    sorted_list = sorted(answer_set)
    print sorted_list
