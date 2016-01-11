# -*- coding: utf-8 -*-


#蓝本中定义程序路由


from datetime import datetime
from flask import render_template,session,redirect,url_for


from . import main
from .forms import NameForm
from .. import db
from .. models import User


@main.route('/',methods = ['GET','POST')
def index():
	name = None
	form = NameForm()
	if form.validate_on_submit():
		old_name = session['name']
		if old_name is not None and old_name != form.name.data:
			flash(u'looks your changed your name')#仅调用flash（）并不能把消息显示出来。需要在模板中渲染Flash消息
		session['name'] = form.name.data #相当于NSUserDefaluts.像dict一样使用它
		return redirect(url_for('.index'))#redirect()重定向  url_for()传入端点名。即响应视图函数的函数名
										#在蓝本中使用时，要在端点名前加上命名空间。main.index....省略微.index
	return render_template('index.html',
							form=form,
							name=session.get('name'),
							known=session.get('known',False),
							current_time=datetime.utcnow())

