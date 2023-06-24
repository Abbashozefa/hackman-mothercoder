from flask import Flask,render_template,request


temp=Flask(__name__)


@temp.route('/',methods=['GET','POST'])
def hello():
    username= request.args.get('email')
    print(username)
    return render_template('temp.html')


if __name__=='__main__':
    temp.run(port=5000,debug=True)