# -*- coding: utf-8 -*-
"""
English catalog for the analysis report.

Keys are the Korean literal fragments the engine emits. Do not collect them
by hand — they come from the AST::

    python tools/i18n_extract.py --missing en
    python tools/i18n_rank.py <report-dir> --lang en --stub

Rules that matter here:

* A key must be a *self-contained* fragment. Never add a bare particle
  ('이 ', '가 ', '의 ') — the substitution would fire inside untranslated
  sentences and shred them. The Hangul-boundary rule in ``i18n.py`` blocks
  most of that, but a key that is genuinely ambiguous should just be left out.
* Trailing/leading spaces in a key are load-bearing. ``'확률 '`` is followed
  by a formatted number; keep the space in the translation.
* Sections below follow the source module, so the catalog can be checked
  against ``tools/i18n_extract.py --by-module``.
"""

CATALOG = {

    # ══════════════════════════════════════════════════════════
    #  glossary.py — 66 tooltip terms
    # ══════════════════════════════════════════════════════════

    # ── term labels ───────────────────────────────────────────
    "과적합 갭": "Overfit gap",
    "켈리": "Kelly",
    "낙폭제약 켈리": "Drawdown-constrained Kelly",
    "레짐": "Regime",
    "팩터 R²": "Factor R²",
    "델타 패널": "Delta panel",
    "하방 베타": "Downside beta",
    "β안정성 CV": "β stability (CV)",
    "최소분산 헤지비율": "Minimum-variance hedge ratio",
    "알파": "Alpha",
    "제곱근 임팩트": "Square-root impact",
    "거부권": "Veto",
    "반증 조건": "Falsifier",
    "증거 위계": "Evidence hierarchy",
    "드리프트": "Drift",
    "생존편향": "Survivorship bias",
    "샤프": "Sharpe",
    "소르티노": "Sortino",
    "칼마": "Calmar",
    "왜도": "Skewness",
    "첨도": "Kurtosis",
    "표준오차": "Standard error",
    "신뢰구간": "Confidence interval",
    "분위수": "Quantile",
    "팻테일": "Fat tail",
    "점프": "Jump",
    "베타": "Beta",
    "헤지": "Hedge",
    "스프레드": "Spread",
    "유동성": "Liquidity",
    "임팩트": "Impact",
    "듀레이션": "Duration",
    "모멘텀": "Momentum",
    "밸류": "Value",
    "자기상관": "Autocorrelation",
    "과적합": "Overfitting",
    "교차검증": "Cross-validation",
    "리밸런싱": "Rebalancing",

    # ── validation · overfitting ──────────────────────────────
    "확률적 샤프 비율 (Probabilistic Sharpe Ratio)":
        "Probabilistic Sharpe Ratio",
    "관측된 샤프가 기준치보다 정말 높을 확률. 표본이 짧거나 수익률이 "
    "비대칭·팻테일이면 샤프는 쉽게 부풀려진다. 95% 미만이면 '좋아 보이는 "
    "것'과 '좋은 것'을 구별하지 못한 상태다.":
        "The probability that the observed Sharpe really exceeds a "
        "benchmark. A short sample, or skewed and fat-tailed returns, "
        "inflates Sharpe easily. Below 95% you cannot tell 'looks good' "
        "from 'is good'.",

    "디플레이티드 샤프 비율 (Deflated Sharpe Ratio)":
        "Deflated Sharpe Ratio",
    "여러 전략을 시도한 뒤 가장 좋은 걸 골랐다는 사실을 보정한 샤프. "
    "100번 던져 나온 최고 기록은 실력이 아니다. 이 값이 90% 미만이면 "
    "다중검정 보정 후 유의성이 없다는 뜻.":
        "Sharpe adjusted for the fact that you tried many strategies and "
        "kept the best. The best of 100 coin flips is not skill. Below "
        "90% it is not significant once multiple testing is accounted for.",

    "과적합 확률 (Probability of Backtest Overfitting)":
        "Probability of Backtest Overfitting",
    "표본을 여러 조합으로 갈라 학습·검증을 바꿔 끼웠을 때, 학습에서 1등이던 "
    "설정이 검증에서 중앙값 아래로 떨어질 확률. 50% 넘으면 선택 절차 자체가 "
    "과적합, 75% 넘으면 폐기 대상.":
        "Split the sample many ways and swap train and test: how often "
        "does the configuration that ranked first in training fall below "
        "the median in testing? Above 50% the selection procedure itself "
        "is overfit; above 75% discard it.",

    "머피 분해의 해상도 (Resolution)": "Resolution (Murphy decomposition)",
    "예측이 기저율(그냥 평균)보다 얼마나 더 많은 정보를 담고 있는지. "
    "Brier = 신뢰도 − 해상도 + 불확실성. 해상도가 0에 가까우면 '맞히는 것처럼 "
    "보여도 실제로는 평균만 말하고 있다'는 정량적 증거.":
        "How much more information a forecast carries than the base rate. "
        "Brier = reliability − resolution + uncertainty. Resolution near "
        "zero is quantitative evidence that the model looks accurate while "
        "actually just repeating the average.",

    "브라이어 스킬 스코어": "Brier skill score",
    "상수 예측(항상 기저율) 대비 얼마나 나은지. 0 이하면 '그냥 평균을 말하는 "
    "것보다 못하다'.":
        "How much better than a constant forecast (always the base rate). "
        "At or below zero it is worse than simply saying the average.",

    "In-sample 정확도 − OOS 정확도": "In-sample accuracy − OOS accuracy",
    "학습 데이터에서의 성적과 처음 보는 데이터에서의 성적 차이. 15%p를 넘으면 "
    "모델이 답을 외운 것이지 배운 게 아니다.":
        "The gap between performance on training data and on data the "
        "model has never seen. Past 15pp the model memorised the answers "
        "rather than learning anything.",

    "퍼지드 교차검증": "Purged cross-validation",
    "라벨이 미래 구간에 걸쳐 있으면 학습·검증 구간이 시간적으로 겹친다. "
    "겹치는 구간을 제거(purge)하고 여유(embargo)를 둬야 '미래를 이미 본' "
    "성적이 나오지 않는다.":
        "When a label spans a future window, the train and test periods "
        "overlap in time. You have to purge the overlapping samples and "
        "add an embargo, or the score reflects a model that already saw "
        "the future.",

    "기권 — 출력 무효화": "Abstain — output invalidated",
    "게이트를 통과하지 못한 모듈은 감점된 점수를 내지 않고 아예 출력을 "
    "취소한다. OOS 정확도 50%는 '약한 신호'가 아니라 '신호 없음'이고, "
    "올바른 출력은 낮은 점수가 아니라 출력 없음이다.":
        "A module that fails its gate does not emit a reduced score — its "
        "output is cancelled. 50% out-of-sample accuracy is not a weak "
        "signal but no signal, and the correct output is not a low number "
        "but no number.",

    # ── risk ──────────────────────────────────────────────────
    "밸류앳리스크 (Value at Risk)": "Value at Risk",
    "주어진 신뢰수준에서의 손실 경계값. VaR 95% 3%는 '100일 중 약 5일은 "
    "3%보다 더 잃는다'는 뜻이지 최대손실이 아니다. 꼬리 안쪽이 얼마나 깊은지는 "
    "ES를 봐야 한다.":
        "The loss threshold at a given confidence level. A 95% VaR of 3% "
        "means roughly 5 days in 100 lose more than 3% — it is not the "
        "maximum loss. How deep it goes beyond that is what ES tells you.",

    "기대손실 (Expected Shortfall / CVaR)":
        "Expected Shortfall (CVaR)",
    "VaR을 넘어선 경우들의 평균 손실. VaR이 문턱이라면 ES는 문턱을 넘었을 때 "
    "실제로 얼마나 아픈지를 말한다.":
        "The average loss across the cases that breach VaR. If VaR is the "
        "threshold, ES tells you how much it actually hurts once you cross "
        "it.",

    "조건부 VaR — ES와 같은 개념": "Conditional VaR — the same thing as ES",
    "VaR을 초과한 손실들의 평균.":
        "The mean of the losses that exceed VaR.",

    "조건부 낙폭 (Conditional Drawdown at Risk)":
        "Conditional Drawdown at Risk",
    "최악 구간 낙폭들의 평균. 한 번의 최대낙폭보다 '나쁜 국면이 평균적으로 "
    "얼마나 깊은지'를 보여 준다.":
        "The average of the worst drawdowns. More informative than a "
        "single maximum: it shows how deep a bad stretch typically runs.",

    "쿠피엑 위반빈도 검정 (POF)": "Kupiec proportion-of-failures test",
    "VaR 위반 횟수가 이론적 빈도와 맞는지. p값이 낮으면 그 VaR 모델은 손실 "
    "빈도 자체를 틀리게 보고 있다.":
        "Whether the number of VaR breaches matches the theoretical rate. "
        "A low p-value means the model has the frequency of losses itself "
        "wrong.",

    "크리스토퍼슨 독립성 검정": "Christoffersen independence test",
    "VaR 위반이 몰려서 발생하는지. 위반이 연달아 터지면 횟수가 맞아도 "
    "위험하다 — 모델이 변동성 군집을 못 잡고 있다는 뜻.":
        "Whether VaR breaches cluster. Back-to-back breaches are dangerous "
        "even when the count is right — it means the model is missing "
        "volatility clustering.",

    "최대낙폭 (Maximum Drawdown)": "Maximum drawdown",
    "고점 대비 최대 하락폭. 수익률보다 이걸 못 견뎌서 그만둔다.":
        "The largest fall from a peak. People quit over this, not over "
        "the return.",

    "켈리 기준 (Kelly Criterion)": "Kelly criterion",
    "장기 성장률을 최대화하는 베팅 비율. 문제는 공식이 아니라 μ(기대수익)를 "
    "안다고 가정한 것이다. μ 추정오차를 넣으면 성장최적 비율이 급격히 줄고, "
    "낙폭 제약을 걸면 더 줄어든다.":
        "The bet size that maximises long-run growth. The problem is not "
        "the formula but the assumption that you know μ. Add estimation "
        "error in μ and the growth-optimal fraction collapses; add a "
        "drawdown constraint and it shrinks further.",

    "성장최적 켈리는 수학적으로 옳아도 운용 불가능한 낙폭을 동반한다. "
    "'95% 확률로 낙폭 X% 이내'를 만족하는 최대 비율로 자른 값.":
        "Growth-optimal Kelly is mathematically correct and comes with a "
        "drawdown you cannot actually run. This is the largest fraction "
        "that still keeps the drawdown within X% at 95% probability.",

    # ── volatility · regime ───────────────────────────────────
    "GJR-GARCH-t 조건부 변동성": "GJR-GARCH-t conditional volatility",
    "변동성이 시간에 따라 변하고 군집한다는 사실을 반영한 모델. GJR은 하락이 "
    "상승보다 변동성을 더 키우는 비대칭(레버리지 효과)을, t는 팻테일을 "
    "반영한다.":
        "A model built on the fact that volatility moves and clusters over "
        "time. GJR captures the asymmetry where declines raise volatility "
        "more than rallies (the leverage effect); the t distribution "
        "captures fat tails.",

    "일간·주간·월간 실현변동성을 함께 넣어 장기 기억을 잡는 모델.":
        "A model that feeds daily, weekly and monthly realised volatility "
        "together to capture long memory.",

    "시장 국면 (Regime)": "Market regime",
    "저변동 상승·고변동 하락처럼 통계적 성질이 다른 구간. 국면이 바뀌면 팩터 "
    "베타와 상관이 함께 바뀐다.":
        "Stretches with different statistical character — a quiet uptrend "
        "versus a violent selloff. When the regime turns, factor betas and "
        "correlations turn with it.",

    "통계적 점프 모델": "Statistical jump model",
    "국면 전환을 감지하되, 전환 페널티를 둬서 잡음에 과민반응하지 않게 한 "
    "방법. HMM보다 과도한 스위칭이 적다.":
        "Detects regime shifts while penalising each switch, so it does "
        "not react to noise. It flips far less often than an HMM.",

    "필터드 히스토리컬 시뮬레이션": "Filtered historical simulation",
    "과거 수익률을 그대로 재사용하지 않고, 조건부 변동성으로 표준화한 잔차를 "
    "재추출한 뒤 현재 변동성으로 되돌린다. '그때는 조용했고 지금은 시끄럽다'를 "
    "반영한다.":
        "Rather than reusing past returns as they were, it resamples "
        "residuals standardised by conditional volatility and rescales "
        "them to today's. It accounts for 'that period was calm and this "
        "one is not'.",

    "일반화 파레토 분포 (극단값 이론)":
        "Generalised Pareto distribution (extreme value theory)",
    "정규분포는 꼬리를 과소평가한다. 임계점 초과분만 따로 적합해 극단 손실 "
    "구간을 제대로 모형화한다.":
        "The normal distribution understates tails. Fitting only the "
        "exceedances above a threshold models the extreme-loss region "
        "properly.",

    # ── factors ───────────────────────────────────────────────
    "팩터 모델 설명력": "Factor model explanatory power",
    "수익 변동 중 팩터로 설명되는 비중. 자산군마다 기대 밴드가 다르다. 밴드 "
    "아래로 떨어지면 그 자산을 그 팩터로 보는 관점 자체가 틀렸다는 신호이고, "
    "델타·헤지·스트레스가 전부 무효가 된다.":
        "The share of return variation the factors explain. The expected "
        "band differs by asset class. Falling below the band signals that "
        "viewing this asset through those factors is simply wrong — and it "
        "invalidates the deltas, the hedge and the stress numbers with it.",

    "리스크 팩터별 민감도 표": "Sensitivity table by risk factor",
    "'샤프 0.96' 같은 요약이 아니라 무엇이 X만큼 움직이면 얼마를 잃는가. "
    "정적 베타 대신 시변 베타를 쓰고 하방 베타를 병기한다.":
        "Not a summary like 'Sharpe 0.96' but: if this moves by X, how "
        "much do you lose? It uses time-varying rather than static betas, "
        "and shows downside beta alongside.",

    "시장이 하락한 날만 골라 추정한 베타. 이게 전체 베타보다 크면 '좋을 땐 덜 "
    "오르고 나쁠 땐 더 빠지는' 비대칭 자산이다. 정적 베타 스트레스는 이걸 "
    "놓친다.":
        "Beta estimated only on days the market fell. If it exceeds the "
        "overall beta, the asset is asymmetric — it rises less in good "
        "times and falls more in bad. Static-beta stress testing misses "
        "this entirely.",

    "베타 변동계수": "Beta coefficient of variation",
    "롤링 베타의 표준편차 ÷ 평균. 0.8을 넘으면 그 베타를 헤지비율로 쓰면 안 "
    "된다 — 오늘 맞춘 헤지가 내일 틀린다.":
        "Standard deviation of the rolling beta divided by its mean. Above "
        "0.8 you must not use that beta as a hedge ratio — a hedge set "
        "today is wrong tomorrow.",

    "소형−대형 (Small Minus Big)": "Small Minus Big",
    "소형주 롱 · 대형주 숏 스프레드. 롱온리 소형주 ETF 수익률을 그대로 쓰면 "
    "팩터가 아니라 그냥 시장이 된다.":
        "Long small caps, short large caps. Using a long-only small-cap "
        "ETF return instead gives you the market, not the factor.",

    "가치−성장 (High Minus Low)": "High Minus Low",
    "가치주 롱 · 성장주 숏 스프레드.":
        "Long value, short growth.",

    "수익성 (Robust Minus Weak)": "Robust Minus Weak",
    "고수익성 롱 · 저수익성 숏 스프레드.":
        "Long high profitability, short low profitability.",

    "모멘텀 (Up Minus Down)": "Up Minus Down",
    "최근 상승 롱 · 하락 숏 스프레드.":
        "Long recent winners, short recent losers.",

    "잔차 분산을 최소화하는 헤지 수량 = 다변량 팩터 회귀 계수. 따라서 팩터 "
    "모델이 틀리면 헤지도 같이 틀린다. 이 연결을 끊고 헤지를 논하면 안 된다.":
        "The hedge quantity that minimises residual variance is the "
        "multivariate factor regression coefficient. So if the factor "
        "model is wrong, the hedge is wrong with it. You cannot discuss "
        "the hedge as though that link were not there.",

    "팩터로 설명되지 않은 초과수익": "Excess return the factors do not explain",
    "진짜 실력일 수도, 모델에 없는 팩터일 수도 있다. t값이 2 미만이면 "
    "통계적으로 0과 구별되지 않는다.":
        "It may be genuine skill, or a factor missing from the model. "
        "Below a t of 2 it is statistically indistinguishable from zero.",

    # ── microstructure ────────────────────────────────────────
    "EDGE 유효 스프레드 추정량": "EDGE effective spread estimator",
    "일봉 OHLC만으로 매수-매도 호가 스프레드를 편향 없이 추정하는 방법. "
    "Corwin-Schultz·Roll은 저스프레드 구간에서 크게 부풀린다.":
        "Estimates the bid-ask spread without bias from daily OHLC alone. "
        "Corwin-Schultz and Roll inflate it badly when spreads are tight.",

    "아미후드 비유동성": "Amihud illiquidity",
    "거래대금 1단위당 가격이 얼마나 움직이는지. 클수록 같은 금액을 사고팔 때 "
    "시장을 더 밀어낸다.":
        "How far the price moves per unit of traded value. The larger it "
        "is, the more the same order size pushes the market.",

    "체결 물량이 커질수록 비용이 √(참여율)에 비례해 늘어난다는 경험 법칙. "
    "사이즈를 키울 때 비용이 선형으로 늘지 않는다.":
        "The empirical rule that cost grows with the square root of "
        "participation rate as size increases. Cost does not scale "
        "linearly when you scale the position.",

    "일평균 거래대금": "Average daily traded value",
    "청산 가능성의 기본 척도.":
        "The basic measure of whether you can get out.",

    # ── verdict · process ─────────────────────────────────────
    "진입하지 않음": "No entry",
    "약세 판단이 아니다. 현 조건에서 포지션을 잡을 근거가 부족하거나 리스크 "
    "한도에 걸린 상태. 방향 확률은 따로 읽어야 한다.":
        "This is not a bearish call. It means there is not enough basis to "
        "take a position under current conditions, or a risk limit binds. "
        "Read the directional probability separately.",

    "특정 전문가가 단독으로 진입을 막을 수 있는 권한. 데이터 무결성·체결 "
    "가능성·리스크 한도처럼 '다른 게 아무리 좋아도 안 되는' 조건에만 "
    "부여된다.":
        "The authority for a single expert to block entry alone. It is "
        "granted only where nothing else can compensate — data integrity, "
        "executability, risk limits.",

    "'무엇이 사실이면 이 논지가 죽는가'를 분석 시점에 미리 정해 둔 것. "
    "사후에 만든 반증 조건은 의미가 없다.":
        "What would have to be true for this thesis to die, written down "
        "in advance. A falsifier invented afterwards is worthless.",

    "반론의 승패를 정하는 순서: ①데이터 무결성 ②체결 가능성 ③표본외 통계 "
    "④표본내 통계 ⑤경제적 메커니즘 ⑥서사. 상위 증거가 하위 주장을 이긴다.":
        "The order that settles a disagreement: (1) data integrity, "
        "(2) executability, (3) out-of-sample statistics, (4) in-sample "
        "statistics, (5) economic mechanism, (6) narrative. Higher "
        "evidence beats lower claims.",

    "위험중립 밀도 (Risk-Neutral Density)": "Risk-neutral density",
    "옵션 가격에서 역산한 시장의 내재 분포. 우리 모델 분포와 비교하면 '시장과 "
    "어디서 의견이 갈리는지'가 보인다.":
        "The market's implied distribution, backed out of option prices. "
        "Compared with our model distribution it shows exactly where we "
        "disagree with the market.",

    "기대수익률 추정치 μ̂": "Estimated expected return μ̂",
    "표준오차가 σ/√T 라, 일봉 표본에서는 거의 항상 추정치 자체만큼 크다. "
    "그래서 '상승확률 71%' 같은 값은 시장이 아니라 가정에 대한 진술이다.":
        "Its standard error is σ/√T, which on daily samples is almost "
        "always as large as the estimate itself. So a number like "
        "'71% chance of a rise' is a statement about assumptions, not "
        "about the market.",

    "데이터 소스에 상장폐지 종목이 없으면, 지금 남아 있는 종목만 보게 된다. "
    "종목선택 전략은 원리적으로 검증 불가능해진다.":
        "If the data source has no delisted names, you only ever see the "
        "survivors. Stock-selection strategies become unverifiable in "
        "principle.",

    # ── ratios · statistics ───────────────────────────────────
    "샤프 비율 (Sharpe Ratio)": "Sharpe ratio",
    "위험 한 단위당 초과수익. 분모가 표준편차라 상승 변동성까지 벌점으로 "
    "친다. 표본이 짧으면 쉽게 부풀려지므로 반드시 PSR·DSR 과 함께 봐야 한다. "
    "샤프 1.0을 t>3 으로 입증하려면 약 9년치 표본이 필요하다.":
        "Excess return per unit of risk. Because the denominator is "
        "standard deviation, upside volatility is penalised too. Short "
        "samples inflate it easily, so always read it with PSR and DSR. "
        "Proving a Sharpe of 1.0 at t>3 takes roughly nine years of data.",

    "소르티노 비율 (Sortino Ratio)": "Sortino ratio",
    "샤프의 분모를 하방 변동성만으로 바꾼 것. 위로 튀는 것은 위험이 아니라는 "
    "관점이다. 소르티노가 샤프보다 훨씬 크면 수익 분포가 우측으로 치우쳐 "
    "있다는 뜻 — 큰 손실은 드물지만 한 번에 온다.":
        "Sharpe with the denominator replaced by downside volatility only, "
        "on the view that upside is not risk. A Sortino much larger than "
        "the Sharpe means the return distribution leans right — big losses "
        "are rare but arrive all at once.",

    "칼마 비율 (Calmar Ratio)": "Calmar ratio",
    "연수익 ÷ 최대낙폭. 변동성이 아니라 실제로 견뎌야 했던 손실로 나눈다. "
    "운용자가 중도 이탈하는 이유는 변동성이 아니라 낙폭이라 실무에서 샤프보다 "
    "체감에 가깝다. 1 미만이면 견딘 고통만큼 못 벌었다.":
        "Annual return divided by maximum drawdown — divided by the loss "
        "you actually had to sit through, not by volatility. People quit "
        "over drawdown rather than volatility, so in practice it tracks "
        "lived experience better than Sharpe. Below 1 you did not earn "
        "what the pain cost.",

    "왜도 (Skewness)": "Skewness",
    "분포의 좌우 비대칭. 음수면 작게 자주 벌고 크게 한 번 잃는 모양 — 옵션 "
    "매도·캐리 전략의 전형이다. 이런 분포에서는 평균과 샤프가 위험을 "
    "체계적으로 과소평가한다.":
        "How asymmetric the distribution is. Negative means many small "
        "gains and one large loss — the signature of option selling and "
        "carry trades. In such a distribution the mean and the Sharpe "
        "systematically understate the risk.",

    "첨도 (Kurtosis)": "Kurtosis",
    "꼬리의 두께. 정규분포는 3이다. 그보다 크면 극단값이 정규분포 가정보다 "
    "훨씬 자주 나온다는 뜻이라, 정규분포로 계산한 VaR 는 실제 손실을 "
    "과소평가한다. 일간 주식 수익률은 보통 5~10이다.":
        "Tail thickness. The normal distribution sits at 3. Anything "
        "higher means extremes occur far more often than a normal "
        "assumption allows, so VaR computed on that assumption understates "
        "real losses. Daily equity returns typically run 5 to 10.",

    "표준오차 (Standard Error)": "Standard error",
    "추정값 자체가 얼마나 흔들리는지. 기대수익률의 표준오차는 σ/√T 라 표본이 "
    "짧으면 거의 언제나 추정값만큼 크다. '연 12% 기대'라는 값의 표준오차가 "
    "15%면 그 숫자는 0과 구별되지 않는다.":
        "How much the estimate itself wobbles. For expected return it is "
        "σ/√T, so on a short sample it is almost always as large as the "
        "estimate. If '12% expected annually' carries a standard error of "
        "15%, that number is indistinguishable from zero.",

    "신뢰구간 (Confidence Interval)": "Confidence interval",
    "같은 절차를 반복했을 때 참값을 포함하는 구간. '이 안에 있을 확률 95%'가 "
    "아니라 '이 절차가 95%의 경우 참값을 담는다' 는 뜻이다. 구간이 0을 "
    "가로지르면 방향을 말할 수 없다.":
        "The interval that contains the true value when the procedure is "
        "repeated. It does not mean 'a 95% chance the value is in here' "
        "but 'this procedure captures the true value 95% of the time'. If "
        "the interval straddles zero, you cannot state a direction.",

    "분위수 (Quantile)": "Quantile",
    "정렬했을 때 특정 비율 지점의 값. VaR 95%는 손실 분포의 5% 분위수다. "
    "평균과 달리 극단값에 끌려가지 않아 꼬리를 볼 때 쓴다.":
        "The value at a given position once the data is sorted. A 95% VaR "
        "is the 5% quantile of the loss distribution. Unlike the mean it "
        "is not dragged around by extremes, which is why it is used for "
        "tails.",

    "팻테일 (Fat Tail)": "Fat tail",
    "정규분포보다 극단값이 두꺼운 꼬리. 시장 수익률은 거의 항상 팻테일이라, "
    "정규분포를 가정한 위험 계산은 최악의 순간에 가장 크게 틀린다. 이 엔진이 "
    "GPD 로 꼬리를 따로 적합하는 이유다.":
        "A tail heavier with extremes than the normal distribution. Market "
        "returns almost always have them, so risk numbers built on a "
        "normal assumption are most wrong exactly when it matters most. "
        "That is why this engine fits the tail separately with a GPD.",

    "점프 (Jump)": "Jump",
    "연속적인 변동으로 설명되지 않는 불연속 가격 변화. 실적·인수·규제처럼 "
    "정보가 한 번에 반영될 때 생긴다. 점프가 잦은 종목은 손절이 설계대로 "
    "체결되지 않으므로 사이즈를 줄여야 한다.":
        "A discontinuous price move that continuous variation cannot "
        "explain. It happens when information arrives all at once — "
        "earnings, an acquisition, a regulatory decision. In names that "
        "jump often, stops do not fill where you designed them to, so the "
        "position has to be smaller.",

    "베타 (Beta)": "Beta",
    "기준 지수가 1% 움직일 때 이 자산이 몇 % 움직이는가. 시간에 따라 변한다 — "
    "기간을 바꾸면 값이 달라지는 게 정상이고, 지평 간 차이가 크면 구조 변화 "
    "신호다. 고정 상수로 다루면 헤지가 어긋난다.":
        "How many percent this asset moves when the benchmark moves 1%. It "
        "changes over time — a different window giving a different value "
        "is normal, and a large gap between horizons signals structural "
        "change. Treat it as a fixed constant and the hedge drifts off.",

    "헤지 (Hedge)": "Hedge",
    "반대 방향 포지션으로 특정 위험만 상쇄하는 것. 모든 위험이 지워지지 "
    "않는다 — 상쇄하고 남는 잔여위험(베이시스)이 무엇인지 모르면 헤지가 아니라 "
    "위험을 다른 위험으로 바꾼 것이다.":
        "Offsetting one specific risk with an opposing position. It does "
        "not erase every risk — if you do not know what residual (basis) "
        "risk is left over, you have not hedged, you have swapped one risk "
        "for another.",

    "호가 스프레드 (Bid-Ask Spread)": "Bid-ask spread",
    "매수호가와 매도호가의 차이. 왕복 거래의 최소 비용이다. 넓은 스프레드는 "
    "그 자체로 거래 불가 사유가 된다 — 기대수익이 스프레드보다 작으면 맞아도 "
    "잃는다.":
        "The gap between the bid and the offer — the minimum cost of a "
        "round trip. A wide spread is on its own a reason not to trade: if "
        "the expected return is smaller than the spread, you lose even "
        "when you are right.",

    "유동성 (Liquidity)": "Liquidity",
    "가격을 크게 밀지 않고 사고팔 수 있는 정도. 호가가 아니라 내 주문이 가격을 "
    "얼마나 움직이는가로 봐야 한다. 유동성이 얇으면 백테스트 수익은 체결 순간 "
    "사라진다.":
        "How much you can buy or sell without pushing the price. Judge it "
        "by how far your own order moves the market, not by the quoted "
        "size. Where liquidity is thin, backtested returns disappear at "
        "the moment of execution.",

    "시장 충격 (Market Impact)": "Market impact",
    "내 주문 자체가 가격을 밀어 올리는(내리는) 비용. 주문 크기의 제곱근에 "
    "대략 비례한다 — 4배 크게 사면 비용은 2배가 아니라 참여율까지 고려해야 "
    "한다. 전략 수용력(capacity)의 상한을 정하는 요인이다.":
        "The cost of your own order pushing the price. It scales roughly "
        "with the square root of order size — buying four times as much "
        "does not merely double the cost once participation rate is "
        "considered. This is what caps a strategy's capacity.",

    "듀레이션 (Duration)": "Duration",
    "금리가 1%p 움직일 때 채권 가격이 몇 % 변하는가. 만기가 아니라 현금흐름의 "
    "가중평균 시점이다. 국채 ETF 를 주식처럼 베타로만 보면 핵심 위험을 통째로 "
    "놓친다.":
        "How many percent a bond's price moves per 1pp change in rates. It "
        "is the weighted average timing of the cash flows, not the "
        "maturity. Look at a treasury ETF through equity beta alone and "
        "you miss the central risk entirely.",

    "모멘텀 (Momentum)": "Momentum",
    "최근 오른 것이 계속 오르는 경향. 가장 오래 살아남은 이상현상이지만 추세 "
    "전환에서 급격히 무너진다(momentum crash). 저변동 구간에서 쌓은 수익을 한 "
    "달에 반납하는 패턴이 반복된다.":
        "The tendency for recent winners to keep winning. It is the "
        "longest-surviving anomaly, but it breaks violently at turning "
        "points — the momentum crash. The pattern repeats: gains "
        "accumulated through a quiet stretch are handed back in a month.",

    "밸류 (Value)": "Value",
    "장부가·이익 대비 싼 종목이 초과수익을 낸다는 팩터. 무형자산 비중이 커진 "
    "뒤로 장부가 기준 밸류는 설명력이 크게 떨어졌다 — 팩터가 죽은 것인지 측정이 "
    "낡은 것인지를 구분해야 한다.":
        "The factor holding that names cheap against book or earnings earn "
        "excess return. Since intangibles became a large share of assets, "
        "book-based value has lost much of its power — and you have to "
        "separate 'the factor died' from 'the measurement is out of date'.",

    "자기상관 (Autocorrelation)": "Autocorrelation",
    "과거 값이 현재 값을 설명하는 정도. 수익률에 자기상관이 있으면 표본이 "
    "겉보기보다 적다 — 독립 관측이 아니므로 표준오차를 그대로 쓰면 유의성이 "
    "부풀려진다. HAC 표준오차가 필요한 이유다.":
        "How much past values explain the present one. When returns are "
        "autocorrelated your sample is smaller than it looks — the "
        "observations are not independent, so naive standard errors "
        "inflate significance. This is why HAC standard errors exist.",

    "과적합 (Overfitting)": "Overfitting",
    "표본 안의 잡음까지 학습해 표본 밖에서 무너지는 상태. in-sample 성적이 "
    "좋을수록 의심해야 한다. 여러 설정을 시도한 뒤 최고를 고르는 행위 자체가 "
    "과적합이라, 시도 횟수를 보정하지 않은 성과는 무의미하다.":
        "Learning the noise inside the sample and collapsing outside it. "
        "The better the in-sample score, the more suspicious you should "
        "be. Trying many configurations and keeping the best is itself "
        "overfitting, so performance not adjusted for the number of trials "
        "is meaningless.",

    "교차검증 (Cross-Validation)": "Cross-validation",
    "데이터를 나눠 학습/평가를 번갈아 하는 것. 시계열에서는 그냥 나누면 미래가 "
    "과거로 새어 들어간다 — 라벨 구간이 겹치는 표본을 제거하고(purging) 경계에 "
    "완충을 두어야(embargo) 결과가 의미를 갖는다.":
        "Splitting the data and alternating between training and "
        "evaluation. On time series a naive split leaks the future into "
        "the past — you have to purge samples whose label windows overlap "
        "and embargo a buffer at the boundary before the result means "
        "anything.",

    "리밸런싱 (Rebalancing)": "Rebalancing",
    "비중을 목표치로 되돌리는 것. 레버리지 ETP 는 매일 강제 리밸런싱을 하므로 "
    "경로에 의존한다 — 지수가 제자리로 와도 손실이 남는다. 이런 상품에 장기 "
    "보유 논리를 적용하면 안 된다.":
        "Returning weights to their targets. Leveraged ETPs rebalance by "
        "force every day, which makes them path dependent — the index can "
        "return to where it started and you are still down. Buy-and-hold "
        "logic must not be applied to these products.",
}
