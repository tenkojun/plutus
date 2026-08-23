# -*- coding: utf-8 -*-
"""
English — the last of the HTML-path modules: panel tails, ML gates,
chart titles, simulation notes, options, microstructure, regime.

'로 ' is included here for the same reason as the subject markers in
``_dynamic1``: as a standalone f-string fragment it is an instrumental
particle sitting right before a tag or a value, and the Hangul-boundary
rule stops it firing inside running Korean text.
"""

CATALOG = {

    # ══ panel.py — tails ══════════════════════════════════════
    "건 중 미해결 쟁점 ": " raised, of which unresolved: ",
    "건이 남았습니다.": ".",
    "의 t값이 ": " has a t-value of ",
    "IV−RV 스프레드 ": "The IV−RV spread of ",
    "는 분산위험프리미엄 프록시이며, ":
        " is a variance-risk-premium proxy, and ",
    "양수이므로 시장이 실현변동성보다 비싸게 보험을 팔고 있습니다 — 옵션 "
    "매도가 구조적으로 유리한 환경.":
        "being positive means the market is selling insurance above "
        "realised volatility — structurally favourable for selling "
        "options.",
    "음수이므로 옵션이 실현변동성 대비 싸며, 보호 매수가 상대적으로 "
    "유리합니다.":
        "being negative means options are cheap against realised "
        "volatility, so buying protection is relatively attractive.",
    "R:R이 ": "The R:R of ",
    "β 변동계수가 0.8을 넘는 레그: ":
        "Legs with a β coefficient of variation above 0.8: ",
    "로 변형 선택이 불안정합니다. 신호 존재를 부정하지는 않으나 신뢰구간을 "
    "확대해 읽어야 합니다.":
        " makes the variant selection unstable. That does not deny a "
        "signal exists, but the confidence interval should be read wider.",
    "시뮬레이션 상승확률 ": "The simulated probability of a rise is ",
    "목표가 ": "Target price ",
    "드리프트 표준오차 ": "Drift standard error ",
    "비용 후 기대손익 ": "Expected P&L after costs ",
    "가 기대손익의 30%를 넘게 잠식합니다. 회전이 늘면 엣지가 빠르게 "
    "소멸합니다.":
        " eats more than 30% of the expected P&L. As turnover rises the "
        "edge disappears quickly.",
    "서사": "Narrative",
    "부분 인용 — '": "Partially cited — '",
    "미해결 쟁점으로 기록 — '": "Recorded as unresolved — '",
    "사후 드리프트 ": "Posterior drift ",
    "알파 t값이 ": "The alpha t-value of ",

    # ══ ml.py ═════════════════════════════════════════════════
    "scikit-learn 미설치": "scikit-learn is not installed",
    "유효 Purged CV 분할 부족":
        "Not enough valid purged-CV splits",
    " ≈ 0 → 기저율 이상의 정보 없음":
        " ≈ 0 → no information beyond the base rate",
    "개 < 300": " < 300",
    "PBO 산출 실패: ": "PBO could not be computed: ",
    "확률 신뢰구간 [": "The probability interval [",
    "] 가 0.5를 포함 → 방향 우위 미확인":
        "] includes 0.5 → no directional edge established",

    # ══ charts.py ═════════════════════════════════════════════
    "신뢰도 다이어그램": "Reliability diagram",
    "상관 행렬": "Correlation matrix",
    "지평 비교": "Horizon comparison",
    "기여도": "Contribution",
    "예측 확률": "Predicted probability",

    # ══ simulate.py ═══════════════════════════════════════════
    "수수료·세금·허들 반영 후 값. 환율·추적오차는 미반영. '물가 초과'와 "
    "'예금 초과'가 같은 3% 기준이면 하나의 명목 허들 초과확률로 해석해야 "
    "한다.":
        "Net of fees, tax and the hurdle. FX and tracking error are not "
        "included. If 'beats inflation' and 'beats deposits' use the same "
        "3% bar, read them as a single probability of clearing one nominal "
        "hurdle.",
    "GPD 꼬리 적합 실패 → 경험분포 재샘플로 대체":
        "GPD tail fit failed → resampling the empirical distribution "
        "instead",
    "GARCH 잔차 부족 → 원시 표준화 수익률 사용":
        "Not enough GARCH residuals → using raw standardised returns",
    "GARCH 미수렴 → 정적 분산 사용":
        "GARCH did not converge → using static variance",
    "x 일간 리밸런싱 경로 재구성 (변동성 드래그 반영)":
        "× daily-rebalanced path reconstructed (volatility drag included)",

    # ══ options.py ════════════════════════════════════════════
    "IV−RV 스프레드는 분산위험프리미엄 프록시. 양수면 시장이 실현변동성보다 "
    "비싸게 보험을 팔고 있다는 뜻. 옵션 스냅샷은 히스토리가 없어 백테스트 "
    "불가.":
        "The IV−RV spread is a variance-risk-premium proxy. Positive means "
        "the market is selling insurance above realised volatility. An "
        "option snapshot has no history, so it cannot be backtested.",
    "시장 함축 확률분포. 위험중립 측도이므로 리스크 프리미엄이 포함돼 있어 "
    "실세계 확률과 동일하지 않다. 우리 모델 분포와 겹쳐 보고 '차이'를 논지로 "
    "삼는 것이 올바른 용법.":
        "The market-implied probability distribution. It is a risk-neutral "
        "measure, so it embeds a risk premium and is not the real-world "
        "probability. The correct use is to overlay it on our model "
        "distribution and make the gap the thesis.",
    "모델이 시장보다 강세": "Our model is more bullish than the market",
    "모델이 시장보다 약세": "Our model is more bearish than the market",
    "모델과 시장이 사실상 동일 — 방향성 엣지 없음":
        "Model and market are effectively the same — no directional edge",

    # ══ micro.py ══════════════════════════════════════════════
    "스프레드 추정 불가": "Spread cannot be estimated",
    " < 한도 $": " < limit $",
    "bp > 한도 ": "bp > limit ",

    # ══ regime.py ═════════════════════════════════════════════
    "횡보": "Sideways",
}
