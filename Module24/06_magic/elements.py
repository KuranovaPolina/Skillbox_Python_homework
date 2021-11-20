class Water:
    def __add__(self, other):
        try:
            if type(other) == Air:
                return Storm()
            elif type(other) == Fire:
                return Steam()
            elif type(other) == Earth:
                return Mud()
            elif type(other) == Vanisher:
                return Nothing()
            else:
                raise BaseException
        except BaseException:
            print("You can't connect it")


class Air:
    def __add__(self, other):
        try:
            if type(other) == Water:
                return Storm()
            elif type(other) == Fire:
                return Lightning()
            elif type(other) == Earth:
                return Dust()
            elif type(other) == Vanisher:
                return Nothing()
            else:
                raise BaseException
        except BaseException:
            print("You can't connect it")


class Fire:
    def __add__(self, other):
        try:
            if type(other) == Water:
                return Steam()
            elif type(other) == Air:
                return Lightning()
            elif type(other) == Earth:
                return Lava()
            elif type(other) == Vanisher:
                return Nothing()
            else:
                raise BaseException
        except BaseException:
            print("You can't connect it")


class Earth:
    def __add__(self, other):
        try:
            if type(other) == Water:
                return Mud()
            elif type(other) == Air:
                return Storm()
            elif type(other) == Fire:
                return Lava()
            elif type(other) == Vanisher:
                return Nothing()
            else:
                raise BaseException
        except BaseException:
            print("You can't connect it")


class Vanisher:
    def __add__(self, other):
        return Nothing()


class Storm:
    Name = 'Storm'

    def __add__(self, other):
        try:
            if type(other) == Vanisher:
                return Nothing()
            else:
                raise BaseException
        except BaseException:
            print("You can't connect it")


class Steam:
    Name = 'Steam'

    def __add__(self, other):
        try:
            if type(other) == Vanisher:
                return Nothing()
            else:
                raise BaseException
        except BaseException:
            print("You can't connect it")


class Mud:
    Name = 'Mud'

    def __add__(self, other):
        try:
            if type(other) == Vanisher:
                return Nothing()
            else:
                raise BaseException
        except BaseException:
            print("You can't connect it")


class Lightning:
    Name = 'Lightning'

    def __add__(self, other):
        try:
            if type(other) == Vanisher:
                return Nothing()
            else:
                raise BaseException
        except BaseException:
            print("You can't connect it")


class Dust:
    Name = 'Dust'

    def __add__(self, other):
        try:
            if type(other) == Vanisher:
                return Nothing()
            else:
                raise BaseException
        except BaseException:
            print("You can't connect it")


class Lava:
    Name = 'Lava'

    def __add__(self, other):
        try:
            if type(other) == Vanisher:
                return Nothing()
            else:
                raise BaseException
        except BaseException:
            print("You can't connect it")


class Nothing:
    Name = 'Nothing'
