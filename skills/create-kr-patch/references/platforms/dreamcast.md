# Sega Dreamcast

SH-4·GD-ROM·texture의 기본 사양은 필요할 때 1차 자료에서 확인한다. 패치 판단에서는 디스크 표현과 실행 표현, track 좌표, 저장 texture와 renderer 소비를 서로 구분한다.

## 1. 저장 실행 파일과 런타임 코드

runtime 주소를 파일 offset으로 바꾸려면 대상 executable·module의 실제 load address, file layout, relocation·decompression을 함께 확인한다. 관습적인 load address나 상위 주소 bit 처리법을 모든 타이틀에 적용하지 않는다.

boot 경로가 실행 binary를 scrambling·packing하면 disk bytes와 runtime instruction bytes는 다른 표현이다. 수정 경계를 고르기 전에 실제 boot transform의 무변경 왕복과 module identity를 검증한다.

코드를 이동하면 현재 SH-4 사양에서 branch delay와 PC-relative literal 의미를 확인하고, 최종 배치 뒤 원본 효과·target·literal을 재검산한다. 공통 기계어 검산 규칙은 `references/conventions/project-conventions.md` §2.4가 소유한다.

## 2. GDI track 좌표

GDI descriptor의 track LBA, track 내부 sector index, backing-file byte offset과 filesystem LBA는 서로 다른 좌표다. sector 표현이 다른 track 사이에서 한 좌표의 산술을 다른 좌표로 이식하지 않는다.

descriptor와 backing file의 실제 sector 구조·크기·순서를 함께 검증하고, data·audio, session·pregap을 보존한다. ISO 파일을 옮길 때도 directory extent 외에 게임 자체 LBA·size table과 streaming 소비자를 확인한다.

CDI 등 다른 container로 변환한 결과가 원본 GDI track 구조를 보존한다고 가정하지 않는다. 변환본은 기준 GDI 산출물과 분리하고 boot·audio·streaming·file content를 다시 검증한다.

## 3. Texture와 글리프 소비

magic·확장자나 decoded image만으로 texture encoder를 승인하지 않는다. target descriptor와 upload path가 읽는 pixel·layout·palette·size 규칙을 확정하고, 정규 표현이 하나가 아니면 decoded pixels와 보호 metadata·consumer 의미의 동등 기준을 둔다.

같은 라벨도 상태·화면·2D/3D renderer가 다른 texture나 slot을 쓸 수 있다. 한 atlas의 성공을 전체 폰트·UI로 확대하지 않으며, 자산을 추가·성장·이동하면 `references/strategy/runtime-assets.md`를 적용한다.

## 4. 텍스트와 참조

인코딩, script VM과 pointer 표현은 실제 reader가 소유한다. CPU endian은 container·VM field의 저장 순서를 대신 정하지 않는다. 엔트리 경계와 pointer ownership은 `references/strategy/text-extraction.md` 및 `references/strategy/reinsertion.md`가 판정한다.

## 5. 재빌드와 검증

다음 중 이번 변경이 닿은 경로만 검증한다.

- disk representation↔runtime module 변환과 실제 code identity
- GDI descriptor↔track↔filesystem↔game LBA 좌표
- texture 저장 표현↔descriptor↔upload↔renderer 소비
- module·scene 전환 뒤 reload·cache 수명
- 변환 배포본의 boot·audio·streaming과 비대상 track 보존

한 container의 부팅이나 한 상태의 texture 표시를 다른 loader·상태 수명의 증거로 쓰지 않는다.
