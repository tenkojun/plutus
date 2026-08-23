# -*- coding: utf-8 -*-
"""
English — remaining panel opinions, trade/hedge construction, macro board.
"""

CATALOG = {

    # ══ panel.py ══════════════════════════════════════════════
    "모델 분포와 시장 RND가 5%p 이내로 수렴하면 방향성 엣지가 없다고 "
    "판단합니다.":
        "If the model distribution and the market RND converge to within "
        "5pp, I judge that there is no directional edge.",
    "제 반론이 더 높은 위계의 증거로 반박되면 철회합니다. 다만 '그럴듯하다'는 "
    "이유로는 철회하지 않습니다.":
        "I withdraw an objection when higher-tier evidence rebuts it. I do "
        "not withdraw it because something merely sounds plausible.",
    "서사·정성": "Narrative / qualitative",
    "옵션 스냅샷은 히스토리가 없어 백테스트가 불가합니다. 오늘부터 매일 "
    "축적해야 1년 뒤 검증이 가능합니다.":
        "An option snapshot has no history, so it cannot be backtested. "
        "Accumulate it daily from today and it becomes testable in a year.",
    "질문은 '얼마나 벌 수 있나'가 아니라 '틀렸을 때 얼마를 잃나'다.":
        "The question is not how much you can make but how much you lose "
        "when you are wrong.",
    "판정 엔진이 사이즈 0을 냈으므로 실행할 트레이드가 없습니다. 아래 계획은 "
    "조건이 충족됐을 때를 위한 참고입니다. 다만 분명히 해두겠습니다 — 이것은 "
    "약세 판단이 아니라 '현 조건에서 포지션을 잡을 수 없다'는 뜻입니다.":
        "The verdict engine returned size zero, so there is no trade to "
        "execute. The plan below is for reference once the conditions are "
        "met. To be clear: this is not a bearish call — it means a "
        "position cannot be taken under current conditions.",
    "이 데이터로는 아래 어떤 분석도 신뢰할 수 없습니다. ":
        "No analysis below can be trusted on this data. ",
    ". 조정종가 정합성이 깨졌다면 수익률 자체가 틀린 것이므로 변동성·샤프·"
    "베타가 모두 오염됩니다. 재수집 전까지 중단을 권고합니다.":
        ". If adjusted-close consistency is broken, the returns themselves "
        "are wrong and volatility, Sharpe and beta are all contaminated. I "
        "recommend halting until the data is re-collected.",
    "주말 거래가 관측되므로 24/7 시장이며, 연율화를 √365로 해야 합니다. "
    "√252를 쓰면 변동성이 약 17% 과소평가됩니다.":
        "Weekend trading is observed, so this is a 24/7 market and "
        "annualisation must use √365. Using √252 understates volatility by "
        "about 17%.",
    "분류 신뢰도가 낮으므로 자산군 특화 해석을 강하게 적용하지 말고 최소 "
    "사이즈만 허용해야 합니다.":
        "Classification confidence is low, so asset-class-specific "
        "interpretation should not be applied strongly and only a minimum "
        "size should be allowed.",
    "팩터 데이터가 없어 의견을 낼 수 없습니다.":
        "There is no factor data, so I cannot give an opinion.",
    "매크로 델타를 산출하지 못했습니다.":
        "The macro deltas could not be computed.",
    "다만 이 팩터의 롤링 R²가 최근 급락했습니다. **과거 베타로 계산한 위 "
    "수치는 이미 틀렸을 수 있습니다.** 재추정 전에는 매크로 시나리오를 근거로 "
    "사이즈를 키우면 안 됩니다.":
        "That said, this factor's rolling R² has fallen sharply. **The "
        "figures above, computed from the old beta, may already be "
        "wrong.** Do not increase size on a macro scenario before "
        "re-estimating.",
    "체결 관점에서 이 종목은 거래 대상이 아닙니다. ":
        "From an execution standpoint this name is not tradable. ",
    ". 백테스트 상 어떤 엣지가 나오든 이 비용을 통과하지 못합니다. 참고로 "
    "일봉 VPIN/CVD 프록시는 체결방향을 모르므로 정보 함량이 사실상 0이며, "
    "저는 EDGE 스프레드만 봅니다.":
        ". Whatever edge a backtest shows, it does not survive this cost. "
        "For the record, daily-bar VPIN and CVD proxies do not know trade "
        "direction and carry essentially no information; I look only at "
        "the EDGE spread.",
    "방향 예측 모듈을 실행하지 않았습니다.":
        "The direction forecast module was not run.",
    "게이트를 통과했습니다. 승자 모델은 ":
        "It passed the gate. The winning model is ",
    "이며 OOS 정확도 ": " with an out-of-sample accuracy of ",
    "(기저율 ": "(base rate ",
    "), 과적합 갭 ": "), overfit gap ",
    "로 기저율 이상의 정보가 확인됩니다. 보정 후 상승확률은 ":
        ", confirming information beyond the base rate. The calibrated "
        "probability of a rise is ",
    "이고 신뢰구간은 [": " with a confidence interval of [",
    "]로 50%를 배제합니다. 전략 DSR ":
        "], which excludes 50%. The strategy DSR of ",
    "로 다중검정 보정 후에도 유의합니다.":
        " remains significant after adjusting for multiple testing.",
    "국면 식별에 실패했습니다.": "Regime identification failed.",
    "시뮬레이션을 실행하지 못했습니다.": "The simulation could not be run.",
    "**표준오차가 추정치 자체보다 큽니다.** 즉 이 드리프트는 '모른다'와 "
    "통계적으로 구별되지 않으며, 기대수익 기반 사이징은 정당화되지 않습니다.":
        "**The standard error exceeds the estimate itself.** This drift is "
        "statistically indistinguishable from 'we do not know', and sizing "
        "on expected return is not justified.",
    "스트레스 한도를 초과합니다. ": "The stress limit is exceeded. ",
    " 손실이 예상되며 이는 한도 ": " of loss is expected, against a limit of ",
    "VaR95는 ": "VaR95 is ",
    " 다만 어떤 VaR 모델도 커버리지 검정을 통과하지 못했으므로, 제시된 수치를 "
    "액면대로 믿지 마십시오.":
        " However, no VaR model passed its coverage test, so do not take "
        "these figures at face value.",
    "트레이드 계획을 구성하지 못했습니다.":
        "A trade plan could not be constructed.",
    "헤지 설계 정보가 없습니다.": "There is no hedge design information.",
    "현 시점에서 제가 차단할 항목은 없습니다. 다만 통과는 '검증됐다'가 아니라 "
    "'아직 반증되지 않았다'는 뜻입니다.":
        "I have nothing to block at this point. But passing means 'not yet "
        "falsified', not 'validated'.",
    "이번에는 유의한 취약점을 찾지 못했습니다 — 이 경우 오히려 제 탐색 범위를 "
    "의심해야 합니다.":
        "I found no material weakness this time — which is a reason to "
        "suspect the scope of my own search.",
    "헤지를 통한 위험 통제": "Risk control through hedging",
    "거부권 ": "Veto ",
    "조정종가 누적수익이 원종가를 ":
        "The adjusted-close cumulative return exceeds the raw close by ",
    " 상회해 배당 반영이 정상으로 보입니다.":
        ", so dividend adjustment looks correct.",
    "1차 자기상관 ": "First-order autocorrelation ",
    "로 수익률 평활화가 의심됩니다. 언스무딩 없이 산출한 샤프는 "
    "과대평가입니다.":
        " suggests the returns are smoothed. A Sharpe computed without "
        "unsmoothing is overstated.",
    "로 이 자산군 기대밴드 하단을 크게 밑돕니다. 잔차 ":
        ", far below the floor of this asset class's expected band. The "
        "residual ",
    "를 '고유위험'이라 부르면 안 됩니다 — 이것은 **누락 변수**입니다.":
        " must not be called idiosyncratic risk — it is an **omitted "
        "variable**.",
    "인 회귀에서 나온 알파 ": " regression produces an alpha of ",
    "하방 구간 베타를 쓰면 ": "Using the downside-quantile beta gives ",
    "기간구조가 ": "The term structure is ",
    "로 백워데이션입니다 — 시장이 단기 스트레스를 가격에 반영하고 있습니다.":
        " — in backwardation, meaning the market is pricing near-term "
        "stress.",
    "우리 모델 상승확률 ": "Our model's probability of a rise is ",
    " vs 시장 위험중립 ": " against the market's risk-neutral ",
    ". 위험중립 확률에는 리스크 프리미엄이 포함돼 있으므로 실세계 확률과 같지 "
    "않지만, **차이의 방향과 크기가 곧 논지**입니다.":
        ". Risk-neutral probabilities embed a risk premium and are not "
        "real-world probabilities, but **the direction and size of the gap "
        "is the thesis**.",
    "다만 관측 구간에서 국면 전환이 ":
        "That said, the observation window contains only ",
    "회뿐입니다. **다른 국면에서의 행태는 사실상 검증되지 않았으므로** 제 "
    "의견의 확신도를 낮춰 읽으십시오.":
        " regime transitions. **Behaviour in other regimes is effectively "
        "untested**, so read my confidence down accordingly.",
    "관측 구간의 국면 전환이 ":
        "The observation window contains only ",
    "회뿐입니다. 현재 국면 밖에서 이 베타가 유지된다는 증거가 없습니다.":
        " regime transitions. There is no evidence this beta holds outside "
        "the current regime.",
    "제거 가능 분산이 ": "The removable variance is ",
    "모델 상승확률 ": "Model probability of a rise ",
    "시장 위험중립 확률은 ": "The market's risk-neutral probability is ",
    "p 차이납니다. 리스크 프리미엄으로 전부 설명되지 않는 크기라면 모델을 "
    "먼저 의심해야 합니다.":
        "p apart. If the gap is larger than a risk premium can explain, "
        "suspect the model first.",
    "반론 인용 — '": "Objection cited — '",
    "'(위계 ": "' (tier ",
    "극단 이동(|일간|>40%)": "Extreme move (|daily| > 40%)",
    "최신성": "Freshness",
    "성공": "Success",
    "행(": "rows (",
    "로 **": " → **",
    " > 한도 ": " > limit ",
    ", 진입 ": ", entry ",
    "), 목표 ": "), target ",
    " × 사이즈로 계좌 손실이 ": " × size gives an account loss of ",
    "가 되어 단일 트레이드 예산 2%를 초과합니다.":
        ", which exceeds the 2% single-trade budget.",
    " 기반 매크로 논지": "-based macro thesis",
    "기간구조 (3M−1M)": "Term structure (3M − 1M)",
    "1개월 ATM IV ": "One-month ATM IV ",
    ", 25Δ 리스크리버설 ": ", 25Δ risk reversal ",
    " · 약세 ": " · bearish ",
    " · 중립 ": " · neutral ",
    " · 기권 ": " · abstain ",
    ". 반대신문 ": ". Cross-examinations ",

    # ══ trade.py ══════════════════════════════════════════════
    "IWM/SPY 스프레드": "IWM/SPY spread",
    "IWD/IWF 스프레드": "IWD/IWF spread",
    "TIP / 10y TIPS 선물": "TIP / 10y TIPS futures",
    "TLT / ZN 선물": "TLT / ZN futures",
    "SHY / ZT 선물": "SHY / ZT futures",
    "ZN-ZT 커브 스프레드": "ZN-ZT curve spread",
    "TIP-IEF 스프레드": "TIP-IEF spread",
    "UUP / DX 선물": "UUP / DX futures",
    "VIX 선물 / VXX": "VIX futures / VXX",
    "USO / CL 선물": "USO / CL futures",
    "BTC 선물": "BTC futures",
    "헤지 불가 (거래 가능한 상품 없음)":
        "Cannot hedge (no tradable instrument)",
    "헤지 무효 — 팩터 미스매칭": "Hedge void — factors mismatched",
    "σ 지평 변동성 (시나리오 미가용)":
        "σ horizon volatility (no scenario available)",
    "시나리오에서 목표를 도출하지 못해 변동성 배수로 대체":
        "No target could be derived from the scenarios, so a volatility "
        "multiple is used instead",
    "시뮬 경로 미저장 → 배리어 확률 산출 불가":
        "Simulated paths were not stored → barrier probabilities cannot be "
        "computed",
    "판정 보류 — 배리어 확률 미산출":
        "Verdict withheld — barrier probabilities not computed",
    "팩터 모델 없음 → 헤지 설계 불가":
        "No factor model → the hedge cannot be designed",
    "헤지 불필요 — 유의한 팩터 노출 없음":
        "No hedge needed — no significant factor exposure",
    "총노출 유지": "Gross exposure retained",
    "부분 중립": "Partially neutral",
    " > 예산 ": " > budget ",
    "기대값 음수 — 진입 부적합":
        "Negative expected value — not suitable for entry",
    "팩터 회귀가 없으면 최소분산 헤지비율을 정의할 수 없다":
        "Without a factor regression there is no minimum-variance hedge "
        "ratio to define",
    "헤지로 제거 가능한 분산이 ":
        "The variance removable by hedging is ",
    "배리어 확률로 계산한 비용 후 기대손익이 0 이하":
        "Expected P&L after costs, computed from barrier probabilities, is "
        "at or below zero",
    "부분 헤지만 가능 (": "Only a partial hedge is possible (",
    " 레그)": " legs)",
    "약세 시나리오 (": "Bear scenario (",
    "엣지 없음 — 손익분기 승률 미달":
        "No edge — below the breakeven hit rate",
    " — 헤지비율이 불안정해 오히려 위험을 추가할 수 있음":
        " — the hedge ratio is unstable and could add risk instead",
    "β 변동계수 0.8 초과 레그: ":
        "Legs with a β coefficient of variation above 0.8: ",
    " 는 ": " and ",
    " 와 상관 ": " have a correlation of ",
    " — 헤지 레그 중복이므로 제외":
        " — a duplicate hedge leg, so it is dropped",
    " < 1 — 승률(": " < 1 — the hit rate (",

    # ══ macro_board.py ════════════════════════════════════════
    "5년 실질금리": "5-year real yield",
    "2년 국채금리": "2-year treasury yield",
    "수익률곡선 2s10s": "Yield curve 2s10s",
    "투자등급 스프레드": "Investment-grade spread",
    "WTI 유가": "WTI crude",
    "주식시장 (SPY)": "Equity market (SPY)",
    "지정학 리스크 지수": "Geopolitical risk index",
    "지지": "Support",
    "역풍": "Headwind",
    "t 미산출": "t not computed",
    "오르면 유리": "Helps when it rises",
    "오르면 불리": "Hurts when it rises",
    ". 최근 3개월 ": ". Over the last three months it moved ",
    " 방향이었습니다.": ".",
    "보합": "Flat",
    "우호적": "Favourable",
    " · 최대 역풍 ": " · largest headwind ",
    ") · 최대 지지 ": ") · largest support ",
    "의 기대 팩터 설명력 밴드는 ":
        "'s expected factor explanatory band is ",
    " 입니다.": ".",
    "'영향' 열은 서술이 아니라 계산입니다 — sign(추정 베타) × sign(최근 3개월 "
    "변화). |t| < 2 인 변수는 통계적으로 0과 구별되지 않으므로 방향을 말하지 "
    "않고 중립으로 둡니다. 베타는 단변량 추정이라 그 변수에 딸려 오는 동반 "
    "움직임을 포함합니다.":
        "The 'impact' column is a calculation, not prose — sign(estimated "
        "beta) × sign(3-month change). Variables with |t| < 2 are "
        "statistically indistinguishable from zero, so no direction is "
        "stated and they are left neutral. The betas are univariate and so "
        "include the co-movement that travels with each variable.",
    "최근 3개월 거시 기여 합 ":
        "Total macro contribution over three months ",
    "약세 우위": "Bearish tilt",
    "상승 우위": "Upward tilt",
    " — 방향성 미미": " — barely directional",
    "하락 우위": "Downward tilt",
    "우호 전환": "Turning favourable",
    "혼조": "Mixed",
    "역풍 연장": "Headwind persisting",
}
