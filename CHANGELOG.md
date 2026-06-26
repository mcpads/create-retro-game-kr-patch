# Changelog

이 프로젝트의 주요 변경 사항을 기록한다. 형식은 [Keep a Changelog](https://keepachangelog.com/ko/1.1.0/)를 따르고, 버전은 [유의적 버전](https://semver.org/lang/ko/)을 따른다.

## [Unreleased]

## [0.3.0]

### Added
- 닌텐도 DS 플랫폼 문서(`references/platforms/nds.md`) 추가 — ARM9/ARM7, NitroFS, 인코딩·렌더 경로 등. `SKILL.md` 라우팅 테이블에 NDS 항목 추가. (mirusu400, PR #1)
- 복수 렌더 타깃의 폰트 설정 외부화 패턴 (`font-strategy` §8) — 타깃별 폰트 프로파일을 타입 검증되는 설정 파일로 분리, CLI override → 설정 값 → 기본값 해결 순서, 단일 폰트 프로젝트에는 과설계라는 경계 명시. `project-conventions`의 JSON 입출력 규약에 cross-ref 연결.

## [0.2.0]

### Changed
- 사례 실적 과시 수치(포인터·글리프·바이트 예산 등)와 "제작자 확인" 류 빈권위 표현을 제거하고 교훈 중심으로 정렬.
- 원칙·교훈 섹션의 비공개 게임 일화를 사례성 표현("한 사례에서는 …")으로 일반화. 일반화 과정에서 단일 사례가 빈도·보편 주장으로 격상되지 않도록 전수 교정. 공식·인코딩 경계·코드·"사례 요약" 섹션은 보존.

### Added
- 실패→원인→해법 디버깅 교훈 보강 (`tips`, `debugging`).
- 글리프 예산 입력값 측정 절차 보강 (`font-strategy`, `text-extraction`).
- 검증 자동화의 선행 비용·한계 경고 + 검증 인프라를 작업 시점에 조사·개조하는 방향 (`build-and-verify`).
- 오역=블로커를 강제하는 자동 검출 게이트 보강 (`translation-workflow`).
- 의도적 EDC/ECC 오류(카피 프로텍션) 정정 금지 경고 (`build-and-verify`, `saturn`, `ps1`).
- 레이아웃을 글자 폭 테이블로 분리하는 설계 옵션 (`reinsertion`).

## [0.1.0]

### Added
- 레트로 게임 한글 패치 제작 skill 최초 공개.
- 단계별 공통 전략 문서 12종 (`references/strategy/`): 초기 조사, 폰트·인코딩, 텍스트 추출, PoC, 재삽입·훅, 번역, 빌드·검증, 디버깅, 그래픽 텍스트, 압축, 저장소 규약, 실전 팁.
- 플랫폼별 하드웨어·사례 노트 8종 (`references/platforms/`): SNES, 메가드라이브, 새턴, PS1, 드림캐스트, PC엔진, PC-98, 게임기어.
- Claude Code 플러그인 매니페스트 및 셀프호스팅 마켓플레이스 구성.
- MIT 라이선스로 공개.
