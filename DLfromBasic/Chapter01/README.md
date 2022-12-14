
## Step 01: 상자로서의 변수  
딥러닝 프레임워크의 가징 기본적인 단위 중 하나인 변수 클래스 구현.  
- 변수(Variable) : 데이터를 담는 클래스. 

## Step 02: 변수를 낳는 함수
나머지 기본적인 단위인 함수 클래스 구현.  
- 함수(Function) : 변수를 입력으로 받아 계산하여 변수를 출력하는 클래스.   

다양한 함수를 구현할 수 있도록 상위 클래스를 만든다.

## Step 03: 함수 연결
상위 함수 클래스를 상속받아 제곱, exp 등의 세부 계산 함수 클래스 구현.  
하위 함수 클래스들을 연결하여 복잡한 수식을 나타내는 것이 가능하다.

## Step 04: 수치 미분
미분의 정의에 따른 미분 구현.  
극한으로 가는 것을 컴퓨터는 표현할 수 없기에, 오차를 줄이기 위해 중앙차분을 사용한다.  
- 중앙차분 : $\Large lim_{x\rightarrow 0}\frac{f(x+h)-f(x-h)}{2h}$

## Step 05: 역전파 이론
역전파의 핵심 아이디어인 연쇄 법칙에 대한 이해.  
- 연쇄 법칙(chain rule) : 함성 함수의 미분에서 연쇄적으로 미분을 곱하는 공식.

$\Large \frac{dy}{dx} = \frac{dy}{dy}\frac{dy}{db}\frac{db}{da}\frac{da}{dx}$  
최종값으로부터 순차적으로 각 단계에서의 미분값을 곱해나가며 입력값에 대한 미분값을 도출할 수 있다.

## Step 06: 수동 역전파
backward 메소드를 만들어 역전파 구현하기.  
모든 계산 과정에 대해 backward를 작성하면서 수동으로 역전파를 진행할 수 있다.

## Step 07: 역전파 자동화
역전파를 자동화하기.  
순전파 계산을 하면 자동으로 역전파를 가능하게 만들어주는 Define-by-Run을 위한 작업을 한다.
- Define-by-Run : 계산 시점(데이터가 흘러가는 시점)에 각 계산을 연결하는 방식. Define-and-Run과 대조된다.

이는 각 함수와 변수에 자신과 연결된 클래스를 저장하는 방식으로 이뤄진다.
- 함수와 변수의 관계
  - 함수에게 변수란 자신의 입출력(input, output)이다.
  - 변수에게 함수란 자신의 창조자(creator)이다.
  
저장을 하고 나면 변수 클래스에 backward 메소드를 만들어 재귀적으로 함수 클래스의 backward가 호출되도록 만든다.

## Step 08: 재귀에서 반복문으로
재귀문을 처리 효율이 뛰어난 반복문으로 바꾸기.

## Step 09: 함수를 더 편리하게
사용성을 개선하기 위해 세가지를 수정.
- 파이썬 함수로 이용하기
- backward 메소드 간소화
- ndarray만 취급하기

## Step 10: 테스트
딥러닝 프레임워크 개발 중 테스트하는 코드 만들기.  
파이썬 내부에 구현된 unittest 를 활용한다.

