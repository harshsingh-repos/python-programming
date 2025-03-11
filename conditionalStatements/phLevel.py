
def phLevel(ph):
    """
    function defination
    """
    if ph >=0 and ph <=4:
        print(f"Strong Acid : {ph}")
    elif ph >=5 and ph<=6:
        print(f"Weak Acid : {ph}")
    elif ph == 7:
        print(f"Neutral : {ph}")
    elif ph>=8 and ph <= 9:
        print(f"Weak Basic : {ph}")
    elif ph>=10 and ph<=14:
        print(f"Strong Base : {ph}")
    else: 
        print(f"Invalid Input : {ph}")


phLevel(1) #calling the function
phLevel(11)
phLevel(9)
phLevel(7)
phLevel(-1)
phLevel(5)