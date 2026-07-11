# PlayStation 국소 사례

여기의 관측은 PlayStation 전체의 규칙이 아니다. 발동 조건이 맞을 때 조사 후보로만 사용한다.

## PS1-001

- **관측 범위:** PlayStation 와쿠와쿠 뿌요뿌요 던전의 부트 재적재 뒤 RAM 훅과 R3000A I-cache 상태.
- **사고 맥락:** 네 명령 trampoline이 16바이트 cache line 두 개에 걸친 상태에서 부트 해제기가 같은 RAM을 다시 썼다. RAM에는 패치가 있었지만 line별 stale/fresh 상태가 달라 원본 `jal`과 패치된 delay slot이 섞여 실행되고 보존 register가 오염됐다.
- **검증 근거:** 두 line의 RAM·실행 명령 조합과 register 결과를 대조해 혼합 실행 사슬을 확인했다. trampoline을 한 cache line 안의 세 명령으로 줄이고 다음 원본 명령을 delay slot으로 유지했으며, 훅 본체는 uncached KSEG1 alias에서 실행하도록 바꿨다.
- **확정 결과:** 다시 쓰이는 patch site의 실행 단위를 한 cache line 안에 묶고 uncached 경로를 사용해 stale/fresh 명령 혼합을 제거했다.
- **전이 한계:** 이 개입은 해당 타이틀의 재적재 범위·cache line·alias·호출 프롤로그에서 검증됐다. 모든 PS1 훅에 KSEG1이나 세 명령 trampoline이 필요한 것은 아니며, cache invalidation과 재적재 순서를 대상에서 다시 판정한다.
- **관련 판단 기준:** `references/strategy/reinsertion.md` §4·§6, `references/strategy/runtime-assets.md` §2, `references/strategy/debugging.md` §3.
