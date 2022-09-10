#this will by attempt to make a simple flask application
#now this flask API is retruning you with card number 10 at a time. Now lets make sure that these card numbers are actually valid! 
from flask import Flask, jsonify, render_template
import random


app = Flask(__name__)


@app.route("/", methods=["GET","POST"])
def get_some():
    count=0
    card_list = []
    while 1:
        try:
            card_number = get_a_card_number()
            if validate_card(card_number):
                card_list.append(card_number)
                count+=1
                if count==10:
                    raise Exception
        except Exception:
            break
    

    return render_template("index.html", data=card_list)


def get_a_card_number():
    card_number = f"{random.randint(0,9999):04} {random.randint(0,9999):04} {random.randint(0,9999):04} {random.randint(0,9999):04}"
    return card_number


#now let's make sure that these are valid card nunbers
def validate_card(card_number):
    card_number = card_number.replace(" ","")
    part1 = [int(i) for i in list(card_number[-1::-2])]
    part2 = [absolute_sum(2*int(i)) for i in list(card_number[-2::-2])]
    sum_val = sum(part1) + sum(part2)
    if sum_val%10==0:
        return True
    else:
        return False


def absolute_sum(val):
    hash_map = {
        10:1,
        12:3,
        14:5,
        16:7,
        18:9
    }
    return hash_map.get(val,val)



if __name__ == "__main__":
    app.run(debug=True)