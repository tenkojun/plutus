# -*- coding: utf-8 -*-
"""
English — asset-class specs, thesis triggers, agent notes, book allocation.
"""

CATALOG = {

    # ══ config.py — asset classes ═════════════════════════════
    "중소형 개별주": "Small/mid-cap single name",
    "주식형 ETF": "Equity ETF",
    "섹터 ETF": "Sector ETF",
    "에너지 원자재": "Energy commodities",
    "광의 원자재": "Broad commodities",
    "국채 ETF": "Treasury ETF",
    "투자등급 크레딧": "Investment-grade credit",
    "하이일드": "High yield",
    "물가연동채": "Inflation-linked bonds",
    "리츠": "REITs",
    "암호자산": "Crypto assets",
    "통화": "Currencies",
    "변동성 ETP": "Volatility ETPs",
    "지수(비거래)": "Index (not tradable)",
    "뮤추얼펀드": "Mutual funds",

    "평활화 수익률 언스무딩 필수. 상폐 편향 경고 대상.":
        "Smoothed returns must be unsmoothed. Flag for delisting bias.",
    "ETF≠현물. 콘탱고 롤 손실을 분해하지 않으면 기초자산 프록시로 쓸 수 없음.":
        "The ETF is not the spot. Without decomposing contango roll loss it "
        "cannot be used as a proxy for the underlying.",
    "DV01·KRD를 델타 패널에 반드시 포함.":
        "DV01 and KRD must be in the delta panel.",
    "주식 베타 0.3~0.5 수준. 채권으로 취급하면 리스크를 과소평가함.":
        "Equity beta runs 0.3 to 0.5. Treating it as a bond understates "
        "the risk.",
    "서브섹터(오피스/데이터센터/물류)가 완전히 다름. 단일 REIT 팩터 금지.":
        "The subsectors — office, data centre, logistics — are completely "
        "different. Do not use a single REIT factor.",
    "연율화 √365. √252를 쓰면 변동성이 약 17% 과소평가됨.":
        "Annualise with √365. Using √252 understates volatility by about "
        "17%.",
    "캐리는 crash risk가 본질. 왜도·꼬리의존성 병기 필수.":
        "Carry is crash risk at heart. Skewness and tail dependence must "
        "be shown alongside.",
    "롤 손실이 수익률을 지배. 장기 보유 전제의 분석 자체가 부적절.":
        "Roll loss dominates the return. Any analysis premised on holding "
        "long term is inappropriate.",
    "거래 불가. 참조용만.": "Not tradable. Reference only.",
    "NAV 기준 → 평활화. 샤프 과대 위험, 언스무딩 필요.":
        "Priced on NAV, hence smoothed. Sharpe is overstated; unsmoothing "
        "is required.",
    "분류 불확실 → 최소 사이즈만 허용.":
        "Classification uncertain → allow minimum size only.",

    # ══ thesis.py ═════════════════════════════════════════════
    "알파 미산출 → 0 적용": "Alpha not computed → set to 0",
    ")를 ": ") is ",
    " 축소해 ": " shrunk to ",
    "상시": "Continuous",
    "이벤트 리스크 구간": "Event-risk window",
    "다음 어닝까지": "Until the next earnings",
    "≤ 14영업일": "≤ 14 trading days",
    "발행사 IR": "Issuer IR",
    "IV 기간구조 백워데이션": "IV term structure in backwardation",
    "시장 신호": "Market signal",
    "β 변동계수 (유의 노출)":
        "β coefficient of variation (significant exposures)",
    "유의한 팩터 노출 없음": "No significant factor exposure",
    "헤지 대상 자체가 없음. 위험 통제는 사이즈로만.":
        "There is nothing to hedge. Risk is controlled by size alone.",
    "구조 변화 발생": "Structural change occurred",
    "롤링 R² 급락": "Rolling R² fell sharply",
    "최근 R² < 과거 중앙값의 35%":
        "Recent R² below 35% of its historical median",
    "발표 다음날 |수익률| 90분위 ":
        "90th percentile |return| the day after a release ",
    ". 이벤트 전 사이즈 축소 또는 옵션으로 대체.":
        ". Cut size before the event, or replace it with options.",
    "현재 '": "Currently '",
    "' 이탈": "' exited",
    "어닝 발표 (": "Earnings release (",
    "|수익률| 90분위 ": "90th percentile |return| ",
    "가 발표일에 집중": " concentrated on release days",
    "|수익률| 중앙값 ": "Median |return| ",
    " / 90분위 ": " / 90th percentile ",
    "국면 전환 예상 ('": "Regime shift expected ('",
    "' 이탈)": "' exited)",

    # ══ agents.py ═════════════════════════════════════════════
    "ML 미실행": "ML not run",
    "데이터 무결성 게이트 실패 → 전체 분석 중단.":
        "Data integrity gate failed → the whole analysis halts.",
    "팩터 모델 없음": "No factor model",
    "변동성 표면": "Volatility surface",
    ". 표본 드리프트는 '모른다'와 통계적으로 구별되지 않는다. 원본식 GBM "
    "상승확률 ":
        ". The sample drift is statistically indistinguishable from 'we do "
        "not know'. The original-style GBM probability of a rise is ",
    "[국면 표본 부족] 관측 구간에서 국면 전환이 ":
        "[Too few regime observations] The window contains only ",
    "회뿐. 다른 국면에서의 행태는 검증되지 않았다.":
        " transitions. Behaviour in other regimes is untested.",
    "[이력 부족] ": "[Insufficient history] ",
    "년). 최소 2개 레짐을 포함하지 못했을 가능성이 크다.":
        " years). It most likely does not span at least two regimes.",
    "데이터범위": "Data scope",
    "리스크/유동성 게이트": "Risk / liquidity gate",
    "내용": "Detail",
    "[구조 변화] ": "[Structural change] ",
    "거래 불가: ": "Not tradable: ",
    ". 이는 약세 판단이 아니라 '현 조건에서 포지션을 잡을 수 없다'는 뜻이며, "
    "방향 확률은 별도로 읽어야 한다.":
        ". This is not a bearish call but a statement that no position can "
        "be taken under current conditions; read the directional "
        "probability separately.",
    "확률을 제출한 에이전트가 없음 → 방향 판단 보류.":
        "No agent submitted a probability → the directional call is "
        "withheld.",
    ", 청산 ": ", liquidation ",
    "VaR 미산출": "VaR not computed",
    "반증 근거 미제출 — 시스템 오류":
        "No counter-evidence filed — system error",
    "기간구조 기울기 ": "Term structure slope ",
    " (VRP 프록시)": " (VRP proxy)",
    " → 사후 ": " → posterior ",
    "통합 확률 ": "Pooled probability ",
    " (밴드 ": " (band ",
    "백워데이션": "Backwardation",

    # ══ portfolio.py ══════════════════════════════════════════
    "역변동성": "Inverse volatility",
    "리스크 패리티": "Risk parity",
    "넷팅비율": "Netting ratio",
    "복합: 긴축+강달러": "Composite: tightening + strong dollar",
    "판정 엔진 리스크 예산": "Verdict engine risk budget",
    "사용자 지정": "User specified",
    "팩터 모델이 있는 포지션이 없음":
        "No position has a factor model",
    "워크포워드 구간이 부족해 경합 불가":
        "Not enough walk-forward windows to run the bake-off",
    ") 생존 규칙: ": ") surviving rules: ",
    "1/N이 제외되었으므로 정교한 규칙을 쓸 근거가 있다.":
        "1/N was excluded, so there is a basis for using a more elaborate "
        "rule.",
    "1/N (판정 엔진 사이즈가 전부 0)":
        "1/N (the verdict engine returned size zero for everything)",
    "단일 종목 비중": "Single-name weight",
    "단일 종목 위험기여": "Single-name risk contribution",
    "책 스트레스 손실": "Book stress loss",
    "델타 없음": "No delta",
    "책 순베타": "Book net beta",
    "책 하방베타": "Book downside beta",
    "손익(정적)": "P&L (static)",
    "손익(하방)": "P&L (downside)",
    "공통 관측 ": "Common observations ",
    "일 — 공분산 추정이 불안정할 수 있음":
        " days — the covariance estimate may be unstable",
    "모든 포지션의 사이즈가 0 — 분석 목적으로 1/N 가정":
        "Every position is size zero — 1/N assumed for analysis",
    "최대 팩터 순베타": "Largest factor net beta",
    " 노출은 포지션 간 상쇄가 커서 순노출이 총노출의 ":
        " exposure offsets heavily across positions, leaving the net at ",
    "에 불과하다. 개별 종목마다 헤지를 걸면 이중 집행이 된다 — 책 레벨에서 "
    "한 번만 헤지하라.":
        " of gross. Hedging each name separately would double up — hedge "
        "once at the book level.",
}
