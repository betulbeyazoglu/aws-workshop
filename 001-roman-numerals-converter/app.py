from flask import Flask, request, render_template

app = Flask(__name__)

developer_name="Betul Beyazoglu"
not_valid=False

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html", developer_name=developer_name , not_valid=not_valid)


@app.route('/', methods=['POST'])
def convert():
    number=request.form['number']
    dict=[(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    number_roman=""
    if number.isdigit():
        number_decimal=int(number)
        if number_decimal > 0 and number_decimal < 4000:
            for i, j in dict:
                while number_decimal >= i:
                    number_roman +=j
                    number_decimal -= i
            return render_template("result.html", number_roman=number_roman, developer_name=developer_name, number_decimal=number)
        else:
            not_valid=True
            return render_template("index.html", not_valid=not_valid, developer_name=developer_name)

    else:
        not_valid=True
        return render_template("index.html", not_valid=not_valid, developer_name=developer_name)  
   

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=80)
    app.run(debug=True)