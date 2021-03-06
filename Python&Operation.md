<center><h1>파이썬</h1></center>

> 파이썬 공부 1일차 내용



## 1. 파이썬 기초 상식



### 1.1. 파이썬의 특징

* 가독성 : 문법이 간결. 들여쓰기(4칸) 활용

* 확장성 : 풍부한 라이브러리
  * Numpy, Pandas, Beautiful Soup, Matplotlib
  * 텐서플로우연계용프로그램

* 접착성 : c, java 모듈 사용 호환성

* 유니코드 : 문자열 유니코드(한글이 잘 호환되는 편)

* 순차적 명령어(C와는 달리, interpreter language)



### 1.2. 파이썬 코딩 규칙

1. 들여쓰기 : 공백 4칸(권장), 보통은 자동으로 됨

   * ```
     {
     	{
     		{
     		
     		}
     	}
     }
     ```

2. 표현식, 문장에 가급적 공백을 쓰지 않는다

   * 공백을 쓰면 다르게 이해될 수 있음

   * `1 + 1` 보다는 `1+1`으로 쓰는것을 권장

   * `()`, `{}`, `[]` 내부와 , `:`, `;` 전에는 불필요한 띄어쓰기를 넣지 않는다

3. `#` : 주석



## 2. 사칙 연산



> `+`, `-`, `*`, `/`, `()`, `**`, `%`, `//` : 왼쪽부터 덧셈, 뺄셈, 곱셈, 나눗셈, 괄호, 거듭제곱, 나머지, 몫



### 2.1 사칙연산의 우선순위

> 같은 순위면 왼쪽부터 오른쪽으로 계산한다

1. `()`
2. `**`
3. `*`, `/`, `%`, `//`
4. `+`, `-`

```
(5*4-15)+((5-2)*(9-7)) == 11
```



### 2.2 수 표기 



* `1e-15`, `1e15` 등의 방법으로 수(int, float 등)를 입력할 수 있다.

* 출력값은 `1000000000000000.0`와 같은 형태로 나오며 1e16 부터는 출력값도 `1e16`과 같이 나옴

* `0b[2진수표현]`, `0o[8진수표현]`, `0x[16진수표현]`과 같이 입력하여 자료형이 `int`인 10진수를 출력할 수 있다
  * 10진수 17을 입력하는 대신 `0b10001`, `0o21`, `0x11`과 같이 써도 된다



## 3. 논리 연산 (logical operation, Boolean operation)

> `True`, `False`, `and`, `&`, `or`, `|`, `not`, `!`
> 불 대수(Boolean algebra)와 연관



* 수리 논리의 진리표 대로 연산된 값이 출력됨

* `True`, `False`의 자료형은 `boolean`



### 4. 비교 연산

> `==`,`!=`, `<`, `>`, `<=`, `>=`



* 비교 연산 결과로 `boolean` 값이 출력됨
* 비교 연산의 우선순위가 논리 연산보다 높음

