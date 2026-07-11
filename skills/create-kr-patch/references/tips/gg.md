# Game Gear 국소 사례

여기의 관측은 Game Gear 전체의 규칙이 아니다. 발동 조건이 맞을 때 조사 후보로만 사용한다.

## GG-001

- **관측 범위:** Game Gear 마도물어 1의 상점 가격 대사와 한글 렌더러.
- **사고 맥락:** 가격이 `금` 옆 자리 대신 창 하단으로 밀리고 후속 대사 순서도 함께 흐트러졌다. 가격 위치를 추적하는 커서가 틀렸다고 보았지만, 가격 채우기는 호출자가 준 고정 RAM 슬롯에 쓰고 최종 VRAM writer는 완성된 행을 복사할 뿐이었다.
- **결정 실험:** 작업 버퍼→shadow diff→VRAM 전송을 역추적하고, 한글 렌더러의 창별 타일 base 선택을 원본 초기화 테이블과 대조했다. 공유 창과 일반 창을 같은 base로 취급한 차이를 고친 뒤 상점 대사 순서와 inline 가격 표시가 함께 정상화됐다.
- **확정 결론:** 이 결함의 원인은 가격 writer가 아니라 그보다 앞선 렌더 세션의 창별 base 선택이었다. 최종 복사 지점이나 한 증상만 추적하면 공유 원인을 놓칠 수 있었다.
- **전이 한계:** 고정 가격 슬롯과 base 선택 값은 이 화면·리비전의 사실이며 다른 Game Gear UI에 이식하지 않는다.
- **관련 판단 기준:** `references/platforms/gg.md` §4, `references/strategy/debugging.md` §4.

## GG-002

- **관측 범위:** Game Gear 마도물어 1의 상점·HUD 돈 단위 `金` 글리프와 scene 초기 VRAM upload.
- **사고 맥락:** ROM의 세 글리프 후보를 바꿔도 표시가 그대로여서 실제 소스가 압축됐거나 런타임 생성된다고 결론냈다. 그러나 실험은 이미 옛 VRAM이 캐시된 save state를 불러와 upload 경계를 건너뛴 상태였다.
- **결정 실험:** 부팅부터 살아 있는 VRAM write probe로 scene 초기 upload를 잡아 source register와 mapper 상태를 ROM 후보에 연결했다. 수정 ROM을 fresh upload 경로로 다시 실행하자 후보 중 하나의 1bpp 글리프가 실제 돈 타일을 구동했다.
- **확정 결론:** 압축·생성 가설은 기각됐고, 원인은 stale VRAM 상태가 만든 거짓 음성이었다. 확인된 글리프를 expected source bytes와 함께 교체하고 fresh upload 뒤 `금` 표시를 검증했다.
- **전이 한계:** save state는 렌더러 이후 동작이나 장면 재현에는 유효하다. 다만 그 상태가 건너뛴 적재·업로드·캐시 갱신을 증명하지 못하며, 특정 bank·주소는 이 리비전에만 적용된다.
- **관련 판단 기준:** `references/strategy/runtime-assets.md` §2, `references/strategy/debugging.md` §2.

## GG-003

- **관측 범위:** Game Gear 마도물어 1의 초기 JP decode와 그 결과를 기준으로 만든 한국어 번역 자산.
- **사고 맥락:** 구 decoder가 JP byte `0x7F`의 온점 `。`을 별표 `☆`로 오독했다. decoder와 JP 필드는 나중에 고쳐졌지만 이미 구 원문을 보고 만든 한국어 554엔트리에는 별표 1,781개와 그 해석이 남았다.
- **결정 실험:** 대상 ROM의 빈도·문맥, 실제 화면 표본과 자매 원문을 대조해 `0x7F=。`를 확정했다. 한국어 별표의 위치도 전수 조사해 모두 문말에 남은 오독 흔적임을 확인하고, 깨끗한 JP·인접 문맥·화자·용어를 다시 공급해 영향 범위를 재번역·교차 검토했다.
- **확정 결론:** decoder 수정과 번역 기준선 갱신은 별도 작업이다. 파생 원문이 바뀌면 그 이전 기준선에서 만든 번역을 그대로 complete로 유지할 수 없으며, 영향받는 범위를 재검증해야 했다.
- **전이 한계:** `0x7F`의 의미와 별표 수는 이 리비전의 사실이다. 다른 프로젝트에서 특정 문자 검색만으로 stale 번역을 판정하지 말고 source identity와 decode 변화의 영향 범위를 비교한다.
- **관련 판단 기준:** `references/conventions/translation-artifacts.md` §1·§5, `references/strategy/translation-workflow.md` §3.1.
