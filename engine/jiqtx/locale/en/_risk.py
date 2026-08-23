# -*- coding: utf-8 -*-
"""
English — risk, sizing, hedging, leverage and simulation labels.

Sixth high-impact batch.
"""

CATALOG = {

    # ── prose ─────────────────────────────────────────────────
    "에 불과합니다. 헤지로 한도를 맞추려는 시도는 비용만 쓰고 실패합니다 — "
    "사이즈를 줄이는 것이 유일한 수단입니다.":
        " only. Trying to hedge your way inside the limit spends money and "
        "fails — cutting size is the only instrument that works.",

    "에 불과. 위험의 대부분이 고유 요인이므로 헤지보다 **사이즈 축소**가 "
    "유효한 통제 수단이다.":
        " only. Most of the risk is idiosyncratic, so **cutting size** is "
        "the effective control, not hedging.",

    "지평 간 결론이 일치합니다 — 보유 기간에 크게 의존하지 않는 상태입니다.":
        "The horizons agree — the conclusion does not depend much on the "
        "holding period.",

    "경로의존 자산. 시뮬레이션은 기초자산에서 생성 후 일간 리밸런싱을 "
    "재구성해야 함 (변동성 드래그).":
        "A path-dependent asset. Simulation has to be generated on the "
        "underlying and the daily rebalancing reconstructed from it "
        "(volatility drag).",

    "배 레버리지**가 탐지됩니다. 일간 리밸런싱 경로의존 자산이므로 기초자산 "
    "시뮬레이션 후 레버리지를 재구성해야 하며, ETF 수익률에 직접 GBM을 돌리면 "
    "변동성 드래그가 통째로 사라집니다.":
        "× leverage** is detected. This is a daily-rebalanced, "
        "path-dependent asset: the simulation must run on the underlying "
        "and rebuild the leverage. Running GBM directly on the ETF return "
        "erases the volatility drag entirely.",

    "두 상승확률의 차이가 곧 변동성 드래그입니다. ETF 수익률에 직접 GBM을 "
    "돌리면 이 손실이 통째로 사라집니다. 장기 보유를 전제한 분석 자체가 이 "
    "자산군에는 부적절합니다.":
        "The gap between the two up-probabilities is the volatility drag. "
        "Running GBM directly on the ETF return makes that loss disappear. "
        "Any analysis premised on holding this asset class long term is "
        "inappropriate to begin with.",

    "보다 큽니다. 기대수익 기반 목표가는 근거가 약하며, 변동성 배수로 잡는 "
    "편이 정직합니다.":
        ". A price target derived from expected return rests on weak "
        "ground; setting it as a multiple of volatility is more honest.",

    " 아래로만 떨어져도 기대값이 음수가 됩니다.":
        " is all it takes for the expected value to turn negative.",

    "는 팩터로 헤지 가능하고 나머지 ": " can be hedged with factors and the remaining ",
    "헤지로 제거 가능한 분산은 ": "The variance removable by hedging is ",

    "입니다. 조건부 커버리지 검정을 통과한 모델은 ":
        ". The model that passed conditional coverage testing is ",

    "이지만 표준오차가 σ/√T = ": " but the standard error is σ/√T = ",

    " → 통계적으로 0과 구별되지 않으므로 시나리오 목표에 반영하지 않음":
        " → statistically indistinguishable from zero, so it is not "
        "carried into the scenario targets",

    ", OHLC 논리 위반 없음. ": ", no OHLC logic violations. ",
    "로 기대밴드 내이며, 주 노출은 ":
        ", inside the expected band, and the main exposure is ",
    "팩터 R²가 자산군 기대밴드 [":
        "The factor R² against the asset-class expected band [",

    "[드리프트 무의미] SE(μ)=": "[Drift meaningless] SE(μ)=",
    " 확대 적용 (게이트 실패 아님)": " widening applied (not a gate failure)",
    " (하방베타 기준 ": " (on downside beta, ",
    "최신 데이터가 ": "The most recent data is ",
    "강세 시나리오 (": "Bull scenario (",

    # ── chart captions ────────────────────────────────────────
    "■ 정적 충격  ▬ 하방베타 적용":
        "■ Static shock  ▬ With downside beta",
    "Blitz-Huij-Martens — 팩터 노이즈 제거":
        "Blitz-Huij-Martens — factor noise removed",
    "종착 가격 분포": "Terminal price distribution",
    "시뮬레이션 분포": "Simulated distribution",
    "분포 시뮬레이션": "Distribution simulation",
    "국면 타임라인": "Regime timeline",
    "팩터 회귀 계수 + β 안정성":
        "Factor regression coefficients + β stability",
    "표준오차 SE(μ̂)=σ/√T": "Standard error SE(μ̂)=σ/√T",

    # ── section titles ────────────────────────────────────────
    "포지션 사이징": "Position sizing",
    "어닝 이벤트 스터디 · PEAD": "Earnings event study · PEAD",
    "매크로 — 외부 피드 연결 필요":
        "Macro — requires an external feed",
    "크라우딩 · 포지셔닝": "Crowding · positioning",
    "트레이드 구조": "Trade structure",
    "에이전트 심의": "Agent deliberation",
    "성과 · 낙폭": "Performance · drawdown",
    "레버리지 탐지": "Leverage detection",
    "벤치마크 상대 성과": "Performance vs benchmark",
    "공매도 잔고 (float 대비)": "Short interest (as a share of float)",

    # ── expert roles ──────────────────────────────────────────
    "매크로 전략가": "Macro strategist",
    "적대적 검토관": "Adversarial reviewer",
    "체결 총괄": "Head of execution",
    "헤지 설계자": "Hedge architect",

    # ── labels ────────────────────────────────────────────────
    "과적합 갭 ": "Overfit gap ",
    "최대 ": "Max ",
    "단변량": "Univariate",
    "전략 DSR ": "Strategy DSR ",
    "R² 붕괴 경보": "R² collapse alert",
    "P(경로 중 −20% 낙폭)": "P(−20% drawdown along the path)",
    "최장 수중기간 ": "Longest underwater period ",
    "총 헤지 명목 (자산 1단위당)":
        "Total hedge notional (per unit of the asset)",
    "목표 선도달": "Target hit first",
    "명": "",
    "강세 ": "Bull ",
    "스프레드 ": "Spread ",
    "행 수 / 기간": "Rows / period",
    "반증 조건 발동": "Falsifier fired",
    "드리프트 추정치": "Drift estimate",
    "드리프트 μ̂": "Drift μ̂",
    "소프트 50% / 하드 75%": "Soft 50% / hard 75%",
    "bp 또는 ADV 50% 급감": "bp, or ADV halving",
    "원": "",
    "실패": "Fail",
    "시장 베타": "Market beta",
    ", 변동성 ": ", volatility ",
    "헤지비율": "Hedge ratio",
    "레버리지 ": "Leverage ",
    "레버리지/인버스 ETP": "Leveraged / inverse ETP",
    "1% AUM 청산 소요": "Time to liquidate 1% of AUM",
    "헤지 가능": "Hedgeable",
    "영업일 전": "trading days ago",
    "베타 기준": "On beta",
    "거래 가능": "Tradable",
    "강세 극단": "Bull extreme",
    "EDGE 스프레드 · ADV": "EDGE spread · ADV",
    "배": "×",
    "해석": "Reading",
    "신뢰도 ": "Confidence ",
    "수익성": "Profitability",
    "**입니다.": "**.",
    "일)": " days)",
    "일)\n": " days)\n",
    "알파 비중": "Alpha share",
    "기대 지속기간 ": "Expected duration ",
    "엣지 (승률 − 손익분기)": "Edge (hit rate − breakeven)",
    "불확실성 중 파라미터 기여 ":
        "Parameter contribution to uncertainty ",
    "quoteType / 섹터": "quoteType / sector",
    "VaR 95% (종착수익)": "VaR 95% (terminal return)",
    "Jump Model 재적합": "Jump Model refit",
    "왕복비용": "Round-trip cost",
}
