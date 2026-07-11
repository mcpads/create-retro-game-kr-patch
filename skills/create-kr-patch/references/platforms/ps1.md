# PlayStation

MIPS·GPU·CD-ROM·ISO 9660의 기본 사양은 필요할 때 1차 자료에서 확인한다. runtime code, 저장 자산, raw sector와 filesystem 좌표는 서로 구분한다.

## 1. 실행 code와 module 정체성

runtime 주소를 파일 위치로 바꾸려면 현재 executable·overlay·module의 load 범위와 relocation·decompression을 함께 확인한다. 통상 load address나 한 executable의 환산식을 다른 module에 이식하지 않는다.

RAM에서 읽은 code bytes와 CPU가 cache를 통해 실행하는 instruction stream은 다를 수 있다. 코드가 동적 적재·덮어쓰기되면 module identity, alias·cache 상태와 갱신 시점을 확인한다. 훅이나 옮긴 명령은 현재 ISA 자료로 delay·load hazard와 live state를 검산하고, 공통 생성·재해석 규칙은 `references/conventions/project-conventions.md` §2.4를 따른다.

## 2. 폰트와 GPU 소비

BIOS에 글리프 서비스가 존재한다는 사실은 대상 게임이나 모든 화면이 그 경로를 쓴다는 증거가 아니다. 확인된 호출 경로의 반환 표현, 게임 변환·cache, VRAM upload와 실제 primitive 소비까지 연결한다.

자체 font·texture도 파일을 decode한 결과만으로 승인하지 않는다. 저장 자산, RAM 표현, VRAM 좌표·CLUT와 화면 소비를 연결해 검증하고, 추가·성장·이동하면 `references/strategy/runtime-assets.md`를 적용한다.

## 3. 텍스트·archive·참조

CPU endian은 문자 bytes, archive field나 script VM의 저장 순서를 대신 정하지 않는다. 실제 reader의 load·swap·pointer 증가와 소비자로 판정한다.

script module은 absolute RAM pointer, module-relative offset, index와 inline code를 섞을 수 있다. 텍스트가 성장할 때는 문자열 참조뿐 아니라 뒤따르는 code·metadata와 내부 위치 의존 값을 확인한다. 같은 확장자나 개발사 선례는 후보일 뿐 무수정 왕복과 대상 reader로 다시 확정한다.

## 4. raw sector와 ISO 좌표

Mode 2 data track은 sector마다 form이 다를 수 있다. 수정 sector의 복제 subheader와 form을 판정해 해당 EDC/ECC 규칙만 적용하고, 변경하지 않은 sector의 비정상·보호 표현을 정상화하지 않는다.

ISO 파일도 항상 하나의 연속 extent는 아니다. multi-extent record를 종결 record까지 묶고, extent·length의 중복 endian 표현과 실제로 이동한 directory·path·game LBA/size 소유자를 함께 갱신한다. 기존 loader 지원을 증명하지 않은 채 새 multi-extent 구조를 도입하지 않는다.

filesystem LBA, raw track sector와 image byte offset은 서로 다른 좌표다. raw-sector 표현을 출력한다면 같은 크기의 제자리 교체도 수정 sector의 보호 필드를 다시 검증한다. 빈 구간처럼 보이는 영역도 data track·filesystem·loader가 모두 새 소비를 허용할 때만 사용한다.

## 5. runtime CD ownership

새 자산 읽기는 기존 CD state machine, IRQ·DMA와 XA·CDDA·movie streaming의 장치 소유권과 경쟁할 수 있다. 기존 loader 재사용이나 별도 장치 제어를 기본 해법으로 지정하지 않는다.

읽기 경로를 바꾸면 호출 시점의 초기화·재진입 가능성, read mode·sector form·buffer, 동시 streaming, 완료 뒤 command·IRQ·DMA 상태 복원과 scene 전환 뒤 자산 수명을 증명한다. 한 번 성공한 read를 장시간 소비 동작의 증거로 확대하지 않는다.

## 6. 빌드와 검증

다음 중 이번 변경이 닿은 경로만 검증한다.

- 실제 executable·module identity와 file↔RAM↔instruction-stream 관계
- 저장 font·texture→변환·VRAM→화면 소비와 cache 수명
- reader가 보는 text·archive field·pointer 경계
- 수정 sector별 form·EDC/ECC와 ISO·game LBA 좌표
- runtime CD ownership, streaming 경합과 상태 복원

특정 실기·광학 장치·image loader 지원을 주장하면 그 경로에서 최종 후보를 검증한다. 부팅 성공은 전체 sector·text·streaming 경로의 증거가 아니다.
