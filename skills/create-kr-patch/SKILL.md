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

## Overview

레트로 게임의 한글 패치를 처음부터 끝까지 만드는 Agent Skill이다. 대상은 ROM 카트리지·CD/GD-ROM·플로피 디스크 매체의 콘솔·PC 게임 전반이며, 범위는 초기 조사(매체·텍스트·폰트·훅·수용량 파악)부터 폰트·인코딩 설계, PoC, 텍스트 추출, 번역, 재삽입, 빌드·패치 생성, 에뮬레이터 검증까지의 전 파이프라인이다. 단계별 판단 기준은 `references/strategy/`, 구현 규약은 `references/conventions/`, 플랫폼별 분기를 바꾸는 하드웨어·매체 사실은 `references/platforms/`가 소유한다. `references/tips/`는 관측 범위가 확인된 국소 실패의 선택적 단서집이며 어느 판단에도 필수 입력이 아니다.

이 SKILL.md는 헌법 티어 문서다. 여기에는 프로젝트가 바뀌어도 유지되어야 하는 원칙, 단계 간 의존, 참조문서 라우팅, 불변식만 둔다. 데이터·기록을 표현할 때 지킬 의미 규칙은 `references/conventions/`, 여러 자료를 교차해야 하는 플랫폼 제약은 `references/platforms/`, 특정 게임의 주소·오프셋과 실제 저장 형식은 프로젝트 문서의 책임이다. 스킬은 도구·언어·라이브러리·폰트 후보 목록을 고정하지 않고, 필요한 능력과 검증 기준만 제시한다. 이 Agent Skill을 처음 읽는 사람은 선행 작업의 맥락을 모른다고 가정하므로, 각 전략 문서는 과거 사례를 전제로 삼지 말고 질문, 판단 기준, 통과 조건을 독립적으로 설명해야 한다.

한 번의 명확한 1차 자료 조회로 복원되는 기본 사양은 스킬에 복제하지 않고 필요 시 최신 자료를 조사한다. `references/platforms/`에는 여러 출처의 적용 범위를 교차해야 하는 제약과 오해하기 쉬운 계층 경계만, `references/tips/`에는 실제 프로젝트의 실패·반례·결정 실험으로 얻은 국소 지식만 보존한다.

**모집단 고지**: 이 전략은 일본어 원문·텍스트 중심의 선행 한글화 경험에서 출발했다. 따라서 빈도 표현과 선행 구조는 새 게임의 사실이 아니라 가설이다. 플랫폼 문서는 적용 범위가 확인된 사실·제약만, tips는 국소 실패 사례만 소유한다. 실제 판정은 해당 strategy와 대상 리비전의 증거로 확정한다.

## 단계 의존과 횡단 게이트

작업에는 고정된 선형 순서가 없다. 현재 결정을 바꾸는 가장 싼 증거에서 시작하되, 다음 의존은 건너뛰지 않는다.

- 모집단·경계·소비 규칙이 확정되지 않은 텍스트는 번역·재삽입 완료로 승격하지 않는다.
- 되돌리기 비싼 구현의 전제가 동등한 증거로 확인되지 않았다면 해당 PoC 게이트를 먼저 통과한다.
- 번역 수요가 글리프·길이·레이아웃 예산을 넘으면 공급 확대 가능성을 판정하고, 의미 손실이 있는 축소는 사람이 승인한다.
- 변경된 산출물은 실제 빌드와 소비 경로의 검증을 통과해야 하며, 결함은 원인 계층의 전략으로 되돌린다.

다음 전략은 조건이 성립할 때만 횡단 적용한다.

- 텍스트가 이미지 픽셀에 포함돼 있으면 `references/strategy/graphics-text.md`.
- 실제 소비 경로에 압축·해제 경계가 있으면 `references/strategy/compression.md`.
- 자산의 저장→탐색→적재·변환→상주→소비 연결 중 하나를 바꾸면 `references/strategy/runtime-assets.md`.
- 재현된 결함의 경쟁 가설을 구분해야 하면 `references/strategy/debugging.md`.

전략을 저장소 시행 규칙으로 옮길 때만 `references/conventions/project-conventions.md`를 적용하며, 동등한 기존 구조가 있으면 유지한다.

## 참조문서 라우팅

### 단계 → strategy 문서

| 단계 | 문서 | 내용 |
|------|------|------|
| 초기 조사 | `references/strategy/initial-survey.md` | 실제 의존 경계, 확정 리비전 사양과 열린 모집단, 가장 싼 판정 증거 선택 |
| 폰트·인코딩 | `references/strategy/font-strategy.md` | 코드→글리프 대응, 전체 레퍼토리와 활성 작업 집합, 표현·도달 검증 |
| 텍스트 추출 | `references/strategy/text-extraction.md` | 모집단 확정, 소비자 기반 경계·토큰, 가역 산출물과 라운드트립 |
| PoC | `references/strategy/poc.md` | 가시성 PoC와 조건부 PoC 게이트의 수행 여부·통과 기준 판정 |
| 재삽입·훅 | `references/strategy/reinsertion.md` | 경계별 정책, 참조 완전성, 훅·공간·소비자 불변식 |
| 번역 | `references/strategy/translation-workflow.md` | Agent 배치, 맥락·승인 SSOT·보호 제약·고위험 의미의 적격 게이트 |
| 빌드·검증 | `references/strategy/build-and-verify.md` | 재현 가능한 산출물, 배포 경계, 계층별 검증과 종료 판정 |
| 디버깅·이슈 처리 | `references/strategy/debugging.md` | 경쟁 가설을 가르는 증거와 원인·수정·회귀 판정 |
| 그래픽 텍스트 (횡단) | `references/strategy/graphics-text.md` | 픽셀 텍스트 모집단, 보호 시각 자산과 소비 경로 검증 |
| 압축 대응 (횡단) | `references/strategy/compression.md` | 실제 변환 경계, 대상 소비자 호환성과 재패킹 검증 |
| 런타임 자산 도달성 (횡단) | `references/strategy/runtime-assets.md` | 변경된 저장→탐색→적재·변환→상주→소비 연결 판정 |

### 시행 컨벤션

| 범위 | 문서 | 내용 |
|------|------|------|
| 프로젝트 구현 (횡단) | `references/conventions/project-conventions.md` | 빌드 경계, 기계어 검산, Expected Write, 외부 구성요소 재현·원본 자산 취급 |
| 번역 자산 | `references/conventions/translation-artifacts.md` | 원문 보호, 제어 토큰, 검토 상태와 빌드 입력의 의미 규칙 |
| 프로젝트 기록 | `references/conventions/project-records.md` | 조사·PoC·그래픽 카탈로그·HITL·QA 증거와 판정의 기록 규칙 |
| 분석·빌드 데이터 | `references/conventions/data-formats.md` | 문자 매핑, 제어코드, 포인터, 번역 자산 연결, 재삽입 정책과 폰트 프로파일의 의미 규칙 |

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

목록에 없는 플랫폼이면 strategy의 조사·검증 원칙만 출발점으로 삼고, 이번 판단에 필요한 하드웨어·매체·주소공간·렌더링 경로를 새로 확정한다. 재사용할 플랫폼 사실이나 범위가 확인된 사례가 생기면 `references/platforms/` 아래에 문서화하되, 고정 목차를 채우지 말고 현재 분기와 검증을 바꾸는 사실·제약·실패 신호만 남긴다.

### 선택적 사례 단서

프로젝트 착수 때 tips를 전부 읽지 않는다. strategy가 현재 판단 영역과 발동 조건을 식별한 뒤에만 `references/tips/README.md`의 짧은 색인을 보고, 해당 사례의 앵커 하나만 읽는다. 관측 플랫폼과 범위는 증거의 출처와 전이 한계이며 선택 필수조건이 아니다. `references/tips/general.md`도 통독하지 않는다. tips는 조사 후보를 제안할 뿐 게이트·완료 조건·플랫폼 사실을 새로 만들 수 없으며, strategy와 충돌하면 strategy의 판단 기준을 따른다.

## 시작 체크리스트

새 게임에 착수할 때 다음 경계를 먼저 세운다. 조사 순서와 수단은 현재 불확실성에 맞춰 선택한다.

1. **대상과 입력 경계** — 게임·플랫폼·지원 리비전과 이번 작업이 바꾸려는 대상을 확인한다.
2. **책임 문서 확인** — 현재 판정을 소유하는 strategy를 읽고, 그 분기를 바꾸는 플랫폼 사실만 해당 문서에서 확인한다.
3. **기존 상태 우선** — 기존 저장소라면 코드·문서·산출물·검증 상태를 먼저 복원한다. 새 프로젝트라면 필요한 기록 위치만 마련한다.
4. **판정 가능한 조사** — `references/strategy/initial-survey.md`에 따라 가장 싼 증거 앵커에서 실제 의존 경계를 열고, 결론과 남은 가설을 기록한다.

## 핵심 불변식

어느 단계에서든 다음을 위반하지 않는다.

- **0원칙 — 플레이어는 보통 한 번만 플레이한다.** 한글 패치의 배포 기준은 "대체로 동작"이 아니라 알려진 치명 문제 0건이다. 크래시나 진행 불가는 물론이고 글자가 깨지거나, 힌트·아이템명이 틀리거나, 용어·말투가 무너지는 것도 플레이어의 단 한 번뿐인 경험을 망치므로 모두 블로커로 다룬다. 특히 오역은 단순 문장 품질 문제가 아니라 진행 실패, 선택지 오판, 캐릭터 이해 붕괴로 이어질 수 있다.
- **원본 ROM·디스크 이미지와 허가되지 않은 저작 자산은 커밋하지 않는다.** 허용 자산과 원본 식별 기준은 `references/conventions/project-conventions.md` §6을 따른다.
- **변환 경계는 수정 전에 검증한다.** 추출·직렬화·압축·컨테이너 재빌드를 사용하는 범위는 무변경 왕복을 먼저 검증한다. 바이트 표현이 유일하지 않은 포맷은 소비 의미와 보호 메타데이터의 동등 기준을 선언한다. 원본에 직접 패치하는 범위는 예상 원본 바이트와 적용 범위를 검증한다.
- **모든 쓰기는 Expected Write로 설명되어야 한다.** 기대 원본, 허용 범위, 소유자와 최종 바이트를 검증하고 쓰기 충돌·보호 범위 침범·추적되지 않은 diff를 빌드 실패로 처리한다.
- **작업 단위는 후속 선택지를 줄여야 한다.** 조사·PoC·번역 배치·검증은 성공/실패/불명확 어느 결과가 나와도 후속 판단을 더 정확하게 만드는 판정 가능한 형태로 설계한다. 시작 전에 무엇을 구분하려는지, 성공하면 승격할 지식이 무엇인지, 실패하면 버릴 가정이 무엇인지, 애매하면 어떤 더 작은 확인으로 쪼갤지를 의식한다. 결과가 후속 행동을 개선하지 못하면 먼저 질문을 좁힌다.
- **필요한 PoC 게이트를 통과하기 전에 본 구현에 착수하지 않는다.** 목표 경로의 가시성이나 위험 신호가 본 구현을 뒤집을 수 있고 동등한 증거로 아직 해소되지 않았다면, 해당 PoC를 통과하기 전까지 전량 번역, 전체 폰트 생성, 엔진 본 패치 같은 되돌리기 비싼 작업을 시작하지 않는다. 수행하는 PoC는 목표(0원칙)를 가장 크게 위협하는 블로커를 직접 검증해야 하며, 더 싼 저위험 실험으로 이를 대체하지 않는다.
- **사례 수치를 새 게임에 그대로 가정하지 않는다.** 글리프 슬롯 수, 빈 공간 크기, 포인터 폭 같은 수치는 선행 사례가 아니라 이 게임에서 재실측한 값을 쓴다. 특히 글리프 예산은 고정값이 아니라 병목 자원 산정 공식의 출력이다(`references/strategy/font-strategy.md` 3절).
- **역공학으로 확정하기 전에는 어떤 가정도 이식하지 않는다.** 같은 플랫폼·같은 개발사·같은 시리즈라도 선행 사례의 구조(스크립트 포맷, 포인터 규약, 제어코드)는 가설이지 사실이 아니다.
- **인코딩 누락은 빌드 에러다.** 번역문에 글리프·코드 매핑이 없는 문자가 있으면 조용히 건너뛰지 말고 빌드를 실패시킨다.
