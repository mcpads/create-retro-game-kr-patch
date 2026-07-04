# create-kr-patch

레트로 게임의 **한글(Hangul) 팬 번역 패치**를 처음부터 끝까지 만드는 Agent Skill.
ROM/디스크 분석 → 텍스트 엔진 역공학 → 한글 폰트·인코딩 설계 → PoC → 텍스트 추출·번역·재삽입 → 포인터 재배치·ASM 훅 → 빌드·패치 생성 → 에뮬레이터 검증까지의 전 파이프라인을 다룬다.

> An Agent Skill for building Korean fan-translation patches for retro games, covering the full pipeline from ROM/disc analysis to emulator verification. Methodology only — **contains no copyrighted ROM data or game assets.**

## 지원 플랫폼

| 플랫폼 | CPU / 매체 |
|--------|-----------|
| SNES (슈퍼패미컴) | 65816 / ROM 카트리지 |
| 메가드라이브 | 68000 / ROM 카트리지 |
| 세가 새턴 | SH-2 ×2 / CD-ROM |
| PS1 | MIPS R3000A / CD-ROM |
| 드림캐스트 | SH-4 / GD-ROM |
| PC엔진 / CD-ROM² | HuC6280 / HuCard·CD-ROM |
| PC-98 | 8086/V30 / 플로피 |
| 게임기어 | Z80A / ROM 카트리지 |
| 닌텐도 DS | ARM9+ARM7 / ROM 카트리지 (NitroFS) |

목록에 없는 플랫폼도 strategy 축의 조사 순서·검증 원칙을 출발점으로 삼아 새 플랫폼 문서를 작성하며 확장한다.

## 설치 — Claude Code 세션

```
/plugin marketplace add mcpads/create-retro-game-kr-patch
/plugin install create-kr-patch
```

## 설치 — Codex 세션

```
codex plugin marketplace add mcpads/create-retro-game-kr-patch --ref main
codex plugin add create-kr-patch --marketplace kr-patch
```

설치 후 한글화·한글 패치 관련 요청을 하면 Agent Skill이 자동으로 발동한다. 트리거 키워드: `한글화`, `한글 패치`, `KR patch`, `ROM 번역` 등.

## 구조

```
plugin metadata           # 플러그인 매니페스트와 셀프호스팅 마켓플레이스 설정
skills/
  create-kr-patch/
    SKILL.md             # 라우팅 + 핵심 불변식 (본문은 얇게)
    references/
      strategy/          # 단계별 공통 전략 12종
      platforms/         # 플랫폼별 하드웨어·사례 노트 9종
```

`SKILL.md`는 라우터·불변식만 담고, 실제 판단 기준·절차는 `references/` 문서에 있다. 에이전트는 단계·플랫폼에 따라 필요한 참조문서만 그때그때 읽는다.

## 핵심 원칙

- **원본 ROM·디스크 이미지·저작 자산은 절대 커밋하지 않는다.** 저장소에는 패치 파일·스크립트·번역 데이터만 둔다. (`.gitignore`로 강제)
- **라운드트립 검증 우선** — 추출→재조립이 바이트 단위로 원본과 동일함을 증명한 뒤에야 수정에 들어간다.
- **필요한 PoC 게이트 통과 전 본 구현 금지** — 최소 가시성 PoC와 위험 신호가 있는 조건부 PoC를 닫기 전까지 되돌리기 비싼 작업은 시작하지 않는다. 한글 1자 출력만으로 글리프 예산·인코딩 공간·재배치 가능성까지 증명됐다고 보지 않는다.

## 기여

새 플랫폼 문서나 전략 보강은 PR로 환영한다. 이 스킬의 기여 철학과 문서 작성 기준은 [CONTRIBUTING.md](CONTRIBUTING.md)를 따른다.

## 버전

현재 **0.6.0**. 버전별 변경 내용은 [CHANGELOG](CHANGELOG.md)를 본다.

설치본 업데이트는 `/plugin` 으로 마켓플레이스를 갱신한 뒤 재설치하고 `/reload-plugins`로 적용한다.

## 라이선스

[MIT](LICENSE) © 2026 mcpads
