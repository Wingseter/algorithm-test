# 🧠 Algorithm Solution Repository (알고리즘 문제 풀이)

이 저장소는 백준(Baekjoon), 리트코드(LeetCode), 프로그래머스(Programmers), SW Expert Academy, 코드트리(CodeTree) 등 다양한 플랫폼의 알고리즘 문제 해결 소스코드를 정리하고 관리하는 공간입니다. Python과 C++을 사용하여 문제를 해결하였습니다.

---

## 🛠 Tech Stack & Badges

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white" alt="C++" />
</p>

---

## 📁 Repository Directory Structure

```directory
AlgorithemTest/
├── C++/
│   ├── BackJoon/              # 백준 C++ 솔루션 (문제번호.cpp)
│   ├── Basic/                 # C++ 기초 템플릿 (순열, 조합 등)
│   └── Programers/            # 프로그래머스 C++ 고득점 Kit 솔루션
│       └── algorithmKit/
│           ├── Hash/
│           ├── Heap/
│           ├── Sort/
│           ├── bfsdfs/
│           ├── brute_force/
│           ├── dp/
│           ├── greedy/
│           └── stack_queue/
└── Python/
    ├── BackJoon/              # 백준 Python 솔루션 (문제번호.py)
    ├── LeetCode/              # 리트코드 Python 솔루션
    ├── Reference/             # 알고리즘 개념/유형별 Reference 코드
    ├── algorithm_white_book/  # 알고리즘 문제 해결 전략 관련 풀이
    ├── codeTree/              # 코드트리 Python 솔루션
    ├── programmers/           # 프로그래머스 Python 솔루션 (카카오 기출 등)
    └── swAcademy/             # SW Expert Academy Python 솔루션
```

---

## 🚀 How to Run & Test (실행 및 테스트 방법)

### Python
Python 솔루션은 보통 표준 입력(`sys.stdin` 또는 `input()`)을 통해 입력을 받습니다. 로컬에서 편리하게 테스트하기 위해 디렉토리 내에 `input.txt` 또는 `sample.txt`에 테스트 입력을 저장한 뒤 다음과 같이 실행할 수 있습니다.

```bash
# 터미널에서 리디렉션을 사용하는 방법
python3 Python/BackJoon/1002.py < Python/BackJoon/sample.txt

# 코드 내에서 직접 파일을 읽는 경우 (주석 해제 후 사용)
# sys.stdin = open("input.txt", "r")
```

### C++
C++ 솔루션은 컴파일 후 실행 파일을 생성하여 테스트합니다.

```bash
# 컴파일
g++ -std=c++17 C++/BackJoon/10430.cpp -o solution

# 실행 및 테스트 케이스 입력
./solution
```

---

## 🔗 Platform Links (알고리즘 문제 출처)

*   [Baekjoon Online Judge (BOJ)](https://www.acmicpc.net/)
*   [Programmers](https://programmers.co.kr/)
*   [LeetCode](https://leetcode.com/)
*   [SW Expert Academy](https://swexpertacademy.com/)
*   [CodeTree](https://www.codetree.ai/)
