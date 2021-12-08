#import modules
from simpleInterest import simple_interest
from flask import Flask, jsonify, request

# instantiate flask object
app = Flask('__name__')


@app.route('/', methods=['GET', 'POST'])
def get_input():
    """
    A flask app to take input and invoke simple interest module to process input parameter and return the interest
    """
    packet = request.get_json(force=True)

    principal = packet['principal']

    rate = packet['rate']

    period = packet['period']

    # Instantiate simple_interest object to evalute inputs

    interest = simple_interest(principal, rate, period)

    return {"interest": interest, "packet": packet}


# main driver function
if __name__ == '__main__':
    app.run(debug=True)
