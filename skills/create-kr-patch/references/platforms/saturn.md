# Sega Saturn

SH-2·VDP·CD-ROM의 기본 사양은 필요할 때 1차 자료에서 확인한다. 이동 code의 literal·delay 의미, VDP1/VDP2 소비, module·압축·disc 계층은 서로 구분한다.

## 1. 이동 code와 적재 module

어느 SH-2와 task가 대상 code를 실행하는지는 게임별로 확인한다. instruction을 이동하거나 block을 늘리면 branch delay, PC-relative literal pool, alignment, live register·PR·flags와 code/inline-data 경계를 함께 검산한다.

## 2. VDP1·VDP2 소비 분리

VDP1 command/texture 경로와 VDP2 pattern/name-table 경로는 자산·주소·palette·clipping·수명 요건이 다르다. 한 renderer의 한글 PoC를 다른 renderer·menu·battle·그래픽 텍스트에 확대하지 않는다.

VDP2 name data의 character·palette·flip 의미와 활성 VRAM 예산은 현재 pattern-name data size, PNCN supplementary mode, color depth·character size와 plane 설정에서 판정한다. 이론적 총량이나 고정 bit 폭을 모든 화면의 글리프 상한으로 쓰지 않는다.

새 glyph를 넣으면 loader, work RAM, VRAM upload와 최종 command·name-table 소비를 `references/strategy/runtime-assets.md`로 연결한다.

## 3. 텍스트·pointer·loadable module

CPU endian은 script VM·container field의 저장 규약을 대신 정하지 않는다. loadable module과 event script가 absolute address, relative offset, index와 inline code/data를 섞으면 각 소비자와 실제 적재 module을 따로 확인한다.

파일 성장 시 text pointer뿐 아니라 load buffer, 뒤따르는 code·literal·metadata, 중간 진입·shared tail과 다른 파일의 중복 address·size table을 확인한다. 한 타이틀의 pointer pattern을 플랫폼 규칙으로 쓰지 않는다.

## 4. 압축 자산

실제 압축 변형은 target loader와 game decompressor로 확정한다. 압축 이름과 magic은 후보를 좁히는 데 사용하고, 대상 소비자 호환성과 결함 시 대조군은 `references/strategy/compression.md`로 판정한다.

## 5. Disc와 ISO 계층

track·sector 표현, filesystem extent와 game LBA·size table은 서로 다른 계층이다. ISO directory가 유효하다는 사실만으로 game loader가 이동한 파일을 읽는다고 판정하지 않는다. multi-extent 파일이면 최종 record까지 같은 파일로 처리하되, 기존 loader 지원 없이 새 배치를 도입하지 않는다.

새 위치는 data track·filesystem의 유효 범위, 다른 extent·track·pregap과의 비중복, game read alignment·buffer·streaming을 통과해야 한다. raw user data를 바꾸면 변경 sector의 실제 mode에 맞는 보호 필드만 갱신하고 원본의 비대상 비정상 field는 보존한다.
