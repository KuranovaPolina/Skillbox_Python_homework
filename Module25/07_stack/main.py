class MyStack:
    def __init__(self):
        self.elements = []

    def add(self, e):
        self.elements.append(e)

    def delete(self):
        del self.elements[-1]


class TaskManager:
    def __init__(self):
        self.tasks = MyStack()

    def new_task(self, str1, int1):
        self.tasks.add([str1, int1])

    def out(self):
        result = {}
        for e in self.tasks.elements[::-1]:
            if e[1] not in result.keys():
                result[e[1]] = e[0]
            else:
                result[e[1]] = e[0] + "; " + result.pop(e[1])

        for i in sorted(result.keys()):
            print(i, result[i])

    # def delete(self, task):
    #     for e in self.tasks.elements[::-1]:
    #         pass


# first = MyStack()
# first.add(1)
# first.add(2)
# first.add(3)
#
# print(first.elements)
# first.delete()
# print(first.elements)

manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
manager.tasks.delete()
manager.out()

# зачтено
