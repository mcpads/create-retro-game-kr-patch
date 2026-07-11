# Nintendo DS

NDS의 header·NitroFS·VRAM 기본 사양은 필요할 때 1차 자료에서 확인한다. 실행 image·overlay·파일·VRAM 소비자는 같은 좌표나 정체성으로 취급하지 않는다.

## 1. 실행 image와 overlay 정체성

ARM9·ARM7 image는 독립된 load 범위를 가지며 어느 CPU가 텍스트·폰트·파일 적재를 담당하는지는 게임별 사실이다. CPU 역할을 관습으로 정하지 않고 실제 호출·적재 경로로 확인한다.

runtime 주소를 ROM 위치로 환산하려면 현재 image의 ROM 범위, load 범위와 변환 여부가 먼저 확정돼야 한다. 선형 대응은 비압축 정적 image 안에서만 성립한다. overlay는 overlay entry와 file ID, FAT extent, 현재 적재 상태를 함께 식별하며, 같은 RAM 주소를 재사용하는 다른 overlay에 주소만으로 패치하지 않는다.

압축·relocation·초기화가 있으면 ROM bytes와 실행 bytes를 직접 대조하지 않는다. 저장 overlay 파일이 성장·이동하면 file ID·FAT extent·저장 크기와 loader read buffer를 확인한다. 해제된 runtime image의 주소·크기, BSS나 static initializer가 바뀌면 overlay entry·RAM 인접 영역과 초기화 소비자를 별도로 검증한다. 저장 파일 크기 변화만으로 runtime image 배치 변경을 가정하지 않는다.

## 2. 파일 이름과 실제 로더

FNT 이름, FAT file ID, raw ROM offset과 게임 자체 archive는 한 ROM 안에 함께 존재할 수 있다. 이름 있는 SDK형 파일을 발견했다는 사실을 모든 자산의 저장 규칙으로 확대하지 않는다.

파일을 성장·이동할 때는 실제 로더가 사용하는 identity를 따라 FAT extent, overlay entry와 게임 자체 offset·size table 가운데 해당되는 소유자를 모두 확인한다. 이름이나 magic이 맞아도 reader가 field·section·compression을 다르게 소비하면 표준 serializer로 교체하지 않는다.

## 3. 저장 자산과 화면 소비

저장 font·bitmap과 최종 BG·OBJ·bitmap·3D texture 표현 사이에는 해제, RAM 변환, VRAM bank mapping과 cache가 있을 수 있다. 한 engine·화면에서 보인 글리프를 다른 engine이나 상태의 증거로 쓰지 않는다.

VRAM mapping·전송 시점·cache slot을 바꾸면 동시에 쓰는 다른 소비자와 화면 전환·sleep·resume 뒤 수명을 검증한다. 파일에 자산을 넣는 것과 renderer가 그 자산을 찾아 상주시켜 소비하는 것은 별도 게이트이며, 변경 시 `references/strategy/runtime-assets.md`를 적용한다.

## 4. secure area와 banner 경계

secure area 전체, 그 안의 암호화된 prefix, 표식과 CRC 범위는 같은 개념이 아니다. 이 영역을 수정할 때만 입력이 암호화·복호화 중 어느 표현인지와 배포 경로가 요구하는 변환을 판정한다. 건드리지 않은 secure area를 재암호화·정상화하지 않는다.

banner는 없을 수 있고, 한국어 title slot과 CRC 범위는 banner version에 따라 달라진다. version을 올려야 한다면 version word만 바꾸지 않고 전체 길이, version별 필드·CRC 범위, 뒤따르는 ROM 영역과 target loader를 함께 검증한다. banner를 수정하지 않는 빌드에는 upgrade 절차를 강제하지 않는다.

## 5. 재빌드와 검증

다음 중 이번 변경이 닿은 경로만 검증한다.

- ARM9·ARM7 image 또는 overlay의 실제 identity와 ROM↔runtime 변환
- FNT 이름·FAT file ID·게임 자체 table 가운데 실제 loader가 소유한 좌표
- 저장 자산→해제·변환→VRAM mapping·cache→실제 renderer 소비
- overlay·화면 전환과 sleep·resume 뒤 reload·상주 수명
- 수정한 경우에만 secure area·banner의 표현과 무결성 범위

특정 flashcart·실기·loader 호환을 주장하면 그 경로에서 최종 후보를 검증한다. 한 에뮬레이터의 부팅 성공을 다른 실행 경로의 증거로 확대하지 않는다.
