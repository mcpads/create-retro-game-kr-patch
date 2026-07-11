# PC Engine 국소 사례

여기의 관측은 PC Engine 전체의 규칙이 아니다. 발동 조건이 맞을 때 조사 후보로만 사용한다.

## PCE-001

- **관측 범위:** PC Engine 마도물어 1의 타일맵 재인코딩.
- **사고 맥락:** 로딩 화면 인코더가 타일 번호 기준을 0으로 가정했다. 원본 맵의 배경 BAT 엔트리는 `0x0100`을 기준으로 삼아, 이대로면 인게임에서 다른 VRAM 타일을 참조할 상태였다.
- **결정 실험:** 원본 surface를 디코드한 뒤 무수정 재인코드해 바이트를 비교했다. round-trip 차이가 load address 가정을 드러냈고 기준을 `0x100`으로 고치자 원본과 일치했다.
- **확정 결론:** 타일맵 인덱스의 기준은 인코더 기본값이 아니라 원본 맵과 실제 업로드 목적지에서 얻는다.
- **전이 한계:** 관측한 화면의 기준 타일을 다른 화면에 재사용하지 않는다.
- **관련 판단 기준:** `references/platforms/pce.md` §2, `references/strategy/graphics-text.md` §4.

## PCE-002

- **관측 범위:** PC Engine CD 이미지의 사용자 데이터 스트림과 raw 섹터 이미지.
- **사고 맥락:** 선행 패치의 그래픽 오프셋은 pregap 없는 2048바이트 user-data ISO 기준이었고, 빌드 대상은 pregap을 포함한 2352바이트 Mode 1 BIN이었다. 좌표계를 구분하지 않으면 버튼 그래픽이 아닌 다른 섹터를 고치게 된다.
- **결정 실험:** JP 원본 바이트열을 deinterleave된 user-data 스트림에서 유일 검색하고 CUE의 INDEX 차이에서 pregap을 계산했다. 두 좌표가 정확히 225 user-data 섹터만큼 차이남을 확인한 뒤 변경 섹터만 다시 썼다.
- **확정 결론:** 외부 오프셋은 어느 섹터 표현과 트랙 기준의 좌표인지 먼저 증명하고, 원본 바이트 앵커로 최종 위치를 교차 검증한다.
- **전이 한계:** 225섹터 보정값은 이 이미지의 트랙 배치에만 속하며 다른 디스크에 이식하지 않는다.
- **관련 판단 기준:** `references/platforms/pce.md` §4·§6, `references/strategy/build-and-verify.md` §2.

## PCE-003

- **관측 범위:** PC Engine CD 마도물어 1 텍스트 핸들러의 `LDA address; LDX immediate; JSR` 호출들과 printing task 진입점 `$6885`.
- **사고 맥락:** 여러 핸들러의 X 즉시값이 bank 번호처럼 보여 별도 sub-script를 고르는 값으로 해석했다. 그러나 HuC6280 논리 주소만 보면 실제 호출 대상과 현재 MPR mapping을 구분할 수 없었다.
- **검증 근거:** `$6885`에서 도달하는 126개 명령에 MPR 상태를 전파하자 printing task 안에는 MPR 변경이 없었고, 호출 대상은 현재 MPR2에 매핑된 System Card BIOS 영역이었다. 값은 호출 직후 덮어써져 이후 bank 선택으로 전파되지 않았고 BIOS 호출의 입력으로만 소비됐다.
- **확정 결과:** X 즉시값은 게임 데이터의 sub-bank ID가 아니라 BIOS task scheduler의 selector·slot 계열 인자였고, 호출 직후 덮어써져 이후 bank나 sub-script 선택으로 이어지지 않았다.
- **전이 한계:** 이 추적은 `$6885`에서 정적으로 도달한 126개 명령과 당시 mapping에 한정된다. 다른 진입점의 sub-script와 간접 경로까지 해명한 것이 아니며, 논리 주소나 즉시값 모양만으로 BIOS·bank 의미를 이식하지 않는다.
- **관련 판단 기준:** `references/strategy/initial-survey.md` §2.2·§3, `references/strategy/debugging.md` §2·§4, `references/platforms/pce.md` §1.
