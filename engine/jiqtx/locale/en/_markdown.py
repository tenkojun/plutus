# -*- coding: utf-8 -*-
"""
English — the Markdown report (``report.py``), used by the CLI.

Same catalog, different renderer: the Markdown path passes the whole
document through ``i18n.t`` once, so table pipes and code fences are
untouched (they contain no Hangul).
"""

CATALOG = {

    # ── headings ──────────────────────────────────────────────
    " — Plutus 정밀 분석 리포트\n": " — Plutus analysis report\n",
    "\n## 최종 판정 — 3축 분리\n":
        "\n## Final verdict — three separate axes\n",
    "\n## 1. 하드 게이트 — 게이트 실패는 감점이 아니라 무효화\n":
        "\n## 1. Hard gates — a failed gate invalidates, it does not "
        "deduct\n",
    "\n## 2. 자산 특성 지문 — 이 종목은 어떤 렌즈로 봐야 하는가\n":
        "\n## 2. Asset fingerprint — which lens this name needs\n",
    "\n## 3. 유동성·거래비용 — VPIN 프록시를 대체하는 정당한 지표\n":
        "\n## 3. Liquidity and cost — a defensible replacement for VPIN "
        "proxies\n",
    "\n## 4. 성과·리스크 요약\n":
        "\n## 4. Performance and risk summary\n",
    "\n## 5. 조건부 변동성 — 단일 표준편차가 아니라 동학\n":
        "\n## 5. Conditional volatility — dynamics, not one standard "
        "deviation\n",
    "\n## 6. 시장 국면 — 번호가 아니라 이름\n":
        "\n## 6. Market regimes — names, not numbers\n",
    "\n## 7. 팩터 모델 — 자산군에 맞는 렌즈인가\n":
        "\n## 7. Factor model — is this the right lens for the asset "
        "class\n",
    "\n## 8. 델타 패널 — 헤지펀드가 실제로 보는 수치\n":
        "\n## 8. Delta panel — the numbers a hedge fund actually reads\n",
    "\n## 9. 방향 예측 — 핵심 기능은 예측이 아니라 기권\n":
        "\n## 9. Direction forecast — the core function is abstention, not "
        "prediction\n",
    "\n## 10. 분포 시뮬레이션 — GBM 폐기\n":
        "\n## 10. Distribution simulation — GBM discarded\n",
    "### 10.1 드리프트가 왜 문제인가\n":
        "### 10.1 Why drift is a problem\n",
    "### 10.2 상승확률: 가정을 풀면 무엇이 남는가\n":
        "### 10.2 Probability of a rise: what survives once the "
        "assumptions are relaxed\n",
    "### 10.3 분포 요약\n": "### 10.3 Distribution summary\n",
    "\n## 11. VaR / ES — 커버리지 검정을 통과했는가\n":
        "\n## 11. VaR / ES — did it pass its coverage test\n",
    "\n## 12. 스트레스 — 주식 베타 곱셈이 아니라 자산군 고유 충격\n":
        "\n## 12. Stress — asset-class shocks, not a multiplied equity "
        "beta\n",
    "\n## 13. 포지션 사이징 — 켈리 200%가 나오는 이유\n":
        "\n## 13. Position sizing — why Kelly comes out at 200%\n",
    "\n## 14. 옵션 표면 — 시장이 말하는 것\n":
        "\n## 14. Option surface — what the market is saying\n",
    "\n### 14.1 시장 함축 확률분포 (Breeden-Litzenberger, ":
        "\n### 14.1 Market-implied distribution (Breeden-Litzenberger, ",
    "\n### 14.2 우리 모델 vs 시장 — 차이가 곧 논지\n":
        "\n### 14.2 Our model vs the market — the gap is the thesis\n",
    "\n## 15. 에이전트 심의 — 정보 비대칭 설계\n":
        "\n## 15. Agent deliberation — designed information asymmetry\n",
    "### 15.1 캘리브레이션 가중 로그오즈 풀링\n":
        "### 15.1 Calibration-weighted log-odds pooling\n",
    "\n## 16. 레드팀 — 사전등록된 반증 프로토콜\n":
        "\n## 16. Red team — the pre-registered falsification protocol\n",
    "\n## 17. 이 분석이 말할 수 없는 것\n":
        "\n## 17. What this analysis cannot tell you\n",
    "### 판정: ": "### Verdict: ",
    "### ★ 보정된 상승확률: **": "### ★ Calibrated probability of a rise: **",

    # ── block quotes ──────────────────────────────────────────
    "> 단일 점수는 산출하지 않습니다. 서로 다른 성질의 정보를 하나의 숫자로 "
    "합치면 정보가 파괴되기 때문입니다.\n":
        "> No single score is produced, because merging different kinds of "
        "information into one number destroys it.\n",
    "> 원본 리포트는 DSR 84%·과적합 갭 49%p를 **알면서도** 점수를 냈습니다. "
    "OOS 50%는 약한 신호가 아니라 신호 없음이고, 올바른 출력은 감점된 점수가 "
    "아니라 **출력 없음**입니다.\n":
        "> The original report published a score **knowing** the DSR was "
        "84% and the overfit gap 49pp. 50% out of sample is not a weak "
        "signal but no signal, and the correct output is not a marked-down "
        "score but **no output**.\n",
    "> 일봉 OHLCV로 만든 VPIN/CVD 프록시는 체결방향을 모르므로 정보 함량이 "
    "사실상 0입니다. EDGE(Ardia-Guidotti-Kroencke, JFE 2024)는 OHLC 전부를 "
    "최적 결합해 거래가 희소해도 편향되지 않습니다.\n":
        "> VPIN and CVD proxies built from daily OHLCV do not know trade "
        "direction, so their information content is essentially zero. EDGE "
        "(Ardia-Guidotti-Kroencke, JFE 2024) combines the full OHLC "
        "optimally and stays unbiased even when trading is sparse.\n",
    "> '샤프 0.96' 같은 요약통계가 아니라 **\"무엇이 X만큼 움직이면 얼마를 "
    "잃는가\"**. 정적 베타가 아니라 시변 베타를 쓰고, 하방 분위 베타를 "
    "나란히 표시합니다.\n":
        "> Not a summary statistic like 'Sharpe 0.96' but **\"if this moves "
        "by X, how much do you lose\"**. It uses time-varying rather than "
        "static betas and shows the downside-quantile beta alongside.\n",
    "> 원본 리포트는 '주식베타 0.20 × 지수충격'으로 스트레스를 만들었습니다. "
    "금에 주식 베타를 곱하는 것은 의미가 없습니다. 이 엔진은 자산군별 "
    "리스크팩터에 직접 충격을 가합니다.\n":
        "> The original report built its stress case as 'equity beta 0.20 × "
        "index shock'. Multiplying gold by an equity beta is meaningless. "
        "This engine shocks the risk factors of each asset class "
        "directly.\n",
    "> LLM 멀티에이전트 토론은 자동으로 정확도를 올리지 않습니다. 동조 효과, "
    "다수의 폭정, 그리고 **동일 입력을 받으면 토론이 마팅게일이 되어 개선이 "
    "없다**는 이론적 결과가 있습니다. 따라서 각 에이전트에 **서로 다른 데이터 "
    "슬라이스**를 주고, 거부권은 통계 에이전트에만 부여하며, 최종 판정은 "
    "LLM이 아니라 결정론적 규칙 엔진이 합니다.\n":
        "> LLM multi-agent debate does not automatically improve accuracy. "
        "There is conformity, tyranny of the majority, and the theoretical "
        "result that **debate on identical inputs is a martingale and "
        "improves nothing**. So each agent receives **a different slice of "
        "the data**, the veto belongs only to the statistics agents, and "
        "the final verdict is made by a deterministic rule engine rather "
        "than an LLM.\n",
    "> K-means의 라벨 0·1·2는 강약 순서를 뜻하지 않아 경제적 해석이 "
    "불가능합니다. Statistical Jump Model은 전환마다 점프 페널티를 부과해 "
    "지속성을 강제하고, 각 국면에 경제적 이름을 붙입니다.\n":
        "> K-means labels 0, 1 and 2 imply no ordering of strength, so they "
        "cannot be interpreted economically. The Statistical Jump Model "
        "charges a penalty per transition to enforce persistence and gives "
        "each regime an economic name.\n",
    "> **Murphy 분해**: Brier = Reliability − Resolution + Uncertainty. "
    "Resolution ≈ 0 이면 모델이 기저율 이상의 정보를 담고 있지 않다는 "
    "**정량적 증명**입니다. 이 한 숫자가 '상승확률 66%'류 출력의 유효성을 "
    "판정합니다.\n":
        "> **Murphy decomposition**: Brier = reliability − resolution + "
        "uncertainty. Resolution ≈ 0 is **quantitative proof** that the "
        "model carries no information beyond the base rate. This one "
        "number decides whether an output like '66% chance of a rise' is "
        "valid at all.\n",
    "> 켈리 공식 자체가 아니라 **μ를 안다고 가정한 것**이 문제입니다. 성장 "
    "최적 켈리는 수학적으로 옳아도 운용 불가능한 낙폭을 동반합니다. 낙폭 "
    "제약이 없으면 어떤 켈리 값도 실무 권고로 쓸 수 없습니다.\n":
        "> The problem is not the Kelly formula but **the assumption that "
        "you know μ**. Growth-optimal Kelly is mathematically correct and "
        "comes with a drawdown you cannot run. Without a drawdown "
        "constraint no Kelly number is usable as practical advice.\n",
    "> 레드팀은 **최소 3개의 구체적 반대 증거 제출이 의무**입니다. 제출 "
    "실패는 시스템 오류로 로깅됩니다.\n":
        "> The red team is **obliged to file at least three concrete "
        "pieces of counter-evidence**. Failing to file is logged as a "
        "system error.\n",
    "> 게이트를 통과하지 못했으므로 **확률을 출력하지 않습니다.** 감점된 "
    "점수를 내는 것은 없는 정보를 있는 것처럼 만드는 일입니다.\n":
        "> The gate was not passed, so **no probability is published.** "
        "Publishing a marked-down score would manufacture information that "
        "does not exist.\n",
    "> 이것이 원본 리포트의 핵심 오류 지점입니다. GLD에 주식형 FF 회귀를 "
    "돌려 R²=2%가 나왔고, 잔차 98%를 '종목 고유위험'으로 해석했습니다. "
    "실제로는 **누락 변수**이며, R²가 2%인 회귀의 알파(+10.3%)는 해석 "
    "불가능한 잔차 평균입니다.\n":
        "> This is where the original report went most wrong. It ran an "
        "equity-style Fama-French regression on GLD, got R²=2%, and read "
        "the 98% residual as idiosyncratic risk. In reality it is **an "
        "omitted variable**, and the alpha (+10.3%) of a regression with "
        "an R² of 2% is an uninterpretable residual mean.\n",
    "> **샤프 유의성**: 샤프 ": "> **Sharpe significance**: a Sharpe of ",
    "를 Harvey-Liu-Zhu 팩터 허들 (t > 3.0)로 입증하려면 **":
        " needs, to clear the Harvey-Liu-Zhu factor hurdle (t > 3.0), **",
    "년**의 표본이 필요합니다. 현재 표본은 ":
        " years** of sample. The current sample is ",
    "\n> ⚠ **평활화 보정**: 언스무딩 시 변동성이 ":
        "\n> ⚠ **Smoothing adjustment**: unsmoothed, volatility widens ",
    "배 확대. 보고된 샤프는 그만큼 과대평가입니다.\n":
        "×. The reported Sharpe is overstated by the same degree.\n",
    "\n> ⛔ **거부권 발동**: ": "\n> ⛔ **Veto raised**: ",

    # ── italic notes ──────────────────────────────────────────
    "_(데이터 없음)_\n": "_(no data)_\n",
    "_팩터 데이터 없음._\n": "_No factor data._\n",
    "_델타 패널 산출 불가 (팩터 데이터 부족)._\n":
        "_Delta panel cannot be computed (not enough factor data)._\n",
    "_ML 모듈 미실행._\n": "_The ML module was not run._\n",
    "_임팩트는 제곱근 법칙 G ≈ Y·σ_d·√(Q/ADV) 기준. 선형 모델은 대형 주문 "
    "비용을 극심하게 과소평가합니다._\n":
        "_Impact follows the square-root law G ≈ Y·σ_d·√(Q/ADV). A linear "
        "model understates the cost of large orders severely._\n",
    "\n_주의: 90% 구간은 통계적 신뢰구간이나 목표주가가 아니라 모델 가정 하의 "
    "시뮬레이션 분위입니다. VaR은 최대손실이 아니라 하위 5% 경계값입니다._\n":
        "\n_Note: the 90% band is not a statistical confidence interval or "
        "a price target — it is a simulation quantile under the model's "
        "assumptions. VaR is not the maximum loss but the lower 5% "
        "boundary._\n",
    "_위험중립 확률에는 리스크 프리미엄이 포함돼 있어 실세계 확률과 동일하지 "
    "않습니다. 차이의 방향과 크기를 논지로 삼는 것이 올바른 용법입니다._\n":
        "_Risk-neutral probabilities embed a risk premium and are not "
        "real-world probabilities. The correct use is to make the "
        "direction and size of the gap your thesis._\n",
    "\n_불확실성 분해: 전체 로그분산 중 파라미터 무지 기여 ":
        "\n_Uncertainty decomposition: of the total log variance, "
        "parameter ignorance contributes ",
    ", 시장 변동성 기여 ": ", market volatility ",
    "_점프 페널티 λ=": "_Jump penalty λ=",
    ", 관측 구간 전환 ": ", transitions observed ",
    "회_\n": "_\n",
    "\n_상위 피처: ": "\n_Top features: ",
    "_소요시간 ": "_Elapsed ",
    "초 · ": "s · ",

    # ── table headers ─────────────────────────────────────────
    "| 축 | 값 | 의미 |": "| Axis | Value | Meaning |",
    "| 항목 | 값 | 판정 근거 |": "| Item | Value | Basis |",
    "| 지표 | 값 |": "| Metric | Value |",
    "| 지표 | 값 | | 지표 | 값 |":
        "| Metric | Value | | Metric | Value |",
    "| 항목 | 값 |": "| Item | Value |",
    "\n| 항목 | 값 |": "\n| Item | Value |",
    "| 방식 | 1년 상승확률 |": "| Method | 1-year P(up) |",
    "| 방식 | 비중 |": "| Method | Weight |",
    "| 모델 | VaR 95% | ES 95% | 실현 위반율 | Kupiec p | 독립성 p | "
    "조건부 p |":
        "| Model | VaR 95% | ES 95% | Realised breach rate | Kupiec p | "
        "Independence p | Conditional p |",
    "| 에이전트 | 역할 | 데이터 범위 (비대칭) | 입장 | 확률 | 거부권 |":
        "| Agent | Role | Data scope (asymmetric) | Position | Probability "
        "| Veto |",
    "| 한계 | 내용 |": "| Limitation | Detail |",
    "| 팩터 | 계수 | t (HAC) |": "| Factor | Coefficient | t (HAC) |",
    "| 팩터 | 현재 β | 평균 β | 표준편차 | CV | 현재 R² | 경보 |":
        "| Factor | Current β | Mean β | Std dev | CV | Current R² | Alert |",
    "| 진단 | 값 | 임계 |": "| Diagnostic | Value | Threshold |",
    "| 지표 | 값 | 해석 |": "| Metric | Value | Reading |",
    "| 분위 | 시장 RND |": "| Quantile | Market RND |",
    "| | 모델 | 시장(위험중립) | 차이 |":
        "| | Model | Market (risk-neutral) | Difference |",

    # ── table rows and inline labels ──────────────────────────
    "**기준일** ": "**As of** ",
    " · **자산군** ": " · **asset class** ",
    ") · **연율화** √": ") · **annualised** √",
    "| **방향 등급** | **": "| **Direction grade** | **",
    ") | 확률 ": ") | probability ",
    "| **리스크 예산** | **": "| **Risk budget** | **",
    "** | 구속 제약: ": "** | binding constraint: ",
    "| **모델 신뢰도** | **": "| **Model confidence** | **",
    "** | 무효화 모듈 ": "** | invalidated modules ",
    "| 자산군 | ": "| Asset class | ",
    "| quoteType / 섹터 | ": "| quoteType / sector | ",
    "| 연율화 기준 | √": "| Annualisation | √",
    "| 연변동성 | ": "| Annualised volatility | ",
    " | 왜도 ": " | skew ",
    ", 첨도 ": ", kurtosis ",
    "| 1차 자기상관 | ": "| First-order autocorrelation | ",
    "| 최적 프록시 | ": "| Best proxy | ",
    "| 레버리지 탐지 | ": "| Leverage detected | ",
    "| 이력 | ": "| History | ",
    "년) | 요구 ": " years) | required ",
    "일 |": " days |",
    " 일 |": " days |",
    "\n**분류 경고**": "\n**Classification warning**",
    "| **EDGE 유효스프레드** | ": "| **EDGE effective spread** | ",
    "| 교차검증 (CS / CHL / Roll) | ": "| Cross-check (CS / CHL / Roll) | ",
    "| 추정량 간 산포 | ": "| Dispersion across estimators | ",
    " bp ← 측정 불확실성 |": " bp ← measurement uncertainty |",
    "| Amihud 비유동성 | ": "| Amihud illiquidity | ",
    "| 무거래일 비율 | ": "| No-trade days | ",
    "| 1% AUM 청산 소요 | ": "| Time to liquidate 1% of AUM | ",
    "\n**용량(capacity) 곡선** — 알파가 소멸하는 AUM 규모\n":
        "\n**Capacity curve** — the AUM at which the alpha disappears\n",
    " | | 최대낙폭 | ": " | | Max drawdown | ",
    "| 샤프 | ": "| Sharpe | ",
    "| 소르티노 | ": "| Sortino | ",
    " | | 최장 수중기간 | ": " | | Longest underwater | ",
    "| 칼마 | ": "| Calmar | ",
    " | | 승률 | ": " | | Hit rate | ",
    "| GJR-GARCH(1,1)-t 현재 변동성 | ":
        "| GJR-GARCH(1,1)-t current volatility | ",
    "| 장기 평균 변동성 | ": "| Long-run average volatility | ",
    "| 최근 21일 실현 | ": "| Realised, last 21 days | ",
    "| HAR 예측 (Corsi 2009) | ": "| HAR forecast (Corsi 2009) | ",
    "| 지속성 α+γ/2+β | ": "| Persistence α+γ/2+β | ",
    " (반감기 ": " (half-life ",
    "일) |": " days) |",
    "| 레버리지 효과 γ | ": "| Leverage effect γ | ",
    " ← 하락 충격이 변동성을 더 키우는 정도 |":
        " ← how much more a downside shock raises volatility |",
    "| t 자유도 ν | ": "| t degrees of freedom ν | ",
    " ← 작을수록 팻테일 |": " ← lower means fatter tails |",
    "| 변동성의 변동성 | ": "| Volatility of volatility | ",
    "| 현재 변동성 백분위 | ": "| Current volatility percentile | ",
    "| 표본 드리프트 μ̂ | ": "| Sample drift μ̂ | ",
    "| 표준오차 SE(μ̂)=σ/√T | ": "| Standard error SE(μ̂)=σ/√T | ",
    "| 95% 신뢰구간 | [": "| 95% confidence interval | [",
    "| 사후 드리프트 (축소 ": "| Posterior drift (shrinkage ",
    "| 드리프트 고정 + 정규 (원본 리포트 방식) | ":
        "| Fixed drift + normal (the original report's approach) | ",
    "| **FHS-GARCH + EVT + 파라미터 불확실성** | **":
        "| **FHS-GARCH + EVT + parameter uncertainty** | **",
    "| 중앙값 | ": "| Median | ",
    "| 90% 시뮬레이션 구간 | ": "| 90% simulation band | ",
    "| VaR 95% (종착수익) | ": "| VaR 95% (terminal return) | ",
    "| P(경로 중 −20% 낙폭) | ": "| P(−20% drawdown along the path) | ",
    "| 경로 최대낙폭 중앙값 | ":
        "| Median maximum drawdown across paths | ",
    "\n**채택 모델**: `": "\n**Adopted model**: `",
    "\n**최악 시나리오**: ": "\n**Worst-case scenario**: ",
    "\n**현재 국면**: `": "\n**Current regime**: `",
    "` (확률 ": "` (probability ",
    "영업일)\n": " trading days)\n",
    "**선택된 팩터**: ": "**Selected factors**: ",
    "| 자산군 기대밴드 | ": "| Asset-class expected band | ",
    "| 연환산 알파 | ": "| Annualised alpha | ",
    "| 알파 해석 허용 | ": "| Alpha interpretation permitted | ",
    "| 승자 모델 | ": "| Winning model | ",
    " | 선형 벤치마크와 경합 |": " | ran against a linear benchmark |",
    "| OOS 정확도 | ": "| OOS accuracy | ",
    " | 기저율 ": " | base rate ",
    "| In-sample 정확도 | ": "| In-sample accuracy | ",
    "| **과적합 갭** | **": "| **Overfit gap** | **",
    " | 작을수록 좋음 |": " | lower is better |",
    " | 소프트 50% / 하드 75% |": " | soft 50% / hard 75% |",
    "| 전략 샤프 | ": "| Strategy Sharpe | ",
    "| **전략 DSR** | **": "| **Strategy DSR** | **",
    "| 유효 라벨 수 | ": "| Effective labels | ",
    "| 시행 횟수 (로깅) | ": "| Trials (logged) | ",
    " | DSR 보정에 사용 |": " | used for the DSR adjustment |",
    "**판정 사유**": "**Reasons for the verdict**",
    "| GPD 꼬리 형상 ξ (하방/상방) | ":
        "| GPD tail shape ξ (down/up) | ",
    "| 단순 켈리 μ/σ² | ": "| Naive Kelly μ/σ² | ",
    "| **낙폭제약 켈리** | **": "| **Drawdown-constrained Kelly** | **",
    "| 변동성 타깃 | ": "| Volatility target | ",
    "| 스트레스 예산 한도 | ": "| Stress budget limit | ",
    "| 유동성 한도 | ": "| Liquidity cap | ",
    "| 자산군 상한 | ": "| Asset-class cap | ",
    "| **최종 비중** | **": "| **Final weight** | **",
    "\n**구속 제약**: ": "\n**Binding constraint**: ",
    "| 기간구조 기울기 (3M−1M) | ":
        "| Term structure slope (3M − 1M) | ",
    "| **IV − RV 스프레드** | ": "| **IV − RV spread** | ",
    " | 분산위험프리미엄 프록시 |": " | variance risk premium proxy |",
    "| Put/Call OI 비율 | ": "| Put/call OI ratio | ",
    "\n무차익 조건 충족: ": "\nNo-arbitrage conditions met: ",
    " · 함축 왜도 ": " · implied skew ",
    "\n에이전트 간 확률 산포: **":
        "\nProbability dispersion across agents: **",
    "** — 산포가 크면 통합 확률을 0.5로 축소합니다(평균내지 않음).\n":
        "** — when dispersion is large the pooled probability is shrunk "
        "towards 0.5 (never averaged).\n",
    "| ADV (중앙값) | $": "| ADV (median) | $",
    "| 상승확률 | ": "| P(up) | ",
    "\n**실행 경고**": "\n**Execution warning**",
    " 고유 주의사항**: ": " — specific cautions**: ",
    "**신뢰도 다이어그램 (예측 vs 실현)**\n":
        "**Reliability diagram (predicted vs realised)**\n",
    "\n**시변 베타 상세**\n": "\n**Time-varying beta detail**\n",
    "\n**읽는 법**": "\n**How to read this**",

    # ── delta panel column names ──────────────────────────────
    "Δ(표준충격)": "Δ (standard shock)",
    "Δ(하방베타)": "Δ (downside beta)",
    "β 안정성(CV)": "β stability (CV)",
    "상관(전체→하방꼬리)": "Correlation (overall → lower tail)",
    "R²(현재)": "R² (current)",
    "정적β 손익": "P&L (static β)",
    "하방β 손익": "P&L (downside β)",
    "ADV대비 참여율": "Participation rate vs ADV",
    "확률구간": "Probability bucket",
    "예측평균": "Mean predicted",
    "실현빈도": "Realised frequency",
    "**아니오**": "**No**",
    "**아니오 — 주의**": "**No — caution**",
    " ⚠ IGARCH 근방(지속성≈1)": " ⚠ near IGARCH (persistence ≈ 1)",

    # ── delta panel reading guide ─────────────────────────────
    "- `Δ(하방베타)`가 `Δ(표준충격)`보다 크면 **하방에서 노출이 확대**되는 "
    "비대칭 자산입니다. 정적 베타 스트레스는 이걸 놓칩니다.":
        "- If `Δ (downside beta)` exceeds `Δ (standard shock)`, the asset "
        "is asymmetric — **exposure widens to the downside**. Static-beta "
        "stress testing misses this.",
    "- `상관(전체→하방꼬리)`: 정상 국면 상관과 극단 국면 상관은 다른 "
    "숫자입니다. 분산투자 효과가 위기에 사라지는지 여기서 보입니다.":
        "- `Correlation (overall → lower tail)`: correlation in a normal "
        "regime and in an extreme one are different numbers. This is where "
        "you see whether diversification disappears in a crisis.",
    "- `β 안정성(CV)` > 0.8 이면 그 베타를 헤지 비율로 쓰면 안 됩니다.":
        "- If `β stability (CV)` exceeds 0.8, that beta must not be used "
        "as a hedge ratio.",
    "- `R²(현재)` 붕괴는 버그가 아니라 **구조 변화 신호**입니다. "
    "금-10년TIPS R²가 2005–2021 약 84%에서 2022년 이후 한 자릿수로 무너진 "
    "것이 대표 사례입니다.\n":
        "- A collapse in `R² (current)` is not a bug but **a signal of "
        "structural change**. The classic case is gold against 10-year "
        "TIPS, whose R² fell from roughly 84% over 2005–2021 to single "
        "digits after 2022.\n",

    # ── limitations table ─────────────────────────────────────
    "| 생존편향 | Yahoo Finance에는 상장폐지 종목이 없습니다. 종목선택 "
    "전략은 원리적으로 검증 불가합니다. |":
        "| Survivorship bias | Yahoo Finance carries no delisted names. "
        "Stock-selection strategies are unverifiable in principle. |",
    "| 인트라데이 | 일봉만 사용하므로 진짜 실현변동성·오더플로우는 계산 "
    "불가합니다. 프록시임을 명시했습니다. |":
        "| Intraday | Only daily bars are used, so true realised "
        "volatility and order flow cannot be computed. They are labelled "
        "as proxies. |",
    "| 펀더멘털 PIT | 재무 데이터는 리스테이트먼트가 반영된 값이라 "
    "point-in-time이 아닙니다. |":
        "| Fundamentals not point-in-time | Financial data reflects "
        "restatements and is not point-in-time. |",
    "| 옵션 히스토리 | 스냅샷만 제공되어 백테스트가 불가합니다. 오늘부터 "
    "축적해야 합니다. |":
        "| Option history | Only a snapshot is available, so no backtest "
        "is possible. It has to be accumulated from today. |",
    "| 체결 가정 | 신호 생성 종가가 아니라 다음 거래일 시가/VWAP 체결을 "
    "가정해야 합니다. 이 선택이 수익성을 뒤집을 수 있습니다. |":
        "| Fill assumption | Execution must be assumed at the next "
        "session's open or VWAP, not at the signal close. That choice can "
        "flip profitability. |",
    "| 세금·환율 | 반영되지 않았습니다. |":
        "| Tax and FX | Not included. |",

    "**엔진**: ": "**Engine**: ",
}
