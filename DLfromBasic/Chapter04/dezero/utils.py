import os
import subprocess


def _dot_var(v, verbose=False):
	dot_var = '{} [label="{}", color=green, style=filled]\n'

	name = '' if v.name is None else v.name
	if verbose and v.data is not None:
		if v.name is not None:
			name += ': '
		name += str(v.shape) + ' ' + str(v.dtype)
	return dot_var.format(id(v), name)

def _dot_func(f):
	dot_func = '{} [label="{}", color=darkgreen, style=filled, shape=box, fontcolor=white]\n'
	txt = dot_func.format(id(f), f.__class__.__name__)

	dot_edge = '{} -> {}\n'
	for x in f.inputs:
		txt += dot_edge.format(id(x), id(f)) #인풋에서 함수로
	for y in f.outputs:
		txt += dot_edge.format(id(f), id(y())) # 함수에서 아웃풋으로, weakref라서 이렇게
	return txt

def get_dot_graph(output, verbose=True):
	txt = ''
	funcs = []
	seen_set = set()

	def add_func(f):
		if f not in seen_set:
			funcs.append(f)
			seen_set.add(f)

	add_func(output.creator)
	txt += _dot_var(output, verbose)
	while funcs:
		func = funcs.pop()
		txt += _dot_func(func)
		for x in func.inputs:
			txt += _dot_var(x, verbose)

			if x.creator is not None:
				add_func(x.creator)
	return 'digraph g {\n' + txt + '}'

def plot_dot_graph(output, verbose=True, to_file='graph.png'):
	dot_graph = get_dot_graph(output, verbose)

	tmp_dir = os.path.join(os.path.expanduser('~'), '.dezero') #숨김디렉으로..
	if not os.path.exists(tmp_dir):
		os.mkdir(tmp_dir)
	graph_path = os.path.join(tmp_dir, 'tmp_graph.dot') # 그 속에 파일이름 넣기

	with open(graph_path, 'w') as f:
		f.write(dot_graph)

	extension = os.path.splitext(to_file)[1][1:] # 확장자를 뚝 잘라주는 함수!
	cmd = 'dot {} -T {} -o {}'.format(graph_path, extension, to_file)
	print(cmd)
	subprocess.run(cmd, shell=True) #shell없어도 실행은 된다.

	try:
		from IPython import display
		return display.Image(filename=to_file)
	except:
		pass