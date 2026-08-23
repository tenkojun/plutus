# -*- coding: utf-8 -*-
"""
English — taxonomy reasons, data warnings, horizons, factors, ledger,
risk notes, report themes.
"""

CATALOG = {

    # ══ taxonomy.py ═══════════════════════════════════════════
    "금 관련이나 주식 설명력이 높음 → 금광주(생산기업)일 가능성. 귀금속 "
    "현물과 팩터 구조가 다름.":
        "Gold-related, but equity factors explain it well → likely a gold "
        "miner rather than the metal. Its factor structure differs from "
        "physical precious metals.",
    "주말 거래 관측 → 24/7 시장. 연율화 √365 적용 (√252 사용 시 변동성 약 ":
        "Weekend trading observed → a 24/7 market. Annualising with √365 "
        "(using √252 would understate volatility by about ",
    " 과소평가)": ")",
    " → 레버리지 ": " → leverage ",
    "x 탐지": "× detected",
    " → 수익률 평활화 의심. 언스무딩 없이 산출한 샤프는 과대평가.":
        " → returns look smoothed. A Sharpe computed without unsmoothing "
        "is overstated.",
    "무거래일 비율 ": "No-trade days ",
    " — 유동성 절벽": " — a liquidity cliff",
    "일 < 요구 ": " days < required ",
    "명칭/카테고리 키워드 → ": "Name and category keywords → ",
    "주식 프록시 설명력이 매우 낮음 — 특수상황/이벤트 자산 가능성":
        "Equity proxies explain very little — possibly a special-situation "
        "or event asset",
    "ETF 카테고리='": "ETF category='",
    "섹터=": "Sector=",
    ", 시총=$": ", market cap=$",

    # ══ data.py ═══════════════════════════════════════════════
    "GPR 지수 수집 실패 — 지정학 팩터는 제외됩니다.":
        "Could not fetch the GPR index — the geopolitical factor is "
        "dropped.",
    "중복 날짜 ": "Duplicate dates ",
    "비양수 가격 ": "Non-positive prices ",
    "|일간수익|>40% ": "|daily return| > 40% ",
    "건 — 분할/배당 조정 오류 가능":
        " — possibly a split or dividend adjustment error",
    "거래일 대비 결측 ": "Missing vs trading days ",
    "15일 이상 데이터 공백 ": "Data gaps of 15 days or more ",
    "pip install yfinance 가 필요합니다.":
        "pip install yfinance is required.",
    ": 가격 데이터를 가져오지 못했습니다.":
        ": could not fetch price data.",
    "Adj Close 누적수익이 Close보다 낮음 (":
        "Adj Close cumulative return is below Close (",
    ") — 조정 오류 의심": ") — adjustment error suspected",
    " 실패: ": " failed: ",
    "프록시 ": "Proxy ",
    ") 실패: ": ") failed: ",

    # ══ horizons.py ═══════════════════════════════════════════
    "데드크로스": "Death cross",
    "확대 — 단기 ": "Expanding — short-term ",
    " 가 장기 ": " is ",
    "배. '보통' 같은 절대 라벨보다 자기 장기 수준 대비 확대됐다는 상대 "
    "비교가 정확하다.":
        "× its long-run level. Comparing against its own long-run level is "
        "more accurate than an absolute label like 'normal'.",
    " — 지평 간 불일치 ": " — horizons disagree ",
    ". 하나의 '추세'로 요약할 수 없다.":
        ". This cannot be summarised as a single trend.",
    "축소 — 단기 ": "Contracting — short-term ",
    "배. 조용한 국면이지만 평균 회귀에 유의.":
        "×. A quiet regime, but watch for mean reversion.",
    "배).": "×).",
    "추세 방향이 지평마다 다르다 — ":
        "The trend direction differs by horizon — ",
    " 로 크게 다르다 — 구조 변화 가능성.":
        " — a large gap, suggesting structural change.",
    "시장 베타가 지평 간 ": "Market beta differs across horizons by ",

    # ══ factors.py ════════════════════════════════════════════
    "명목10년 +100bp": "Nominal 10-year +100bp",
    "지정학위험 +1σ": "Geopolitical risk +1σ",
    "커브 +100bp": "Curve +100bp",
    "표본 부족 또는 팩터 없음": "Not enough sample, or no factors",
    "는 '고유위험'이 아니라 '누락 변수'로 해석해야 하며, 알파 추정치는 무효.":
        " should be read as an omitted variable, not as idiosyncratic "
        "risk, and the alpha estimate is void.",
    "최근 R² ": "Recent R² ",
    " vs 과거 중앙값 ": " vs historical median ",
    " → 구조 변화 경보. 팩터 관계가 붕괴 중일 수 있음. 정적 베타 사용 금지.":
        " → structural-change alert. The factor relationship may be "
        "breaking down. Do not use a static beta.",
    "연 ": "",
    "% 의 구조적 롤 ": "% structural roll per year, ",
    " 추정": " (estimated)",
    " 가 밴드 상단 초과 → 사실상 프록시 복제 관계. 독립적 알파 원천으로 보기 "
    "어려움.":
        " exceeds the top of the band → effectively a replication of the "
        "proxy. Hard to treat as an independent source of alpha.",
    "이익": "Earnings",

    # ══ ledger.py ═════════════════════════════════════════════
    "등급별 실현수익": "Realised return by grade",
    "평균수익": "Mean return",
    "등급": "Grade",
    "모델신뢰도": "Model confidence",
    "ML판정": "ML verdict",
    "확률제출": "Probability submitted",
    "방향적중": "Direction correct",
    "확신주장수": "Confident claims",
    "확신주장 적중": "Confident claims correct",
    "평균제출확률": "Mean submitted probability",

    # ══ risk.py ═══════════════════════════════════════════════
    "VaR은 최대손실이 아니라 하위 ":
        "VaR is not the maximum loss but the lower ",
    "% 경계값이다. ES(조건부 기대손실)를 함께 보라.":
        "% boundary. Read it together with ES (conditional expected "
        "shortfall).",
    " ⚠ 모든 VaR 모델이 커버리지 검정을 통과하지 못함.":
        " ⚠ No VaR model passed its coverage test.",
    "회복 패턴 정상 범위": "Recovery pattern within normal range",
    "스트레스 손익은 선형 델타 근사이며 역사적 재현값도 손실 상한도 아니다. "
    "비선형 반응(유동성 확보 매도 후 안전자산 반등 등)은 포함되지 않는다. "
    "복합 시나리오는 부분(다변량) 베타로 계산한다 — 단변량 베타를 더하면 같은 "
    "시장 충격을 여러 번 세게 된다.":
        "Stress P&L is a linear delta approximation — neither a historical "
        "replay nor an upper bound on loss. Non-linear responses (a "
        "liquidity-driven selloff followed by a safe-haven rebound, for "
        "instance) are excluded. Composite scenarios use partial "
        "(multivariate) betas: adding univariate betas would count the "
        "same market shock several times.",
    "켈리 상한": "Kelly cap",
    "). 원본 리포트의 '하프켈리 200%'는 첫 번째 값을 쓴 결과다.":
        "). The original report's 'half-Kelly 200%' came from using the "
        "first value.",
    "단변량(부분베타 없음)": "Univariate (no partial beta)",
    "델타 패널 없음 → 스트레스 산출 불가":
        "No delta panel → stress cannot be computed",

    # ══ report_theme.py ═══════════════════════════════════════
    "다크": "Dark",
    "기본 — 화면에서 오래 보기 좋다":
        "Default — easy on the eyes for long sessions",
    "라이트": "Light",
    "밝은 배경 — 인쇄·공유에 적합":
        "Light background — good for printing and sharing",
    "세피아": "Sepia",
    "눈부심이 적은 종이 느낌": "Paper-like, less glare",
    "고대비": "High contrast",
    "저시력·프로젝터용 강한 대비":
        "Strong contrast for low vision and projectors",
}
