from pyramid.view import view_config

@view_config(route_name='home', renderer='./templates/home.jinja2')
def home(request):
    return {}

@view_config(route_name='add', renderer='./templates/add.jinja2')
def add(request):
	return {}

@view_config(route_name='sub', renderer='./templates/sub.jinja2')
def sub(request):
	return {}

@view_config(route_name='mul', renderer='./templates/mul.jinja2')
def mul(request):
	return {}

@view_config(route_name='div', renderer='./templates/div.jinja2')
def div(request):
	return {}

@view_config(route_name='result', renderer='./templates/result.jinja2')
def resultforadd(request):
	n1=float(request.params['number1'])
	n2=float(request.params['number2'])
	return {'result':n1+n2}


@view_config(route_name='result1', renderer='./templates/result1.jinja2')
def resultforsub(request):
	n1=float(request.params['number3'])
	n2=float(request.params['number4'])
	return {'result1':n1-n2}


@view_config(route_name='result2', renderer='./templates/result2.jinja2')
def resultformul(request):
	n1=float(request.params['number5'])
	n2=float(request.params['number6'])
	return {'result2':n1*n2}

@view_config(route_name='result3', renderer='./templates/result3.jinja2')
def resultfordiv(request):
	n1=float(request.params['number7'])
	n2=float(request.params['number8'])
	return {'result3':n1/n2}
