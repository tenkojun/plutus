# -*- coding: utf-8 -*-
"""
English — section headings, expert stances, gate actions, table labels.

Third high-impact batch.
"""

CATALOG = {

    # ── section and chart titles ──────────────────────────────
    "직능별 소견과 반대신문": "Opinions by discipline and cross-examination",
    "수익률 꼬리 + 스트레스 시나리오": "Return tails + stress scenarios",
    "지평별 수익 · 변동성 · 낙폭":
        "Return, volatility and drawdown by horizon",
    "수익 귀인 — 알파인가 베타인가":
        "Return attribution — alpha or beta",
    "1년 시뮬레이션 분포 (팬차트)":
        "One-year simulated distribution (fan chart)",
    "촉매 캘린더 · 모니터링 플랜": "Catalyst calendar · monitoring plan",
    "델타 패널 — 헤지펀드 민감도": "Delta panel — hedge fund sensitivities",
    "이 분석이 말할 수 없는 것": "What this analysis cannot tell you",
    "유동성 · 거래비용 · 용량": "Liquidity · transaction cost · capacity",
    "조건부 변동성": "Conditional volatility",
    "시변 베타 — ": "Time-varying beta — ",
    "추정량 간 산포": "Dispersion across estimators",
    "자산군 표준 충격": "Asset-class standard shock",
    "최장 수중기간": "Longest underwater period",
    "기대밴드": "Expected band",

    # ── expert stances and blind spots ────────────────────────
    "비용에 과민하다. 좋은 아이디어를 비용 때문에 죽일 위험이 있음.":
        "Oversensitive to cost. Risks killing a good idea over expenses.",
    "헤지 가능한 위험을 과대평가하는 경향. 잔차 위험을 잊기 쉬움.":
        "Tends to overrate hedgeable risk and to forget residual risk.",
    "추정 불확실성을 크게 본다. 기대수익 기반 의사결정에 부정적.":
        "Weighs estimation uncertainty heavily. Sceptical of decisions "
        "driven by expected return.",
    "실행 가능성을 중시. 정교하지만 실행 불가능한 결론을 싫어함.":
        "Prioritises executability. Dislikes conclusions that are elegant "
        "but cannot be traded.",
    "국면 전환을 과하게 읽는 경향. 표본이 적으면 과신 위험.":
        "Inclined to read regime shifts into noise. Risks overconfidence "
        "on a small sample.",
    "구조적으로 부정적. 좋은 기회를 놓치게 만들 수 있음.":
        "Structurally negative. Can cause good opportunities to be missed.",
    "메타데이터를 불신한다. 라벨보다 수익률 지문을 믿는다.":
        "Distrusts metadata. Believes the return fingerprint over the "
        "label.",
    "거래할 수 없으면 옳아도 소용없다. 알파는 스프레드에서 죽는다.":
        "Being right is worthless if you cannot trade it. Alpha dies in "
        "the spread.",
    "먼저 이것이 무엇인지 정하지 않으면 어떤 지표도 의미가 없다.":
        "Until you settle what this thing is, no metric means anything.",
    "설명되지 않는 수익은 알파가 아니라 아직 찾지 못한 팩터다.":
        "Unexplained return is not alpha — it is a factor you have not "
        "found yet.",
    "발견은 검증되기 전까지 가설이다. 나는 반증 절차만 본다.":
        "A finding is a hypothesis until it is validated. I look only at "
        "the falsification procedure.",
    "좋은 분석과 좋은 트레이드는 다르다. 나는 후자만 본다.":
        "A good analysis and a good trade are different things. I only "
        "look at the second.",
    "무엇을 상쇄할 수 있고 무엇이 남는지를 먼저 정한다.":
        "First settle what can be offset and what is left over.",

    # ── inputs each expert sees ───────────────────────────────
    "OHLCV 미시구조 지표만 (EDGE / Amihud / ADV)":
        "OHLCV microstructure metrics only (EDGE / Amihud / ADV)",
    "매크로 팩터 시계열 + 발표 캘린더 (발표 예정치 선반영 금지)":
        "Macro factor series + release calendar (no pricing in of "
        "scheduled figures)",
    "원시 OHLCV · 배당/분할 이벤트 · 거래소 캘린더만":
        "Raw OHLCV, dividend and split events, exchange calendar only",
    "수익률 파생 국면 피처만 — **날짜·종목명 블라인드**":
        "Return-derived regime features only — **blind to date and "
        "ticker**",

    # ── gate actions ──────────────────────────────────────────
    "팩터 기반 델타·헤지·스트레스 전부 무효화. 가격 모듈만 사용.":
        "Factor-based deltas, hedge and stress are all invalidated. Use "
        "the price modules only.",
    "체결 비용이 기대 엣지를 잠식. 사이즈 0 또는 지정가 분할.":
        "Execution cost eats the expected edge. Size zero, or work it with "
        "limit orders.",
    "기대수익 기반 사이징 금지. 변동성·낙폭 기준으로만 사이징.":
        "No sizing on expected return. Size on volatility and drawdown "
        "only.",
    "사이즈 0. 헤지로 노출을 줄이기 전까지 진입 불가.":
        "Size zero. No entry until the exposure is hedged down.",
    "Brier skill ≤ 0 이 지속되면 확률 출력 중단":
        "If Brier skill stays at or below zero, stop publishing "
        "probabilities",
    "β 변동계수가 0.5 아래로 안정되면 전량 헤지를 권고합니다.":
        "Once the beta coefficient of variation settles below 0.5, I "
        "recommend hedging in full.",
    "bp를 넘거나 ADV가 절반으로 줄면 즉시 차단합니다.":
        "bp, or if ADV halves, I halt immediately.",

    # ── interpretation notes ──────────────────────────────────
    "] 내. 팩터 해석 유효.": "]. The factor interpretation holds.",
    "년). 장기 보유 시 회복 지연 위험.":
        " years). Holding long term risks a slow recovery.",
    "가 시장 변동성이 아니라 **우리의 파라미터 무지**에서 옵니다.":
        " comes not from market volatility but from **our ignorance of the "
        "parameters**.",
    " — 변형 선택이 불안정하나 신호 존재를 부정하지는 않음. 확률 신뢰구간을 ±":
        " — the variant selection is unstable, but that does not deny a "
        "signal exists. The probability interval is widened by ±",
    " → 선택 절차가 구조적으로 과적합 (변형 산포 t=":
        " → the selection procedure is structurally overfit (variant "
        "dispersion t=",
    " (자산군 밴드 하단의 55%)": " (55% of the asset-class band floor)",

    "⚠ 이 드라이버 조합만으로는 손실이 발생하지 않는다. 즉 하방 위험의 출처가 "
    "선택된 팩터가 아니라 고유(잔차)·꼬리·유동성이라는 뜻이다. 팩터 스트레스로 "
    "하방을 재면 과소평가된다 — VaR/ES와 낙폭 섹션을 기준으로 보라.":
        "⚠ This driver combination alone produces no loss. That means the "
        "downside comes from idiosyncratic (residual) risk, tails and "
        "liquidity — not from the selected factors. Measuring downside "
        "with factor stress understates it; read the VaR/ES and drawdown "
        "sections instead.",

    "를 넘습니다. 헤지로 노출을 줄이거나 사이즈를 0으로 두기 전까지 저는 "
    "진입에 동의하지 않습니다. 참고로 이 손익은 선형 델타 근사이므로 비선형 "
    "반응과 유동성 연쇄는 포함되지 않았습니다 — 실제로는 더 나쁠 수 "
    "있습니다.":
        ". I do not consent to entry until the exposure is hedged down or "
        "the size is set to zero. Note that this P&L is a linear delta "
        "approximation: it excludes non-linear response and liquidity "
        "cascades, so reality can be worse.",

    "로 Harvey-Liu-Zhu 허들(3.0)에 미달합니다. 다중검정을 고려하면 0과 "
    "구별되지 않으므로 기대수익 산정에 넣지 말아야 합니다.":
        ", short of the Harvey-Liu-Zhu hurdle of 3.0. Allowing for "
        "multiple testing it is indistinguishable from zero and should not "
        "enter the expected-return calculation.",

    "로 허들을 넘습니다. 다만 단일 종목 표본에서의 t값이므로, 같은 절차를 여러 "
    "종목에 반복했다면 선택편향 보정이 필요합니다.":
        ", clearing the hurdle. But this is a t-value on a single-name "
        "sample: if the same procedure was repeated across many names, it "
        "needs a selection-bias adjustment.",

    "로 큽니다. 평균을 내지 않고 통합 확률을 중립 쪽으로 축소했습니다 — "
    "불일치 자체가 정보입니다.":
        ", which is large. Rather than averaging, the pooled probability "
        "is shrunk towards neutral — the disagreement is itself "
        "information.",

    "복잡한 모델이 선형을 이기지 못해 로지스틱을 채택":
        "The complex models did not beat linear, so logistic was adopted",

    "일간 리밸런싱 → 경로의존. 장기 기대 로그수익 ≈ Lμ − L(L−1)σ²/2. "
    "몬테카를로는 기초자산에 돌리고 레버리지 경로를 재구성해야 함.":
        "Daily rebalancing makes it path dependent. The long-run expected "
        "log return is ≈ Lμ − L(L−1)σ²/2. Monte Carlo has to be run on the "
        "underlying and the levered path reconstructed from it.",

    "종가 기준 참고가. 실제 체결은 다음 거래일 시가/VWAP 가정":
        "Reference price at the close. Actual execution assumes the next "
        "session's open or VWAP",

    "스냅샷만 제공 → 백테스트 불가. 오늘부터 축적해야 합니다.":
        "Only a snapshot is available, so no backtest is possible. It has "
        "to be accumulated from today.",

    "일봉만 사용 → 진짜 실현변동성·오더플로우 계산 불가.":
        "Daily bars only, so true realised volatility and order flow "
        "cannot be computed.",

    "거래소 quoteType=EQUITY → 개별주. 명칭 키워드보다 우선한다.":
        "Exchange quoteType=EQUITY, so a single name. This outranks "
        "keyword matching on the name.",

    # ── short labels ──────────────────────────────────────────
    "값": "Value",
    "예": "Yes",
    "항목": "Item",
    "강세 시나리오": "Bull scenario",
    "β 불안정 — 헤지 사용 부적합":
        "β unstable — unsuitable as a hedge",
    "리스크 예산": "Risk budget",
    "현재": "Current",
    " 구조": " structure",
    "방향 예측": "Direction forecast",
    "신뢰": "Confidence",
    "분포": "Distribution",
    "손절": "Stop",
    "자산군 상한": "Asset-class cap",
    "OHLC 논리 위반": "OHLC logic violation",
    "장기": "Long term",
    "상승": "Up",
    "기준": "Basis",
    "국면 ": "Regime ",
}
