# CLAUDE.md

## 프로젝트
- TodoList 웹앱 (HTML/CSS/JavaScript, 저장은 localStorage)
- 빌드 도구·프레임워크 없이 `index.html`을 브라우저로 열면 실행된다.
- 요구사항은 `docs/prd/todo-list-webapp.md`(PRD)를 따른다. PRD에 없는 기능은 임의로 추가하지 않는다.

## 브랜치
- 기본 브랜치는 `master`이다. `master`에 직접 커밋하지 않는다.
- 작업 브랜치는 최신 `master`에서 만든다.
- 이름 규칙: `<타입>/<이슈번호>-<짧은-영문-설명>` (예: `feat/3-add-todo`)
- 하나의 브랜치에서는 하나의 Issue만 작업한다. Issue 범위 밖의 파일은 수정하지 않는다.

## 커밋 메시지
- 형식: `<타입>: <한글 요약> (#이슈번호)`
- 예: `feat: 할 일 추가 기능 구현 (#3)`

## 타입
| 타입 | 용도 |
|------|------|
| feat | 기능 |
| fix | 버그 |
| docs | 문서 |
| refactor | 구조 개선 |
| chore | 설정 |

## Pull Request
- PR 본문에는 `Closes #이슈번호`를 넣는다.
- `.github/pull_request_template.md` 양식을 따른다.
- 강제 푸시(force push)는 하지 않는다.
