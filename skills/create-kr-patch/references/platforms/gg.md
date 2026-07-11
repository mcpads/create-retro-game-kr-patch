# Sega Game Gear

Z80·VDP·mapper의 기본 사양은 필요할 때 1차 자료에서 확인한다. 패치 판단에서는 bank가 바뀌는 실행 좌표, VDP port와 값 생성자, 저장 자산과 화면 소비를 서로 구분한다.

## 1. 논리 주소와 bank identity

16-bit 논리 주소만으로 ROM 파일 위치를 정할 수 없다. 해당 접근 시점의 slot, bank register, fixed window·RAM mapping과 mapper 변형이 함께 있어야 한다. 확인된 mapping에서만 논리 주소↔bank↔파일 위치 변환을 사양으로 둔다.

훅이 bank를 바꾸면 실행·데이터 수명과 interrupt·callback의 공유 상태를 검증하고 진입 전 bank·interrupt 상태를 복원한다. 특정 enable/disable 쌍을 전역 해법으로 두지 않는다.

## 2. ROM 확장

파일 크기와 header size code의 변경만으로 추가 bank가 노출되지 않는다. mapper의 선택 경로, header·checksum 소비, save RAM window와 실제 cartridge·loader 지원이 모두 새 범위를 표현할 때만 확장 자산을 둔다.

## 3. VDP 좌표와 쓰기 관찰 범위

VRAM·CRAM은 일반 memory write가 아니라 VDP port I/O로 소비된다. 일반 메모리 쓰기 기록에 나타나지 않았다는 사실만으로 화면 쓰기 부재를 판정하지 않는다.

내부 name table과 실제 LCD viewport의 관계는 현재 VDP register·scroll·display 상태가 소유한다. 고정 행·열 offset이나 이론적 tile 수를 모든 화면의 좌표·폰트 예산으로 쓰지 않는다.

저장 글리프가 최종 VDP tile 표현인지, 중간 RAM 변환을 거치는지도 실제 전송 전후로 판정한다.

## 4. 저장에서 화면 소비까지

VDP port 전송은 최종 하드웨어 upload/write 경계이며 그 값을 만든 writer나 적재 시점과 같지 않을 수 있다. 그 write가 실제 name table·sprite·viewport에서 소비되는지는 별도로 확인한다. 새 bank의 폰트나 VRAM slot을 쓰면 저장→적재·변환→상주→소비 연결과 상태별 작업 집합을 `references/strategy/runtime-assets.md` 및 `references/strategy/font-strategy.md` §3으로 판정한다.

상점 렌더 세션에서 최종 VDP writer가 아니라 앞선 창별 base 선택이 원인이었던 사례는 현재 조건이 맞을 때만 `references/tips/gg.md#gg-001`에서 읽는다.

## 5. 텍스트와 코드 공간

인코딩, token 폭과 pointer 규약은 게임별 소비자에서 확정한다. 새 prefix·pair를 쓰면 실제 허용 집합에서 원본 문자·제어·종료·별도 renderer 의미를 뺀 범위만 코드 공간으로 인정한다.

## 6. 코드 개입과 공간

훅의 층수·형태는 플랫폼 규칙이 아니다. 실제 branch range, bank budget, live state와 원본 효과의 검증 기준은 `references/strategy/reinsertion.md` §4를 따른다. 공유 VWF·tile allocator 상태를 쓰면 모든 writer와 초기화·전이·해제 owner를 확인한다.

## 7. 검증

다음 중 이번 변경이 닿은 경로만 검증한다.

- 논리 주소·slot·bank·파일 위치 왕복
- bank·interrupt·공유 상태의 복귀 불변식
- 저장 글리프→RAM 변환→VDP port→화면 소비
- viewport 좌표와 화면 전환·재진입 뒤 자산 수명
- 확장 bank와 save path를 사용하는 실제 배포 대상

다른 build의 상태 저장을 재사용하면 ROM·RAM layout 호환성을 먼저 확인한다.
