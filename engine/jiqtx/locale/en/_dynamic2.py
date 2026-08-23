# -*- coding: utf-8 -*-
"""
English — dynamic_report, part 2: panel intro, horizons, macro board,
attribution, event risk.
"""

CATALOG = {

    # ── delta panel / ML ──────────────────────────────────────
    "선택 팩터: ": "Selected factors: ",
    " (Elastic-Net 선택 → OLS/Newey-West 재추정)":
        " (Elastic-Net selection → re-estimated with OLS/Newey-West)",
    "'샤프 0.96' 같은 요약통계가 아니라 ":
        "Not a summary statistic like 'Sharpe 0.96' but ",
    "무엇이 X만큼 움직이면 얼마를 잃는가":
        "if this moves by X, how much do you lose",
    ". 정적 베타가 아니라 시변 베타를 쓰고 하방 분위 베타를 나란히 "
    "표시합니다.":
        ". It uses time-varying rather than static betas and shows the "
        "downside-quantile beta alongside.",
    " · 승자 모델 ": " · winning model ",
    "Murphy 분해": "Murphy decomposition",
    ": Brier = Reliability − Resolution + Uncertainty. Resolution ≈ 0이면 "
    "모델이 기저율 이상의 정보를 담고 있지 않다는 ":
        ": Brier = reliability − resolution + uncertainty. Resolution ≈ 0 "
        "is ",
    "정량적 증명": "quantitative proof that the model carries no "
                   "information beyond the base rate",
    "엔진: ": "Engine: ",
    "드리프트가 왜 문제인가": "Why drift is a problem",
    " — 표본 드리프트의 표준오차는 σ/√T이며, 일봉 표본에서 거의 항상 추정치 "
    "자체만큼 큽니다.":
        " — the standard error of the sample drift is σ/√T, and on daily "
        "data it is almost always as large as the estimate itself.",
    "시장 함축 분포 (RND)": "Market-implied distribution (RND)",
    "채택 모델: ": "Adopted model: ",
    "최악: ": "Worst: ",
    " (한도 ": " (limit ",
    "보정 상승확률 ": "Calibrated probability of a rise ",
    "게이트를 통과하지 못했으므로 ": "The gate was not passed, so ",
    "확률을 출력하지 않습니다.": "no probability is published.",
    " 감점된 점수를 내는 것은 없는 정보를 있는 것처럼 만드는 일입니다.":
        " Publishing a marked-down score would manufacture information "
        "that does not exist.",
    "상위 피처: ": "Top features: ",
    "위반율": "Breach rate",

    # ── Kelly ─────────────────────────────────────────────────
    "켈리 공식 자체가 아니라 ": "It is not the Kelly formula but ",
    "μ를 안다고 가정한 것": "the assumption that you know μ",
    "이 문제입니다. 성장 최적 켈리는 수학적으로 옳아도 운용 불가능한 낙폭을 "
    "동반합니다. 낙폭 제약이 없으면 어떤 켈리 값도 실무 권고로 쓸 수 "
    "없습니다.":
        " that is the problem. Growth-optimal Kelly is mathematically "
        "correct and comes with a drawdown you cannot run. Without a "
        "drawdown constraint no Kelly number is usable as practical "
        "advice.",
    "우리 모델 vs 시장 — 차이가 곧 논지":
        "Our model vs the market — the gap is the thesis",

    # ── panel ─────────────────────────────────────────────────
    "각 전문가는 ": "Each expert first declares ",
    "직함과 선언된 편향": "their title and their stated bias",
    "을 먼저 밝히고, 자기 체크리스트로 심사한 뒤 소견을 냅니다. 소견문은 LLM "
    "생성이 아니라 각자의 결정 규칙에서 도출되므로 같은 입력이면 같은 소견이 "
    "나옵니다 — 감사 가능합니다.":
        ", works through their own checklist, and then files an opinion. "
        "The text is not LLM-generated but derived from each one's "
        "decision rules, so the same input yields the same opinion — it "
        "is auditable.",
    "합의된 사실 (상위 위계 통과 항목)":
        "Agreed facts (items that cleared the higher evidence tiers)",
    "LLM 멀티에이전트 토론은 자동으로 정확도를 올리지 않습니다. 동조 효과, "
    "다수의 폭정, 그리고 ":
        "LLM multi-agent debate does not automatically improve accuracy. "
        "There is conformity, tyranny of the majority, and ",
    "동일 입력을 받으면 토론이 마팅게일이 되어 개선이 없다":
        "the theoretical result that debate on identical inputs is a "
        "martingale and improves nothing",
    "는 이론적 결과가 있습니다. 따라서 각 에이전트에 서로 다른 데이터 "
    "슬라이스를 주고, 거부권은 통계 에이전트에만 부여하며, 최종 판정은 "
    "결정론적 규칙 엔진이 합니다.":
        ". So each agent gets a different slice of the data, the veto "
        "belongs only to the statistics agents, and the final verdict is "
        "made by a deterministic rule engine.",
    "캘리브레이션 가중 로그오즈 풀링":
        "Calibration-weighted log-odds pooling",
    "소속": "Affiliation",
    "렌즈": "Lens",
    "생각을 바꿀 조건": "What would change their mind",
    "역할": "Role",
    "반론의 승패는 ": "A disagreement is settled by ",
    "로 결정됩니다: ① 데이터 무결성 → ② 체결 가능성 → ③ 표본외 통계 → "
    "④ 표본내 통계 → ⑤ 경제적 메커니즘 → ⑥ 서사. 상위 증거가 하위 주장을 "
    "이깁니다.":
        ": (1) data integrity → (2) executability → (3) out-of-sample "
        "statistics → (4) in-sample statistics → (5) economic mechanism → "
        "(6) narrative. Higher evidence beats lower claims.",
    " — 산포가 크면 통합 확률을 0.5로 축소합니다(평균내지 않음).":
        " — when dispersion is large the pooled probability is shrunk "
        "towards 0.5 (never averaged).",
    "거부권 발동": "Veto raised",

    # ── monitoring ────────────────────────────────────────────
    "촉매 캘린더": "Catalyst calendar",
    "모니터링 플랜": "Monitoring plan",
    "모니터링 플랜이 없는 논지는 검증되지 않습니다. 각 항목은 ":
        "A thesis without a monitoring plan never gets tested. Each item "
        "needs ",
    "출처와 주기와 임계": "a source, a frequency and a threshold",
    "가 지정되어 있어야 누군가 실제로 확인할 수 있습니다.":
        " before anyone can actually check it.",
    "미반영.": "Not included.",

    # ── horizons ──────────────────────────────────────────────
    "지평별 결과를 ": "Results by horizon are ",
    "평균하지 않습니다.": "never averaged.",
    " 단기 55점·중기 72점·장기 74점을 기간가중해 67점(BUY)을 만들면 '장기 "
    "구조적 상승 안의 중기 조정' 같은 정보가 통째로 사라집니다. 평균 하나만 "
    "남고, 그 평균은 어느 기간에도 해당하지 않습니다. 여기서는 지평별로 따로 "
    "계산하고 ":
        " Weighting short 55, mid 72 and long 74 into a single 67 (BUY) "
        "erases the fact that this is a mid-term correction inside a "
        "long-term structural uptrend. All that is left is one average, "
        "and it describes no horizon at all. Here each horizon is computed "
        "separately and ",
    "서로 어긋나는 지점": "the points where they disagree",
    "을 찾아 드러냅니다.": " are found and shown.",
    "드리프트 표준오차는 σ/√T 입니다. 지평이 짧을수록 커져서, 짧은 구간의 "
    "기대수익률은 거의 언제나 0과 구별되지 않습니다. |t| < 2 인 지평의 "
    "수익률로 미래를 말하면 안 됩니다.":
        "The drift standard error is σ/√T. The shorter the horizon the "
        "larger it grows, so a short window's expected return is almost "
        "always indistinguishable from zero. Do not talk about the future "
        "using a horizon whose |t| is below 2.",
    "지평 간 불일치": "Disagreement across horizons",
    "변동성 기간구조 — ": "Volatility term structure — ",
    "추세": "Trend",
    "교차": "Crossover",
    "시장β": "Market β",

    # ── macro board ───────────────────────────────────────────
    "전술적 거시 판단": "Tactical macro view",
    "구조적 거시 판단": "Structural macro view",
    "핵심 전환 신호": "Key transition signal",
    "거시 시나리오 매트릭스": "Macro scenario matrix",
    "에 실제로 영향을 주는 거시 변수만 골라 봅니다. 자산군마다 보는 변수가 "
    "다릅니다 — 금에는 실질금리·달러가, 국채에는 명목금리·커브가, "
    "개별주에는 시장·변동성·크레딧이 들어갑니다.":
        " only the macro variables that genuinely move it are shown. Each "
        "asset class looks at different ones — real rates and the dollar "
        "for gold, nominal rates and the curve for treasuries, market, "
        "volatility and credit for single names.",
    "최신값": "Latest",
    "출처: ": "Source: ",

    # ── archetype ─────────────────────────────────────────────
    "아키타입 신뢰도 ": "Archetype confidence ",
    " · 코드 ": " · code ",
    "밸류에이션 앵커": "Valuation anchors",
    "이 성격에서 특히 볼 것": "What to watch for this character in particular",
    "이 아키타입 판정에 따라 아래 섹션 구성이 달라집니다 → 활성 섹션: ":
        "This archetype call changes which sections appear below → active "
        "sections: ",
    " 고유 주의사항": " — specific cautions",
    "이며, 현재 판정은 ": " and the current verdict is ",
    "주말 거래 관측 → 24/7 시장":
        "Weekend trading observed → a 24/7 market",
    "경로의존 — 변동성 드래그 반영":
        "Path dependent — volatility drag included",
    "⚠ 평활화 의심 → 샤프 과대":
        "⚠ Smoothing suspected → Sharpe overstated",

    # ── attribution ───────────────────────────────────────────
    "손익의 최대 단일 기여 요인은 ":
        "The largest single contributor to P&L is ",
    "로, 표준 충격 시 ": ", and under a standard shock ",
    "는 고유 요인이라 ": " is idiosyncratic and therefore ",
    "사이즈로만 통제": "controlled only through size",
    "됩니다.": ".",
    "시나리오 가중 기대수익은 ":
        "The scenario-weighted expected return is ",
    "(상방 ": "(upside ",
    " / 하방 ": " / downside ",
    "발동된": "fired",
    " 반증 조건: ": " falsifiers: ",
    "기대손익 (비용 후)": "Expected P&L (after costs)",
    "무헤지 ": "Unhedged ",
    "팩터 설명분": "Explained by factors",
    "금리 델타": "Rate delta",
    "연수익": "Annual return",
    "최악일": "Worst day",
    "이것이 원본 리포트의 핵심 오류 지점입니다. GLD에 주식형 FF 회귀를 돌려 "
    "R²=2%가 나왔고 잔차 98%를 '종목 고유위험'으로 해석했습니다. 실제로는 ":
        "This is where the original report went most wrong. It ran an "
        "equity-style Fama-French regression on GLD, got R²=2%, and read "
        "the 98% residual as idiosyncratic risk. In reality it is ",
    "누락 변수": "an omitted variable",
    "이며, R²가 2%인 회귀의 알파는 해석 불가능한 잔차 평균입니다.":
        ", and the alpha of a regression with an R² of 2% is an "
        "uninterpretable residual mean.",

    # ── scenarios ─────────────────────────────────────────────
    "복합 시나리오는 ": "Composite scenarios are computed with ",
    "부분(다변량) 베타": "partial (multivariate) betas",
    "로 계산합니다. 델타 패널의 단변량 베타에는 그 충격에 딸려 오는 시장 "
    "움직임이 이미 포함돼 있어서, 여러 팩터를 동시에 때리는 시나리오에서 "
    "그대로 더하면 같은 충격을 여러 번 세게 됩니다. 단일 팩터 시나리오는 "
    "총효과가 맞으므로 단변량을 그대로 씁니다.":
        ". The univariate betas in the delta panel already contain the "
        "market move that travels with each shock, so adding them up in a "
        "scenario that hits several factors at once counts the same shock "
        "repeatedly. For a single-factor scenario the total effect is what "
        "you want, so the univariate beta is used as is.",
    "드라이버 기반 시나리오 중 ": "Among the driver-based scenarios, ",
    "손실이 나는 것이 없습니다.": "none produces a loss.",
    " 페이오프 비율이 정의되지 않으며, 이는 좋은 신호가 아니라 ":
        " The payoff ratio is undefined, which is not a good sign but ",
    "하방 위험의 출처가 선택된 팩터가 아니라는 뜻":
        "an indication that the downside does not come from the selected "
        "factors",
    "입니다. 하방은 VaR/ES·낙폭·점프 섹션에서 읽어야 합니다.":
        ". Read the downside in the VaR/ES, drawdown and jump sections.",

    # ── event risk ────────────────────────────────────────────
    "분산이 소수의 발표일에 집중되어 있습니다. 평상시 변동성으로 리스크를 재면 "
    "심각히 과소평가되며, 정규 VaR은 이 구조를 표현하지 못합니다. 어닝 전후 "
    "사이즈를 별도로 관리해야 합니다.":
        "Variance is concentrated in a handful of release days. Measuring "
        "risk with everyday volatility understates it badly, and normal "
        "VaR cannot express this structure. Size has to be managed "
        "separately around earnings.",
    "이 종목은 ": "In this name ",
    "점프가 수익률을 지배": "jumps dominate the return",
    "합니다. 샤프비율·정규 VaR·GBM 시뮬레이션은 구조적으로 부적합하며, "
    "포지션 사이징이 방향 예측보다 훨씬 중요합니다.":
        ". Sharpe, normal VaR and GBM simulation are structurally "
        "inappropriate, and position sizing matters far more than "
        "predicting direction.",
    "일 뒤 어닝 발표": " days until earnings",
    "). 이벤트 리스크 구간입니다.": "). This is an event-risk window.",
    "발표일 |수익률| 중앙값": "Median |return| on release days",
    " — 동시 청산 리스크": " — simultaneous-liquidation risk",
    "고유위험 비중 ": "Idiosyncratic risk share ",
    " — 팩터 헤지 불가": " — cannot be hedged with factors",
    "1% AUM 청산에 ": "Liquidating 1% of AUM takes ",

    # ── benchmark ─────────────────────────────────────────────
    "상대수익 1년": "Relative return, 1 year",
    "상대수익 3개월": "Relative return, 3 months",
    "상관계수": "Correlation",
    "트래킹에러 (연)": "Tracking error (annual)",
    "정보비율": "Information ratio",
    "상대강도 백분위": "Relative strength percentile",
    "흑자 — 해당 없음": "Profitable — not applicable",

    # ── small labels ──────────────────────────────────────────
    "영업일)": " trading days)",
    "왜도 ": "Skew ",
    " · 첨도 ": " · kurtosis ",
    "일": " days",
    "구분": "Category",
    "관측횟수": "Observations",
    "발동 ": "Fired ",
    "IV 기간구조": "IV term structure",
}
