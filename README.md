练习网站：https://www.caloriecounter.cn/

vercel.json的设置在根目录下，api的文件也在目录下，py文件放在api文件下 { "version": 2, "builds": [ { "src": "api/main.py", "use": "@vercel/python" //设置api文件夹下的main.py用python运行，如果其他文件需要python运行，可以用*.py来指定 } ], "routes": [ { "src": "/api/(.*)", "dest": "/api/main.py" //打开网站首页时将请求返回给main.py } ] }

使用Flask返回前端html时，这时候py文件跟html不在同一个目录下，通过设置路径来解决这个问题 app = Flask(name,template_folder='../templates') #模板文件夹位于当前文件的父级目录中的 templates 文件夹下。../filename 能找到不同目录下的文件