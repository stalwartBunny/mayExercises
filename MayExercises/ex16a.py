from sys import argv

script, filename = argv

txt = open(filename)
print("Press return to have your file displayed.")
input("___?___")
print(txt.read())
print("*Unrelated Admin Notice: Touch grass, tarnished undead.*")
