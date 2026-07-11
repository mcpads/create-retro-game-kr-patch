# Sega Mega Drive / Genesis

CPU·VDP의 기본 사양은 필요할 때 1차 자료에서 확인한다. 패치 판단에서는 ROM 좌표, 저장 글리프와 VDP 소비, 확장 매체의 경계를 서로 구분한다.

## 1. 실행 좌표와 데이터 의미

68000 실행 코드의 endian·정렬은 훅과 직접 읽는 테이블에 적용되지만, archive·VM·byte stream 필드의 저장 순서를 대신 확정하지 않는다. 실제 reader의 load·swap·주소 계산으로 각 필드를 판정한다.

코드를 이동하면 원본 instruction 경계, PC-relative operand, branch target, live register·condition code의 의미를 새 위치에서 검증한다.

## 2. ROM mapping과 확장

CPU 주소와 파일 offset의 직접 대응은 mapper가 개입하지 않는 확인된 범위에만 적용한다. 파일을 키우거나 header의 크기 표현을 바꿨다는 사실만으로 새 ROM 범위가 CPU·실기·loader에 노출되지 않는다.

확장 범위를 쓰면 mapper의 실제 선택 경로, header·checksum 소비 범위, SRAM·주변 mapping과 배포 대상의 최종 크기 지원을 함께 검증한다.

## 3. 저장 글리프와 VDP 소비

ROM의 폰트 바이트가 VDP의 최종 tile 표현이라는 보장은 없다. 압축·RAM staging·runtime conversion이 있으면 저장 자산, 변환 결과, VRAM 전송과 name-table·sprite 소비를 연결한다.

VRAM은 글리프 외의 화면 자산도 공유한다. 전체 레퍼토리와 상태별 작업 집합을 분리하고, 선택한 상주 방식의 reload·eviction·last-writer 수명을 `references/strategy/font-strategy.md` §3과 `references/strategy/runtime-assets.md`로 판정한다.

전송은 게임의 DMA·interrupt ownership과 표시 상태 안에서 성립해야 한다. 본문 plane의 성공을 Window·sprite·menu·HUD 경로로 확대하지 않는다.

## 4. 텍스트와 참조

인코딩, token 폭, pointer의 폭·기준·정렬은 플랫폼 이름으로 정하지 않는다. 실제 fetch·dispatcher·glyph lookup과 각 pointer 소비자가 사양을 소유한다.

토큰 정책은 `references/strategy/translation-workflow.md` §4, 추출과 재배치 판정은 `references/strategy/text-extraction.md` 및 `references/strategy/reinsertion.md`가 소유한다.

## 5. 검증

다음 중 이번 변경이 닿은 경로만 검증한다.

- 실행 code의 원본 효과·분기·live state
- mapper를 포함한 CPU 주소↔파일 위치 왕복과 확장 범위 도달
- 저장 글리프→변환→VRAM→실제 renderer 연결
- 화면 전환·재진입 뒤 자산·상태 수명
- header·checksum과 배포 대상의 최종 크기 지원 조건

부팅이나 한 화면의 정상 표시를 다른 mapper·renderer·상태 수명의 증거로 쓰지 않는다.
