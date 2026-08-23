# -*- coding: utf-8 -*-
"""
English — trade construction, sizing ladder, regime and macro labels.

Seventh high-impact batch.
"""

CATALOG = {

    # ── prose ─────────────────────────────────────────────────
    " 민감도를 추정할 표본이 부족합니다.":
        " — there is not enough sample to estimate that sensitivity.",
    "손절폭이 목표폭보다 큽니다. 승률 ":
        "The stop distance is wider than the target distance. A hit rate of ",
    "시뮬 경로에서 목표 선도달 확률 ":
        "Probability of reaching the target first across simulated paths ",
    "] 하단을 크게 밑돎 → 팩터 미스매칭. 잔차 ":
        "] — far below the floor, so the factors are mismatched. Residual ",
    "이므로 95% 구간이 [": ", so the 95% interval is [",
    "**이며, 표준 충격 시 ": "**, and under a standard shock ",
    ")입니다. 손절은 임의 %가 아니라 ":
        "). The stop is not an arbitrary percentage but ",
    ") + 왕복비용 ": ") + round-trip cost ",
    ")  →  낙폭제약 켈리 ": ")  →  drawdown-constrained Kelly ",
    " (그때 95% MDD ": " (with a 95% MDD of ",
    "(FHS-EVT), ES95는 ": "(FHS-EVT); ES95 is ",
    "국면 내 연환산 수익 ": "Annualised return within the regime ",
    "현재 국면: ": "Current regime: ",
    "시나리오 알파 처리: ": "Scenario alpha treatment: ",
    "단순 켈리 μ/σ² = ": "Naive Kelly μ/σ² = ",
    "bp (추정량 간 산포 ": "bp (dispersion across estimators ",
    "일 / 요구 ": " days / required ",
    "년 필요 / ": " years required / ",
    "일, 점프페널티 λ=": " days, jump penalty λ=",
    "일 변동성 (": "-day volatility (",
    "β 변동계수 (": "β coefficient of variation (",
    ", 결측 ": ", missing ",
    "행 ": "rows ",
    "단일: ": "Single: ",
    "15% 초과 시 스퀴즈/크라우딩 리스크":
        "Above 15% there is squeeze and crowding risk",

    # ── section titles ────────────────────────────────────────
    "전문가 심의": "Expert deliberation",
    "종목 진단": "Ticker diagnostics",
    "자산군 분류": "Asset-class classification",
    "성격에 맞춘 개별 분석": "Analysis matched to the ticker's character",
    "금리 민감도 심층": "Rate sensitivity in depth",
    "점프 · 꼬리 구조": "Jump and tail structure",
    "변동성 드래그 분해": "Volatility drag decomposition",
    "옵션 표면 · RND": "Option surface · RND",
    "듀레이션 · DV01": "Duration · DV01",
    "포트폴리오": "Portfolio",

    # ── expert roles ──────────────────────────────────────────
    "확률모형 총괄": "Head of probabilistic modelling",
    "계량 리서처": "Quantitative researcher",
    "검증 감사관": "Validation auditor",

    # ── labels ────────────────────────────────────────────────
    "하락": "Down",
    "엣지": "Edge",
    "손절폭/(손절폭+목표폭)": "Stop / (stop + target)",
    "손절 도달 시 계좌 손실": "Account loss if the stop is hit",
    "상방기여 / |하방기여|": "Upside contribution / |downside contribution|",
    "기대손익 (배리어 반영)": "Expected P&L (barrier-aware)",
    "≈ 0 또는 게이트 실패": "≈ 0, or the gate failed",
    "In-sample 정확도": "In-sample accuracy",
    "채택": "Adopted",
    "없음": "None",
    "중앙값": "Median",
    "복합: 리스크오프": "Composite: risk-off",
    "스트레스 한도 초과": "Stress limit exceeded",
    "일간": "Daily",
    "아키타입": "Archetype",
    "경로 최대낙폭 중앙값": "Median maximum drawdown across paths",
    "골든크로스": "Golden cross",
    "최소분산": "Minimum variance",
    "누적수익": "Cumulative return",
    "경험확률": "Empirical probability",
    "연율화 기준": "Annualisation basis",
    "시장 변동성": "Market volatility",
    "내부 재계산": "Recomputed internally",
    "유효 라벨 / 시행횟수": "Effective labels / trials",
    "원본식 GBM 상승확률": "Original-style GBM probability of a rise",
    "데이터 범위 (비대칭)": "Data range (asymmetric)",
    "Adj Close 정합": "Adj Close consistency",
    "중립": "Neutral",
    "한도 ": "Limit ",
    "국면 전환": "Regime shift",
    "헤지 실행 가능": "Hedge is executable",
    "10년 국채금리": "10-year treasury yield",
    "팩터 중립 (고유위험만 노출)":
        "Factor neutral (idiosyncratic exposure only)",
    "스트레스 최악 ": "Worst-case stress ",
    "헤지 후 잔차 vol": "Residual vol after hedging",
    "지속성 α+γ/2+β": "Persistence α+γ/2+β",
    "보상/위험 (R:R)": "Reward / risk (R:R)",
    "견해 산포(표준편차)": "Dispersion of views (standard deviation)",
    "SPY / ES 선물": "SPY / ES futures",
    "EDGE 유효스프레드 ": "EDGE effective spread ",
    "Amihud 비유동성": "Amihud illiquidity",
    "출처": "Source",
    "전체": "All",
    "성격": "Character",
    "년)": " years)",
    "변수": "Variable",
    "보수적": "Conservative",
    "손절 선도달": "Stop hit first",
    "제거 가능 분산": "Removable variance",
    "광의달러 +5%": "Broad dollar +5%",
    "한계적 — 분할 진입만": "Marginal — scale in only",
    "확률 보정": "Probability calibration",
}
