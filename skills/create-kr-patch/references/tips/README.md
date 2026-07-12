# 검증된 국소 사례 색인

이 사례들은 범위가 확인된 실패·반례, 입증된 성공 기법, 운영 함정과 어려운 교차 조사 결과를 보존한다. 모두 비규범적이며, 현재 게임의 판단 기준과 완료 조건은 `references/strategy/`에서 확인한다.

프로젝트 착수 때 전부 읽지 않는다. strategy와 필요한 경우 플랫폼 문서에서 판단 영역과 위험 신호를 확인한 뒤, 발동 조건에 가장 가까운 앵커만 읽는다. 독립된 조건마다 하나씩 고르며, 관측 플랫폼은 증거 범위이지 선택 필수조건이 아니다. 사례는 조사 후보일 뿐 현재 게임의 원인·해법·완료를 증명하지 않는다.

| ID | 판단 영역 | 관측 플랫폼 | 발동 조건 | 사례 파일 |
|---|---|---|---|---|
| DC-001 | 추출·재배치 | Dreamcast | 포인터 간격 추출, 중첩 엔트리 | `references/tips/dreamcast.md#dc-001` |
| DC-002 | 폰트·그래픽 | Dreamcast | 공유 폰트 슬롯 때문에 라벨끼리 충돌 | `references/tips/dreamcast.md#dc-002` |
| DC-003 | 추출·디버깅 | Dreamcast | 사람이 붙인 라벨과 소비 바이트 불일치 | `references/tips/general.md#dc-003` |
| DC-004 | 재삽입·공간 | Dreamcast | 0 padding을 live code가 아닌 것으로 오인 | `references/tips/general.md#dc-004` |
| DC-005 | 번역·타이밍 | Dreamcast | 번역문이 짧아지자 다음 음성이 일찍 시작 | `references/tips/dreamcast.md#dc-005` |
| DC-006 | 빌드·쓰기 | Dreamcast | 생성된 리터럴 풀을 과거 고정 주소 쓰기가 덮음 | `references/tips/dreamcast.md#dc-006` |
| DC-007 | 매체 재빌드 | Dreamcast | 큰 파일 간격을 빈 경계로 오인해 뒤 파일을 덮음 | `references/tips/dreamcast.md#dc-007` |
| DC-008 | 폰트·런타임 | Dreamcast | 파일명과 선행 PoC만으로 활성 대사 폰트를 잘못 선택 | `references/tips/dreamcast.md#dc-008` |
| SNES-001 | 추출 | SNES | 2바이트 접두사 절단으로 종료자 소실 | `references/tips/snes.md#snes-001` |
| SNES-002 | 추출 | SNES | 고정 워드 폭 소비자에 1바이트 토큰 삽입 | `references/tips/snes.md#snes-002` |
| SNES-003 | 폰트·렌더 | SNES | 가로 인덱싱 ×2와 2×2 글리프 혼동 | `references/tips/snes.md#snes-003` |
| SNES-004 | 런타임 자산 | SNES | 퍼즐 조건 화면의 task→NMI 상태 전달이 불안정 | `references/tips/snes.md#snes-004` |
| SNES-006 | 런타임 자산 | SNES | 후속 청크가 로고 일부를 다시 덮음 | `references/tips/general.md#snes-006` |
| SNES-008 | 디버깅 | SNES | 원인 후보 훅을 빼도 증상 유지 | `references/tips/general.md#snes-008` |
| SNES-009 | 빌드·회귀 | SNES | 특정 분기에서만 시작 즉시 깨짐 | `references/tips/snes.md#snes-009` |
| SNES-010 | 추출 | SNES | 제어코드 첫 바이트를 종료자로 오인 | `references/tips/snes.md#snes-010` |
| SNES-011 | 압축·런타임 | SNES | 안정된 해제 경계와 기존 소비 경로를 재사용할 수 있음 | `references/tips/snes.md#snes-011` |
| SNES-012 | 그래픽·런타임 | SNES | WRAM 수정이 1회 적재된 OBJ VRAM에 도달하지 않음 | `references/tips/snes.md#snes-012` |
| SNES-013 | 그래픽·시각 표현 | SNES | 한 라벨의 글자·배경·표현 층이 여러 타일 경계를 가로지름 | `references/tips/snes.md#snes-013` |
| SNES-014 | 재삽입·공간 | SNES | 같은-bank 참조와 cross-bank 참조가 공간을 경쟁 | `references/tips/snes.md#snes-014` |
| SNES-015 | 폰트·도구 | SNES | 파싱된 bitmap-embedded TTF가 0×0 글리프를 반환 | `references/tips/general.md#snes-015` |
| SNES-016 | 압축·초기 조사 | SNES | 런타임 글리프는 알지만 저장 압축 원천을 찾지 못함 | `references/tips/snes.md#snes-016` |
| SNES-017 | 렌더·클리어 | SNES | 문자열 패딩을 없애자 이전 행의 VRAM 타일이 남음 | `references/tips/snes.md#snes-017` |
| SNES-018 | 그래픽·공유 상태 | SNES | 정적 번역 타일맵이 게임의 동적 셀을 마지막에 덮음 | `references/tips/snes.md#snes-018` |
| SNES-019 | PoC·런타임 자산 | SNES | 저장·VRAM 바이트는 맞지만 목표 글자가 아닌 타일을 교체 | `references/tips/snes.md#snes-019` |
| SNES-021 | 레이아웃·창 | SNES | 한국어 대사의 가시 폭·행 수에 따라 창 크기가 달라짐 | `references/tips/snes.md#snes-021` |
| SNES-022 | UI·상태 | SNES | 길어진 선택지 뒤쪽에 포커스 강조가 적용되지 않음 | `references/tips/snes.md#snes-022` |
| SATURN-002 | 재삽입·공간 | Saturn | 정적 참조 0건을 미사용 code로 오인 | `references/tips/general.md#saturn-002` |
| SATURN-003 | 압축 | Saturn | 무변경 원본 재압축도 게임에서 손상 | `references/tips/general.md#saturn-003` |
| SATURN-004 | 추출·재삽입 | Saturn | opcode 인자를 포인터 prefix로 오인 | `references/tips/saturn.md#saturn-004` |
| SATURN-005 | 그래픽·런타임 | Saturn | 메뉴 표시보다 앞서 적재된 스프라이트 | `references/tips/general.md#saturn-005` |
| SATURN-007 | 폰트·번역 | Saturn | 글리프 부족으로 번역 표현을 임시 축약 | `references/tips/general.md#saturn-007` |
| SATURN-008 | 그래픽·포맷 | Saturn | bpp를 확정해도 구간별 시작 오프셋·폭·행 간격이 달라짐 | `references/tips/saturn.md#saturn-008` |
| SATURN-009 | 그래픽·복원 | Saturn | 같은 배경의 여러 라벨에서 원문 없는 배경이 필요함 | `references/tips/saturn.md#saturn-009` |
| SATURN-010 | 재삽입·정렬 | Saturn | 최종 파일은 정렬됐지만 중간 구조에서 멈춤 | `references/tips/saturn.md#saturn-010` |
| SATURN-011 | 재삽입·제어 | Saturn | 길이 패딩 뒤 이벤트가 하드락 | `references/tips/saturn.md#saturn-011` |
| SATURN-012 | 재삽입·포인터 | Saturn | 한 번역 엔트리 안의 하위 문자열을 포인터가 직접 참조 | `references/tips/saturn.md#saturn-012` |
| SATURN-013 | 재삽입·경계 | Saturn | 같은 고정 슬롯 파일에서 패딩이 일부 문자열 연결을 깨뜨림 | `references/tips/saturn.md#saturn-013` |
| SATURN-014 | 그래픽·포맷 | Saturn | 헤더 없는 시트의 파일 중간에서 합성 영역을 분리해야 함 | `references/tips/saturn.md#saturn-014` |
| SATURN-015 | 폰트·공유 자산 | Saturn | 반복·빈 타일처럼 보이는 폰트 영역을 회수하려면 비텍스트 참조도 바꿔야 함 | `references/tips/saturn.md#saturn-015` |
| SATURN-016 | 추출·폰트 | Saturn | 메시지 내장 글리프 풀을 전역 첫 등장 순서로 해석 | `references/tips/saturn.md#saturn-016` |
| SATURN-017 | 폰트·런타임 | Saturn | 상태별 폰트 분할로 활성 글리프 공급을 늘리려 함 | `references/tips/saturn.md#saturn-017` |
| PS1-001 | 훅·런타임 | PlayStation | RAM 재적재 뒤 캐시 두 줄의 원본·패치 명령이 섞임 | `references/tips/ps1.md#ps1-001` |
| PS1-002 | 재삽입·포인터 | PlayStation | 중복 문자열 통합 뒤 내부 포인터가 원문 tail을 가리킴 | `references/tips/ps1.md#ps1-002` |
| PS1-003 | 그래픽·UI | PlayStation | 소형 라벨이 실제 선택 배경에서 대비를 유지해야 함 | `references/tips/ps1.md#ps1-003` |
| PS1-004 | 그래픽·포맷 | PlayStation | 같은 파일 크기에 맞는 bpp·폭·높이 후보가 여러 개임 | `references/tips/ps1.md#ps1-004` |
| PS1-005 | 폰트·런타임 | PlayStation | 기존 글리프 소비 경로 재사용은 성공했지만 첫 자산 적재가 음악을 중단 | `references/tips/ps1.md#ps1-005` |
| PS1-006 | 재삽입·제어 | PlayStation | 고정 2바이트 소비자에서 0x0000 패딩이 오류 글리프로 표시 | `references/tips/ps1.md#ps1-006` |
| NDS-001 | 폰트·그래픽·런타임 | Nintendo DS | 이름 입력 후보만 바뀌고 선택 후 재표시는 그대로임 | `references/tips/nds.md#nds-001` |
| NDS-002 | 폰트·디버깅 | Nintendo DS | 폰트 확장 뒤 내부 파일 크기와 엔트리 경계가 함께 변하며 부팅 실패 | `references/tips/nds.md#nds-002` |
| PCE-001 | 그래픽 | PC Engine | 타일맵이 한 타일셋만큼 밀림 | `references/tips/pce.md#pce-001` |
| PCE-002 | 매체 재빌드 | PC Engine CD | 사용자 데이터 오프셋으로 raw 이미지를 패치 | `references/tips/pce.md#pce-002` |
| PCE-003 | 초기 조사·코드 | PC Engine | 핸들러의 즉시값을 sub-bank ID로 해석 | `references/tips/pce.md#pce-003` |
| PCE-004 | 폰트·런타임 | PC Engine CD | 글리프 공급 경계만 바꿔 기존 변환·업로드를 재사용할 수 있음 | `references/tips/pce.md#pce-004` |
| PC98-001 | 폰트·인코딩 | PC-98 | 표준 디코더 통계로 미사용 lead 선정 | `references/tips/pc98.md#pc98-001` |
| PC98-002 | 인코딩·검증 | PC-98 | 생성기와 검증기가 같은 경계식을 공유 | `references/tips/pc98.md#pc98-002` |
| PC98-003 | 재삽입·포인터 | PC-98 | 개별 NUL 간격으로는 긴 크레딧 문자열을 수용할 수 없음 | `references/tips/pc98.md#pc98-003` |
| PC98-004 | 재삽입·포인터 | PC-98 | 여러 성장점의 저장 위치와 타깃 이동량이 누적 | `references/tips/pc98.md#pc98-004` |
| PC98-005 | 추출·포인터 | PC-98 | Shift_JIS trail byte를 포인터 적재 opcode로 오인 | `references/tips/pc98.md#pc98-005` |
| GG-001 | 디버깅·렌더 | Game Gear | 상점 가격과 후속 대사가 함께 어긋남 | `references/tips/gg.md#gg-001` |
| GG-002 | 런타임 자산 | Game Gear | stale VRAM save state로 font source를 기각 | `references/tips/general.md#gg-002` |
| GG-003 | 번역 기준선 | Game Gear | decoder 수정 뒤에도 구 원문 기반 번역이 잔존 | `references/tips/general.md#gg-003` |
| GG-004 | 그래픽·공유 자산 | Game Gear | 서로 다른 라벨이 일부 물리 타일을 공유 | `references/tips/gg.md#gg-004` |
| GG-005 | 재삽입·공간 | Game Gear | 한 bank의 여러 포인터 테이블이 suffix 공유 후보를 가짐 | `references/tips/gg.md#gg-005` |
| GG-006 | 번역·제어 | Game Gear | 번역에서 포트레이트 제어가 페이지별로 누락 | `references/tips/gg.md#gg-006` |
| GG-007 | 번역·제어 | Game Gear | 원본 토큰을 보존했지만 대상 엔진에서 다른 문자열로 치환 | `references/tips/gg.md#gg-007` |
| GG-008 | 재삽입·런타임 | Game Gear | 길이 0 엔트리가 런타임 문자열 포인터였음 | `references/tips/gg.md#gg-008` |
| GG-009 | 훅·상태 | Game Gear | 공유 글리프 훅이 한 호출자의 문자 카운터를 덮음 | `references/tips/gg.md#gg-009` |
| GG-010 | 레이아웃·진행 | Game Gear | 박스 태그별 제약에서 재줄바꿈·페이지 분할을 구분해야 함 | `references/tips/gg.md#gg-010` |
| GG-011 | 렌더·클리어 | Game Gear | 정렬 변경 뒤 한 호출자에서만 이전 타일이 남음 | `references/tips/gg.md#gg-011` |
| MD-001 | 재삽입·빌드 | Mega Drive | 번역 뒤 특정 대사에서 진행 정지 | `references/tips/megadrive.md#md-001` |
| MD-002 | 번역 맥락 | Mega Drive | 초기 KR 번역이 화자 제어 순서를 무시 | `references/tips/general.md#md-002` |
| MD-003 | 폰트·렌더 | Mega Drive | 반복 데이터처럼 보이는 사전 시프트 글리프 복사본 | `references/tips/megadrive.md#md-003` |
