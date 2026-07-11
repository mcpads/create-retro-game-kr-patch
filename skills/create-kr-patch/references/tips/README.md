# 국소 사례 단서 색인

이 디렉터리는 특정 타이틀에서 실제로 겪은 실패를 보존하는 **비규범적 단서집**이다. 판단 기준과 완료 조건은 `references/strategy/`가 소유하며, strategy 문서는 이 사례들을 읽지 않아도 완결되어야 한다.

프로젝트 착수 때 전부 읽지 않는다. strategy와 해당 플랫폼 문서로 위험 신호를 식별한 뒤, 아래 색인에서 **현재 플랫폼 또는 발동 조건이 맞는 행만** 골라 해당 플랫폼 파일을 읽는다. 다른 플랫폼의 사례를 가져올 때도 같은 증상이 아니라 같은 발동 조건이 확인되어야 한다. 사례는 조사 후보를 제안할 뿐, 대상 게임의 구조나 원인을 증명하지 않는다.

tip에 들어갈 수 있는 것은 관측 플랫폼·범위, 당시 자산·경로의 맥락, 구체 증상, 틀렸던 가정, 원인을 가른 실험, 확정된 수정 또는 기각 결론이 복원된 사례뿐이다. 어느 하나가 빠져 일반적인 명령문만 남으면 tip이 아니다. 출처 범위를 복원할 수 없는 조언, 공개 검색으로 재구성 가능한 배경지식, strategy의 판정 기준을 되풀이한 문장은 두지 않는다.

중간 조사·archive·journal은 당시의 가설을 복원하는 증거이지 현재 결론을 대신하지 않는다. 사례를 추가하거나 고칠 때는 현 코드와 후속 상태 문서·커밋까지 확인해 가설이 뒤집히거나 해결되지 않았는지 대조한다. 최종 판정을 복원하지 못하면 미해결 가설을 성공 사례로 승격하지 말고 해당 항목을 두지 않는다.

| ID | 관측 플랫폼 | 발동 조건 | 사례 파일 |
|---|---|---|---|
| DC-001 | Dreamcast | 포인터 간격 추출, 중첩 엔트리 | `references/tips/dreamcast.md#dc-001` |
| DC-002 | Dreamcast | 공유 폰트 슬롯 때문에 라벨끼리 충돌 | `references/tips/dreamcast.md#dc-002` |
| DC-003 | Dreamcast | 사람이 붙인 라벨과 소비 바이트 불일치 | `references/tips/dreamcast.md#dc-003` |
| DC-004 | Dreamcast | 0 padding을 live code가 아닌 것으로 오인 | `references/tips/dreamcast.md#dc-004` |
| SNES-001 | SNES | 2바이트 접두사 절단으로 종료자 소실 | `references/tips/snes.md#snes-001` |
| SNES-002 | SNES | 고정 워드 폭 소비자에 1바이트 토큰 삽입 | `references/tips/snes.md#snes-002` |
| SNES-003 | SNES | 가로 인덱싱 ×2와 2×2 글리프 혼동 | `references/tips/snes.md#snes-003` |
| SNES-004 | SNES | 퍼즐 조건 화면의 task→NMI 상태 전달이 불안정 | `references/tips/snes.md#snes-004` |
| SNES-006 | SNES | 후속 청크가 로고 일부를 다시 덮음 | `references/tips/snes.md#snes-006` |
| SNES-008 | SNES | 원인 후보 훅을 빼도 증상 유지 | `references/tips/snes.md#snes-008` |
| SNES-009 | SNES | 특정 분기에서만 시작 즉시 깨짐 | `references/tips/snes.md#snes-009` |
| SNES-010 | SNES | 제어코드 첫 바이트를 종료자로 오인 | `references/tips/snes.md#snes-010` |
| SATURN-002 | Saturn | 정적으로 비어 보이는 코드 영역 사용 | `references/tips/saturn.md#saturn-002` |
| SATURN-003 | Saturn | 무변경 원본 재압축도 게임에서 손상 | `references/tips/saturn.md#saturn-003` |
| SATURN-004 | Saturn | opcode 인자를 포인터 prefix로 오인 | `references/tips/saturn.md#saturn-004` |
| SATURN-005 | Saturn | 메뉴 표시보다 앞서 적재된 스프라이트 | `references/tips/saturn.md#saturn-005` |
| SATURN-007 | Saturn | 글리프 부족으로 번역 표현을 임시 축약 | `references/tips/saturn.md#saturn-007` |
| PCE-001 | PC Engine | 타일맵이 한 타일셋만큼 밀림 | `references/tips/pce.md#pce-001` |
| PCE-002 | PC Engine CD | 사용자 데이터 오프셋으로 raw 이미지를 패치 | `references/tips/pce.md#pce-002` |
| PC98-001 | PC-98 | 표준 디코더 통계로 미사용 lead 선정 | `references/tips/pc98.md#pc98-001` |
| GG-001 | Game Gear | 상점 가격과 후속 대사가 함께 어긋남 | `references/tips/gg.md#gg-001` |
| GG-002 | Game Gear | stale VRAM save state로 font source를 기각 | `references/tips/gg.md#gg-002` |
| GG-003 | Game Gear | decoder 수정 뒤에도 구 원문 기반 번역이 잔존 | `references/tips/gg.md#gg-003` |
| MD-001 | Mega Drive | 번역 뒤 특정 대사에서 진행 정지 | `references/tips/megadrive.md#md-001` |
| MD-002 | Mega Drive | 초기 KR 번역이 화자 제어 순서를 무시 | `references/tips/megadrive.md#md-002` |
