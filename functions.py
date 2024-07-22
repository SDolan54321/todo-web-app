FILEPATH = "todos.txt"

def get_todos(filepath= FILEPATH):
	with open(filepath, 'r') as f:
		todos_local = f.readlines()
		#todos_local = f.read().splitlines()
	return todos_local


def write_todos(todos_arg, filepath= FILEPATH):
	with open(filepath, 'w') as f:
		f.writelines(todos_arg)

#cli.py will try to execute this along with the functions above
#print("Hello from functions")


if __name__ == "__main__":
	print("Hello from functions")