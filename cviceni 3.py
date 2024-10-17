def my_range(start, stop, step=1):
    
    #Nase vlastni implementace range(), chceme, aby se chovala uplne stejne jako range
    
    my_range = []
    i = 0
    while i < 10:
        my_range.append(i)
        i = i + 1
    print(my_range)
    
   # result = []
   # value = start
   # while value < stop:
   #     result.append(value)
   #     value += step
  #  return value


def my_enumerate(iterable, start=0):
    """
    Nase vlastni implementace enumerate()
    """
    result = []
    index = start
    for value in iterable:
        result.append((index, value))
        index += 1
    return result

def while_enumerat(iterable, start=0):
    result=[]
    while i < len(iterable):
        result.append((i, iterable[i]))
        i += 1
    return result

def my_zip(*iterables, start=1):
    """
    Nase vlastni implementace zip()
    """
    results = []
    lenght = len(iterables[0])
    for i in range(0,lenght):
        subresult = []
        for j in range(0, len(iterables)):
            subresult.append(iterables[j][i])
        results.append(tuple(subresult))

    return results

if __name__ == "__main__":

   # print(list(range(1, 10)))
  #  print(my_range(1, 10, 1))


#    print(list(enumerate("abcdef")))
#    print(while_enumerat("abcdef"))
#
#    print(list(enumerate(['Alice','Bob', 'Eva' ])))
#
    #jmena = ['Alice','Bob', 'Eva' ]
    #i = 0
    #jednojmeno = jmena[i]
    #while i < len(jmena):
    #    print(jmena[i])
    #    i = i + 1

  #  for i, char in enumerate(jednojmeno):
    #    print(f'Znak: {char}, index: {i}')
    my_zip([1,2,3], [4,5,6], [7,8,9], [10,11,12], ["a", "b", "c"])

    print(list(zip([1,2,3], [4,5,6], [7,8,9], [10,11,12], ["a", "b", "c"])))
    print(my_zip([1,2,3], [4,5,6], [7,8,9], [10,11,12], ["a", "b", "c"]))
