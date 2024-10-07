from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
Sky()
player = FirstPersonController()
Sky()
boxes = []

def random_color():
@@ -12,29 +14,29 @@ def random_color():
    return color.rgb(red, green, blue)

def add_box(position):
    box = Button(
    boxes.append(
        Button(
        parent=scene,
        model='cube',
        origin=0.5,
        color= random_color(), #color.blue,
        texture = 'grass', #https://stackoverflow.com/questions/66385821/how-to-make-python-ursina-engines-cube-texture
        highligt=color.lime,
        position=position
        color=random_color(),
        position=position,
        texture='grass'
      )
    )
    boxes.append(box)

for x in range(20):
    for y in range(20):
        add_box(position=(x, 0, y))
  for y in range(20):
    add_box( (x, 0, y) )

def input(key):
    for box in boxes:
        if box.hovered:
            if key == 'left mouse down':
                add_box(position=box.position + mouse.normal)
            if key == 'right mouse down':
            if key == "left mouse down":
                add_box(box.position + mouse.normal)
            if key == "right mouse down":
                boxes.remove(box)
                destroy(box)

app.run()
