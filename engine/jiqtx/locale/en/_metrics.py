# -*- coding: utf-8 -*-
"""
English — metric labels, chart captions, sizing ladder, panel roles.

Fifth high-impact batch.
"""

CATALOG = {

    # ── chart and block captions ──────────────────────────────
    "낙폭 (수중 곡선)": "Drawdown (underwater curve)",
    "하락 충격이 변동성을 더 키우는 정도":
        "How much more a downside shock raises volatility",
    "연 헤지 비용 (분기 리밸런싱 가정)":
        "Annual hedge cost (assuming quarterly rebalancing)",
    "드리프트 고정 + 정규 (원본 방식)":
        "Fixed drift + normal (the original approach)",
    "  →  성장최적(불확실성·팻테일 반영) ":
        "  →  growth optimal (with uncertainty and fat tails) ",
    "단순 켈리 μ/σ²": "Naive Kelly μ/σ²",
    "HAR 예측 (Corsi 2009)": "HAR forecast (Corsi 2009)",
    "GJR-GARCH(1,1)-t 현재": "GJR-GARCH(1,1)-t current",
    "EDGE 스프레드 + 제곱근 임팩트": "EDGE spread + square-root impact",
    "■ 경험적 확률   ■ 모델 분포 확률":
        "■ Empirical probability   ■ Model distribution probability",
    "점프 페널티 λ=": "Jump penalty λ=",
    "수익률 시계열 + GARCH 잔차": "Return series + GARCH residuals",
    "원시 OHLCV + 배당/분할 이벤트만":
        "Raw OHLCV and dividend/split events only",

    # ── section titles ────────────────────────────────────────
    "투자 논지": "Investment thesis",
    "수익 귀인": "Return attribution",
    "헤지 후 위험 구성": "Risk composition after hedging",
    "스타일 로딩 · 고유위험": "Style loadings · idiosyncratic risk",
    "현금소진 · 런웨이 · 희석": "Cash burn · runway · dilution",
    "거시경제 대시보드": "Macro dashboard",
    "모니터링과 이 분석이 못 하는 것":
        "Monitoring, and what this analysis cannot do",
    "이 자산이 무엇이고 지금 어떤 결론인가":
        "What this asset is, and what the conclusion is now",
    "반대신문": "Cross-examination",

    # ── prose ─────────────────────────────────────────────────
    "모든 유의 팩터에서 순노출 ≈ 총노출이다. 즉 포지션들이 같은 방향으로 같은 "
    "팩터에 노출돼 있고 **상쇄가 전혀 없다**. 종목 수가 늘어도 이것은 분산이 "
    "아니라 동일 베팅의 레버리지다. 진짜 분산을 원하면 팩터 노출이 반대인 "
    "자산을 넣거나 책 레벨에서 헤지하라.":
        "On every significant factor the net exposure equals the gross. "
        "The positions all lean the same way on the same factors and "
        "**nothing offsets anything**. Adding more names does not "
        "diversify that — it leverages the same bet. For real "
        "diversification, add assets with opposite factor exposure or "
        "hedge at the book level.",

    "드리프트 추정오차가 추정치 자체보다 큼 — 방향 신호로 사용 불가":
        "The drift estimation error exceeds the estimate itself — "
        "unusable as a directional signal",

    "]가 50%를 포함 → 방향 우위 미확인. 신규 진입 근거 없음.":
        "] includes 50% → no directional edge established. No basis for a "
        "new entry.",

    "] 밖으로 나가면 분류를 재검토합니다.":
        "], I revisit the classification.",

    "로 확대됩니다. 즉 이 자산은 매크로 악화 국면에서 **비대칭적으로 더 "
    "맞습니다**. 정적 베타 스트레스는 이를 놓칩니다.":
        ". In other words this asset is hit **asymmetrically harder** when "
        "macro conditions deteriorate. Static-beta stress testing misses "
        "that.",

    "는 시장이 아니라 가정에 대한 진술이다.":
        " is a statement about assumptions, not about the market.",

    "70% 초과면 팩터로 설명 불가 — 종목 고유 리스크가 지배":
        "Above 70% the factors cannot explain it — idiosyncratic risk "
        "dominates",

    "유동성 증발은 청산 국면에만 드러남":
        "Liquidity evaporation only shows up when you try to get out",

    "시스템이 자기 예측력을 스스로 채점":
        "The system scores its own predictive power",

    "손익의 최대 단일 기여 요인은 **":
        "The largest single contributor to P&L is **",

    "방향 예측 모듈의 원시 출력(OOS ":
        "Raw output of the direction forecast module (OOS ",

    "예측력은 표본외에서만 존재를 인정한다.":
        "Predictive power is only granted existence out of sample.",

    "상위 드라이버가 금리·달러면 직접 충격":
        "When the leading drivers are rates and the dollar, the shock is "
        "direct",

    "수익률 지문 기준 이 자산은 **":
        "By its return fingerprint this asset is **",

    "에이전트 간 확률 산포 ": "Probability dispersion across agents ",

    ".\n이 자산에 해당하지 않아 생략: ":
        ".\nOmitted as not applicable to this asset: ",

    " — 기대밴드 [": " — expected band [",
    ")입니다.": ").",

    # ── metric labels ─────────────────────────────────────────
    "사이즈 ": "Size ",
    "판정 ": "Verdict ",
    "연변동성": "Annualised volatility",
    "자산군 기대밴드": "Asset-class expected band",
    "하방에서 베타 확대 (비대칭 노출)":
        "Beta widens to the downside (asymmetric exposure)",
    "드리프트 추정오차 허용 범위": "Tolerated drift estimation error",
    "비중": "Weight",
    "파라미터 무지": "Parameter ignorance",
    "무거래일 비율": "Share of no-trade days",
    "기대 지속기간": "Expected duration",
    "OOS 정확도": "OOS accuracy",
    "알파 ": "Alpha ",
    "0과 구별 불가": "Indistinguishable from zero",
    "드리프트 표준오차": "Drift standard error",
    "드리프트 추정 무의미": "Drift estimate is meaningless",
    "1% AUM 청산": "Liquidating 1% of AUM",
    "회": " trials",
    "진입": "Entry",
    "지표": "Metric",
    "체결 가정": "Fill assumption",
    "약세 극단(테일)": "Bear extreme (tail)",
    "약세 시나리오": "Bear scenario",
    "게이트 실패 아님": "Not a gate failure",
    "한도": "Limit",
    " 초과": " exceeded",
    "손익분기 승률": "Breakeven hit rate",
    "단기": "Short term",
    "임계": "Threshold",
    "샤프 ": "Sharpe ",
    "정상": "Normal",
    "승률": "Hit rate",
    "발동": "Fired",
    "하드 게이트": "Hard gate",
    "표본내 통계": "In-sample statistics",
    "표본외 통계 검정": "Out-of-sample statistical tests",
    "β안정성CV": "β stability CV",
    "스트레스 한도": "Stress limit",
    "스트레스 최악": "Worst-case stress",
    "리스크 책임자": "Head of risk",
    "포트폴리오 매니저": "Portfolio manager",
    "헤지 비율 불안정": "Hedge ratio unstable",
    "표준 충격당 손익": "P&L per standard shock",
    "팩터 모델 적합성": "Factor model goodness of fit",
    "영업일 대비 결측": "Missing vs trading days",
    "상관(전체→하방)": "Correlation (overall → downside)",
    "방향 엣지 미확인": "No directional edge established",
}
