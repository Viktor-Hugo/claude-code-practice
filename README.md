# claude-code-practice

Claude Code와 GitHub MCP를 실습하는 저장소입니다.
실습 대상으로 간단한 TODO 관리 CLI(`todo.py`)를 함께 다룹니다.

## 요구 사항

- Python 3.8 이상 (외부 패키지 없음)

## 사용법

```bash
# 할 일 추가
python todo.py add "README 정리하기"

# 목록 보기
python todo.py list

# 완료 처리 (번호 지정)
python todo.py done 1

# 삭제
python todo.py remove 1
```

출력 예시:

```
[x] 1. README 정리하기
[ ] 2. 우선순위 기능 검토하기
```

할 일 데이터는 `todo.py`와 같은 폴더의 `todos.json`에 저장되며, Git에는 올라가지 않습니다.

## 파일 구성

| 파일 | 설명 |
|---|---|
| `todo.py` | TODO 관리 CLI |
| `README.md` | 프로젝트 설명 |
| `.gitignore` | `todos.json` 등 로컬 파일 제외 |

## 진행 상황

- [x] GitHub MCP 연결 확인 ([#1](https://github.com/Viktor-Hugo/claude-code-practice/issues/1))
- [x] 기본 TODO 기능 (추가 / 목록 / 완료 / 삭제)
- [ ] TODO 우선순위 기능 검토
