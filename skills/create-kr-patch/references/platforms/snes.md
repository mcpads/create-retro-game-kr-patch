# SNES / Super Famicom

65816·PPU·ROM mapping의 기본 사양은 필요할 때 1차 자료에서 확인한다. 실행 mode와 명령 경계, ROM 좌표, 저장 폰트와 PPU 소비는 서로 구분한다.

## 1. 실행 mode와 훅 불변식

65816의 M/X 상태는 register 폭뿐 아니라 immediate instruction 길이를 바꾼다. 훅이나 옮긴 원본 코드는 진입점의 M/X, bank·direct-page·stack과 live flags를 포함해 원래 명령 경계와 효과를 보존해야 한다.

## 2. ROM 좌표와 확장

CPU 주소↔파일 offset 관계는 확인된 mapping mode, mirror, copier-header 표현과 특수 chip mapping 안에서만 성립한다. 한 mapping의 공식을 다른 mode나 확장 영역에 이식하지 않는다.

ROM 파일을 늘렸다는 사실만으로 CPU·실기·loader가 새 bank를 읽지 않는다. mapper·header·checksum, save memory·mirror 충돌과 실제 배포 대상이 새 범위를 표현할 때만 확장 자산을 둔다.

## 3. 저장 폰트와 PPU 소비

ROM·WRAM의 폰트 바이트가 PPU의 최종 tile 표현이라는 보장은 없다. 압축·staging·runtime layout conversion이 있으면 저장 자산, 전송 직전 표현, VRAM 좌표와 tilemap·OBJ 소비를 연결한다.

VRAM register 좌표와 파일 byte offset은 단위가 다를 수 있다. 변환 경계에서 단위를 명시하고 같은 좌표 변환 규칙을 사용한다. 본문 BG의 성공을 OBJ·menu·그래픽 텍스트 경로로 확대하지 않는다.

## 4. 전송과 자산 수명

VRAM write·DMA는 게임의 blanking·NMI queue·DMA ownership 안에서 성립해야 한다. 패치가 잠깐 보였다가 사라지면 대상 범위의 모든 writer, 마지막 writer, 화면 전환·재진입 뒤 reload와 staging 영역의 다른 소비자를 확인한다.

새 font bank·overlay tile·추가 slot을 쓰면 `references/strategy/runtime-assets.md`의 적재·상주·소비 게이트를 적용한다.

## 5. 텍스트와 참조

문자·token 폭은 CPU 이름이 아니라 실제 fetch 시점의 mode와 pointer 증가가 소유한다. pointer는 현재 bank·base와 mapping 없이 파일 타깃을 정하지 못한다.

## 6. 검증

다음 중 이번 변경이 닿은 경로만 검증한다.

- 훅 진입·복귀의 mode·bank·stack·live-state 불변식
- mapping별 CPU 주소↔파일 위치 왕복과 확장 bank 도달
- 저장 글리프→변환→VRAM→실제 BG·OBJ 소비
- NMI·DMA queue와 화면 재진입 뒤 마지막 writer
- 확장 ROM을 사용하는 실제 배포 대상
