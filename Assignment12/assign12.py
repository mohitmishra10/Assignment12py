from games import roll_dice,add_quiz,mul_quiz,number_guess,rock_paper_scissor

class exception1(Exception):
    def __init__(self, *args):
        super().__init__(*args)

f =open("Record.txt","+at")

a = True
while a == True:
    print("This is a menu driven progrsm")
    print("Games: \n1)Addition quiz \n2)Multiplication quiz \n3)Number guess \n4)Rock paper scissor \n5)Roll dice")
    num = int(input("Enter your choice in num :"))
    if num == 1:
        add_quiz.addition_quiz()
        f.write("Addition quiz \n")

    elif num == 2:
        mul_quiz.multiplication_quiz()
        f.write("Multiplication quiz \n")

    elif num == 3:
        number_guess.num_guess()
        f.write("Number guess \n")

    elif num == 4:
        rock_paper_scissor.rps()
        f.write("Rock Paper Scissor \n")

    elif num == 5:
        roll_dice.dice_rolling_simulator()
        f.write("Roll dice \n")

    else :
        try:
            raise exception1("Invalid choice!")
        except exception1 as e:
            print(e.args[0])
        break