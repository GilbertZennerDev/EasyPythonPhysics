from direct.showbase.ShowBase import ShowBase
from panda3d.core import AmbientLight, DirectionalLight, CardMaker
import random

class FloatingSpheresDemo(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.disableMouse()
        self.camera.setPos(0, -20, 0)
        self.setBackgroundColor(0.1, 0.1, 0.2, 1)
        self.create_spheres(1)
        self.add_lights()
        self.taskMgr.add(self.move_spheres_task, 'MoveSpheresTask')

    def create_spheres(self, count):
        self.spheres = []
        self.directions = []
        size = 5 * 0.45
        for _ in range(count):
            sphere = self.loader.loadModel('models/misc/sphere')
            x = random.uniform(-size, size)
            y = random.uniform(-size, size)
            z = random.uniform(-size, size)
            sphere.setPos(x, y, z)
            sphere.setScale(0.5)
            sphere.setColor(random.random(), random.random(), random.random(), 1)
            sphere.reparentTo(self.render)
            self.spheres.append(sphere)
            # Random initial direction
            direction = (
                random.uniform(-0.05, 0.05),
                random.uniform(-0.05, 0.05),
                random.uniform(-0.05, 0.05)
            )
            self.directions.append(direction)

    def add_lights(self):
        alight = AmbientLight('alight')
        alight.setColor((0.5, 0.5, 0.5, 1))
        alnp = self.render.attachNewNode(alight)
        self.render.setLight(alnp)

        dlight = DirectionalLight('dlight')
        dlight.setColor((1.0, 1.0, 1.0, 1))
        dlnp = self.render.attachNewNode(dlight)
        dlnp.setHpr(45, -45, 0)
        self.render.setLight(dlnp)

    def move_spheres_task(self, task):
        size = 5 * 0.45
        for i, sphere in enumerate(self.spheres):
            pos = sphere.getPos()
            dx, dy, dz = self.directions[i]
            # Predict new position
            new_x = pos.x + dx
            new_y = pos.y + dy
            new_z = pos.z + dz
            # Bounce off cube walls
            if not -size <= new_x <= size:
                dx = -dx
            if not -size <= new_y <= size:
                dy = -dy
            if not -size <= new_z <= size:
                dz = -dz
            self.directions[i] = (dx, dy, dz)
            sphere.setPos(pos.x + dx, pos.y + dy, pos.z + dz)
        return task.cont

app = FloatingSpheresDemo()
app.run()
