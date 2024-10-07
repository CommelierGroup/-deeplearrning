# Pre-Study Warm-Up: Python Quiz for Deep Learning

## 파이썬 설치하기

대충 여기에서 설치하시면 되긴 하는데요, 굳이 그러실 필요는 없을 수도 있습니다! 스터디하시는 분들 전부 맥을 사용하시니까요. 사실 맥이나 리눅스에는 기본적으로 Python이 설치되어 있습니다. 왜냐고요? 특정 Python 버전에 의존하는 프로그램들이 많아서 기본적으로 깔려 있는 거죠! 😎

## 그렇지만

기본적으로 깔려 있는 파이썬 버전은 호환성 때문에 구버전이 설치되니, `pyenv`라는 라이브러리를 이용하여 최신버전의 파이썬을 설치합시다.

## pyenv 설치 (homebrew)

```sh
brew update
brew install pyenv
```

mac 이외에 다른 운영체제는 [여기](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation)서 올바른 설치 방법을 찾아보세요!

## pyenv를 사용하기 위한 환경변수 설정

### 환경변수 설정

```sh
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

위 명령어를 실행해서 .zshrc를 업데이트 하세요.

```sh
source ~/.zshrc
```

위 명령어를 실행하면 .zshrc가 터미널에 반영됩니다.

### 실행 확인

```sh
pyenv --version
```

```text
pyenv 2.4.14
```

## 특정 버전의 파이썬 설치 및 적용

### 설치

```sh
pyenv install 3.12.5
```

### 설치된 파이썬 목록 나열

```sh
pyenv versions
```

```text
* system (set by /Users/yujehwan/.pyenv/version)
3.12.5
```

### 특정 버전의 파이썬으로 설정하기

```sh
pyenv global 3.12.5
pyenv versions # 확인
```

```text
  system
* 3.12.5 (set by /Users/yujehwan/.pyenv/version)
```

## 자 이제, 시작할 준비가 되었습니다. 아래의 퀴즈를 풀어오세요.

### Q1. python의 가상환경이 무엇인가요? 개념을 간략하게 설명해주세요.

### Q2. python의 가상환경을 만드려면 어떤 명령어를 사용해야할까요? 이 파일은 git에 공유해야하나요?

### Q3. python 내장명령어가 아닌 pyenv로도 환경변수를 설정할 수 있습니다. 둘의 차이가 무엇인가요?

### Q4. 다양한 개발자들과 협업하기 위해서는 의존성 관리를 해야합니다. 파이썬의 대표적인 의존성 관리 방법을 설명해주세요.

- 방법 1) requirement.txt
- 방법 2) pipenv
- 방법 3) Poetry

### Q5. Poetry 방식으로 이 디렉토리를 초기화해주세요. 초기화하려면 어떻게 해야합니까?

### Q6. Numpy 라이브러리를 설치한 이후 의존성을 명시해주세요. 의존성을 명시하려면 어떻게 해야합니까?

### Q7. 아래와 같은 1차원 배열이 있습니다. 이를 2X3 형태의 2차원 배열로 변환해보세요.

```
np.array([1, 2, 3, 4, 5, 6])
```

### Q8. 아래와 같은 2차원 배열이 있습니다. 이 배열의 전체 합과 평균을 구하세요.

```
np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
```

### Q9. 아래와 같은 2차원 배열이 있습니다. 이 배열에서 최대값과 그 위치를 찾으세요.

```text
np.array([[3, 7, 2], [5, 9, 1], [8, 4, 6]])
```

### Q10. 아래와 같은 1차원 배열과 2차원 배열이 있습니다. 두 행렬의 곱을 계산하세요.

```text
a = np.array([1, 2, 3, 4])
b = np.array([[2, 0], [1, 3], [3, 1], [0, 2]])
```

### Q11. 1에서 50까지의 숫자로 구성된 배열이 있습니다. 이 중에서 소수만 추출하세요.
