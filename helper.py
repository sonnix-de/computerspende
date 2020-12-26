
import json


def loadJsonFile(filename):
    file = open(filename)
    content = file.read()
    result = json.loads(content)
    return result
