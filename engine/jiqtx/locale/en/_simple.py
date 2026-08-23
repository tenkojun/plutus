# -*- coding: utf-8 -*-
"""
English — the plain-language "quick research" report.

The Korean here is deliberately written for someone who is not a quant, so
the English keeps the same register: short sentences, no jargon left
unexplained, concrete money amounts.
"""

CATALOG = {

    # ── page chrome ───────────────────────────────────────────
    " 간단 리서치 — Plutus": " quick research — Plutus",
    " · 분석일 ": " · analysed ",

    # ── question headings ─────────────────────────────────────
    "이건 어떤 종목인가요?": "What is this?",
    "얼마나 위험한가요?": "How risky is it?",
    "지금 흐름은 어떤가요?": "What is the trend right now?",
    "무엇이 이 종목을 움직이나요?": "What moves this?",
    "얼마나 사야 하나요?": "How much should you buy?",
    "무엇을 보면 판단이 틀렸다는 걸 아나요?":
        "What would tell you the call was wrong?",
    "이 분석이 모르는 것": "What this analysis does not know",

    # ── verdicts ──────────────────────────────────────────────
    "매수 검토": "Consider buying",
    "관망": "Wait",
    "회피": "Avoid",
    "매도 검토": "Consider selling",
    "조건이 갖춰졌다고 봅니다. 다만 아래 위험 크기를 먼저 확인하세요.":
        "The conditions look met. Check the size of the risk below first.",
    "지금 새로 들어갈 근거가 뚜렷하지 않습니다. 이미 갖고 있다면 유지.":
        "There is no clear reason to open a new position now. If you "
        "already hold it, hold.",
    "지금은 들어가지 않는 게 낫습니다. ": "Better not to enter right now. ",
    "약세 전망이 아니라": "This is not a bearish view",
    ", 판단 근거가 부족하거나 위험 한도에 걸렸다는 뜻입니다.":
        " — it means there is not enough basis, or a risk limit binds.",
    "피하는 것을 권합니다.": "Best avoided.",
    "줄이는 것을 검토하세요.": "Consider reducing.",
    "진입을 막은 조건": "What blocked entry",

    # ── explanatory notes ─────────────────────────────────────
    "자산 종류에 따라 ": "Different kinds of asset ",
    "봐야 할 것이 다릅니다.": "need different things looked at.",
    " 금은 실질금리와 달러가, 국채는 금리와 커브가, 개별주는 시장·변동성·"
    "신용이 핵심입니다. 이 보고서는 이 종목에 맞는 것만 골라 보여 줍니다.":
        " For gold it is real rates and the dollar; for treasuries, rates "
        "and the curve; for a single stock, the market, volatility and "
        "credit. This report shows only the ones that fit this asset.",

    "변동성은 ": "Volatility is ",
    "방향이 아니라 폭": "size, not direction",
    "입니다. 크다고 나쁜 게 아니라 그만큼 흔들린다는 뜻이고, 그 흔들림을 "
    "견딜 수 있는 금액만 넣어야 합니다.":
        ". A large number is not bad in itself — it means it moves that "
        "much, and you should only put in an amount you can watch move "
        "that much.",

    "짧은 기간의 수익률은 ": "Returns over a short window are ",
    "운의 비중이 큽니다.": "mostly luck.",
    " 3개월 +20% 는 실력의 증거가 되기 어렵습니다.":
        " +20% over three months is not evidence of skill.",

    "여기 없는 변수는 ": "Variables that are not shown here were ",
    "연결이 뚜렷하지 않아 뺀 것":
        "left out because the link was not clear",
    "입니다. 통계적으로 구별되지 않는 관계로 이야기를 만들면 그럴듯하지만 "
    "틀립니다.":
        ". Building a story on a relationship you cannot distinguish "
        "statistically sounds convincing and is wrong.",

    "이 조건들은 ": "These conditions were set ",
    "분석 시점에 미리": "in advance, at the time of the analysis",
    " 정한 것입니다. 일이 벌어진 뒤에 만든 기준은 아무것도 반증하지 "
    "못합니다.":
        ". A criterion invented after the event falsifies nothing.",

    "이 목록은 겸손이 아니라 ": "This list is not modesty — it is ",
    "사용 설명서": "the manual",
    "입니다. 모르는 것을 아는 척하지 않는 것이 이 엔진의 원칙입니다.":
        ". Not pretending to know what it does not know is this engine's "
        "principle.",

    "과거 데이터에 ": "The historical data has ",
    "상장폐지된 종목이 없습니다.": "no delisted companies in it.",
    " 살아남은 것만 보고 있다는 뜻이라, 종목을 고르는 능력은 원리적으로 "
    "검증할 수 없습니다.":
        " That means you only ever see the survivors, so the ability to "
        "pick stocks cannot be verified in principle.",

    "펀더멘털은 ": "The fundamentals are ",
    "지금 시점의 값": "today's values",
    "입니다. 과거 어느 시점에 무엇을 알 수 있었는지는 재현되지 않습니다.":
        ". What was actually knowable at some past date is not "
        "reconstructed.",

    "이 보고서는 매수·매도 권유가 아닙니다.":
        "This report is not a recommendation to buy or sell.",
    " 과거 데이터로 계산한\n  통계적 성질을 정리한 것이고, 미래를 맞히기 "
    "위한 것이 아닙니다.\n  투자 판단과 그 결과는 본인에게 있습니다.\n  ":
        " It sets out statistical properties\n  computed from historical "
        "data; it is not an attempt to predict the future.\n  The decision "
        "and its consequences are yours.\n  ",

    "이건 오류가 아니라 정보입니다. ": "This is information, not an error. ",
    "얼마나 들고 있을 것인지": "How long you intend to hold",
    "를 먼저 정하지 않으면 어느 쪽 숫자를 봐야 할지 정할 수 없습니다.":
        " has to be settled first, or there is no way to decide which "
        "number to read.",

    "통계적으로 뚜렷하게 연결된 거시 변수를 찾지 못했습니다. 이 종목은 큰 "
    "흐름보다 개별 요인에 더 움직인다는 뜻일 수 있습니다.":
        "No macro variable was found to be clearly linked. That may mean "
        "this name moves more on its own factors than on the broad "
        "picture.",
    "확실하지 않은 연결을 억지로 말하지 않습니다.":
        "Uncertain links are not asserted.",

    "이 비중을 정한 ": "The weight was set by the ",
    "가장 강한 제약": "tightest constraint",
    "은 “": ", which is “",
    "” 입니다. 여러 기준(낙폭 한도·변동성 목표·유동성·자산군 상한)을 모두 "
    "계산해 ":
        "”. Every criterion — drawdown limit, volatility target, "
        "liquidity, asset-class cap — is computed and ",
    "가장 보수적인 값": "the most conservative one",
    "을 택합니다.": " is chosen.",
    "전체 투자금이 1,000만원이면 ": "On a 10,000,000 KRW portfolio, ",
    " 정도.": " or so.",

    "방향 예측을 하지 않았습니다.": "No directional forecast was made.",
    " 모델이 검정을 통과하지 못해 출력을 취소했습니다. 낮은 점수를 준 게 "
    "아니라 ":
        " The model failed its test, so the output was cancelled. It was "
        "not given a low score — it ",
    "아무 값도 내지 않은": "produced no value at all",
    " 것입니다.": ".",

    "팩터 회귀, 옵션 내재분포, 커버리지 검정, 전문가 패널 심의 같은 상세는 "
    '<a href="':
        "Details such as the factor regression, the option-implied "
        'distribution, coverage tests and the expert panel are in the <a href="',
    '">전문 보고서': '">full report',
    "에 있습니다.": ".",

    # ── labels ────────────────────────────────────────────────
    "자산 종류": "Asset type",
    "분류 확신도": "Classification confidence",
    "기간별 수익률": "Return by period",
    "권장 비중": "Suggested weight",
    "섹터": "Sector",
    "보통 하루 움직임": "A typical day's move",
    "과거 최대 하락": "Largest historical fall",
    "가장 오래 물린 기간": "Longest time underwater",
    "원금 대비 하락 (과거)": "Fall from your capital (historical)",
    "기간마다 방향이 다릅니다.": "The direction differs by period.",
    "최근 3개월 영향 (클수록 큰 영향)":
        "Impact over the last three months (larger means more)",
    " · 최근값 ": " · latest ",
    " · 추세 ": " · trend ",
    "← 이미 발생": "← already happened",
    "만원": "0,000 KRW",

    "100만원이면 하루에 ": "On 1,000,000 KRW that is about ",
    " 정도 흔들립니다.": " of movement in a day.",
    "고점에서 여기까지 떨어진 적이 있습니다. 100만원이면 ":
        "It has fallen this far from a peak before. On 1,000,000 KRW that "
        "is ",
    " 손실.": " of loss.",
    "년 동안 원금을 회복하지 못한 구간이 있었습니다.":
        " years is the longest it has gone without recovering.",
}
