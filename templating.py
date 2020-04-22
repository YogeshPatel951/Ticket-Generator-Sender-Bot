from jinja2 import Environment, FileSystemLoader
def generate(data):
    folder=FileSystemLoader('templates')
    env = Environment(
        loader=folder,
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
   )
    template=env.get_template('message.txt')
    message = template.render(data=data,status=data[5])
    print('message generated')
    return message

