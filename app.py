from flask import Flask,url_for,abort,render_template,jsonify
#导入基类转换器 使用父类中的某些方法,并且重写父类的某些方法
from werkzeug.routing import BaseConverter

app = Flask(__name__)

debug=True
# 1.自定义类,继承自BaseConverter
class MyRegexConverter(BaseConverter):

    # 2.编写初始化方法, init方法, 接收两个参数, url_map, regex, 并初始化父类空间和子类空间
    def __init__(self,url_map,regex):
        super(MyRegexConverter, self).__init__(url_map)
        self.regex = regex

# 3.将自定义转换器类,添加到默认的转换列表中
app.url_map.converters['re'] = MyRegexConverter

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/demo")
def demo():
    return url_for('demo')
@app.route('/response1')
def response1():
    info={
        "id":1,
        "name":"lala"
    }
    return info
# @app.route('/demo1/<re("\d{3}"):num>')
@app.route('/demo1/<int:num>')
def demo1(num):
    abort(404)#强制弹出异常 按异常代码规则弹出
    return "demo1:%s"%num

@app.errorhandler(404)
def errtest():
    return render_template("404.html")

@app.route('/goods_detail/<int:goods_id>',methods=["get","post"])
def  good_detail(goods_id):
    return "商品的id是%s"%goods_id

if __name__ == '__main__':
    app.run()