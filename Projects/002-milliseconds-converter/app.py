from flask import Flask, request, render_template

app = Flask(__name__)

developer_name="Betul Beyazoglu"
not_valid=False

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html", developer_name=developer_name , not_valid=False)

@app.route('/', methods=['POST'])
def ms_converter():
    time=""
    number=request.form['number']
    if number.isdigit():
        num=int(number)
        if num > 0 and num< 1000:
            msec=num
            return render_template("result.html", milliseconds=number, result=f"just {msec} millisecond/s", developer_name=developer_name)
        elif num>=1000:
            hour=num//3600000
            if hour:
                time+=f"{hour} hour/s "
            min=(num%3600000)//60000
            if min:
                time+=f"{min} min/s "    
            sec=(num%60000)//1000
            if sec:
                time+=f"{sec} second/s"
            return render_template("result.html", milliseconds=num, result=time, developer_name=developer_name)     
        else:
            return render_template("index.html", not_valid=True, developer_name=developer_name)
    else:
        return render_template("index.html", not_valid=True, developer_name=developer_name)

if __name__=='__main__':
    #app.run(host='0.0.0.0', port=80)
    app.run(debug=True)