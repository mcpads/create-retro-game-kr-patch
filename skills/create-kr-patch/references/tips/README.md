# 국소 사례 단서 색인

이 사례들은 특정 타이틀에서 실제로 겪은 실패를 보존한 비규범적 단서다. 현재 게임의 판단 기준과 완료 조건은 `references/strategy/`에서 확인한다.

프로젝트 착수 때 전부 읽지 않는다. strategy와 필요한 경우 해당 플랫폼 문서로 현재 판단 영역과 위험 신호를 식별한 뒤, 아래 색인에서 **판단 영역·발동 조건이 맞는 행의 앵커 하나만** 읽는다. 관측 플랫폼과 범위는 증거의 출처와 전이 한계다. 같은 플랫폼이라고 자동 선택하지 않고, 다른 플랫폼이라고 자동 제외하지 않는다. 사례는 조사 후보를 제안할 뿐, 대상 게임의 구조나 원인을 증명하지 않는다.

| ID | 판단 영역 | 관측 플랫폼 | 발동 조건 | 사례 파일 |
|---|---|---|---|---|
| DC-001 | 추출·재배치 | Dreamcast | 포인터 간격 추출, 중첩 엔트리 | `references/tips/dreamcast.md#dc-001` |
| DC-002 | 폰트·그래픽 | Dreamcast | 공유 폰트 슬롯 때문에 라벨끼리 충돌 | `references/tips/dreamcast.md#dc-002` |
| DC-003 | 추출·디버깅 | Dreamcast | 사람이 붙인 라벨과 소비 바이트 불일치 | `references/tips/general.md#dc-003` |
| DC-004 | 재삽입·공간 | Dreamcast | 0 padding을 live code가 아닌 것으로 오인 | `references/tips/general.md#dc-004` |
| SNES-001 | 추출 | SNES | 2바이트 접두사 절단으로 종료자 소실 | `references/tips/snes.md#snes-001` |
| SNES-002 | 추출 | SNES | 고정 워드 폭 소비자에 1바이트 토큰 삽입 | `references/tips/snes.md#snes-002` |
| SNES-003 | 폰트·렌더 | SNES | 가로 인덱싱 ×2와 2×2 글리프 혼동 | `references/tips/snes.md#snes-003` |
| SNES-004 | 런타임 자산 | SNES | 퍼즐 조건 화면의 task→NMI 상태 전달이 불안정 | `references/tips/snes.md#snes-004` |
| SNES-006 | 런타임 자산 | SNES | 후속 청크가 로고 일부를 다시 덮음 | `references/tips/general.md#snes-006` |
| SNES-008 | 디버깅 | SNES | 원인 후보 훅을 빼도 증상 유지 | `references/tips/general.md#snes-008` |
| SNES-009 | 빌드·회귀 | SNES | 특정 분기에서만 시작 즉시 깨짐 | `references/tips/snes.md#snes-009` |
| SNES-010 | 추출 | SNES | 제어코드 첫 바이트를 종료자로 오인 | `references/tips/snes.md#snes-010` |
| SATURN-002 | 재삽입·공간 | Saturn | 정적 참조 0건을 미사용 code로 오인 | `references/tips/general.md#saturn-002` |
| SATURN-003 | 압축 | Saturn | 무변경 원본 재압축도 게임에서 손상 | `references/tips/general.md#saturn-003` |
| SATURN-004 | 추출·재삽입 | Saturn | opcode 인자를 포인터 prefix로 오인 | `references/tips/saturn.md#saturn-004` |
| SATURN-005 | 그래픽·런타임 | Saturn | 메뉴 표시보다 앞서 적재된 스프라이트 | `references/tips/general.md#saturn-005` |
| SATURN-007 | 폰트·번역 | Saturn | 글리프 부족으로 번역 표현을 임시 축약 | `references/tips/general.md#saturn-007` |
| PCE-001 | 그래픽 | PC Engine | 타일맵이 한 타일셋만큼 밀림 | `references/tips/pce.md#pce-001` |
| PCE-002 | 매체 재빌드 | PC Engine CD | 사용자 데이터 오프셋으로 raw 이미지를 패치 | `references/tips/pce.md#pce-002` |
| PC98-001 | 폰트·인코딩 | PC-98 | 표준 디코더 통계로 미사용 lead 선정 | `references/tips/pc98.md#pc98-001` |
| GG-001 | 디버깅·렌더 | Game Gear | 상점 가격과 후속 대사가 함께 어긋남 | `references/tips/gg.md#gg-001` |
| GG-002 | 런타임 자산 | Game Gear | stale VRAM save state로 font source를 기각 | `references/tips/general.md#gg-002` |
| GG-003 | 번역 기준선 | Game Gear | decoder 수정 뒤에도 구 원문 기반 번역이 잔존 | `references/tips/general.md#gg-003` |
| MD-001 | 재삽입·빌드 | Mega Drive | 번역 뒤 특정 대사에서 진행 정지 | `references/tips/megadrive.md#md-001` |
| MD-002 | 번역 맥락 | Mega Drive | 초기 KR 번역이 화자 제어 순서를 무시 | `references/tips/general.md#md-002` |
