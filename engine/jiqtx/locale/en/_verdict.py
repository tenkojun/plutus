# -*- coding: utf-8 -*-
"""
English — verdict strip, scenario table, attribution, expert roles.

Fourth high-impact batch.
"""

CATALOG = {

    # ── part and section titles ───────────────────────────────
    "최종 판정 — 3축 분리": "Final verdict — three separate axes",
    "방향 예측 — 핵심은 기권": "Direction forecast — the point is abstention",
    "레드팀 — 사전등록된 반증": "Red team — pre-registered falsifiers",
    "펀더멘털 — 아키타입별 지표 선택":
        "Fundamentals — metrics selected by archetype",
    "시나리오 · 확률 × 손익": "Scenarios · probability × P&L",
    "단기 · 중기 · 장기": "Short · mid · long",
    "시나리오 · 트레이드 · 헤지 · 반증 조건":
        "Scenarios · trade · hedge · falsifiers",
    "수익률 꼬리 + 스트레스 시나리오 + 낙폭":
        "Return tails + stress scenarios + drawdown",
    "VaR/ES · 스트레스": "VaR/ES · stress",
    "수익 귀인 워터폴 — ": "Return attribution waterfall — ",
    "알파 t값 vs 허들 3.0": "Alpha t-value vs the 3.0 hurdle",
    "샤프 유의성에 필요한 표본":
        "Sample needed for Sharpe significance",
    "예측 불확실성의 출처": "Sources of forecast uncertainty",
    "교차검증 (CS / CHL / Roll)": "Cross-check (CS / CHL / Roll)",
    "매크로 발표 캘린더 (FOMC/CPI/고용)":
        "Macro release calendar (FOMC / CPI / payrolls)",
    "FHS-GARCH + EVT + 파라미터 불확실성":
        "FHS-GARCH + EVT + parameter uncertainty",

    # ── expert roles and mottos ───────────────────────────────
    "크로스에셋 분류 전략가": "Cross-asset classification strategist",
    "팩터 이코노미스트": "Factor economist",
    "이 결론을 무효화할 가장 그럴듯한 세계는 무엇인가.":
        "What is the most plausible world in which this conclusion is "
        "wrong?",
    "생산성에 무관심하다. 통과시키지 않는 것이 기본값.":
        "Indifferent to throughput. The default is to not let it pass.",
    "모든 결론은 입력 데이터의 품질을 넘을 수 없다.":
        "No conclusion can exceed the quality of the input data.",
    "가격은 결국 실질금리·달러·유동성의 함수다.":
        "Price is, in the end, a function of real rates, the dollar and "
        "liquidity.",
    "같은 자산도 국면이 바뀌면 다른 자산이다.":
        "The same asset in a different regime is a different asset.",
    "R² 붕괴는 버그가 아니라 구조 변화 신호":
        "A collapse in R² is not a bug — it is a signal of structural "
        "change",

    # ── inputs each expert sees ───────────────────────────────
    "OHLCV 미시구조 지표만": "OHLCV microstructure metrics only",
    "판정 결과 + 시나리오 + 유동성 + 사이징 제약":
        "Verdict + scenarios + liquidity + sizing constraints",
    "타 전문가의 결론 — **최종 단계에서만 열람**":
        "Other experts' conclusions — **read only at the final stage**",
    "타 에이전트 결론 (최종 단계에서만 열람)":
        "Other agents' conclusions (read only at the final stage)",
    "수익률 파생 국면 피처만 (날짜·종목명 블라인드)":
        "Return-derived regime features only (blind to date and ticker)",
    "팩터 수익률 패널만 (자산 가격 수준 미열람)":
        "Factor return panel only (price levels not read)",
    "수익률 시계열 + GARCH 표준화 잔차":
        "Return series + GARCH-standardised residuals",
    "발표 예정 지표는 선반영하지 않음 (PIT 원칙)":
        "Scheduled releases are not priced in (point-in-time principle)",

    # ── prose ─────────────────────────────────────────────────
    "유의한 거시 민감도가 없어 전환 신호를 정의할 수 없습니다.":
        "With no significant macro sensitivity, no transition signal can "
        "be defined.",

    " — 성과의 대부분이 팩터 노출입니다. 개별 종목 리스크를 지면서 ETF로 얻을 "
    "수 있는 것을 얻고 있는지 점검하십시오.":
        " — most of the performance is factor exposure. Check whether you "
        "are taking single-name risk to obtain something an ETF would have "
        "given you.",

    " — 성과의 대부분이 팩터로 설명되지 않습니다. 진짜 알파일 수도, 모델에 "
    "없는 팩터일 수도 있습니다. 팩터 R²(":
        " — most of the performance is not explained by the factors. It "
        "may be genuine alpha, or a factor the model lacks. The factor R² (",

    "방향 예측 모듈은 제 게이트를 통과하지 못했습니다: ":
        "The direction forecast module did not pass my gate: ",

    "제 모듈은 **출력을 내지 않습니다**. ":
        "My module **produces no output**. ",

    ". 게이트 실패는 감점이 아니라 출력 무효화다.":
        ". A failed gate invalidates the output; it does not dock points.",

    ")를 넘어야만 성립하는 구조. 승률 가정이 조금만 틀려도 기대값이 뒤집힌다.":
        "). The structure only holds above that, and a small error in the "
        "hit-rate assumption flips the expected value.",

    "**위험의 대부분이 고유 요인입니다.** 이 경우 헤지는 비용만 쓰고 효과가 "
    "작으므로, 실질적인 통제 수단은 헤지가 아니라 **사이즈 축소**입니다.":
        "**Most of the risk is idiosyncratic.** Hedging here costs money "
        "for little effect, so the real control is not a hedge but "
        "**cutting size**.",

    ". 선택한 팩터 세트가 이 자산을 설명하지 못한다. 결론이 팩터 선택에 "
    "의존한다면 그 결론은 무효.":
        ". The chosen factor set does not explain this asset. Any "
        "conclusion that depends on that choice is void.",

    " 의 R²가 최근 급락. 과거 베타로 추정한 델타는 이미 틀렸을 수 있다.":
        " has seen its R² fall sharply. Deltas estimated from the old beta "
        "may already be wrong.",

    "로 허들 3.0에 미달합니다. 통계적으로 0과 구별되지 않는 값을 기대수익에 "
    "넣으면 안 됩니다.":
        ", short of the 3.0 hurdle. A value statistically indistinguishable "
        "from zero must not enter an expected-return calculation.",

    "로 체결은 가능합니다. 추정량 간 산포가 ":
        ", so execution is feasible. The dispersion across estimators is ",

    "영업일입니다. 이 국면 안에서 연환산 수익 ":
        " trading days. Within this regime the annualised return is ",

    "경험확률과 모델확률의 괴리가 큰 시나리오: ":
        "Scenarios where the empirical and model probabilities diverge "
        "most: ",

    "0.10 초과면 통합 확률을 중립으로 축소":
        "Above 0.10 the pooled probability is shrunk towards neutral",

    "회 보정, 임계샤프 ": " trials adjusted, threshold Sharpe ",
    " → 1σ 이동 시 ": " → on a 1σ move, ",
    "R²가 ": "R² is ",
    "[베타 불안정] ": "[Beta unstable] ",
    " (게이트 실패 아님)": " (not a gate failure)",
    " · 확률 ": " · probability ",
    "반증 근거 ": "Counter-evidence ",
    "부분(다변량)": "Partial (multivariate)",

    # ── labels ────────────────────────────────────────────────
    "지평": "Horizon",
    "목표": "Target",
    "연 헤지 비용": "Annual hedge cost",
    "기본 시나리오": "Base scenario",
    "불안정": "Unstable",
    "중기": "Mid term",
    "주식시장 -10%": "Equity market −10%",
    "비용 후 기대손익": "Expected P&L after costs",
    "EDGE 스프레드 ": "EDGE spread ",
    "구간": "Range",
    "이벤트": "Event",
    "현재 국면": "Current regime",
    "현재 ": "Current ",
    "통과": "Pass",
    "통합 확률": "Pooled probability",
    "중변동": "Medium volatility",
    "최대낙폭": "Maximum drawdown",
    "기대밴드 ": "Expected band ",
    "팩터 모델 적합": "Factor model fit",
    "예측 불확실성의 ": "Forecast uncertainty ",
    "팩터 모델 설명력 붕괴": "Factor model explanatory power collapse",
    "시나리오 가중 기대수익": "Scenario-weighted expected return",
    "손실": "Loss",
    "상장폐지": "Delisting",
    "개": "",
}
