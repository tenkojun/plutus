# -*- coding: utf-8 -*-
"""
English — equity archetypes, their valuation anchors and risk flags.
"""

CATALOG = {

    # ── archetype names ───────────────────────────────────────
    "우량 복리성장주": "Quality compounder",
    "고성장 적자기업": "High-growth, loss-making",
    "딥밸류": "Deep value",
    "배당 인컴주": "Dividend income",
    "경기민감주": "Cyclical",
    "경기방어주": "Defensive",
    "고베타 투기적": "High-beta speculative",
    "이벤트 드리븐": "Event driven",
    "부실/턴어라운드": "Distressed / turnaround",
    "미분류": "Unclassified",

    # ── archetype descriptions ────────────────────────────────
    "저PBR·저PER. 핵심은 '싸다'가 아니라 '가치 함정인가'.":
        "Low P/B and low P/E. The question is not whether it is cheap but "
        "whether it is a value trap.",
    "사이클 위치가 밸류에이션보다 중요. 고점 PER이 저점 신호일 수 있음.":
        "Where you are in the cycle matters more than the valuation. A "
        "peak P/E can be a bottom signal.",
    "낮은 베타·안정 현금흐름. 금리와 상대 밸류에이션이 주 변수.":
        "Low beta, stable cash flow. Rates and relative valuation are the "
        "main variables.",
    "높은 베타·높은 고유변동성. 포지션 사이징이 분석보다 중요.":
        "High beta, high idiosyncratic volatility. Position sizing matters "
        "more than the analysis.",
    "자본구조가 주가를 지배. 에쿼티는 사실상 콜옵션.":
        "The capital structure drives the price. The equity is effectively "
        "a call option.",
    "펀더멘털 데이터 부족 또는 특성이 뚜렷하지 않음.":
        "Not enough fundamental data, or no distinct character.",

    # ── valuation anchors / risk flags ────────────────────────
    "재투자율 × ROIC": "Reinvestment rate × ROIC",
    "멀티플 축소 리스크": "Multiple compression risk",
    "성장 둔화 시 디레이팅 폭":
        "How far it de-rates if growth slows",
    "현금소진 잔여기간(runway)": "Cash runway",
    "금리 상승 시 듀레이션 리스크 극대":
        "Duration risk peaks when rates rise",
    "자금조달 창구 폐쇄": "Funding window closing",
    "청산가치": "Liquidation value",
    "가치 함정(구조적 쇠퇴)": "Value trap (structural decline)",
    "부채 만기": "Debt maturities",
    "실적 하향 지속": "Continued earnings downgrades",
    "배당 성장률": "Dividend growth rate",
    "금리 상승 시 채권 대체재로서 매력 하락":
        "Loses appeal as a bond substitute when rates rise",
    "배당 삭감": "Dividend cut",
    "정상화 이익(normalized EPS)": "Normalised EPS",
    "사이클 조정 PER": "Cycle-adjusted P/E",
    "마진 레버리지(양방향)": "Margin leverage (both ways)",
    "재고 사이클": "Inventory cycle",
    "고점 실적 함정": "Peak-earnings trap",
    "배당수익률 vs 국채": "Dividend yield vs treasuries",
    "안정 마진": "Stable margins",
    "금리 상승 시 상대 매력 하락":
        "Relative appeal falls as rates rise",
    "저성장 디레이팅": "De-rating on low growth",
    "없음 — 밸류에이션 앵커 부재": "None — no valuation anchor",
    "급락 시 갭 리스크": "Gap risk in a sharp fall",
    "숏스퀴즈/크라우딩": "Short squeeze / crowding",
    "이벤트 확률 × 페이오프": "Event probability × payoff",
    "단일 이벤트 집중 리스크":
        "Concentration risk in a single event",
    "정규분포 가정 전면 붕괴":
        "The normality assumption breaks down entirely",
    "순부채/EBITDA": "Net debt / EBITDA",
    "이자보상배율": "Interest coverage",
    "만기 스케줄": "Maturity schedule",
    "유상증자 희석": "Dilution from an equity raise",
    "채무 재조정": "Debt restructuring",
    "분류 불확실 → 최소 사이즈":
        "Classification uncertain → minimum size",
    "표본 부족": "Not enough sample",

    # ── factor short names ────────────────────────────────────
    "소형": "Size",
    "가치": "Value",
    "보수적투자": "Investment",

    # ── classification reasons ────────────────────────────────
    "점프가 총 분산의 ": "Jumps account for ",
    "점프가 분산의 ": "Jumps account for ",
    " — 이벤트 지배": " of variance — event driven",
    "점프 기여 ": "Jump contribution ",
    " — 꼬리 모델링 필수.": " — tail modelling is mandatory.",
    " — 연속 확산이 지배.": " — continuous diffusion dominates.",
    "고유변동성 비중 ": "Idiosyncratic volatility share ",
    " — 팩터로 설명 안 됨": " — not explained by factors",
    "연변동성 ": "Annualised volatility ",
    " — 투기적 구간": " — speculative territory",
    "순이익률 ": "Net margin ",
    " — 적자": " — loss making",
    " — 고수익성": " — highly profitable",
    "순현금이 시총의 ": "Net cash is ",
    "배당수익률 ": "Dividend yield ",
    "공매도잔고 ": "Short interest ",
    " of float — 스퀴즈 리스크": " of float — squeeze risk",
    "최고 점수 ": "Top score ",
    " < 임계 ": " < threshold ",
    " (펀더멘털 부족으로 임계 상향)":
        " (threshold raised for lack of fundamentals)",
    "시장 β=": "Market β=",
    " — 고베타": " — high beta",
    " — 저베타": " — low beta",
    "매출성장 ": "Revenue growth ",
    " — 고성장 적자": " — high growth, loss making",
    ", 순이익률 ": ", net margin ",
    "부채비율 ": "Debt ratio ",
    "% — 레버리지 높음": "% — highly levered",
    " — 커버리지 취약": " — coverage is fragile",
    " — 딥밸류 영역": " — deep value territory",
    "섹터 '": "Sector '",
    "' — 경기민감": "' — cyclical",
    "' — 방어적": "' — defensive",
    "펀더멘털 필드 ": "Only ",
    "개만 확보 — 아키타입 판정 신뢰도 저하":
        " fundamental fields available — archetype confidence reduced",

    # ── event study ───────────────────────────────────────────
    "일 뒤 어닝 — 이벤트 리스크 구간. 과거 발표 다음날 |수익률| 중앙값 ":
        " days to earnings — an event-risk window. Historically the median "
        "|return| the day after a release is ",
    ", 90분위 ": ", 90th percentile ",
    "연 분산의 ": "",
    "가 어닝 4일에 집중 — 평상시 변동성으로 리스크를 재면 심각히 과소평가":
        " of annual variance sits in four earnings days — measuring risk "
        "with everyday volatility understates it badly",
    "PEAD 스프레드 ": "PEAD spread ",
    ") — 발표 후 드리프트 존재 가능":
        ") — post-announcement drift may be present",
    "특이사항 없음": "Nothing notable",
    "어닝 이벤트 스터디 실패: ": "Earnings event study failed: ",
}
