# -*- coding: utf-8 -*-
"""
English — section titles, expert profiles, retraction conditions, labels.

Second high-impact batch. Same exclusion as ``_panel``: bare particles are
not keys.
"""

CATALOG = {

    # ── expert profiles (panel bios) ──────────────────────────
    "품질에 대해 보수적. 의심스러우면 중단시킨다 — 거짓 음성보다 거짓 양성이 "
    "훨씬 비싸다고 본다.":
        "Conservative about quality. Halts when in doubt — holds that a "
        "false positive costs far more than a false negative.",

    "구조적으로 반대편에 선다. 모든 신호를 죽일 위험이 있으므로 반론에도 "
    "통계적 근거를 요구받는다.":
        "Structurally takes the opposing side. Because that risks killing "
        "every signal, the objections themselves are held to a statistical "
        "standard.",

    "모델을 만든 당사자이므로 자기 모델에 우호적일 수 있음. 그래서 판정 "
    "권한은 감사관에게 있다.":
        "Built the model, so may be partial to it. That is why the "
        "adjudicating authority sits with the auditor.",

    "매크로가 모든 것을 설명한다고 보는 경향이 있음. 종목 고유 요인을 "
    "과소평가할 수 있음.":
        "Inclined to think macro explains everything, and may underweight "
        "idiosyncratic drivers.",

    "구조적으로 회의적. 메커니즘을 서술할 수 없는 팩터는 후보에도 넣지 "
    "않는다.":
        "Structurally sceptical. A factor whose mechanism cannot be "
        "described is not even a candidate.",

    "시장이 대체로 옳다고 본다. 모델이 시장과 다르면 모델을 먼저 의심함.":
        "Assumes the market is usually right. When the model disagrees "
        "with it, suspects the model first.",

    "분포를 모르면 확률을 말할 수 없다. 그리고 우리는 드리프트를 모른다.":
        "Without the distribution you cannot state a probability. And we "
        "do not know the drift.",

    "옵션은 시장의 확률분포를 직접 보여준다. 우리 모델과 다르면 둘 중 하나는 "
    "틀렸다.":
        "Options show the market's probability distribution directly. If "
        "it differs from ours, one of the two is wrong.",

    # ── what each expert is allowed to see ────────────────────
    "팩터 수익률 패널만 — **자산 가격을 보지 않는다** (사후합리화 차단)":
        "Factor return panel only — **does not see the asset price** "
        "(blocks post-hoc rationalisation)",
    "검증 통계만 (DSR / PBO / Murphy / 커버리지 / 시행횟수)":
        "Validation statistics only (DSR / PBO / Murphy / coverage / trial "
        "count)",
    "가격 파생 피처 + 트리플배리어 라벨":
        "Price-derived features + triple-barrier labels",
    "매크로 팩터 시계열 + 발표 캘린더":
        "Macro factor series + release calendar",

    # ── retraction / escalation conditions ────────────────────
    "현재 국면 확률이 60% 아래로 내려가면 전환 진행으로 보고 국면 조건부 "
    "베타를 재추정합니다.":
        "If the current regime probability falls below 60%, I treat a "
        "transition as under way and re-estimate the regime-conditional "
        "betas.",

    "의 롤링 R²가 붕괴하거나 β 변동계수가 0.8을 넘으면 매크로 기반 논지를 "
    "철회합니다.":
        " collapses in rolling R², or its beta coefficient of variation "
        "exceeds 0.8, I withdraw the macro-based argument.",

    "결측이 2%를 넘거나 조정종가 누적수익이 원종가보다 낮아지면 즉시 차단으로 "
    "전환합니다.":
        "If missing data exceeds 2%, or the adjusted-close cumulative "
        "return falls below the raw close, I switch to an immediate halt.",

    "엣지가 음수로 돌아서거나 손절폭 × 사이즈가 계좌 2%를 넘으면 실행하지 "
    "않습니다.":
        "If the edge turns negative, or stop distance × size exceeds 2% of "
        "the account, I do not execute.",

    "발표 예정 지표는 선반영하지 않았습니다. 캘린더 이벤트 전에는 포지션을 "
    "별도로 관리해야 합니다.":
        "Scheduled releases are not priced in here. Positions have to be "
        "managed separately ahead of calendar events.",

    # ── interpretation notes ──────────────────────────────────
    ". 드라이버 기반 빈도와 모델 분포가 다르다는 뜻이며, 둘 중 하나(또는 둘 "
    "다)가 틀렸습니다.":
        ". That means the driver-based frequency and the model "
        "distribution disagree, and one of them — or both — is wrong.",

    "불일치는 오류가 아니라 정보입니다. 어느 한 지평의 결론만 인용하면 정반대 "
    "이야기가 나온다는 뜻이므로, 보유 기간을 정하지 않은 채로는 결론을 낼 수 "
    "없습니다.":
        "Disagreement is information, not error. It means quoting one "
        "horizon alone yields the opposite story — so no conclusion is "
        "possible until you fix the holding period.",

    "년)입니다. 강조하자면 **VaR은 최대손실이 아니라 하위 5% 경계값**이며, "
    "그보다 큰 손실이 5%의 확률로 발생합니다.":
        " years). To be explicit: **VaR is not the maximum loss but the "
        "lower 5% boundary**, and a larger loss occurs 5% of the time.",

    "유의한 거시 민감도가 확인되지 않았습니다. 이 자산의 최근 움직임을 거시 "
    "변수로 설명하기 어렵습니다.":
        "No significant macro sensitivity was found. This asset's recent "
        "moves are hard to explain with macro variables.",

    "로 지속성을 강제했습니다 — K-means처럼 라벨이 하루 단위로 튀지 않습니다.":
        " enforces persistence — the labels do not flip day to day the way "
        "K-means does.",

    "드리프트를 상수로 고정한 정규 GBM(원본 리포트 방식)에서는 상승확률이 ":
        "Under a normal GBM with drift fixed as a constant (the original "
        "report's approach) the probability of a rise is ",

    "로 나옵니다. 파라미터 불확실성·변동성 클러스터링·팻테일을 반영하면 **":
        ". Once parameter uncertainty, volatility clustering and fat tails "
        "are accounted for it becomes **",

    "로 이동합니다 — 분산 효과가 위기에 어떻게 변하는지의 실측치입니다.":
        " — a measured reading of how the diversification benefit changes "
        "in a crisis.",

    "해당 팩터로 헤지 불가. 헤지 없이 총노출로 사이징하거나 진입 보류.":
        "Cannot hedge with that factor. Either size on gross exposure "
        "without a hedge, or hold off entry.",

    "확률 출력 사용 금지. 방향 베팅이 아니라 리스크 예산으로만 접근.":
        "Do not use the probability output. Approach this as a risk budget "
        "rather than a directional bet.",

    # ── data caveats ──────────────────────────────────────────
    "yfinance 펀더멘털은 리스테이트먼트가 반영된 값으로 point-in-time이 "
    "아니다. 현재 상태 진단용으로만 사용하고 시계열 백테스트에는 쓰지 말 것.":
        "yfinance fundamentals reflect restatements and are not "
        "point-in-time. Use them to diagnose the current state only, never "
        "for time-series backtesting.",

    "리스테이트먼트가 반영된 값이라 point-in-time이 아닙니다.":
        "These reflect restatements and are not point-in-time.",

    "Adj Close 열이 없어 배당 반영 여부는 별도 검증이 필요합니다.":
        "There is no Adj Close column, so whether dividends are included "
        "needs separate verification.",

    "실질금리 β는 반드시 시변. 금-TIPS R²는 2005-2021 약 84%에서 2022년 이후 "
    "한 자릿수로 붕괴한 전례가 있음(한계 매수자 교체). 은은 산업수요 비중이 커 "
    "PMI/산업생산 로딩을 추가해야 함.":
        "The real-rate beta must be time-varying. Gold-TIPS R² has gone "
        "from roughly 84% over 2005-2021 to single digits after 2022 (the "
        "marginal buyer changed). Silver carries a large industrial-demand "
        "share, so PMI and industrial-production loadings should be added.",

    # ── section titles ────────────────────────────────────────
    "요약 — 무엇을 / 왜 / 무엇이 바뀌면":
        "Summary — what / why / what would change it",
    "투자 논지 — 드라이버 기반 시나리오":
        "Investment thesis — driver-based scenarios",
    "종목 성격 — 어떤 렌즈로 볼 것인가":
        "Ticker character — which lens to use",
    "헤지 설계 — 무엇을 상쇄하고 무엇이 남는가":
        "Hedge design — what is offset and what remains",
    "반증 조건 — 무엇이 사실이면 논지가 죽는가":
        "Falsifiers — what would have to be true for this thesis to die",
    "전문가 패널 — 직능별 소견과 반대신문":
        "Expert panel — opinions by discipline and cross-examination",
    "지평별 샤프 · 시장 베타 (부호 역전 확인)":
        "Sharpe and market beta by horizon (sign reversals flagged)",
    "GARCH 조건부 변동성 (최근 3년)":
        "GARCH conditional volatility (last 3 years)",
    " (Elastic-Net 선택 → OLS/Newey-West 재추정)\n":
        " (Elastic-Net selection → re-estimated with OLS/Newey-West)\n",

    # ── recurring short labels ────────────────────────────────
    "리스크": "Risk",
    "베타 ": "Beta ",
    "영업일": "trading days",
    "종목": "Ticker",
    "데이터 ": "Data ",
    "건": "",
    " +1단위": " +1 unit",
    "수익률": "Return",
    "손익": "P&L",
    "가능": "Yes",
    "불가": "No",
    "없습니다": "none",
    "헤지 후 잔차 변동성": "Residual volatility after hedging",
    "잔차 변동성": "Residual volatility",
    "EDGE 유효스프레드": "EDGE effective spread",
    "EDGE 스프레드": "EDGE spread",
    "방향": "Direction",
    "시장": "Market",
    "구조": "Structure",
    "적합": "Fit",
    "게이트": "Gate",
    "대형 개별주": "Large-cap single name",
    "에이전트": "Agent",
    "충격": "Shock",
    "사이즈": "Size",
    "기간": "Period",
}
