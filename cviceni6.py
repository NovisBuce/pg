import json

data = [
    {'Jmeno': 'Alice', 'vek': 20}, 
    {'Jmeno': 'Bob', 'vek': 25}, 
    {'Jmeno': 'Dave', 'vek': 31}, 
    {'Jmeno': 'Monika', 'vek': 28}
]

if __name__ == "__main__":
    with open("data.json", "r") as fp:
          json_data2 = fp.read()
          data2 = json.loads(json_data2)

    data2.pop(0)
print(data2)