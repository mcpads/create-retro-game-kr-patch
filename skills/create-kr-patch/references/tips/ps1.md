# PlayStation 국소 사례

여기의 관측은 PlayStation 전체의 규칙이 아니다. 발동 조건이 맞을 때 조사 후보로만 사용한다.

## PS1-001

- **관측 범위:** PlayStation 와쿠와쿠 뿌요뿌요 던전의 부트 재적재 뒤 RAM 훅과 R3000A I-cache 상태.
- **사고 맥락:** 네 명령 trampoline이 16바이트 cache line 두 개에 걸친 상태에서 부트 해제기가 같은 RAM을 다시 썼다. RAM에는 패치가 있었지만 line별 stale/fresh 상태가 달라 원본 `jal`과 패치된 delay slot이 섞여 실행되고 보존 register가 오염됐다.
- **검증 근거:** 두 line의 RAM·실행 명령 조합과 register 결과를 대조해 혼합 실행 사슬을 확인했다. trampoline을 한 cache line 안의 세 명령으로 줄이고 다음 원본 명령을 delay slot으로 유지했으며, 훅 본체는 uncached KSEG1 alias에서 실행하도록 바꿨다.
- **확정 결과:** 다시 쓰이는 patch site의 실행 단위를 한 cache line 안에 묶고 uncached 경로를 사용해 stale/fresh 명령 혼합을 제거했다.
- **전이 한계:** 이 개입은 해당 타이틀의 재적재 범위·cache line·alias·호출 프롤로그에서 검증됐다. 모든 PS1 훅에 KSEG1이나 세 명령 trampoline이 필요한 것은 아니며, cache invalidation과 재적재 순서를 대상에서 다시 판정한다.
- **관련 판단 기준:** `references/strategy/reinsertion.md` §4·§6, `references/strategy/runtime-assets.md` §2, `references/strategy/debugging.md` §3.

## PS1-002

- **관측 범위:** PlayStation 와쿠와쿠 뿌요뿌요 던전의 Story SEQ에서 한 포인터가 다른 메시지 내부의 완전한 제어 세그먼트 경계로 진입하고, 추출 단계가 겹친 문자열을 합친 경우.
- **사고 맥락:** 중복 제거 뒤 남은 엔트리를 목록 순서로 다시 번호 매기면 다른 포인터 슬롯을 번역하게 된다. 제거된 내부 포인터를 별도 원문 블록으로 복사하면 부모 메시지는 번역돼도 그 포인터로 진입한 화면에는 원문 tail이 남았다.
- **검증 근거:** 추출 산출물이 원본 포인터 슬롯 번호를 유지하고 재삽입기가 이를 우선해 읽는 회귀 테스트를 만들었다. 별도 내부 포인터는 원문 부모 안의 완전한 제어 세그먼트 경계와 번역된 부모의 같은 세그먼트 경계를 대응시켜 파생했으며, 중첩된 각 포인터가 기대한 번역 tail을 소비하는 합성 SEQ 테스트로 확인했다.
- **확정 결과:** 문자열을 합쳐도 재삽입 정체성은 원본 포인터 슬롯에 귀속하고, 부모 내부 타깃은 목록 순서나 원문 바이트 거리가 아니라 번역 뒤에도 보존되는 완전한 구조 anchor로 다시 계산해야 했다.
- **전이 한계:** 관측된 제어 구분자와 세그먼트 의미는 이 SEQ 소비자의 사실이며 다른 포맷의 공통 경계가 아니다. 원문·번역의 구조 anchor를 가역적으로 대응할 수 없거나 내부 진입의 의미가 다르면 이 방법으로 타깃을 추정하지 않는다.
- **관련 판단 기준:** `references/strategy/text-extraction.md` §1.3·§4.1·§4.2, `references/strategy/reinsertion.md` §1.2·§2·§3.
