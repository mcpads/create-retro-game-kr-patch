---
name: create-kr-patch
description: >-
  Create Korean (Hangul) fan-translation patches for retro games from ROM or
  disc survey and text-engine reverse engineering through fonts, encoding,
  extraction, translation, reinsertion, hooks, reproducible builds, patch
  generation, and emulator verification. 레트로 게임 한글화·한글 패치·ROM 번역의
  신규 조사와 기존 프로젝트 후속 작업에 사용한다.
---

# 레트로 게임 한글 패치 제작

## 방향

대상 게임의 증거로 현재 판단을 갱신하며 초기 조사부터 폰트·인코딩, PoC, 추출, 번역, 재삽입, 빌드, 배포 패치와 실행 검증까지 연결한다.

도구·언어·라이브러리·폰트는 대상 프로젝트의 기존 구조와 현재 환경에서 선택하고, 선택과 무관하게 요구 능력과 검증 기준을 충족한다. 명확한 1차 자료 한 곳에서 쉽게 확인할 수 있는 기본 사양은 필요할 때 최신 자료에서 확인한다.

이 방법론은 일본어 원문·텍스트 중심의 선행 경험에서 출발했다. 빈도와 선행 구조는 대상 리비전의 증거로 다시 판정한다.

## 라우팅

기존 저장소에서는 코드·문서·산출물·검증 상태를 복원한 뒤 현재 판단을 고른다. 새 게임이나 구조가 불명확한 대상은 초기 조사에서 시작한다.

| 판단 영역 | 문서 | 내용 |
|------|------|------|
| 초기 조사 | `references/strategy/initial-survey.md` | 완성 여부를 좌우하는 조건, 실제 의존 경계, 초기 분량·미확정 모집단과 확정 리비전 사양 |
| 폰트·인코딩 | `references/strategy/font-strategy.md` | 코드→글리프 대응, 전체 레퍼토리와 활성 작업 집합, 표현·도달 검증 |
| 텍스트 추출 | `references/strategy/text-extraction.md` | 모집단·초기 분량 확정, 소비자 기반 경계·토큰, 가역 산출물과 라운드트립 |
| PoC | `references/strategy/poc.md` | 가시성·조건부 PoC의 수행 여부와 통과 기준 판정 |
| 재삽입·훅 | `references/strategy/reinsertion.md` | 경계별 정책, 참조 완전성, 훅·공간·소비자 불변식 |
| 번역 | `references/strategy/translation-workflow.md` | 에이전트 배치, 맥락 확정, 승인 용어·문체, 보호 제약과 고위험 의미의 적격 판정 |
| 빌드·검증 | `references/strategy/build-and-verify.md` | 재현 가능한 산출물, 배포 경계, 계층별 검증과 종료 판정 |
| 디버깅·이슈 처리 | `references/strategy/debugging.md` | 플레이 경로·목표 상태 도달, 상태 개입의 증명 범위와 원인·수정·회귀 판정 |
| 그래픽 텍스트 (횡단) | `references/strategy/graphics-text.md` | 픽셀 텍스트 모집단, 보호 시각 자산과 소비 경로 검증 |
| 압축 대응 (횡단) | `references/strategy/compression.md` | 실제 변환 경계, 대상 소비자 호환성과 재패킹 검증 |
| 런타임 자산 도달성 (횡단) | `references/strategy/runtime-assets.md` | 변경된 저장→탐색→적재·변환→상주→소비 연결 판정 |

산출물·교환 데이터·기록을 설계하거나 검증할 때 해당 시행 규약을 함께 적용한다. 기존 저장소에 동등한 구조가 있으면 그 구조를 유지한다.

| 범위 | 문서 | 내용 |
|------|------|------|
| 프로젝트 구현 (횡단) | `references/conventions/project-conventions.md` | 빌드 경계, 기계어 검산, 최종 변경 검증, 외부 구성요소 재현·원본 자산 취급 |
| 번역 자산 | `references/conventions/translation-artifacts.md` | 원문 보호, 제어 토큰, 검토 상태와 빌드 입력의 의미 규칙 |
| 프로젝트 기록 | `references/conventions/project-records.md` | 조사·PoC·그래픽 카탈로그·HITL·QA 증거와 판정의 기록 규칙 |
| 분석·빌드 데이터 | `references/conventions/data-formats.md` | 문자 매핑, 제어코드, 포인터, 번역 자산 연결, 재삽입 정책과 폰트 구성 정보의 의미 규칙 |

현재 분기를 바꾸는 하드웨어·매체·주소공간·렌더링 제약은 해당 플랫폼 문서에서 확인한다.

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

목록에 없는 플랫폼은 현재 판단에 필요한 제약을 대상 게임에서 확정한다.

새 판단을 시작하거나 관측 증상이 바뀌면 `references/tips/README.md`에서 판단 영역과 발동 조건을 대조하고, 맞는 사례의 전이 한계를 현재 대상에서 검증한다. 완료는 주 strategy의 기준으로 판정한다.

## 판단 흐름

- 선언한 완성 범위와 반드시 성립해야 할 조건을 먼저 확인한다.
- 실패하면 완성이 불가능하거나 설계를 크게 바꾸는 미확정 조건을 먼저 판정하고, 같은 조건을 가르는 증거 중 비용이 낮은 것을 고른다.
- 서로 독립된 경계는 병렬로 조사하고, 새 증거가 뒤집은 판정만 원인 경계로 되돌린다.
- 모집단·경계·소비 규칙이 확정된 범위만 번역·재삽입 완료로 판정한다.
- 대표 PoC는 모집단 조사와 병행할 수 있다. 전체 배포 범위로 번역을 확대하기 전 모집단·분량은 `references/strategy/text-extraction.md` §1.5로, 초벌 코퍼스에서 드러난 글리프 수요와 공급 가능성은 `references/strategy/translation-workflow.md` §5와 `references/strategy/font-strategy.md` §3으로 판정한다.
- 유한한 표시 영역은 원본이 실제로 사용한 범위와 소비자가 허용하는 한도를 구분해 `references/strategy/translation-workflow.md` §4로 판정한다.
- 글리프·길이·레이아웃 예산이 부족하면 공급 확대 가능성을 판정하고, 의미 손실이 있는 축소는 사람이 승인한다.
- 변경 산출물은 실제 빌드와 소비 경로에서 검증하고, 결함은 처음 값이 달라진 원인 경계에서 수정한다.

## 핵심 불변식

어느 작업에서든 다음을 위반하지 않는다.

- **0원칙 — 플레이어는 보통 한 번만 플레이한다.** 한글 패치의 배포 기준은 "대체로 동작한다"가 아니라 알려진 치명 문제 0건이다. 크래시나 진행 불가는 물론, 글자가 깨지거나 힌트·아이템명이 틀리거나 용어·말투가 무너지는 문제도 플레이어의 단 한 번뿐인 경험을 망치므로 모두 배포를 막는다. 특히 오역은 단순한 문장 품질 문제가 아니라 진행 실패나 선택지 오판을 부르고 인물 이해까지 무너뜨릴 수 있다.
- **원본 ROM·디스크 이미지와 허가되지 않은 저작 자산은 커밋하지 않는다.** 허용 자산과 원본 식별 기준은 `references/conventions/project-conventions.md` §6을 따른다.
- **변환 경계는 수정 전에 검증한다.** 해당 경계가 요구하는 바이트 가역성 또는 소비 의미와 보호 정보의 동등성을 입증한다. 상세 조건은 `references/conventions/project-conventions.md` §5.1을 따른다.
- **최종 산출물의 모든 변경은 적용 전에 검증 가능해야 한다.** 불변 원본을 기준으로 각 변경을 만드는 경로와 허용 범위를 확인하고, 서로 겹치는 변경·보호 범위 침범·설명되지 않은 최종 변경을 빌드 실패로 처리한다. 상세 조건은 `references/conventions/project-conventions.md` §5.2를 따른다.
- **기계어 생성·이동은 대상 명령 집합의 유효 범위를 선언하고 그 전체를 검산한다.** 패치에 필요한 일부 명령만 검증해 생성·이동·제어 흐름의 완전성을 주장하지 않는다. 상세 조건과 제한된 예외는 `references/conventions/project-conventions.md` §2.3을 따른다.
- **번역 일괄 변경은 사람이 승인한다.** 자동 검출은 후보와 영향 범위만 만들며, 기준선·변환 규칙·적용 범위·예상 영향을 사람이 확인하기 전에는 번역문을 일괄 변경하지 않는다. 상세 조건은 `references/strategy/translation-workflow.md` §5를 따른다.
- **언어 품질 휴리스틱은 판정이 아니다.** 사전 등재 여부, 빈도, 맞춤법·띄어쓰기 검사와 LLM이 매긴 점수는 검토 후보와 근거만 만든다. 사람이 적용 단위와 허용값을 확정했거나 보호 정보·실제 소비 제약처럼 참·거짓을 기계적으로 가릴 수 있는 경우만 위반을 자동 판정한다. 이 경우에도 번역문 일괄 변경은 앞 원칙의 승인을 따른다. 상세 경계는 `references/strategy/translation-workflow.md` §5를 따른다.
- **증거는 하나의 완성 경로를 판정해야 한다.** 조사·PoC·번역·검증은 선언한 완성 범위의 선택을 줄여야 한다. 구성요소별 성공을 합산해 완성으로 판정하지 않는다. 선언한 범위의 모든 변경을 불변 원본과 승인 입력에서 주 빌드 경로로 함께 생성한 동일한 빌드 결과에서 검증한다. 완성 여부를 좌우하는 조건을 그대로 둔 부분 성공은 그 조건의 통과 증거가 아니다.
- **사례 수치를 새 게임에 그대로 가정하지 않는다.** 필요한 값은 대상 리비전과 실제 소비 조건에서 다시 측정한다.
- **역공학으로 확정하기 전에는 어떤 가정도 이식하지 않는다.** 같은 플랫폼·같은 개발사·같은 시리즈라도 선행 사례의 구조(스크립트 포맷, 포인터 규약, 제어코드)는 가설이지 사실이 아니다.
- **주요 문자 집합은 검증 가능한 기성 글꼴에서 공급한다.** PoC의 편의를 이유로 본문 자형을 직접 만들지 않는다. 직접 제작·보정은 필수 글리프의 국소 누락이나 확인된 UX 요구에 한정하며, 상세 판정은 `references/strategy/font-strategy.md` §4를 따른다.
- **인코딩 누락은 빌드 에러다.** 번역문에 글리프·코드 매핑이 없는 문자가 있으면 조용히 건너뛰지 말고 빌드를 실패시킨다.
