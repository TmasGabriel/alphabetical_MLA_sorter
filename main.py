import pyperclip

names = input()
names_list = names.replace(' &', '').split('.,')
sorted_names = sorted(names_list)

new_order = ''
for i, name in enumerate(sorted_names):
    name = name.strip()
    if name[-1] != ".":
        name += "."
    if i != len(sorted_names) - 1:
        new_order += name + ", "
    else:
        new_order += "& " + name

pyperclip.copy(new_order)
print(new_order)
print('correct order copied to clipboard')
