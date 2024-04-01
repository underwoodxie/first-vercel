from flask import Flask, render_template, send_file

app = Flask(__name__,template_folder='../templates')
#模板文件夹位于当前文件的父级目录中的 templates 文件夹下

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/sitemap.xml')
def sitemap():
    sitemap_file_path = '../sitemap.xml'  # 替换为您的站点地图文件路径
    return send_file(sitemap_file_path, mimetype='text/xml')


if __name__ == '__main__':
    app.run(debug=True)