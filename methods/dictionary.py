play = {
    'name' : 'sieun',
    'age' : 12,
    'alive' : True
}

print(play.get('age'))
print(play.get('name'))


print(play['alive'])

# play.pop('age')

play['color'] = ["blackz"]
#
# print(play)
# print(type(play['color']))
#
play['color'].append("yellow")
print(play.get('color'))

numbers = [5,3,1,5,7,3,"ture"]


sieun = {
    'name' : 'park',
    'cat' : {
        'name' : ['momo'],
        'age' : 12

    }
}

print(sieun['cat']['age'])
sieun['cat']['name'].append('rey')
print(sieun)



# 요약
# 키와 값으로 이루어져 있다
# 여러 메소드를 쓸 수 있다(리스트처럼)
# 리스트 처럼 값을 불린 리스트 스트링 등으로 모두 할 수 있다

