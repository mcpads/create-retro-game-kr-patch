# PC Engine / CD-ROM²

HuC6280·VDC·CD-ROM²의 기본 사양은 필요할 때 1차 자료에서 확인한다. MPR 상태가 만드는 좌표, CD 적재와 runtime overlay, 저장 폰트와 화면 소비의 경계를 서로 구분한다.

## 1. MPR과 주소 identity

논리 주소만으로 ROM·RAM·파일 위치를 정할 수 없다. 접근 시점의 MPR state와 매체의 physical layout이 함께 있어야 하며, CD-loaded code·buffer에는 loader의 sector/file→RAM 관계가 추가된다.

pointer가 논리 주소만 저장하면 현재 MPR·base도 사양의 일부다. bank를 바꾸는 훅은 interrupt·callback의 공유 page, code·data 수명과 복귀 mapping을 검증한다. runtime overlay identity가 미확정이면 현재 mapping을 고정값으로 가장하지 않는다.

## 2. 저장 글리프와 VDC 소비

ROM·RAM font가 VDC의 최종 pattern 표현이라는 보장은 없다. 압축·staging·runtime composition이 있으면 저장 자산, 전송 직전 표현, VRAM과 BAT·sprite 소비를 연결한다.

VRAM은 다른 화면 자산과 공유되므로 이론적 총량을 폰트 예산으로 쓰지 않는다. 본문·menu·sprite·그래픽 텍스트와 BIOS font 경로의 증거도 각 소비자 범위에만 적용한다. 새 font page나 cache는 `references/strategy/runtime-assets.md`로 판정한다.

## 3. HuCard와 CD-loaded 경계

HuCard 파일 확장만으로 새 physical segment가 실기·loader에 노출되지 않는다. mapper와 배포 대상이 새 범위를 실제로 선택해야 한다.

CD 게임의 runtime 주소를 disk 위치로 연결하려면 track·sector 표현, file/sector start와 read length, destination RAM·MPR, overlay reload identity를 함께 확인한다. BIOS call 이름이나 한 타이틀의 loader sequence를 전체 CD 경로로 일반화하지 않는다.

## 4. CD 이미지와 sector

cooked user-data offset과 raw sector file offset을 섞지 않는다. raw 출력을 바꾸면 실제 sector mode의 보호 필드는 serialization 경계가 책임지고, 변경하지 않은 audio·비정상 sector·track padding은 근거 없이 정상화하지 않는다.

파일·자산을 옮기면 filesystem뿐 아니라 게임의 sector·length table, read alignment, RAM buffer와 streaming timing을 검증한다. 빈 sector처럼 보이는 범위는 다른 track·pregap·streaming 예약을 배제하기 전에는 자유 공간이 아니다.

## 5. 텍스트와 새 런타임 경로

인코딩·token·pointer 경계는 실제 소비자에서 확정한다. 음성·컷신에 자막을 새로 추가하면 번역 데이터뿐 아니라 timing, skip input, audio state와 화면 layer가 새 런타임 요건이 된다.

BIOS font 경로의 한글 가시성은 그 경로만 증명하며 새 code space, 전체 글리프 공급이나 다른 renderer를 증명하지 않는다. 조건부 PoC는 `references/strategy/poc.md`가 소유한다.

## 6. 검증

다음 중 이번 변경이 닿은 경로만 검증한다.

- 논리 주소·MPR·physical 위치와 file/sector 좌표 연결
- bank·interrupt 전후의 mapping 복귀
- 저장 글리프→변환→VRAM→BAT·sprite 소비
- CD track·sector·게임 read table과 overlay reload
- 자막·음성 변경의 timing·skip·scene transition
- 배포에서 주장하는 System Card·optical loader·hardware 경로
