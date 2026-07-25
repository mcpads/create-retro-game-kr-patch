# 검증된 국소 사례 색인

이 색인은 범위가 확인된 실패와 반례, 입증된 성공 기법, 운영 중 확인한 함정과 한 번의 검색으로 복원하기 어려운 조사 결과를 보존한다.

현재 판단 영역과 관측한 증상이 발동 조건과 맞는 항목만 선택한다. 사례의 관측 범위와 전이 한계로 새 대상에서 다시 확인할 경계를 정하고, 완료는 사례가 아니라 그 사례의 **관련 판단 기준**이 가리키는 문서로 판정한다.

판단 영역은 사례 본문의 관련 판단 기준이 가리키는 strategy 문서를 등장 순서대로 줄여 쓴 것이며, `SKILL.md` 라우팅 표의 판단 영역과 다음과 같이 대응한다. 시행 규약(`references/conventions/`)은 판단 영역에 넣지 않는다.

| 색인 라벨 | 라우팅 판단 영역 | 문서 |
|---|---|---|
| 초기 조사 | 초기 조사 | `references/strategy/initial-survey.md` |
| 폰트 | 폰트·인코딩 | `references/strategy/font-strategy.md` |
| 추출 | 텍스트 추출 | `references/strategy/text-extraction.md` |
| PoC | PoC | `references/strategy/poc.md` |
| 재삽입 | 재삽입·훅 | `references/strategy/reinsertion.md` |
| 번역 | 번역 | `references/strategy/translation-workflow.md` |
| 빌드 | 빌드·검증 | `references/strategy/build-and-verify.md` |
| 디버깅 | 디버깅·이슈 처리 | `references/strategy/debugging.md` |
| 그래픽 | 그래픽 텍스트 | `references/strategy/graphics-text.md` |
| 압축 | 압축 대응 | `references/strategy/compression.md` |
| 런타임 자산 | 런타임 자산 도달성 | `references/strategy/runtime-assets.md` |

| ID | 판단 영역 | 관측 플랫폼 | 발동 조건 | 사례 파일 |
|---|---|---|---|---|
| DC-001 | 추출 | Dreamcast | 포인터 간격으로 자른 항목이 다음 항목과 겹침 | `references/tips/dreamcast.md#dc-001` |
| DC-002 | 폰트·그래픽·런타임 자산 | Dreamcast·SNES·Game Gear·Saturn | 공유 글리프·타일 슬롯이 다른 라벨·비텍스트 그래픽에서도 소비됨 | `references/tips/dreamcast.md#dc-002` |
| DC-003 | 디버깅·추출 | Dreamcast | 사람이 붙인 라벨과 실제 표시 데이터가 불일치 | `references/tips/general.md#dc-003` |
| DC-004 | 재삽입·초기 조사 | Dreamcast·Saturn | 0 채움이나 정적 참조 부재로 고른 공간에서 부팅·진입 중 정지 | `references/tips/general.md#dc-004` |
| DC-005 | 추출·번역·빌드 | Dreamcast | 번역문이 짧아진 뒤 후반 음성이 점점 일찍 끊김 | `references/tips/dreamcast.md#dc-005` |
| DC-006 | 빌드 | Dreamcast | 생성된 리터럴 풀을 남아 있던 고정 주소 직접 쓰기가 덮음 | `references/tips/dreamcast.md#dc-006` |
| DC-007 | 재삽입·빌드 | Dreamcast | 큰 파일 간격을 빈 경계로 오인해 뒤 파일을 덮음 | `references/tips/dreamcast.md#dc-007` |
| DC-008 | 폰트·런타임 자산·PoC | Dreamcast | 파일명과 선행 PoC만으로 활성 대사 폰트를 잘못 선택 | `references/tips/dreamcast.md#dc-008` |
| SNES-001 | 재삽입·추출 | SNES | 2바이트 접두사 절단으로 종료자 소실 | `references/tips/snes.md#snes-001` |
| SNES-002 | 추출 | SNES | 항상 2바이트씩 읽는 텍스트 경로에 1바이트 토큰 삽입 | `references/tips/snes.md#snes-002` |
| SNES-003 | 폰트·런타임 자산 | SNES | 가로 인덱싱 ×2와 2×2 글리프 혼동 | `references/tips/snes.md#snes-003` |
| SNES-004 | 재삽입·디버깅 | SNES | 조건 문구 타일 덮기가 재진입·인접 화면에도 잘못 실행 | `references/tips/snes.md#snes-004` |
| SNES-006 | 런타임 자산·재삽입 | SNES·PC Engine CD | 후속 원본 쓰기가 한국어 로고·자막을 다시 덮음 | `references/tips/general.md#snes-006` |
| SNES-008 | 디버깅 | SNES | 원인 후보 훅을 빼도 증상 유지 | `references/tips/general.md#snes-008` |
| SNES-009 | 빌드 | SNES | 특정 분기에서만 시작 즉시 깨짐 | `references/tips/snes.md#snes-009` |
| SNES-010 | 추출 | SNES | 제어코드 첫 바이트를 종료자로 오인 | `references/tips/snes.md#snes-010` |
| SNES-011 | 압축·런타임 자산·재삽입 | SNES | 압축 UI 일부를 바꿔야 하지만 재압축 형식이나 새 전송 경로가 없음 | `references/tips/snes.md#snes-011` |
| SNES-012 | 런타임 자산·그래픽·재삽입 | SNES | WRAM 수정이 1회 적재된 OBJ VRAM에 도달하지 않음 | `references/tips/snes.md#snes-012` |
| SNES-013 | 그래픽·런타임 자산·빌드 | SNES | 한 라벨의 글자·배경·표현 층이 여러 타일 경계를 가로지름 | `references/tips/snes.md#snes-013` |
| SNES-014 | 재삽입 | SNES | 같은 뱅크 전용 참조와 뱅크 간 참조가 같은 공간을 두고 경쟁 | `references/tips/snes.md#snes-014` |
| SNES-015 | 폰트 | SNES | 폰트 파싱은 성공했지만 실제 글리프 출력이 비어 있음 | `references/tips/general.md#snes-015` |
| SNES-016 | 압축·초기 조사·런타임 자산 | SNES | 실행 중 글리프는 알지만 저장된 압축 원본 위치를 찾지 못함 | `references/tips/snes.md#snes-016` |
| SNES-017 | 재삽입·런타임 자산 | SNES·NES | 보이는 공간을 썼지만 게임이 지우지 않아 다음 화면에 타일이 남음 | `references/tips/snes.md#snes-017` |
| SNES-018 | 그래픽·런타임 자산·재삽입 | SNES | 정적 번역 타일맵이 게임의 동적 셀을 마지막에 덮음 | `references/tips/snes.md#snes-018` |
| SNES-019 | PoC·런타임 자산·폰트 | SNES | 저장·VRAM 바이트는 맞지만 목표 글자가 아닌 타일을 교체 | `references/tips/snes.md#snes-019` |
| SNES-021 | 번역·재삽입·빌드 | SNES | 일본어 고정 크기의 창에서 한국어 대사가 잘리거나 화면 밖으로 넘침 | `references/tips/snes.md#snes-021` |
| SNES-022 | 그래픽·런타임 자산·재삽입 | SNES | 정적 분석에서 선택 강조 데이터와 읽기 범위가 원문 길이에 묶임 | `references/tips/snes.md#snes-022` |
| SNES-024 | 추출·재삽입·런타임 자산 | SNES | 두 번째 포인터를 바꿨지만 전환 뒤 첫 블록 다음 주소부터 계속 읽음 | `references/tips/snes.md#snes-024` |
| SATURN-003 | 압축·디버깅 | Saturn | 무변경 원본 재압축도 게임에서 손상 | `references/tips/general.md#saturn-003` |
| SATURN-004 | 추출·재삽입 | Saturn·SNES·PC-98 | 바이트 모양만으로 참조를 포함·제외해 거짓 참조나 실제 포인터 누락이 생김 | `references/tips/saturn.md#saturn-004` |
| SATURN-005 | 그래픽·런타임 자산 | Saturn | 주 폰트를 바꿔도 메뉴 라벨이 남고 메뉴를 열 때 새 VRAM 쓰기가 없음 | `references/tips/general.md#saturn-005` |
| SATURN-007 | 폰트·번역 | Saturn | 글리프 부족으로 번역 표현을 임시 축약 | `references/tips/general.md#saturn-007` |
| SATURN-008 | 그래픽·초기 조사·런타임 자산 | Saturn·PlayStation | 저장 길이나 보이는 픽셀만으로는 비트 깊이·시작점·폭·높이·구간 경계 후보가 여러 개임 | `references/tips/saturn.md#saturn-008` |
| SATURN-009 | 그래픽 | Saturn | 같은 배경의 여러 라벨에서 원문 없는 배경이 필요함 | `references/tips/saturn.md#saturn-009` |
| SATURN-010 | 재삽입 | Saturn | 최종 파일은 정렬됐지만 중간 구조에서 멈춤 | `references/tips/saturn.md#saturn-010` |
| SATURN-012 | 추출·재삽입 | Saturn | 한 번역 항목 안의 하위 문자열을 포인터가 직접 참조 | `references/tips/saturn.md#saturn-012` |
| SATURN-013 | 추출·재삽입 | Saturn·PlayStation | 고정 슬롯을 패딩·절단한 뒤 정지·빈 페이지·연결 공백·오류 글리프가 생김 | `references/tips/saturn.md#saturn-013` |
| SATURN-016 | 추출·폰트·디버깅 | Saturn | 초반 글리프 대응은 맞지만 뒤쪽 메시지부터 다른 글자로 해석 | `references/tips/saturn.md#saturn-016` |
| SATURN-017 | 폰트·런타임 자산 | Saturn | 대체 폰트를 바꿨지만 캐릭터 선택 뒤 실제 화면에는 반영되지 않음 | `references/tips/saturn.md#saturn-017` |
| SATURN-018 | 압축·재삽입·런타임 자산 | Saturn | 파일 크기는 늘었지만 고정 해제 크기 때문에 끝부분이 적재되지 않음 | `references/tips/saturn.md#saturn-018` |
| SATURN-019 | 재삽입·런타임 자산·빌드 | Saturn | 문자열이 고정 슬롯을 넘는데 주소형 값 전체를 포인터로 옮긴 빌드는 멈춤 | `references/tips/saturn.md#saturn-019` |
| SATURN-020 | 디버깅·압축·런타임 자산 | Saturn | 추가 문자열 주소의 읽기를 실제 텍스트 소비로 오인 | `references/tips/saturn.md#saturn-020` |
| PS1-001 | 재삽입·런타임 자산·디버깅 | PlayStation | RAM 재적재 뒤 캐시 두 줄의 원본·패치 명령이 섞임 | `references/tips/ps1.md#ps1-001` |
| PS1-002 | 추출·재삽입 | PlayStation | 중복 문자열 통합 뒤 다른 포인터 슬롯이 번역되거나 내부 진입 화면에 원문 뒷부분이 남음 | `references/tips/ps1.md#ps1-002` |
| PS1-003 | 그래픽·폰트·빌드 | PlayStation | 실제 선택 배경에서 소형 라벨의 본문·외곽선 구분이 필요 | `references/tips/ps1.md#ps1-003` |
| PS1-005 | 폰트·재삽입·런타임 자산 | PlayStation | 한글은 표시되지만 첫 폰트 CD 적재 때 배경 음악이 중단됨 | `references/tips/ps1.md#ps1-005` |
| NDS-001 | 폰트·런타임 자산 | Nintendo DS | 이름 입력 후보만 바뀌고 선택 후 재표시는 그대로임 | `references/tips/nds.md#nds-001` |
| NDS-002 | 폰트·디버깅 | Nintendo DS | 폰트 항목을 하나 늘리자 타이틀 전 흰 화면에서 멈춤 | `references/tips/nds.md#nds-002` |
| NDS-003 | 폰트 | Nintendo DS | 문서의 NFTR 청크명으로 raw byte를 검색하면 실패하고 기존 CMAP은 새 매핑 범위를 이미 덮음 | `references/tips/nds.md#nds-003` |
| NES-001 | 초기 조사·빌드·디버깅 | NES | 선행 패치의 PRG-RAM 사용과 이미지 헤더 선언이 불일치 | `references/tips/general.md#nes-001` |
| PCE-001 | 그래픽 | PC Engine CD·SNES | 논리 타일 번호를 물리 타일 좌표로 사용해 화면이 밀리거나 배경이 손상 | `references/tips/pce.md#pce-001` |
| PCE-002 | 빌드 | PC Engine CD | 사용자 데이터 오프셋으로 원시 섹터 이미지를 패치 | `references/tips/pce.md#pce-002` |
| PCE-003 | 초기 조사·디버깅 | PC Engine CD | 핸들러의 즉시값을 하위 뱅크 식별자로 해석 | `references/tips/pce.md#pce-003` |
| PCE-004 | 폰트·재삽입·런타임 자산 | PC Engine CD·PlayStation | 별도 표시 루틴이 필요해 보이나 기존 글리프 변환·업로드 경로가 존재 | `references/tips/pce.md#pce-004` |
| PC98-001 | 폰트 | PC-98 | 표준 디코더 통계로 미사용 선행 바이트 선정 | `references/tips/pc98.md#pc98-001` |
| PC98-002 | 폰트·빌드 | PC-98 | 생성기와 검증기가 같은 경계식을 공유 | `references/tips/pc98.md#pc98-002` |
| PC98-003 | 재삽입·빌드 | PC-98 | 개별 NUL 간격으로는 긴 크레딧 문자열을 수용할 수 없음 | `references/tips/pc98.md#pc98-003` |
| PC98-004 | 재삽입·빌드 | PC-98 | 여러 구간을 늘리자 뒤 포인터 위치와 가리키는 주소의 이동이 누락·중복 | `references/tips/pc98.md#pc98-004` |
| GG-001 | 디버깅 | Game Gear | 상점 가격과 후속 대사가 함께 어긋남 | `references/tips/gg.md#gg-001` |
| GG-002 | 런타임 자산·디버깅 | Game Gear | 이전 VRAM이 남은 저장 상태 때문에 실제 폰트 원본 위치를 기각 | `references/tips/general.md#gg-002` |
| GG-003 | 번역 | Game Gear | 디코더 수정 뒤에도 구 원문 기반 번역이 잔존 | `references/tips/general.md#gg-003` |
| GG-005 | 재삽입 | Game Gear | 한 뱅크의 여러 포인터 테이블이 문자열 뒷부분을 공유 | `references/tips/gg.md#gg-005` |
| GG-006 | 추출·번역 | Game Gear | 번역에서 인물 초상 제어가 페이지별로 누락 | `references/tips/gg.md#gg-006` |
| GG-007 | 번역·추출 | Game Gear·NES | 원본 토큰을 보존했지만 대상 엔진에서 다른 의미로 소비 | `references/tips/gg.md#gg-007` |
| GG-008 | 재삽입·런타임 자산 | Game Gear | 길이 0인 항목이 실행 중 만들어지는 문자열의 포인터였음 | `references/tips/gg.md#gg-008` |
| GG-009 | 재삽입·디버깅 | Game Gear | 공유 글리프 훅이 한 호출자의 문자 카운터를 덮음 | `references/tips/gg.md#gg-009` |
| GG-010 | 추출·번역·빌드 | Game Gear | 넓은 창 기준 검사로 같은 스크립트 영역의 좁은 창 넘침을 놓침 | `references/tips/gg.md#gg-010` |
| GG-011 | 디버깅·재삽입·런타임 자산 | Game Gear | 정렬 변경 뒤 한 호출자에서만 이전 타일이 남음 | `references/tips/gg.md#gg-011` |
| MD-001 | 빌드·추출 | Mega Drive | 번역 뒤 특정 대사에서 진행 정지 | `references/tips/megadrive.md#md-001` |
| MD-002 | 번역 | Mega Drive | 초기 한국어 번역이 화자 제어 순서를 무시 | `references/tips/general.md#md-002` |
| MD-003 | 폰트·런타임 자산·디버깅 | Mega Drive | 글리프마다 비슷한 데이터 블록 네 개가 반복됨 | `references/tips/megadrive.md#md-003` |
