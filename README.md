# create-kr-patch

레트로 게임의 **한글(Korean) 팬 번역 패치**를 처음부터 끝까지 만드는 Agent Skill.
ROM·디스크 분석, 텍스트 엔진 역공학, 한글 폰트·인코딩 설계, PoC, 번역·재삽입, 포인터·ASM 훅, 빌드·에뮬레이터 검증 등 한글 패치 전 과정의 판단 영역을 다룬다.

> An Agent Skill for building Korean fan-translation patches for retro games, with guidance for decisions across ROM/disc analysis, patch development, and emulator verification. Methodology only — **contains no copyrighted ROM data or game assets.**

## 지원 플랫폼

Game Boy·Game Boy Color, NES·Famicom, SNES, 메가드라이브, 세가 새턴, PlayStation, Dreamcast, PC Engine, PC-98, Game Gear, Nintendo DS는 플랫폼 문서를 따로 둔다. 목록에 없는 플랫폼에도 쓸 수 있다.

## 프로젝트 템플릿

새 한글 패치 저장소를 시작할 때는 [create-kr-patch-template](https://github.com/mcpads/create-kr-patch-template)을 사용할 수 있다. 이 스킬은 조사부터 빌드·검증·배포 판정까지 필요한 기준을 제공하고, 템플릿은 그 기준을 새 저장소의 기본 구조와 실행 진입점으로 옮기는 선택적 뼈대다. 플랫폼과 구현 언어는 고정하지 않는다.

## 설치 — Claude Code 세션

```
/plugin marketplace add mcpads/create-retro-game-kr-patch@main
/plugin install create-kr-patch@kr-patch
```

## 설치 — Codex 세션

```
codex plugin marketplace add mcpads/create-retro-game-kr-patch --ref main
codex plugin add create-kr-patch@kr-patch
```

## 릴리스 채널과 채널 전환

- `main`: 최신 안정 릴리스 채널. 검증을 마치고 정식 버전으로 확정된 변경만 반영한다.
- `next`: 다음 안정 릴리스를 준비하며 계속 갱신되는 프리릴리스 채널. alpha·beta·rc를 먼저 사용해 보고 피드백하려는 사용자를 위한 채널이며, 정식 릴리스 전에는 호환성과 문서 구조가 바뀔 수 있다.

`next`는 최신 개발 상태를 계속 따라가며, 특정 프리릴리스 상태가 필요하면 버전 태그를 사용한다. 두 채널은 같은 플러그인 ID를 사용하므로 동시에 설치하지 않고, 기존 marketplace를 원하는 Git ref로 교체한다.

Claude Code에서 `next`로 전환:

```
/plugin marketplace remove kr-patch
/plugin marketplace add mcpads/create-retro-game-kr-patch@next
/plugin install create-kr-patch@kr-patch
/reload-plugins
```

Codex에서 `next`로 전환:

```
codex plugin remove create-kr-patch@kr-patch
codex plugin marketplace remove kr-patch
codex plugin marketplace add mcpads/create-retro-game-kr-patch --ref next
codex plugin add create-kr-patch@kr-patch
```

안정판으로 돌아갈 때는 같은 순서에서 `next`를 `main`으로 바꾼다. 같은 채널을 업데이트할 때도 marketplace를 갱신한 뒤 플러그인을 업데이트하거나 재설치한다. Claude Code는 reload 뒤, Codex는 새 스레드에서 선택한 버전을 적용한다.

설치 후 레트로 게임을 한글화하겠다고 요청하면 Agent Skill이 발동한다. `한글화`, `한글패치`, `ROM 번역` 어느 쪽으로 말해도 되고, 새로 조사를 시작할 때도 기존 프로젝트를 이어 갈 때도 같다.

## 구조

```
plugin metadata           # 플러그인 매니페스트와 셀프호스팅 마켓플레이스 설정
skills/
  create-kr-patch/
    SKILL.md             # 최상위 원칙 + 작업 원칙 + 영역별 라우팅
    references/
      strategy/          # 판단 영역별 기준과 검증 방법
      conventions/       # 저장소 역할·데이터·기록 시행 규약
      platforms/         # 플랫폼별 분기를 바꾸는 사실·제약 11종
      tips/
        general/         # 플랫폼 규칙 없이 적용되는 사례별 파일
        platforms/       # 플랫폼 규칙이 있어야 성립하는 사례별 파일
```

`SKILL.md`가 진입점이다. 플레이어 경험을 지키는 최상위 원칙과 긴 작업의 방향을 잡는 세 가지 작업 원칙을 먼저 제시하고, 지금 하려는 일에 맞는 세부 지침과 검증 기준으로 연결한다.

## 기여

새 플랫폼 문서나 전략 보강은 PR로 환영한다. 이 스킬의 기여 철학과 문서 작성 기준은 [CONTRIBUTING.md](CONTRIBUTING.md)를 따른다.

## 버전

현재 버전과 버전별 변경 내용은 [CHANGELOG](CHANGELOG.md)를 본다.

## 라이선스

[MIT](LICENSE) © 2026 mcpads
