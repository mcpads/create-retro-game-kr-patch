# create-kr-patch

레트로 게임의 **한글(Korean) 팬 번역 패치**를 처음부터 끝까지 만드는 Agent Skill.
ROM/디스크 분석 → 텍스트 엔진 역공학 → 한글 폰트·인코딩 설계 → PoC → 텍스트 추출·번역·재삽입 → 포인터 재배치·ASM 훅 → 빌드·패치 생성 → 에뮬레이터 검증까지의 전 파이프라인을 다룬다.

> An Agent Skill for building Korean fan-translation patches for retro games, covering the full pipeline from ROM/disc analysis to emulator verification. Methodology only — **contains no copyrighted ROM data or game assets.**

## 지원 플랫폼

SNES, 메가드라이브, 세가 새턴, PlayStation, Dreamcast, PC Engine, PC-98, Game Gear, Nintendo DS의 조건부 플랫폼 제약을 제공한다. 목록에 없는 플랫폼도 strategy의 판정 기준을 적용하고, 현재 분기를 바꾸는 하드웨어·매체 사실만 새로 확인해 확장할 수 있다.

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

## 릴리스 채널과 `next` 소식

- `main`: 최신 안정 릴리스 채널. 검증을 마치고 정식 버전으로 확정된 변경만 반영한다.
- `next`: 다음 안정 릴리스를 준비하는 이동형 프리릴리스 채널. alpha·beta·rc를 먼저 사용해 보고 피드백하려는 사용자를 위한 채널이며, 정식 릴리스 전에는 호환성과 문서 구조가 바뀔 수 있다.

현재 버전은 `main` 0.7.0, `next` 1.0.0-alpha.1이다. `next`는 특정 프리릴리스에 고정된 태그가 아니라 최신 개발 상태를 따라가는 브랜치다. 두 채널은 같은 플러그인 ID를 사용하므로 동시에 설치하지 않고, 기존 marketplace를 원하는 Git ref로 교체한다.

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

안정판으로 돌아갈 때는 같은 순서에서 `next`를 `main`으로 바꾼다. Claude Code는 reload 뒤, Codex는 새 스레드에서 선택한 버전을 적용한다.

설치 후 한글화·한글 패치 관련 요청을 하면 Agent Skill이 자동으로 발동한다. 트리거 키워드: `한글화`, `한글 패치`, `KR patch`, `ROM 번역` 등.

## 구조

```
plugin metadata           # 플러그인 매니페스트와 셀프호스팅 마켓플레이스 설정
skills/
  create-kr-patch/
    SKILL.md             # 라우팅 + 핵심 불변식 (본문은 얇게)
    references/
      strategy/          # 단계별 판단 기준과 검증 게이트
      conventions/       # 저장소 역할·데이터·기록 시행 규약
      platforms/         # 플랫폼별 분기를 바꾸는 사실·제약 9종
      tips/              # 판단 영역·조건으로 선택하는 검증된 국소 사례
```

`SKILL.md`는 라우터·불변식만 담고, 판단 기준은 `references/strategy/`, 시행 규약은 `references/conventions/`, 플랫폼 사실은 `references/platforms/`가 소유한다. `references/tips/`는 판단 영역·발동 조건으로 고르고 관측 범위를 전이 한계로 확인하는 비규범적 검증 사례다. 에이전트는 단계·플랫폼에 따라 필요한 참조문서만 그때그때 읽는다.

## 기여

새 플랫폼 문서나 전략 보강은 PR로 환영한다. 이 스킬의 기여 철학과 문서 작성 기준은 [CONTRIBUTING.md](CONTRIBUTING.md)를 따른다.

## 버전

`main` 안정판은 **0.7.0**, `next` 프리릴리스는 **1.0.0-alpha.1**이다. 버전별 변경 내용은 [CHANGELOG](CHANGELOG.md)를 본다.

같은 채널을 업데이트할 때도 해당 marketplace를 갱신한 뒤 플러그인을 업데이트하거나 재설치한다. Claude Code는 reload 뒤, Codex는 새 스레드에서 새 설치본을 적용한다.

## 라이선스

[MIT](LICENSE) © 2026 mcpads
