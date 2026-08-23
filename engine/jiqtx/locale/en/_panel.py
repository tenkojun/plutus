# -*- coding: utf-8 -*-
"""
English — expert panel prose and the verdict language around it.

These are the longest strings in the report and they dominate the character
count, so they are translated first.

Deliberately **not** translated here: bare Korean particles emitted as
f-string fragments ('이 ', '가 ', '로 ', '일'). They carry no meaning on
their own and would only fire in the middle of sentences. The
Hangul-boundary rule already blocks most of those matches; leaving them out
of the catalog closes the rest of the door.
"""

CATALOG = {

    # ── sentence tails ────────────────────────────────────────
    # Emitted as f'...{value}입니다.' — the polite copula that closes a
    # Korean sentence. English needs only the stop.
    "입니다.": ".",

    # ── the red team / devil's advocate ───────────────────────
    "제 역할은 동의가 아니라 반증입니다. 사전등록된 프로토콜에 따라 최소 3개의 "
    "구체적 반대 근거를 제출할 의무가 있고, 제출하지 못하면 그 자체가 시스템 "
    "오류로 기록됩니다. 아래가 이번 분석에서 제가 찾은 취약점입니다. ":
        "My job is to falsify, not to agree. Under the pre-registered "
        "protocol I am obliged to file at least three concrete objections; "
        "failing to file them is itself logged as a system error. Here are "
        "the weaknesses I found in this analysis. ",

    "생존편향된 데이터 소스, 개발자 look-ahead, 그리고 이 코드가 전체 기간을 "
    "보고 작성됐다는 사실이 모두 이 결론에 유리하게 작용합니다. 실시간 페이퍼 "
    "트레이딩 기록이 없는 한 이 확신도는 정당화되지 않습니다.":
        "A survivorship-biased data source, developer look-ahead, and the "
        "plain fact that this code was written with the whole period in "
        "view all work in favour of this conclusion. Without a live "
        "paper-trading record, this level of confidence is not justified.",

    "사후에 만든 반증 조건은 의미가 없습니다. 분석 시점에 자동 생성해 원장에 "
    "남기고, 이후 채점 때 함께 검증합니다.":
        "A falsifier invented after the fact means nothing. They are "
        "generated automatically at analysis time, written to the ledger, "
        "and checked when the prediction is later scored.",

    # ── overfitting · PBO · DSR ───────────────────────────────
    "한 가지를 분명히 하겠습니다 — **PBO는 전략 선택 절차의 과적합을 재는 "
    "지표이지 신호의 존재를 재는 지표가 아닙니다.** 변형들이 사실상 동일하면 "
    "순위가 무작위가 되어 PBO가 기계적으로 0.5 근방에 나옵니다. 따라서 PBO는 "
    "소프트 게이트(불확실성 확대)로 쓰고, 하드 게이트는 전략 DSR로 겁니다.":
        "Let me be precise about one thing — **PBO measures overfitting in "
        "the strategy-selection procedure, not whether a signal exists.** "
        "When the variants are effectively identical the ranking becomes "
        "random and PBO lands near 0.5 mechanically. So PBO is used as a "
        "soft gate (it widens the uncertainty) and the hard gate is the "
        "strategy DSR.",

    "그리고 DSR은 시행횟수 N에 극도로 민감합니다. N을 로깅하지 않은 DSR 값은 "
    "의미가 없으며, 설정을 바꿀 때마다 N에 카운트해야 합니다.":
        "And DSR is extremely sensitive to the number of trials N. A DSR "
        "reported without logging N is meaningless, and every change of "
        "configuration has to count towards N.",

    "사전등록 후 실시간 페이퍼 트레이딩에서 12개월간 Brier skill이 양수로 "
    "유지되면 검증됐다고 인정하겠습니다.":
        "I will accept it as validated if, after pre-registration, Brier "
        "skill stays positive through twelve months of live paper trading.",

    "Murphy resolution이 0을 유의하게 상회하고 과적합 갭이 15%p 아래로 "
    "내려오면 확률을 제출합니다.":
        "I will submit a probability once Murphy resolution is "
        "significantly above zero and the overfit gap falls below 15pp.",

    "는 약한 신호가 아니라 신호 없음입니다. 이 상황에서 감점된 확률을 내놓는 "
    "것은 없는 정보를 있는 것처럼 만드는 일이므로, 저는 기권합니다.":
        " is not a weak signal but no signal. Publishing a marked-down "
        "probability here would manufacture information that does not "
        "exist, so I abstain.",

    "는 기저율 이상의 정보가 없다는 뜻입니다. 감점된 확률을 내는 것이 아니라 "
    "출력을 무효화해야 합니다.":
        " means there is no information beyond the base rate. The right "
        "response is to invalidate the output, not to publish a "
        "marked-down probability.",

    # ── execution assumptions · costs ─────────────────────────
    "[체결 가정] 신호 생성 종가가 아니라 다음 거래일 시가/VWAP 체결을 "
    "가정해야 한다. 이 선택 하나가 수익성을 뒤집을 수 있다.":
        "[Fill assumption] You must assume execution at the next session's "
        "open or VWAP, not at the close that generated the signal. That "
        "single choice can flip profitability.",

    "신호 생성 종가가 아니라 다음 거래일 시가/VWAP를 가정해야 합니다. 이 "
    "선택이 수익성을 뒤집을 수 있습니다.":
        "You must assume the next session's open or VWAP, not the close "
        "that generated the signal. That choice can flip profitability.",

    "일이 걸립니다 — 급매 국면에서는 이 값이 몇 배로 늘어납니다. 체결은 신호 "
    "생성 종가가 아니라 **다음 거래일 시가/VWAP**를 가정해야 하며, 이 선택 "
    "하나가 수익성을 뒤집을 수 있습니다.":
        " days — and in a forced-selling regime that figure multiplies. "
        "Execution has to be assumed at the **next session's open or "
        "VWAP**, not at the signal close, and that one choice can flip "
        "profitability.",

    "임팩트는 제곱근 법칙 G ≈ Y·σ_d·√(Q/ADV) 기준. 선형 모델은 대형 주문 "
    "비용을 극심하게 과소평가합니다.":
        "Impact follows the square-root law G ≈ Y·σ_d·√(Q/ADV). A linear "
        "model understates the cost of large orders severely.",

    "bp이므로 측정 자체의 불확실성도 함께 감안해야 합니다. AUM 1%를 ADV의 "
    "10%씩 처분하면 ":
        "bp, so the uncertainty in the measurement itself has to be "
        "carried too. Liquidating 1% of AUM at 10% of ADV per day takes ",

    "일봉 VPIN/CVD 프록시는 체결방향을 모르므로 정보 함량이 사실상 0입니다. "
    "EDGE(JFE 2024)는 OHLC 전부를 최적 결합해 거래가 희소해도 편향되지 "
    "않습니다.":
        "Daily-bar VPIN and CVD proxies do not know trade direction, so "
        "their information content is essentially zero. EDGE (JFE 2024) "
        "combines the full OHLC optimally and stays unbiased even when "
        "trading is sparse.",

    # ── factor model · hedging ────────────────────────────────
    " 의 베타 변동계수가 0.8 초과. 헤지 비율로 사용 불가.":
        " has a beta coefficient of variation above 0.8. It cannot be used "
        "as a hedge ratio.",

    ")의 55% 아래로 내려가거나 롤링 R²가 과거 중앙값의 35% 미만이 되면 팩터 "
    "해석 전체를 철회합니다.":
        "), or if the rolling R² falls below 35% of its historical median, "
        "I withdraw the factor interpretation entirely.",

    ". 최소분산 헤지비율은 다변량 팩터 회귀 계수와 동일하므로, 팩터 모델이 "
    "무효면 헤지도 함께 무효입니다.":
        ". The minimum-variance hedge ratio is the multivariate factor "
        "regression coefficient, so if the factor model is void the hedge "
        "is void with it.",

    "원본 리포트는 '주식베타 0.20 × 지수충격'으로 스트레스를 만들었습니다. "
    "금에 주식 베타를 곱하는 것은 의미가 없습니다.":
        "The original report built its stress case as 'equity beta 0.20 × "
        "index shock'. Multiplying gold by an equity beta is meaningless.",

    "기대 R²가 밴드 하단 미만이면 이벤트/특수상황 플래그.":
        "If the expected R² is below the bottom of the band, flag it as an "
        "event or special-situation name.",

    # ── distribution · probability ────────────────────────────
    "90% 구간은 통계적 신뢰구간이나 목표주가가 아니라 모델 가정 하의 "
    "시뮬레이션 분위입니다. VaR은 최대손실이 아니라 하위 5% 경계값입니다.":
        "The 90% band is not a statistical confidence interval or a price "
        "target — it is a simulation quantile under the model's "
        "assumptions. VaR is not the maximum loss but the lower 5% "
        "boundary.",

    "드라이버가 중립일 때. 잔차 드리프트만 반영. 경험확률은 표본 기간의 "
    "무조건부 빈도이므로 그 기간의 드리프트를 그대로 물려받는다 — 상승장 "
    "표본에서는 강세 시나리오 확률이 구조적으로 높다.":
        "With drivers neutral, reflecting residual drift only. The "
        "empirical probability is the unconditional frequency over the "
        "sample period, so it inherits that period's drift wholesale — in "
        "a bull-market sample the bullish scenario is structurally "
        "over-weighted.",

    "옵션 체인이 없어 시장 함축 분포를 확인할 수 없습니다. 이 경우 우리 모델 "
    "분포를 검증할 외부 기준이 없다는 뜻이므로, 분포 기반 확률을 더 "
    "보수적으로 읽어야 합니다.":
        "There is no option chain, so the market-implied distribution "
        "cannot be checked. That means no external benchmark exists to "
        "validate our model distribution, and any distribution-based "
        "probability should be read more conservatively.",

    " — 불일치가 크므로 통합 확률을 0.5 쪽으로 축소. 단순 평균은 정보를 "
    "파괴한다(원본 리포트가 단기/중기/장기 점수를 평균해 67점을 만든 지점).":
        " — the disagreement is large, so the pooled probability is shrunk "
        "towards 0.5. A plain average destroys information (this is "
        "exactly where the original report averaged its short, mid and "
        "long scores into a single 67).",

    "표본이 늘어 SE(μ̂)가 |μ̂|의 절반 아래로 내려오면 기대수익 기반 논지를 "
    "받아들이겠습니다.":
        "Once the sample grows enough that SE(μ̂) falls below half of "
        "|μ̂|, I will accept an expected-return argument.",

    "**입니다. 이 차이는 시장에 대한 것이 아니라 우리가 무엇을 안다고 "
    "가정했는지에 대한 것입니다.":
        "**. That difference is not about the market — it is about what we "
        "assumed we knew.",

    # ── evidence hierarchy · adjudication ─────────────────────
    ") — 통계적으로 0과 구별되지 않습니다. 방향을 단정할 근거가 없습니다.":
        ") — statistically indistinguishable from zero. There is no basis "
        "for asserting a direction.",

    ")은 피고발 주장보다 상위 증거입니다. 해당 주장은 하향 조정됩니다.":
        ") outranks the challenged claim in the evidence hierarchy. That "
        "claim is marked down.",

    "). 주장을 기각하지는 않되 신뢰구간을 확대합니다.":
        "). The claim is not rejected, but the confidence interval widens.",

    "발동된 조건이 있습니다. 해당 모듈의 출력은 이미 신뢰 구간을 벗어났을 수 "
    "있으며, 조치 열에 적힌 대로 처리해야 합니다.":
        "conditions have fired. Those modules' outputs may already be "
        "outside their trustworthy range and must be handled as the action "
        "column specifies.",

    "스트레스 손실이 한도 아래로 내려오고 VaR 모델이 조건부 커버리지 검정을 "
    "통과하면 사이즈 허용으로 전환합니다.":
        "Once the stress loss drops below the limit and the VaR model "
        "passes its conditional coverage test, I will allow sizing again.",

    "로 1 미만입니다. 승률이 손익분기를 넘어야만 성립하는 구조이므로, "
    "**승률 가정이 조금만 틀려도 기대값이 뒤집힙니다.** 저는 이런 구조를 "
    "풀사이즈로 잡지 않습니다.":
        ", below 1. The structure only works if the hit rate clears "
        "breakeven, which means **a small error in the hit-rate "
        "assumption flips the expected value.** I do not take a structure "
        "like this at full size.",

    # ── survivorship · data limits ────────────────────────────
    "[생존편향] Yahoo Finance에는 상장폐지 종목이 없다. 이 분석은 "
    "'오늘 존재하는 종목'만 본다.":
        "[Survivorship bias] Yahoo Finance carries no delisted names. This "
        "analysis only ever sees the tickers that still exist today.",

    "Yahoo Finance에 상장폐지 종목이 없습니다. 종목선택 전략은 원리적으로 "
    "검증 불가합니다.":
        "Yahoo Finance has no delisted names. Stock-selection strategies "
        "are unverifiable in principle.",

    " 다만 **상장폐지 종목이 없는 데이터 소스**라는 점은 구조적 한계이며, "
    "종목선택 전략 검증에는 쓸 수 없습니다.":
        " That said, **a data source without delisted names** is a "
        "structural limitation, and it cannot be used to validate "
        "stock-selection strategies.",

    "본 산출물은 방법론 검증용 정보 제공이며 투자 자문이 아니다. 확률은 모델 "
    "가정에 조건부이며, 미래 성과를 보장하지 않는다.":
        "This output is information for methodology validation and is not "
        "investment advice. The probabilities are conditional on the "
        "model's assumptions and guarantee nothing about future "
        "performance.",

    "단일 점수는 산출하지 않습니다. 서로 다른 성질의 정보를 하나의 숫자로 "
    "합치면 정보가 파괴됩니다.":
        "No single score is produced. Merging different kinds of "
        "information into one number destroys it.",

    # ── short labels that recur constantly ────────────────────
    "시나리오": "Scenario",
    "확률": "Probability",
    "팩터": "Factor",
    "판정": "Verdict",
    "모델": "Model",
    "심사 항목": "Check",
    "자산군": "Asset class",
    "전략 DSR": "Strategy DSR",
    "드리프트 ": "Drift ",
    "국면": "Regime",
    "데이터 무결성": "Data integrity",
    "데이터 무결성 책임자": "Data integrity officer",
    "트레이드 구성 — 진입 · 손절 · 목표 · 기대값":
        "Trade construction — entry · stop · target · expected value",
    "메타데이터 + 수익률 통계지문 (가격 수준 미열람)":
        "Metadata + return statistical fingerprint (price levels not read)",
    "포지션 손익의 최대 단일 기여 요인":
        "Largest single contributor to position P&L",
    "[예측력 부재] ML 판정 ABSTAIN. resolution ":
        "[No predictive power] ML verdict ABSTAIN. resolution ",
    " ≤ 0 → 상수 예측만도 못함": " ≤ 0 → worse than a constant forecast",
    ". 방향 신호를 근거로 쓸 수 없다.":
        ". The directional signal cannot be used as a basis.",
    ") → 다중검정 보정 후 유의성 부족":
        ") → not significant after multiple-testing adjustment",
}
