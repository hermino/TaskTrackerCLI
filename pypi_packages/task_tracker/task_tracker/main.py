from .task import TaskManager

def main():
    t = TaskManager.create_task("uma task")
    a = vars(t)
    print(a)
    print(t.description)


if __name__ == "__main__":
    main()