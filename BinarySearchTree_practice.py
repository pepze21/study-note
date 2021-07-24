## class & function

class Node() :
    def __init__(self) :
        Node.data = None
        Node.left = None
        Node.right = None


def addData() : # data들을 사용자에게 input 받아서, 이진트리에 저장하는 함수
    global root
    
    if root.data == None : # 최초의 input은 값을 비교하는 과정 없이 그냥 root.data에 저장.
        root.data = input('추가할 data를 입력하십시오. (끝내려면 endinput을 입력) : ')
        print(root.data, '을/를 저장했습니다')

    while True :

        current = root # 지역변수 current 정의하고, 전역변수 root가 가리키는 값으로 초기화
        node = Node()

        node.data = input('추가할 data를 입력하십시오. (끝내려면 endinput을 입력) : ')
        if (node.data == 'endinput'):
            print('저장을 마치겠습니다.')
            del(node) # 쓰레기값(object) 이렇게 없애는거 맞나? node.clear() ? node=None ?
            break
        print(node.data, '을/를 저장했습니다')


        '''
        아래는 저장할 곳을 찾아다니면서 저장하는 과정
        (저장할 node.data가 current.data 보다 작으면 왼쪽, 크면 오른쪽으로, 빈 node를 찾아다님)
        '''
        while True : 
            
            if node.data < current.data :
                if current.left == None :
                    current.left = node
                    break
                current = current.left
            elif node.data > current.data :
                if current.right == None :   
                    current.right = node
                    break
                current = current.right
            else :
                print('이미 저장되어있는 data입니다.')
                break

def searchData() : ## data를 사용자에게 input 받아서, 이진 트리에서 검색하는 함수
    global root

    while True :

        current = root
        node = Node()

        node.data = input('찾고자 하는 data를 입력하십시오. (끝내려면 endsearch를 입력) : ')

        if (node.data == 'endsearch') :
            print('검색을 마치겠습니다.')
            break


        """
        node.data(입력받은 data)가 이진트리에 있는지 찾기
        """
        while True :
            if (node.data == current.data) :
                print(node.data, '을/를 찾았습니다.')
                break
            elif (node.data < current.data) :
                if current.left == None :
                    print(node.data, '을/를 찾을 수 없습니다.')
                    break
                current = current.left
            else :
                if current.right == None :
                    print(node.data, '을/를 찾을 수 없습니다.')
                    break
                current = current.right
    
## global variables


root = Node() # 이 두 줄을 합쳐서 root = Node()라고 하는게 나은가?
current = root # starting node
a = 0


# 쓰레기 노드 제거
# curruent




## main

while True :
    a = input('(1. data 저장, 2. data 검색, 3. 프로그램 종료) : ')
    if a == '1' :
        addData()
    elif a == '2' :
        searchData()
    elif a == '3' :
        print('프로그램을 종료합니다.')
        break
    else :
        print('정확히 입력해주세요.')

# 인스턴스? 오브젝트? 쓰레기값 지울때 어떻게함? 오브젝트를 메모리에서 지울때
# del(object) object.clear() ?? object = None ?

