from flask import Flask, request, render_template

app = Flask(__name__)

developer_name="Betul Beyazoglu"
not_valid=False

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html", developer_name=developer_name , not_valid=not_valid)

@app.route('/', methods=['POST'])
def ms_converter():
    number=request.form['number']
    if number.isdigit():
        num=int(number)
        if num > 0 and num< 1000:
            msec=num
            return render_template("result.html", milliseconds=number, result=f"just {msec} millisecond/s", developer_name=developer_name)
        elif num>=1000:
            hour=num//3600000
            min=(num%3600000)//60000
            sec=(num%60000)//1000
            if hour!=0 and min!=0 and sec!=0:
                return render_template("result.html", milliseconds=num, result=f"{hour} hour/s {min} minute/s {sec} second/s", developer_name=developer_name)
            elif hour!=0 and min!=0 and sec==0:
                return render_template("result.html", milliseconds=num, result=f"{hour} hour/s {min} minute/s", developer_name=developer_name)
            elif hour!=0 and min==0 and sec!=0:
                return render_template("result.html", milliseconds=num, result=f"{hour} hour/s {sec} second/s", developer_name=developer_name)
            elif hour!=0 and min==0 and sec==0:
                return render_template("result.html", milliseconds=num, result=f"{hour} hour/s", developer_name=developer_name)
            elif hour==0 and min!=0 and sec!=0:
                return render_template("result.html", milliseconds=num, result=f"{min} minute/s {sec} second/s", developer_name=developer_name)
            elif hour==0 and min!=0 and sec==0:
                return render_template("result.html", milliseconds=num, result=f"{min} minute/s", developer_name=developer_name)
            elif hour==0 and min==0 and sec!=0:
                return render_template("result.html", milliseconds=num, result=f"{sec} second/s", developer_name=developer_name)
            
        else:
            not_valid=True
            return render_template("index.html", not_valid=not_valid, developer_name=developer_name)
    else:
        not_valid=True
        return render_template("index.html", not_valid=not_valid, developer_name=developer_name)

if __name__=='__main__':
    #app.run(host='0.0.0.0', port=80)
    app.run(debug=True)