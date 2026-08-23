# -*- coding: utf-8 -*-
"""
English — factor names, alpha attribution, execution and liquidity labels.

Ninth high-impact batch.
"""

CATALOG = {

    # ── prose ─────────────────────────────────────────────────
    "이 상태에서는 최소분산 헤지비율도 함께 무효입니다. 헤지비율은 이 회귀 "
    "계수와 동일하기 때문입니다.":
        "In this state the minimum-variance hedge ratio is void as well, "
        "because the hedge ratio is that same regression coefficient.",

    "는 해석 불가능한 잔차 평균이므로, 저는 이 알파를 근거로 한 어떤 주장에도 "
    "동의하지 않습니다.":
        " is an uninterpretable residual mean, so I do not agree with any "
        "claim resting on this alpha.",

    "년 — 자금조달 시계가 분석 구간 안에 들어옵니다. 금리·리스크선호 변화에 "
    "이중으로 민감합니다.":
        " years — the financing clock falls inside the analysis window. "
        "That makes it doubly sensitive to changes in rates and risk "
        "appetite.",

    "입니다. 현재 팩터 세트가 자산군에 맞지 않을 가능성을 먼저 배제해야 "
    "합니다.":
        ". You first have to rule out the possibility that the current "
        "factor set does not fit this asset class.",

    "높은 ROE·안정 마진·낮은 부채. 밸류에이션 프리미엄이 정당화되는지가 핵심.":
        "High ROE, stable margins, low debt. The question is whether the "
        "valuation premium is justified.",

    "과거 베타로 추정한 델타는 이미 틀렸을 수 있음. 재추정 전 신규 진입 금지.":
        "Deltas estimated from the old beta may already be wrong. No new "
        "entry before re-estimation.",

    ". 어느 하나만 인용하면 정반대 결론이 나온다.":
        ". Quote any one of them alone and you reach the opposite "
        "conclusion.",

    "팩터 R²가 ": "The factor R² is ",
    "이 자산은 ": "This asset is ",
    "이며 채택 모델은 ": " and the adopted model is ",
    "를 빼면 기대손익 ": ", net of which the expected P&L is ",
    "확률을 제출한 전문가 ": "Experts who submitted a probability ",
    "장기 알파 비중 ": "Long-run alpha share ",
    "마지막 데이터 ": "Last data point ",
    "최대 노출: ": "Largest exposure: ",
    "입니다(무헤지 ": " (unhedged ",
    "**이며 확률 ": "**, probability ",
    "위험의 ": "of the risk ",
    " 시나리오에서 ": " in the scenario, ",
    " → 사이즈를 ": " → size is ",
    " = 계좌손실 ": " = account loss ",
    "년 → t ≈ ": " years → t ≈ ",
    "; 채택 모델 ": "; adopted model ",
    ", 기대 지속 ": ", expected duration ",
    ", 최장 수중기간 ": ", longest underwater period ",
    ") vs 한도 ": ") vs limit ",
    " · 연율화 √": " · annualised √",
    " · P(목표) ": " · P(target) ",
    " 가정이 ": " assumption is ",
    " (확률 ": " (probability ",
    "가 되면": " is reached",
    "SPY 대비 β=": "β vs SPY = ",
    "행 (": "rows (",
    "영업일 (약 ": " trading days (about ",
    "요구 ": "Required ",
    " 일": " days",

    # ── factor names ──────────────────────────────────────────
    "12-1 잔차 모멘텀": "12-1 residual momentum",
    "12-1 원시 모멘텀": "12-1 raw momentum",
    "10년 기대인플레이션": "10-year breakeven inflation",
    "하이일드 스프레드": "High-yield spread",
    "실질금리 +100bp": "Real rates +100bp",
    "기대인플레 +50bp": "Breakeven inflation +50bp",
    "1/N (동일가중)": "1/N (equal weight)",
    "최적 프록시": "Best proxy",
    "팩터 경제학": "Factor economics",

    # ── expert roles ──────────────────────────────────────────
    "레짐 사관": "Regime historian",

    # ── labels ────────────────────────────────────────────────
    "주식 전용": "Equity only",
    "보수적 채택": "Conservatively adopted",
    "충족": "Met",
    "벤치마크": "Benchmark",
    "년 보유": "-year holding",
    "최악 ": "Worst ",
    "헤지 불가": "Cannot hedge",
    "헤지 레그 수": "Hedge legs",
    "페이오프 비율": "Payoff ratio",
    "측정 불확실성": "Measurement uncertainty",
    "지평 도래 시": "At the horizon",
    "왜도 / 첨도": "Skewness / kurtosis",
    "왕복 거래비용": "Round-trip transaction cost",
    "옵션 히스토리": "Option history",
    "시행횟수 로깅": "Trial count logged",
    "스트레스 예산": "Stress budget",
    "선택 팩터 수": "Factors selected",
    "선택 팩터 ": "Selected factors ",
    "발동 시 조치": "Action if fired",
    "무헤지 변동성": "Unhedged volatility",
    "드라이버 조건": "Driver conditions",
    "고유위험 비중": "Idiosyncratic risk share",
    "t 자유도 ν": "t degrees of freedom ν",
    "1차 자기상관": "First-order autocorrelation",
    "정규": "Normal",
    "임계 ": "Threshold ",
    "이력": "History",
    "기관 보유 비중": "Institutional ownership",
    "총수익": "Total return",
    "손절폭 ": "Stop distance ",
    "부적합": "Unsuitable",
    "진입 불가": "No entry",
    "경보": "Alert",
    "판단보류": "Judgement withheld",
    "주간": "Weekly",
    "조치": "Action",
    "입장": "Position",
    "규칙": "Rule",
    "하방β": "Downside β",
    "기준일": "As of",
    "평활화 의심": "Smoothing suspected",
    "체결 가능성": "Executability",
    "참여 전문가": "Participating experts",
    "진입 참고가": "Reference entry price",
    "적대적 반증": "Adversarial falsification",
    "자산군 배정": "Asset-class assignment",
    "유동성·체결": "Liquidity · execution",
    "유동성 한도": "Liquidity cap",
    "유동성 증발": "Liquidity evaporation",
    "영업일 기준": "In trading days",
    "연환산 알파": "Annualised alpha",
    "알파(잔차)": "Alpha (residual)",
    "알파 유의성": "Alpha significance",
    "순알파(연)": "Net alpha (annual)",
    "불안정 레그": "Unstable leg",
}
