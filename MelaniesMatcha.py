# all variables stored as teaspoons(US)

from sys import argv

if len(argv) >= 1:
	file, servings = argv
else:
	servings = 1

matcha = float(servings) * 1.5
turmeric = float(servings) * 0.75
cinnamon = float(servings) / 8
coco_oil = float(servings) * 2


print(f"""
	Melanie's Matcha:
	{servings} servings requires:
	{round(coco_oil / 3, 1)} tablespoons of Coconut Oil ({round(coco_oil / 48.69221, 2)} cups)
	{round(matcha / 3, 1) } tablespoons of Matcha powder ({round(matcha / 48.69221, 2)} cups)
	{round(turmeric / 3, 1)} tablespoons of Turmeric
	{round(cinnamon, 2)} teaspoons of Cinnamon """)