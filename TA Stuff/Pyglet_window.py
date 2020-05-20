import pyglet
import Functions
from Main import entity_map, infection_rate, recovery_rate, recovery_rate_increase, fatality_rate, \
    fatality_rate_decrease

recovery_rate_internal = recovery_rate
fatality_rate_internal = fatality_rate

cycleCount = 0

pyglet.resource.path = ["assets"]
pyglet.resource.reindex()


def centerImage(image):
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2


window = pyglet.window.Window(width=810, height=810)

background_image = pyglet.resource.image("window_background.png")
simulation_background_image = pyglet.resource.image("simulation_background.png")
entity_healthy_image = pyglet.resource.image("entity_healthy.png")
entity_infected_image = pyglet.resource.image("entity_infected.png")
entity_recovered_image = pyglet.resource.image("entity_recovered.png")
entity_dead_image = pyglet.resource.image("entity_dead.png")
top_text = pyglet.text.Label("Epidemic Simulation: Running", font_name="Lucida Grande", font_size=24,
                             x=window.width // 2,
                             y=775, anchor_x="center", anchor_y="center")

window_background = pyglet.sprite.Sprite(background_image, x=0, y=0)
window_background.scale = 0.75
simulation_background = pyglet.sprite.Sprite(simulation_background_image, x=35, y=308)
simulation_background.scale = 0.4

centerImage(background_image)
centerImage(simulation_background_image)

entity_batch = pyglet.graphics.Batch()
entity_sprites = []

centerImage(entity_healthy_image)
centerImage(entity_infected_image)
centerImage(entity_recovered_image)
centerImage(entity_dead_image)


@window.event
def on_draw():
    window.clear()
    window_background.draw()
    simulation_background.draw()
    top_text.draw()
    entity_batch.draw()


# noinspection PyPep8Naming
@window.event
def updateSprites(dt):
    global cycleCount
    cycleCount += 1
    if cycleCount == 1:
        array = entity_map
    else:
        array = Functions.tickWorld(entity_map, infection_rate, recovery_rate, fatality_rate)
    entity_sprites.clear()
    for row in range(len(array)):
        for column in range(len(array)):
            if array[row][column] == "H  ":
                entity_sprites.append(pyglet.sprite.Sprite(entity_healthy_image, (column + 1) * 40, (row + 1) * 40,
                                                           batch=entity_batch))
            elif array[row][column] == "I  ":
                entity_sprites.append(pyglet.sprite.Sprite(entity_infected_image, (column + 1) * 40, (row + 1) * 40,
                                                           batch=entity_batch))
            elif array[row][column] == "R  ":
                entity_sprites.append(pyglet.sprite.Sprite(entity_recovered_image, (column + 1) * 40, (row + 1) * 40,
                                                           batch=entity_batch))
            elif array[row][column] == "D  ":
                entity_sprites.append(pyglet.sprite.Sprite(entity_dead_image, (column + 1) * 40, (row + 1) * 40,
                                                           batch=entity_batch))
    window.clear()
    window_background.draw()
    simulation_background.draw()
    top_text.draw()
    entity_batch.draw()
    '''
    global recovery_rate_internal
    global fatality_rate_internal
    if recovery_rate_internal < 100:
        recovery_rate_internal += recovery_rate_increase
    if fatality_rate_internal > 0:
        fatality_rate_internal -= fatality_rate_decrease
    if fatality_rate_internal <= 0 and recovery_rate_internal <= 0:
        print("closing")
        window.close()
    '''


pyglet.clock.schedule_interval(updateSprites, 3)
pyglet.app.run()