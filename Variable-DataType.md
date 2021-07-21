<center><h1>Variable & Data types</h1></center>





## 1. Variable

> `int`,`float`, `str`,  `list`, `tuple`, `set`, `dictionary`



### 1.1. int



* 정수를 표현하는 data type
* `a = 1`과 같이 정수를 대입하면 자동으로 `int type` 변수가 선언됨
* arbitrary precision을 통해 알아서 size가 조절되기 때문에 overflow가 없음
* 큰 수를 다루는 데에도 제약도 없음

* 그 대신 fixed precision에 비해 연산 속도가 느림



### 1.2 float



* 실수를 표현하는 data type

* `a = 0.1`과 같이 `float type`의 변수를 선언할 수 있다



### 1.3 str



* 문자열을 표현하는 data type
* `string = 'abc'`와 같이 `'`나 `"`를 이용하여 문자열을 대입하면 `str type` 변수가 선언됨

* `str type`끼리 `+`나 `concat()`을 이용하여 이어붙일 수 있다(concatenation)



* 메모리에는 다음과 같이 저장된다

  * 'APPLE'

  * A | P | P | L | E | 10(끝이라는표시)

    char char char char ...

    char들의 집합 -> str



* `len()`을 통해 길이를 알 수 있다
  * 이후에 나올 `list`, `tuple`, `dictionary`에서도 길이(element의 수)를 반환함



### 1.4 list



* ~~element들을 link 하는 방식으로 sequence를 표현하는 data type.~~
  * ~~link를 이용하므로 가변적이어서 다루기 쉬운 장점이 있으나, 검색이 느림~~

* 파이썬의 `list`는 linked list가 아니라 linear list, 즉 `array`와 비슷한 것으로 이해하면 된다고 한다



* 각 요소를 element 또는 item이라고 부름

* `list = [1, 'b', False, [2, 3]]`와 같이 선언한다



* `list[i]` : `i-1`번째 element의 값
  * `i`의 range는 `-len()`부터 `len()-1`까지
  * `list[j]==list[j-len()] # 0 <= j < len()`



* `list[num1:num2:num3]` : `num1`부터 `num2 - 1`까지 `num3`씩 건너뛰면서 slicing
  * `num3`가 음수면, 감소하는 방향(역순)으로 출력
  * `num3 == 1`인 경우, 생략하여 `list[num1:num2]`로 쓸 수 있음
  * `num1 > num2`인경우 `[]`(empty list)를 반환
  * `num1 == 0` 또는 `num2 == len()-1`인 경우, 각각 `num2`, `num1`을 생략하여
    `list[:num2]` 또는 `list[num1:]`으로 쓸 수 있음



* `if`문에서 empty list `[]`는 False를 return, 그렇지 않은 list는 True를 return

  * ```
    list_empty = []
    list_not_empty = [1, 2]
    if not list_empty:
    	print('empty list')
    if list_not_empty:
    	print('not empty list')
    
    # output :
    # empty list
    # not empty list
    ```



* list의 element에 list를 넣는 방식으로 n차원 행렬을 만들 수 있다.
  * list를 element로 하는 list를 element로 하는 list를 element로 하는 list...
  * `list = [[1, 0, 0], [0, 1, 0], [0, 0, 1]] # 3*3 identity matrix`
  * `list[i-1][j-1] # a_ij`
  * `list = [ [ [0, 1], [1, 2] ], [ [1, 2], [2, 3] ] ]`
    * `list[i][j][k] == i + j + k`



* list에 활용되는 method들

  | method      | method                                                       |
  | ----------- | ------------------------------------------------------------ |
  | `append()`  | 마지막에 element 추가 `(element)`                            |
  | `insert()`  | 해당 인덱스에 element 추가. +1씩 뒤로 밀림 `(index, element)` |
  | `extend()`  | 마지막에 elements 여러개 추가 `(element1, element2, ...)`    |
  | `remove()`  | 입력받은 값과 일치하는 첫 element 삭제 `(element)`           |
  | `pop()`     | 마지막 element 제거하고, 그 element를 반환                   |
  | `index()`   | 입력값과 일치하는 첫번째 element의  index를 반환             |
  | `count()`   | 입력값과 일치하는 element들의 개수를 반환                    |
  | `sort()`    | element들을 오름차순(ascending order)으로 정렬               |
  | `reverse()` | 역순으로 정렬                                                |



* `sort()`는 모두 숫자이거나, 모두 문자열인 경우에 sorting 해줌 (혼합은 x)
  * 문자열의 경우 유니코드상 앞에있는 것부터 사전식 순서(lexicographical order)로 정렬
  * `str`들을 sorting 했을 때, 숫자, 알파벳, 한글 순으로 사전식 정렬된다.
    * 유니코드상에 숫자, 알파벳, 한글 순으로 되어있기 때문
    * 유니코드(UTF-8)는 한 글자를 1byte로 표현하고, 한 문자를 표현할 때 1~4bytes의 가변 길이 인코딩(Variable-width encoding) 방식이다. 알파벳은 1byte, 한글은 3bytes



* `del list[i]` : index 1에 있는 element를 삭제 (`len()` 1 감소)



### 1.5 tuple



* 리스트와 유사하지만, 한번 입력하면 element(item)의 수정이 안됨
  * 각 element만 수정하는게 불가능해서, tuple 그 자체를 덮어씌워야됨



* 소괄호 `()`를 사용하여 선언해도 되고, 그냥 생략해도 된다

  ```
  tuple = (1, 2)
  tuple = 1, 2
  ```



* element가 하나뿐인 tuple을 생성할 때는 반드시 element 뒤에 `,`를 입력해야 한다

  ```
  tuple = (1,)
  tuple = 1,
  ```

  * 그냥 내 생각) `signed int`인 -1, +1, 1 등의 연산 우선순위를 명확히 표기하기위해
    (-1), (+1), (1)를 사용할 때, 혼동을 피하기 위함이 아닐까?



* 튜플의 요소를 변경하고나 삭제하는 method는 사용 불가
  * `index()`나 `count()` 같은 건 사용 가능



### 1.6 set



* 수학에서의 집합(set)과 같은 logic
  * 순서가 없고, element를 중복하여 표기하지 않음



* `set = {1, 2}`와 같이, `{}`를 사용하여 선언



* 연산을 해주는 method들

  | 설명  | method              |         |
  | ----- | ------------------- | ------- |
  | A ∩ B | `A.intersection(B)` | `A & B` |
  | A ∪ B | `A.union(B)`        | `A | B` |
  | A - B | `A.difference(B)`   | `A - B` |



* `list()`, `tuple()`, `set()`을 이용하면 서로의 data type을 변환할 수 있다



### 1.7 dictionary

>  다른 언어에서는 map이라고도 불림



* key 와 value의 순서쌍들을 표현하는 data type
* `dict = {key1:value1, key2:value2}`와 같이 선언

* `dict[key3] = value3 `과 같이 element 추가



* `key`는 반드시 한번 정의되면 변형 불가능한(immutable) 값이어야 한다.
  * `list`나 `set`같이 변형 가능한 것을 `key`로 입력하면
    `TypeError: unhashable type: 'list'`와 같은 TypeError가 뜬다
    반면 `tuple`은 `key`로 사용 가능



* Python 3.6부터는 입력순으로 정렬
  * 단순히 정렬을 위한 업데이트는 아니고, 성능 때문이라고 함
  * `print()`를 사용하지 않고 그냥 `dict`과 같이 입력하면 key를 기준으로 오름차순 정렬해서 보여줌
    * `(1, 2), (1, 2, 3), 1, '1', 2, 3, '3', 4, 'a', '가'`의 순으로 정렬(?)됨



* dictionary와 관련된 method들

  | method                | 설명                                                         |
  | --------------------- | ------------------------------------------------------------ |
  | `keys()`              | `key`들을 `dict_keys`라는 데이터 형태로 반환                 |
  | `values()`            | `value`들을 `dict_values`라는 데이터 형태로 반환             |
  | `items()`             | `(key, value)`들을 `dict_items`라는 데이터 형태로 반환       |
  | `dict1.update(dict2)` | dict1에 dict2를 합해줌 `key`가 겹치는건 덮어쓰고, 안겹치는건 추가해줌 |
  | `clear()`             | dictionary의 모든 항목 삭제                                  |
  | `list(dict1)`         | `(key, value)`를 element로 갖는 `list`로 변환하여 반환 (dict1은 변화 x) |



* `keys()`, `values()`, `items()`로 반환된 값에 `list()`를 이용하면 `list`로 변환할 수 있음

  ```
  dict1 = {key1:value1:key2:value2}
  print(list(dict1.items()))
  
  # output:
  # [(key1,value1), (key2,value2)]
  ```



