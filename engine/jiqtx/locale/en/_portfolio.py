# -*- coding: utf-8 -*-
"""
English — portfolio, archetype notes, dilution/runway, table headers.

Tenth high-impact batch.
"""

CATALOG = {

    # ── prose ─────────────────────────────────────────────────
    "위험기여 엔트로피 기반. 종목 수보다 훨씬 작으면 실제로는 소수 베팅":
        "Based on the entropy of risk contributions. Far below the number "
        "of holdings means it is really only a handful of bets",

    "가중평균 개별변동성 / 책 변동성. 1에 가까우면 분산 효과 없음":
        "Weighted average single-name volatility divided by book "
        "volatility. Near 1 means no diversification benefit",

    "점프가 수익률을 지배. 평균·표준편차 기반 통계가 대부분 무의미.":
        "Jumps dominate the return. Statistics built on means and standard "
        "deviations are largely meaningless.",

    "PER 무의미. 매출성장·현금소진·희석·자금조달 접근성이 핵심.":
        "P/E is meaningless here. What matters is revenue growth, cash "
        "burn, dilution and access to funding.",

    "총수익의 상당부분이 배당. 커버리지와 금리 민감도가 핵심.":
        "A large part of total return is the dividend. Coverage and rate "
        "sensitivity are what matter.",

    "배당수익률 4% 초과 — 인컴 렌즈가 섹터 특성보다 지배적":
        "Dividend yield above 4% — the income lens dominates the sector "
        "characteristics",

    "책 레벨 선형 델타 근사. 비선형·유동성 연쇄는 미포함.":
        "A book-level linear delta approximation. Non-linear effects and "
        "liquidity cascades are excluded.",

    ")은 결정적 반박에 이르지 못합니다. 양측 견해를 병기합니다.":
        ") does not amount to a decisive rebuttal. Both views are recorded.",

    "건이 발동되어 신규 진입은 불가합니다. ":
        " have fired, so no new entry is possible. ",

    "샤프 부호가 지평 간 뒤집힌다 — ":
        "The sign of the Sharpe flips across horizons — ",

    ")와 함께 읽으십시오.": ") alongside this.",
    " 가 자산군 기대밴드 [": " against the asset-class expected band [",
    "명의 견해 산포가 ": " experts, with a dispersion of ",
    "이므로 엣지는 ": ", so the edge is ",
    "이고, 왕복비용 ": ", and the round-trip cost is ",
    "로 잡았습니다.": ".",
    "가 추정치 ": " against the estimate of ",
    "의 신뢰구간 [": "'s confidence interval [",
    ")이 손익분기(": ") against breakeven (",
    "판정: ": "Verdict: ",
    "평상 — 단기 ": "Normal — short ",
    "[팩터 대체] R²=": "[Factor substitution] R²=",
    "알파 t=": "Alpha t=",
    ", 조정정합 ": ", adjustment consistency ",
    ", 무거래일 ": ", no-trade days ",
    ", 과적합갭 ": ", overfit gap ",
    ", 손절 ": ", stop ",
    ", 손절 선도달 ": ", stop hit first ",
    "), 결측 ": "), missing ",
    "행, 결측 ": " rows, missing ",
    " (승자 모델 ": " (winning model ",
    " · 장기 ": " · long ",
    " × 사이즈 ": " × size ",
    " 대비 β=": " β = ",
    " · 기준일 ": " · as of ",
    " (통합확률 ": " (pooled probability ",
    " 의 ": "'s ",
    " 이탈": " breach",
    " 적용": " applied",
    "]입니다.": "].",
    "이력 ": "History ",
    "회\n": " trials\n",
    "기관 보유 ": "Institutional ownership ",
    "스프레드가 ": "The spread is ",
    "유효 라벨 ": "Effective labels ",
    "헤지 레그 ": "Hedge leg ",

    # ── chart and table captions ──────────────────────────────
    "자기 이력 대비 현재 위치": "Where it sits against its own history",
    "워크포워드 샤프 (비용 차감 후)":
        "Walk-forward Sharpe (after costs)",
    "충격별 책 손익 (보수적 채택)":
        "Book P&L by shock (conservative choice)",
    "증자로 메울 경우의 최소 희석률":
        "Minimum dilution if funded by an equity raise",
    "현금 잔여기간 (runway)": "Cash runway",
    "연간 희석 압력 (소진/시총)":
        "Annual dilution pressure (burn / market cap)",
    "레짐 조건부 베타 재추정 필요":
        "Regime-conditional betas need re-estimating",
    "20% 초과 시 스퀴즈 리스크": "Above 20% there is squeeze risk",
    "분산 분해": "Variance decomposition",

    # ── labels ────────────────────────────────────────────────
    "변동성 타깃": "Volatility target",
    "리스크 한도": "Risk limit",
    "공매도 잔고 ": "Short interest ",
    "거래 가능성": "Tradability",
    "SMA기울기": "SMA slope",
    "순노출": "Net exposure",
    "총노출": "Gross exposure",
    "고변동": "High volatility",
    "저변동": "Low volatility",
    "고유변동성 (연)": "Idiosyncratic volatility (annual)",
    "HRP (계층적)": "HRP (hierarchical)",
    "히스토리컬": "Historical",
    "확인 대상": "To verify",
    "헤지 수단": "Hedge instrument",
    "하방 기여": "Downside contribution",
    "상방 기여": "Upside contribution",
    "팩터 델타": "Factor delta",
    "팩터 기여": "Factor contribution",
    "총수익 (": "Total return (",
    "진입 보류": "Entry on hold",
    "진입 조건 충족": "Entry conditions met",
    "조건부 p": "Conditional p",
    "독립성 p": "Independence p",
    "전략 샤프": "Strategy Sharpe",
    "장기 평균": "Long-run average",
    "입장 분포": "Distribution of positions",
    "임계/기준": "Threshold / basis",
    "인트라데이": "Intraday",
    "예측 채점": "Forecast scoring",
    "예상 영향": "Expected impact",
    "분포 예측": "Distribution forecast",
    "보유 지평": "Holding horizon",
    "국면 식별": "Regime identification",
    "거시 경로": "Macro path",
    "β(현재)": "β (current)",
    "3M 변화": "3M change",
    "1M 변화": "1M change",
    "목표가": "Price target",
    "수익성(RMW)": "Profitability (RMW)",
    "모멘텀(UMD)": "Momentum (UMD)",
    "고유(특이) 분": "Idiosyncratic share",
    "희석": "Dilution",
    "시점": "Point in time",
    "상태": "Status",
    "미해결": "Unresolved",
    "귀금속": "Precious metals",
}
