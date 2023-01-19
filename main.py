from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('block')
env = Environment(loader=file_loader)
tm = env.get_template('main.html')
msg = tm.render(title='Домашнеее задание', homework='Страница с домашним заданием',
                note='Домашнее задание выполнено !!!')
print(msg)
