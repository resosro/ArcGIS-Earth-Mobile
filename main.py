import os

if __name__ == "__main__":
    path = os.path.join('report.json')
    print(path)
    open(path, 'w')
    # with open(path, 'w') as path:
    #     path.write("{}")