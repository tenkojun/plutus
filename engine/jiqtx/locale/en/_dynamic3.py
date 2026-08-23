# -*- coding: utf-8 -*-
"""
English — dynamic_report, part 3: archetype detail (value trap, dividend,
burn), jumps, duration, leveraged ETP, options surface, panel table headers.
"""

CATALOG = {

    # ── value trap / quality ──────────────────────────────────
    "가치 함정 점검": "Value trap check",
    ": 뚜렷한 함정 신호 없음": ": no clear trap signal",
    "저ROE·저PBR 동시 — P/B가 싼 이유가 ROE일 가능성":
        "Low ROE and low P/B together — the cheapness may simply be the ROE",
    "높은 레버리지": "High leverage",
    "매출 역성장": "Revenue shrinking",
    "부채비율": "Debt ratio",
    "자금조달 여력": "Funding headroom",
    "순이익률": "Net margin",
    "40 이상이 기준": "40 or above is the bar",
    "P/B의 정당성 판단 기준": "The test of whether the P/B is justified",
    "음수면 가치함정 경보": "Negative triggers a value-trap alert",
    "모델 R²": "Model R²",
    "지배 스타일": "Dominant style",
    "순이익률 / 영업이익률": "Net margin / operating margin",
    "매출성장 / 이익성장": "Revenue growth / earnings growth",
    "1.0 미만이면 경보": "Below 1.0 raises an alert",

    # ── dividend ──────────────────────────────────────────────
    "배당수익률": "Dividend yield",
    "배당 커버리지": "Dividend coverage",
    "85% 초과 시 커버리지 취약": "Above 85% the coverage is fragile",
    "FCF 수익률": "FCF yield",
    "배당 지속성의 실질 근거": "The real basis for dividend sustainability",
    "FCF가 배당의 ": "FCF covers the dividend ",
    "⚠ FCF가 배당의 ": "⚠ FCF covers the dividend only ",
    "배 — 커버리지 부족": "× — coverage is insufficient",

    # ── burn / distress ───────────────────────────────────────
    "⚠ 현금 잔여기간 ": "⚠ Cash runway ",
    ". 향후 12개월 내 자금조달 가능성이 높고, 조달 조건이 주가에 직접 "
    "반영됩니다. 이 구간에서는 밸류에이션보다 ":
        ". A raise within twelve months is likely and its terms feed "
        "straight into the share price. In this state the price is driven "
        "less by valuation than by ",
    "조달 창구 접근성": "access to funding",
    "이 주가를 지배합니다.": ".",
    "현금 잔여기간 ": "Cash runway ",
    "년 — 단기 조달 압력은 낮음.":
        " years — little near-term funding pressure.",
    "부실기업의 에쿼티는 사실상 자산에 대한 콜옵션입니다. 정규분포 기반 "
    "통계보다 ":
        "The equity of a distressed company is effectively a call option "
        "on its assets. Rather than statistics built on a normal "
        "distribution, ",
    "자본구조와 만기 스케줄": "the capital structure and maturity schedule",
    "이 주가를 지배하며, 유상증자 희석 리스크가 상시 존재합니다.":
        " drive the price, and dilution risk from an equity raise is "
        "always present.",

    # ── momentum ──────────────────────────────────────────────
    "원시 모멘텀(": "Raw momentum (",
    ")과 잔차 모멘텀(": ") and residual momentum (",
    ")의 괴리가 ": ") differ by ",
    "입니다. 최근 성과의 상당 부분이 ":
        ". A large part of recent performance came from ",
    "종목 고유 요인이 아니라 팩터 노출":
        "factor exposure rather than anything idiosyncratic",
    "에서 왔거나, 그 반대입니다.": ", or the other way round.",

    # ── jumps ─────────────────────────────────────────────────
    "점프의 분산 기여": "Jump contribution to variance",
    "연간 점프 횟수": "Jumps per year",
    "점프 제거 후 변동성": "Volatility with jumps removed",
    "탐지 점프 수 (|r| > 4σₜ)": "Jumps detected (|r| > 4σₜ)",
    "연간 점프 빈도": "Annual jump frequency",
    "최대 상승 점프": "Largest upward jump",
    "최대 하락 점프": "Largest downward jump",
    "점프 비대칭 (하락 우위)": "Jump asymmetry (downside skew)",
    "점프 제거 후 연변동성":
        "Annualised volatility with jumps removed",
    "90분위 (테일 이벤트)": "90th percentile (tail event)",

    # ── crowding / short interest ─────────────────────────────
    " of float — 극단": " of float — extreme",
    "동시 청산 취약성": "Vulnerability to simultaneous liquidation",
    "팩터 헤지 불가 정도": "Degree that cannot be hedged with factors",

    # ── duration ──────────────────────────────────────────────
    "금리 β (1%p 당)": "Rate β (per 1pp)",
    "실효 듀레이션 (근사)": "Effective duration (approximate)",
    "가격 = −듀레이션 × Δ금리 관계에서 역산":
        "Backed out of price = −duration × Δrate",
    "DV01 (1bp 당)": "DV01 (per 1bp)",
    "+100bp 시 손익": "P&L at +100bp",
    "+200bp 시 손익 (볼록성 무시)":
        "P&L at +200bp (ignoring convexity)",

    # ── leveraged ETP ─────────────────────────────────────────
    " ETP는 ": " ETPs are ",
    "일간 리밸런싱": "rebalanced daily",
    "되므로 경로의존적입니다. 기초자산이 제자리로 돌아와도 손실이 남습니다.":
        " and therefore path dependent. The underlying can return to where "
        "it started and you are still down.",
    "탐지 레버리지": "Detected leverage",
    "ETP 연변동성": "ETP annualised volatility",
    "기초자산 추정 변동성": "Estimated volatility of the underlying",
    "이론적 변동성 드래그 (연)": "Theoretical volatility drag (annual)",
    "½·L(L−1)·σ² — 기초자산이 횡보해도 발생":
        "½·L(L−1)·σ² — it accrues even if the underlying goes nowhere",
    "ETP 수익률에 직접 GBM 적용 (틀림)":
        "GBM applied directly to the ETP return (wrong)",
    "경로 재구성 상승확률":
        "Probability of a rise with the path reconstructed",
    "기초자산 경로 → 일간 리밸런싱 재구성 (올바름)":
        "Underlying path → daily rebalancing reconstructed (correct)",
    "시뮬 경로 최대낙폭 중앙값":
        "Median maximum drawdown across simulated paths",

    # ── volatility notes ──────────────────────────────────────
    "⚠ IGARCH 근방(지속성≈1)": "⚠ Near IGARCH (persistence ≈ 1)",
    "반감기 ": "half-life ",
    "평활화 보정": "Smoothing adjustment",
    ": 언스무딩 시 변동성이 ": ": unsmoothed, volatility widens ",
    "배 확대됩니다. 보고된 샤프는 그만큼 과대평가입니다.":
        "×. The reported Sharpe is overstated by the same degree.",
    "를 Harvey-Liu-Zhu 허들(t &gt; 3.0)로 입증하려면 ":
        " needs, to clear the Harvey-Liu-Zhu hurdle (t &gt; 3.0), ",
    "이 필요합니다. 현 표본은 ": ". The current sample is ",

    # ── sizing ────────────────────────────────────────────────
    "정적β": "Static β",
    "최종 비중": "Final weight",
    "구속 제약: ": "Binding constraint: ",
    "참여율": "Participation rate",

    # ── options ───────────────────────────────────────────────
    "기간구조 기울기 (3M−1M)": "Term structure slope (3M − 1M)",
    "IV − RV 스프레드": "IV − RV spread",
    "분산위험프리미엄 프록시": "Variance risk premium proxy",
    "Put/Call OI 비율": "Put/call open interest ratio",
    " — 위험중립 확률에는 리스크 프리미엄이 포함돼 실세계 확률과 다릅니다. "
    "차이의 방향과 크기를 논지로 삼는 것이 올바른 용법입니다.":
        " — risk-neutral probabilities embed a risk premium and differ "
        "from real-world ones. The correct use is to make the direction "
        "and size of the gap your thesis.",
    "백워데이션 → 단기 스트레스": "Backwardation → near-term stress",
    "하방 공포 프리미엄": "Downside fear premium",
    "상방 선호": "Upside preference",
    "모델 상승확률": "Model probability of a rise",
    "시장(위험중립) 상승확률":
        "Market (risk-neutral) probability of a rise",
    "차이": "Difference",
    "모델 / 시장 중앙값": "Model / market median",

    # ── panel table headers ───────────────────────────────────
    "선언된 편향": "Declared bias",
    "열람 범위": "Data visible",
    "대상 주장": "Claim addressed",
    "반론": "Objection",
    "가중치": "Weight",
    "레드팀은 ": "The red team is ",
    "최소 3개의 구체적 반대 증거 제출이 의무":
        "obliged to file at least three concrete pieces of "
        "counter-evidence",
    "입니다. 제출 실패는 시스템 오류로 로깅됩니다.":
        ". Failing to file is logged as a system error.",
    "의미 있음": "Meaningful",
    "무엇인가": "what it is",
    "무엇이 바뀌면 생각을 바꾸는가": "what would change their mind",
    " 확신도 ": " confidence ",
    " — 결정적 반박에 이르지 못해 양측 견해를 병기합니다.":
        " — not a decisive rebuttal, so both views are recorded.",
    "왜 그런가": "why",
    ", 성격은 ": ", and its character is ",

    # ── misc ──────────────────────────────────────────────────
    "섹션 렌더 실패: ": "Section failed to render: ",
    "산출 불가": "Cannot be computed",
    "미상": "Unknown",
    "아니오": "No",
    "축소 ": "shrunk ",
    "주기": "Frequency",
    "이유": "Reason",
    "발생 조건": "Trigger condition",
    "관찰 지표": "Metric watched",
    "년": " years",
    " 년": " years",
    " — 높음": " — high",
}
