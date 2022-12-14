## Step 11: 가변 길이 인수(순전파 편)

add와 같이 분기가 일어나는 연산이 가능하도록 수정.  
함수의 입력값과 출력값이 리스트로 들어오고 나갈 수 있도록 만들기.

## Step 12: 가변 길이 인수(개선 편)

11에서 수동적으로 변수들을 리스트에 묶이게 설정해야 한다는 점을 개선.  
*를 인자 앞에 붙여 입력값을 위치 가변 인자로 받아 클래스 내에서 알아서 리스트로 받도록 수정.  
출력값 역시 값이 하나가 반환될 때 알아서 튜플로 묶도록 수정.

## Step 13: 가변 길이 인수(역전파 편)

분기가 발생하는 하위 함수 객체에서 역전파 정의하기.  
이에 맞춰 변수 객체에서 backward 진행 시 분기가 일어나도 전부 역전파가 진행되도록 수정.

## Step 14: 같은 변수 반복 사용

### 인플레이스 연산

![inplace](./inplace.png)

여기에서 id(x)의 결과를 보면(x는 ndarray 인스턴스), x가 메모리에서 덮어 써지는지 아니면 새로 생성되는지 알 수 있습니다. 보다시피 누적 대입 연산자인 +=를 사용하면 x의 객체 ID가 변하지 않습니다. 즉, 메모리 위치가 동일하다는 뜻으로, 값만 덮어 쓴 것입니다. 이처럼 복사하지 않고 메모리의 값을 직접 덮어 쓰는 연산을 인플레이스 연산이라고 합니다.

## Step 15: 복잡한 계산 그래프(이론 편)

위상: 그래프의 '연결된 형태'

## Step 16: 복잡한 계산 그래프(이론 편)

중첩 함수는 주로 다음 두 조건을 충족할 때 적합합니다.
- 감싸는 메서드 안에서만 이용한다.
- 감싸는 메서드에 정의된 변수를 사용해야 한다.

## Step 17: 메모리 관리와 순환 참조

### 파이썬 메모리 관리
- 파이썬 인터프리터가 필요 없어진 객체를 메모리에서 자동으로 삭제
- 하지만, 코드를 제대로 작성하지 않으면 메모리 누수, 메모리 부족 문제 발생  

**메모리 관리 방법 2가지**  

**1. 참조(reference) 수를 세는 방법: 참조 카운트**
- 참조 카운트가 0인 상태로 생성되고, 다른 객체가 참조할 때마다 1씩 증가
- 객체에 대한 참조가 끊길 때마다 1만큼 감소하고 0이 되면 파이썬 인터프리터가 회수 후 즉시 메모리에서 삭제
- 구조가 간단하고 속도가 빠르다는 장점
- 예시) 대입 연산자를 사용할 떄, 함수에 인자로 전달할 때, 컨테이너 타입 객체(리스트, 튜플, 클래스 등)에 추가할 때

**2. 세대(generation)을 기준으로 쓸모없어진 객체를 회수하는 방법: GC(Garbage Collection)**
- 순환 참조의 경우 참조 카운트 방법으로 해결이 불가능하나 GC는 해결 가능
- 참조 카운트와는 달리 메모리가 부족해지는 시점에 파이썬 인터프리터에 의해 자동으로 호출
- 명시적으로 호출할 경우 gc.collect()로 실행
- 작동 원리: 1) Python GC는 총 3세대이며, 객체는 현재 세대의 Garbage 수집 프로세스에서 살아남을 대마다 이전 세대로 이동 2) 객체 수가 해당 임계값을 초과하면 GC이 Collection 프로세스를 trigger(추적) 3) 세대는 0~2세대로 구분되고 최근 생성된 객체는 0세대(young)에 들어가고 오래된 객체일수록 2세대(old)로 이동/GC는 0세대일수록 더 자주 가비지 컬렉션을 하도록 설계  
[참고]: https://medium.com/dmsfordsm/garbage-collection-in-python-777916fd3189

### weakref 모듈
- weakref.ref 함수를 이용한 약한 참조
- 약한 참조: 다른 객체를 참조하되 참조 카운트는 증가시키지 않는 기능

## Step 18: 메모리 절약 모드
- 메모리 사용을 개선할 수 있는 2가지 구조  

**1. 역전파 시 사용하는 메모리양을 줄이는 방법(불필요한 미분 결과를 보관하지 않고 즉시 삭제)**
- Variable 클래스의 backward 메소드에 retain_grad 추가해 사용  

**2. 역전파가 필요 없는 경우용 모드(불필요한 계산을 생략)**
- Config 클래스를 사용해 모드 전환
- contesxtlib 모듈을 활용해 간편하게 사용

## Step 19: 변수 사용성 개선
- 변수 이름 지정
- ndarray 인스턴스 변수
- __len__, __repr__ 정의
