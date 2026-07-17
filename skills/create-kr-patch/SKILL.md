---
name: create-kr-patch
description: >-
  Korean (Hangul) fan-translation patch creation for retro games — full pipeline
  from ROM/disc analysis, text-engine reverse engineering, Hangul font/encoding
  design, PoC, text extraction/translation/reinsertion, pointer relocation, ASM
  hooks, build & patch generation, to emulator verification. 레트로 게임(SNES,
  메가드라이브, 새턴, PS1, 드림캐스트, PC엔진, PC-98, 게임기어, 닌텐도 DS 등
  한글 패치 제작 전 과정 — ROM/디스크 분석, 텍스트 엔진 역공학, 한글 폰트·인코딩
  설계, PoC, 텍스트 추출·번역·재삽입, 포인터 재배치, ASM 훅, 빌드·패치 생성,
  에뮬레이터 검증. 트리거 키워드 예: "한글화", "한글 패치", "KR patch", "ROM 번역",
  "ROM hacking 한글", 특정 게임 한글화 요청, 기존 한글화 프로젝트의 후속 작업.
---

# 레트로 게임 한글 패치 제작

## 개요

레트로 게임의 한글 패치를 처음부터 끝까지 만드는 에이전트용 스킬이다. 대상은 ROM 카트리지·CD/GD-ROM·플로피 디스크 매체의 콘솔·PC 게임 전반이며, 범위는 초기 조사(매체·텍스트·폰트·훅·수용량 파악)부터 폰트·인코딩 설계, PoC, 텍스트 추출, 번역, 재삽입, 빌드·패치 생성, 에뮬레이터 검증까지의 전 파이프라인이다. 판단 영역별 전략은 `references/strategy/`, 구현 시 지킬 의미와 검증 규칙은 `references/conventions/`, 현재 분기를 바꾸는 플랫폼 제약은 `references/platforms/`에서 확인한다. `references/tips/`는 관측 범위가 확인된 국소 사례를 필요할 때만 선택해 읽는다.

도구·언어·라이브러리·폰트는 대상 프로젝트의 기존 구조와 현재 환경에서 선택하고, 선택과 무관하게 요구 능력과 검증 기준을 충족한다. 쉽게 접근 가능한 명확한 1차 자료 한 곳에서 복원되는 기본 사양은 필요할 때 최신 자료에서 확인한다.

**모집단 고지**: 이 전략은 일본어 원문·텍스트 중심의 선행 한글화 경험에서 출발했다. 따라서 빈도 표현과 선행 구조는 새 게임의 사실이 아니라 가설이다. 실제 판정은 대상 리비전의 증거로 확정한다.

## 판단 영역의 의존과 횡단 게이트

작업에는 고정된 선형 순서가 없다. 현재 결정을 바꾸는 가장 싼 증거에서 시작하되, 다음 의존은 건너뛰지 않는다.

서로 독립된 경계는 병렬로 열 수 있다. 새 증거가 기존 판단을 뒤집으면 영향받는 판정만 취소해 원인 경계로 돌아가고, 나머지 증거는 유지한다.

- 모집단·경계·소비 규칙이 확정되지 않은 텍스트는 번역·재삽입 완료로 승격하지 않는다.
- 되돌리기 비싼 작업의 전제가 동등한 증거로 확인되지 않았다면 해당 PoC 게이트를 먼저 통과한다.
- 번역 수요가 글리프·길이·레이아웃 예산을 넘으면 공급 확대 가능성을 판정하고, 의미 손실이 있는 축소는 사람이 승인한다.
- 변경된 산출물은 실제 빌드와 소비 경로의 검증을 통과해야 하며, 결함은 원인 계층의 전략으로 되돌린다.

다음 전략은 조건이 성립할 때만 횡단 적용한다.

- 텍스트가 이미지 픽셀에 포함돼 있으면 `references/strategy/graphics-text.md`.
- 실제 소비 경로에 압축·해제 경계가 있으면 `references/strategy/compression.md`.
- 자산의 저장→탐색→적재·변환→상주→소비 연결 중 하나를 바꾸면 `references/strategy/runtime-assets.md`.
- 실행 검증의 목표 상태·플레이 경로가 미확정이거나 재현된 결함의 경쟁 가설을 구분해야 하면 `references/strategy/debugging.md`.

판단 영역을 새로 열거나 관측한 증상이 바뀌면 아래의 발동 조건별 검증 사례 라우팅을 다시 적용한다.

전략을 저장소 시행 규칙으로 옮길 때만 `references/conventions/project-conventions.md`를 적용하며, 동등한 기존 구조가 있으면 유지한다.

## 참조문서 라우팅

### 판단 영역 → strategy 문서

| 판단 영역 | 문서 | 내용 |
|------|------|------|
| 초기 조사 | `references/strategy/initial-survey.md` | 실제 의존 경계, 확정 리비전 사양과 열린 모집단, 가장 싼 판정 증거 선택 |
| 폰트·인코딩 | `references/strategy/font-strategy.md` | 코드→글리프 대응, 전체 레퍼토리와 활성 작업 집합, 표현·도달 검증 |
| 텍스트 추출 | `references/strategy/text-extraction.md` | 모집단 확정, 소비자 기반 경계·토큰, 가역 산출물과 라운드트립 |
| PoC | `references/strategy/poc.md` | 가시성 PoC와 조건부 PoC 게이트의 수행 여부·통과 기준 판정 |
| 재삽입·훅 | `references/strategy/reinsertion.md` | 경계별 정책, 참조 완전성, 훅·공간·소비자 불변식 |
| 번역 | `references/strategy/translation-workflow.md` | 에이전트 배치, 맥락 확정, 승인 용어·문체, 보호 제약과 고위험 의미의 적격 게이트 |
| 빌드·검증 | `references/strategy/build-and-verify.md` | 재현 가능한 산출물, 배포 경계, 계층별 검증과 종료 판정 |
| 디버깅·이슈 처리 | `references/strategy/debugging.md` | 플레이 경로·목표 상태 도달, 상태 개입의 증명 범위와 원인·수정·회귀 판정 |
| 그래픽 텍스트 (횡단) | `references/strategy/graphics-text.md` | 픽셀 텍스트 모집단, 보호 시각 자산과 소비 경로 검증 |
| 압축 대응 (횡단) | `references/strategy/compression.md` | 실제 변환 경계, 대상 소비자 호환성과 재패킹 검증 |
| 런타임 자산 도달성 (횡단) | `references/strategy/runtime-assets.md` | 변경된 저장→탐색→적재·변환→상주→소비 연결 판정 |

### 시행 컨벤션

| 범위 | 문서 | 내용 |
|------|------|------|
| 프로젝트 구현 (횡단) | `references/conventions/project-conventions.md` | 빌드 경계, 기계어 검산, 최종 변경 검증, 외부 구성요소 재현·원본 자산 취급 |
| 번역 자산 | `references/conventions/translation-artifacts.md` | 원문 보호, 제어 토큰, 검토 상태와 빌드 입력의 의미 규칙 |
| 프로젝트 기록 | `references/conventions/project-records.md` | 조사·PoC·그래픽 카탈로그·HITL·QA 증거와 판정의 기록 규칙 |
| 분석·빌드 데이터 | `references/conventions/data-formats.md` | 문자 매핑, 제어코드, 포인터, 번역 자산 연결, 재삽입 정책과 폰트 구성 정보의 의미 규칙 |

### 플랫폼 → platforms 문서

| 플랫폼 | 문서 |
|--------|------|
| SNES (슈퍼패미컴) | `references/platforms/snes.md` |
| 메가드라이브 | `references/platforms/megadrive.md` |
| 세가 새턴 | `references/platforms/saturn.md` |
| PS1 | `references/platforms/ps1.md` |
| 드림캐스트 | `references/platforms/dreamcast.md` |
| PC엔진 / CD-ROM² | `references/platforms/pce.md` |
| PC-98 | `references/platforms/pc98.md` |
| 게임기어 | `references/platforms/gg.md` |
| 닌텐도 DS | `references/platforms/nds.md` |

목록에 없는 플랫폼이면 strategy의 조사·검증 원칙만 출발점으로 삼고, 이번 판단에 필요한 하드웨어·매체·주소공간·렌더링 경로를 새로 확정한다.

### 발동 조건별 검증 사례

tips 전체의 열람은 선택적이지만 색인 대조는 생략하지 않는다. strategy가 현재 판단 영역과 발동 조건을 식별하면 `references/tips/README.md`의 짧은 색인을 보고, 일치할 때만 가장 직접 맞는 사례 앵커를 읽는다. 독립된 발동 조건이 여러 개면 조건별로 고른다. 관측 플랫폼과 범위는 증거의 출처와 전이 한계이며 선택 필수조건이 아니다. `references/tips/general.md`도 통독하지 않는다. 사례는 조사 후보나 개입 가설을 제안할 뿐 현재 게임의 구조·원인·해법을 증명하지 않으며, 게이트와 완료 조건은 strategy의 판단 기준을 따른다.

## 시작 체크리스트

새 게임에 착수할 때 다음 경계를 먼저 세운다. 조사 순서와 수단은 현재 불확실성에 맞춰 선택한다.

1. **대상과 입력 경계** — 게임·플랫폼·지원 리비전과 이번 작업이 바꾸려는 대상을 확인한다.
2. **판단 기준 확인** — 현재 판단 영역의 strategy를 읽고, 그 분기를 바꾸는 플랫폼 사실만 해당 문서에서 확인한다.
3. **기존 상태 우선** — 기존 저장소라면 코드·문서·산출물·검증 상태를 먼저 복원한다. 새 프로젝트라면 필요한 기록 위치만 마련한다.
4. **사례 발동 확인** — 현재 판단과 관측을 `references/tips/README.md`의 발동 조건과 대조하고, 일치하는 사례가 있으면 해당 앵커를 조사·개입 설계 전에 읽는다.
5. **판정 가능한 조사** — `references/strategy/initial-survey.md`에 따라 가장 싼 증거 앵커에서 실제 의존 경계를 열고, 결론과 남은 가설을 기록한다.

## 핵심 불변식

어느 작업에서든 다음을 위반하지 않는다.

- **0원칙 — 플레이어는 보통 한 번만 플레이한다.** 한글 패치의 배포 기준은 "대체로 동작한다"가 아니라 알려진 치명 문제 0건이다. 크래시나 진행 불가는 물론, 글자가 깨지거나 힌트·아이템명이 틀리거나 용어·말투가 무너지는 문제도 플레이어의 단 한 번뿐인 경험을 망치므로 모두 배포를 막는다. 특히 오역은 단순한 문장 품질 문제가 아니라 진행 실패나 선택지 오판을 부르고 인물 이해까지 무너뜨릴 수 있다.
- **원본 ROM·디스크 이미지와 허가되지 않은 저작 자산은 커밋하지 않는다.** 허용 자산과 원본 식별 기준은 `references/conventions/project-conventions.md` §6을 따른다.
- **변환 경계는 수정 전에 검증한다.** 해당 경계가 요구하는 바이트 가역성 또는 소비 의미와 보호 정보의 동등성을 입증한다. 상세 조건은 `references/conventions/project-conventions.md` §5.1을 따른다.
- **최종 산출물의 모든 변경은 적용 전에 검증 가능해야 한다.** 불변 원본을 기준으로 각 변경을 만드는 경로와 허용 범위를 확인하고, 서로 겹치는 변경·보호 범위 침범·설명되지 않은 최종 변경을 빌드 실패로 처리한다. 상세 조건은 `references/conventions/project-conventions.md` §5.2를 따른다.
- **기계어 생성·이동은 대상 명령 집합의 유효 범위를 선언하고 그 전체를 검산한다.** 패치에 필요한 일부 명령만 검증해 생성·이동·제어 흐름의 완전성을 주장하지 않는다. 상세 조건과 제한된 예외는 `references/conventions/project-conventions.md` §2.3을 따른다.
- **작업 결과는 다음 선택을 줄여야 한다.** 조사·PoC·번역·검증은 결과가 어느 쪽이든 후속 판단을 더 정확하게 만들도록 설계한다.
- **사례 수치를 새 게임에 그대로 가정하지 않는다.** 필요한 값은 대상 리비전과 실제 소비 조건에서 다시 측정한다.
- **역공학으로 확정하기 전에는 어떤 가정도 이식하지 않는다.** 같은 플랫폼·같은 개발사·같은 시리즈라도 선행 사례의 구조(스크립트 포맷, 포인터 규약, 제어코드)는 가설이지 사실이 아니다.
- **인코딩 누락은 빌드 에러다.** 번역문에 글리프·코드 매핑이 없는 문자가 있으면 조용히 건너뛰지 말고 빌드를 실패시킨다.
