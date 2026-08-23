# -*- coding: utf-8 -*-
"""
English — macro board, hedging caveats, calibration ledger, table headers.

Eighth high-impact batch.
"""

CATALOG = {

    # ── prose ─────────────────────────────────────────────────
    "|t| &lt; 2 인 변수는 이 그림에서 뺐습니다. 유의하지 않은 베타로 그림을 "
    "그리면 없던 이야기가 생깁니다.":
        "Variables with |t| &lt; 2 are left out of this chart. Drawing a "
        "picture from an insignificant beta invents a story that is not "
        "there.",

    "이 조건들이 동반될 때 거시 역풍이 지지로 바뀝니다. 각각은 아래 표의 베타 "
    "부호에서 유도된 방향입니다.":
        "When these conditions come together the macro headwind turns into "
        "support. Each direction is derived from the sign of the beta in "
        "the table below.",

    "해당 팩터의 롤링 R²가 최근 붕괴했습니다. 과거 계수로 만든 헤지비율은 "
    "이미 틀렸을 가능성이 큽니다.":
        "That factor's rolling R² has collapsed recently. A hedge ratio "
        "built from the old coefficients is most likely already wrong.",

    "팩터 R²가 자산군 기대밴드를 밑돎. 최소분산 헤지비율은 이 회귀 계수와 "
    "동일하므로 헤지도 함께 무효다.":
        "The factor R² is below the asset-class expected band. The "
        "minimum-variance hedge ratio is that same regression coefficient, "
        "so the hedge is void with it.",

    ". 헤지비율이 불안정하면 헤지가 위험을 **추가**할 수 있으므로 해당 레그는 "
    "집행하지 않는 편이 낫습니다.":
        ". An unstable hedge ratio can **add** risk rather than remove it, "
        "so it is better not to execute that leg.",

    ". 인컴주는 금리 상승 시 채권 대체재로서의 상대 매력이 떨어져 "
    "디레이팅됩니다. 아래 금리 델타를 함께 보십시오.":
        ". As rates rise, an income name loses relative appeal as a bond "
        "substitute and de-rates. Read the rate deltas below alongside "
        "this.",

    "로 이 자산을 설명하지 못합니다. 드리프트에 섞인 알파는 누락 변수의 "
    "잔차이며, 이를 미래로 연장할 근거가 없습니다.":
        " does not explain this asset. The alpha mixed into the drift is "
        "the residual of an omitted variable, and there is no basis for "
        "extending it into the future.",

    "**1/N이 생존했다 → 통계적으로 구별되지 않으므로 1/N을 쓴다.** 정교한 "
    "최적화의 이점이 표본에서 확인되지 않았다.":
        "**1/N survived → it is statistically indistinguishable, so use "
        "1/N.** The sample shows no benefit from the more elaborate "
        "optimisation.",

    "를 차지 — 이벤트 드리븐 성격. 평균·표준편차 기반 통계(샤프, 정규 VaR)는 "
    "대부분 무의미하다.":
        " — an event-driven profile. Statistics built on means and "
        "standard deviations (Sharpe, normal VaR) are largely meaningless "
        "here.",

    "판정 엔진이 사이즈 0을 냈으므로 트레이드 계획은 참고용":
        "The verdict engine returned size zero, so the trade plan is for "
        "reference only",

    "최근 3개월 거시 기여도 (유의한 변수만 · 베타 × 변화)":
        "Macro contribution over the last three months (significant "
        "variables only · beta × change)",

    "현재 미통과 항목: ": "Currently failing: ",
    "무효화된 모듈: ": "Invalidated modules: ",
    "입니다. 손익분기 승률이 ": ". The breakeven hit rate is ",
    "입니다. 과거 최대낙폭 ": ". The historical maximum drawdown of ",
    "드리프트 추정치는 ": "The drift estimate is ",
    "이고 잔차 변동성은 ": " and the residual volatility is ",
    "가 하방 꼬리에서 ": " in the lower tail is ",
    "가 관측됐습니다.": " was observed.",
    "현재 국면은 **": "The current regime is **",
    "의 결론 (확신도 ": "'s conclusion (confidence ",
    "로 축소해야 함": " and should be shrunk",
    "R²가 밴드 하단(": "R² against the band floor (",
    "OHLC 논리 위반 ": "OHLC logic violations ",
    ", 1%AUM 청산 ": ", liquidating 1% of AUM ",
    " · 관측 구간 전환 ": " · observed transitions ",
    " vs 원본식 GBM ": " vs original-style GBM ",
    ". OOS 정확도 ": ". OOS accuracy ",
    ", 기대 지속기간 ": ", expected duration ",
    " — 구속 제약: ": " — binding constraint: ",
    " (시행 ": " (trials ",
    " (신뢰도 ": " (confidence ",
    "영업일(": " trading days (",
    "영업일(약 ": " trading days (about ",
    "약 ": "about ",
    "기저율 ": "Base rate ",

    # ── chart legends ─────────────────────────────────────────
    "■ 팩터(헤지가능) ": "■ Factor (hedgeable) ",
    "   ■ 고유(헤지불가) ": "   ■ Idiosyncratic (unhedgeable) ",

    # ── section titles ────────────────────────────────────────
    "운영·한계": "Operations & limits",
    "손실 측정과 사이징": "Measuring loss and sizing",
    "캘리브레이션 원장": "Calibration ledger",
    "미해결 쟁점": "Unresolved disputes",
    "경제적 메커니즘": "Economic mechanism",

    # ── expert roles ──────────────────────────────────────────
    "파생 스트럭처러": "Derivatives structurer",

    # ── labels ────────────────────────────────────────────────
    "이력 충족": "Track record met",
    "시장 국면": "Market regime",
    "기대 지속 ": "Expected duration ",
    "국면 확률": "Regime probability",
    "β 안정성": "β stability",
    "Δ(하방)": "Δ (downside)",
    "사후 드리프트": "Posterior drift",
    "현재 변동성 백분위": "Current volatility percentile",
    "하방베타 확대 여부": "Whether downside beta widens",
    "표본 드리프트 μ̂": "Sample drift μ̂",
    "파라미터 무지 기여": "Contribution of parameter ignorance",
    "최악 시나리오 손실": "Worst-case scenario loss",
    "제거되는 분산 비중": "Share of variance removed",
    "자산군 분류 신뢰도": "Asset-class classification confidence",
    "옵션 체인 스냅샷만": "Option chain snapshot only",
    "손절 시 계좌 손실": "Account loss if stopped out",
    "세금·환율·추적오차": "Tax · FX · tracking error",
    "왕복비용 ": "Round-trip cost ",
    "기저율": "Base rate",
    "표준오차 σ/√T": "Standard error σ/√T",
    "최대 매크로 노출": "Largest macro exposure",
    "최근 21일 실현": "Realised over the last 21 days",
    "자산군 고유 요인": "Asset-class-specific factors",
    "사이즈 × 손절폭": "Size × stop distance",
    "레버리지 효과 γ": "Leverage effect γ",
    "VaR 채택 모델": "VaR model adopted",
    "VIX 변동성지수": "VIX volatility index",
    "P(목표 선도달)": "P(target hit first)",
    "ML 과적합·보정": "ML overfit / calibration",
    "GPD 꼬리 적합": "GPD tail fit",
    "ADV (중앙값)": "ADV (median)",
    "90% 시뮬 구간": "90% simulated interval",
    "위반": "Breach",
    "제거 ": "Removed ",
    "영향": "Impact",
    "기준 ": "Basis ",
    "모델확률": "Model probability",
    "로그오즈": "Log odds",
    "광의 달러지수": "Broad dollar index",
    "헤지 후 순노출": "Net exposure after hedging",
    "펀더멘털 PIT": "Fundamentals point-in-time",
    "지평 내 미도달": "Not reached within the horizon",
    "정상 국면 상관 ": "Correlation in the normal regime ",
    "작을수록 팻테일": "Lower means fatter tails",
    "알파 해석 허용": "Alpha interpretation permitted",
    "변동성의 변동성": "Volatility of volatility",
    "롤링 팩터 R²": "Rolling factor R²",
    "관측 전환 횟수": "Observed transitions",
    "거래 비용 초과": "Transaction cost exceeded",
    "거래 가능 판정": "Tradability verdict",
    "95% 신뢰구간": "95% confidence interval",
    "10년 실질금리": "10-year real yield",
}
