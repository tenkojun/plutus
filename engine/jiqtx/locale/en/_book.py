# -*- coding: utf-8 -*-
"""
English — portfolio (book-level) report and pipeline progress lines.
"""

CATALOG = {

    # ══ portfolio_report ══════════════════════════════════════

    # ── section titles ────────────────────────────────────────
    "위험 분해 — 비중이 아니라 기여":
        "Risk decomposition — contribution, not weight",
    "상관 구조": "Correlation structure",
    "팩터 넷팅 — 상쇄되는가": "Factor netting — does anything offset",
    "배분 규칙 경합 — 워크포워드 + MCS":
        "Allocation rule bake-off — walk-forward + MCS",
    "책 레벨 스트레스": "Book-level stress",
    "한도 점검": "Limit check",
    "구성 종목": "Holdings",
    "◑ 위험 분해": "◑ Risk decomposition",
    "⊞ 상관": "⊞ Correlation",
    "⇄ 팩터 넷팅": "⇄ Factor netting",
    "⚖ 배분 경합": "⚖ Allocation bake-off",
    "⛨ 스트레스": "⛨ Stress",
    "▣ 한도": "▣ Limits",
    "≡ 구성": "≡ Holdings",

    # ── chrome ────────────────────────────────────────────────
    " — Plutus 포트폴리오": " — Plutus portfolio",
    " · 책 레벨 분석": " · book-level analysis",
    "개 포지션 · ": " positions · ",
    " ·\n책 변동성 ": " ·\nbook volatility ",
    "전체 펼치기": "Expand all",
    "전체 접기": "Collapse all",
    "각 종목의 상세 분석은 개별 리포트를 참조하십시오.":
        "See the individual reports for detail on each holding.",
    "개별 종목 분석은 각 종목 리포트를 참조. 본 산출물은 방법론 검증용\n"
    "정보 제공이며 투자 자문이 아닙니다.":
        "See each holding's own report for single-name analysis. This "
        "output is information for methodology validation and\nis not "
        "investment advice.",

    # ── explanatory notes ─────────────────────────────────────
    "비중과 위험기여는 다릅니다. 동일 비중이어도 변동성과 상관에 따라 어떤 "
    "포지션은 책 위험의 대부분을 차지합니다. PM이 보는 것은 비중이 아니라 ":
        "Weight and risk contribution are different things. At the same "
        "weight, volatility and correlation can leave one position "
        "carrying most of the book's risk. What a PM looks at is not the "
        "weight but ",
    "한계기여위험": "marginal contribution to risk",

    "정상 국면 상관입니다. 개별 종목 리포트의 ":
        "This is the normal-regime correlation. Read it together with the ",
    "하방 꼬리 상관": "lower-tail correlation",
    "(λ_L)과 반드시 함께 보십시오 — 분산 효과는 위기에 사라집니다.":
        " (λ_L) in each holding's report — the diversification benefit "
        "disappears in a crisis.",

    "개별로는 큰 노출이 책 전체에서 상쇄될 수 있고, 그 반대도 가능합니다. ":
        "A large exposure in one name can be offset across the book, and "
        "the reverse is also possible. ",
    "넷팅비율 = |순노출| / 총노출":
        "Netting ratio = |net exposure| / gross exposure",
    "이며, 1에 가까우면 전혀 상쇄되지 않는다는 뜻입니다.":
        ", and a value near 1 means nothing offsets at all.",

    "각 리밸런싱 시점에서 ": "At each rebalancing date the weights are "
                            "built ",
    "과거 데이터만으로": "from past data only",
    " 가중치를 만들고 다음 구간 실현 수익으로 평가합니다. 회전비용도 "
    "차감합니다. 그 뒤 Hansen MCS로 통계적으로 구별되지 않는 규칙 집합을 "
    "남깁니다.":
        " and evaluated on the next period's realised return, net of "
        "turnover cost. A Hansen MCS then keeps the set of rules that "
        "cannot be told apart statistically.",

    "HRP·최소분산이 표본 내에서 더 높은 샤프를 보여도, MCS가 1/N을 제외하지 "
    "못하면 그 차이는 ":
        "Even when HRP or minimum variance shows a higher in-sample "
        "Sharpe, if the MCS cannot exclude 1/N then the difference is ",
    "통계적으로 구별되지 않습니다": "not statistically distinguishable",
    ". 이 경우 더 단순한 규칙을 쓰는 것이 옳습니다 — 복잡한 규칙은 "
    "추정오차를 더 많이 먹습니다.":
        ". In that case the simpler rule is the right one — a more "
        "elaborate rule absorbs more estimation error.",

    "단일 종목이 책 위험의 ": "A single name carries ",
    "를 차지합니다. 종목 수가 많아도 실질적으로는 ":
        " of the book's risk. However many holdings there are, in practice "
        "this is ",
    "개 베팅": " bets",

    # ── labels ────────────────────────────────────────────────
    "책 변동성 (연)": "Book volatility (annual)",
    "유효 베팅 수": "Effective number of bets",
    "종목 ": "Holdings ",
    "개 · 분산비율 ": " · diversification ratio ",
    "최대 위험 집중": "Largest risk concentration",
    "평균 상관 ": "Mean correlation ",
    "평균 상관": "Mean correlation",
    "한도 위반": "Limit breach",
    "위반된 한도: ": "Limits breached: ",
    "가중치 출처: ": "Weights from: ",
    "위험 기여 비중": "Share of risk contribution",
    "단독 변동성": "Standalone volatility",
    "위험기여": "Risk contribution",
    "위험기여 비중": "Risk contribution share",
    "분산비율": "Diversification ratio",
    "VaR 95% (일간)": "VaR 95% (daily)",
    "ES 95% (일간)": "ES 95% (daily)",
    "팩터별 책 순노출 (β)": "Book net exposure by factor (β)",
    "리밸런싱 횟수": "Rebalances",
    "MCS 생존 규칙": "Rules surviving the MCS",
    "1/N 초과 입증": "Beats 1/N with evidence",

    # ══ pipeline progress lines ═══════════════════════════════
    "행 · 무결성 ": " rows · integrity ",
    "분류 → ": "Classification → ",
    ", 연율화 √": ", annualised √",
    "유동성 → EDGE ": "Liquidity → EDGE ",
    "변동성 → GARCH ": "Volatility → GARCH ",
    " (장기 ": " (long-run ",
    "시뮬 → P(up) ": "Simulation → P(up) ",
    " (원본식 GBM ": " (original-style GBM ",
    ") · 드리프트 SE ": ") · drift SE ",
    "리스크 → VaR95 ": "Risk → VaR95 ",
    "(채택 ": "(adopted ",
    " · 스트레스 최악 ": " · worst-case stress ",
    "판정 → ": "Verdict → ",
    " · 사이즈 ": " · size ",
    " · 신뢰도 ": " · confidence ",
    "레짐 → '": "Regime → '",
    ", 전환 ": ", transitions ",
    "회)": ")",
    "팩터 → R²=": "Factors → R²=",
    " · 선택 ": " · selected ",
    "팩터 모델 무효 → 알파 0":
        "Factor model void → alpha set to 0",
    "논지 → 시나리오 ": "Thesis → scenarios ",
    "개 · 킬조건 ": " · kill criteria ",
    " 발동 · 트레이드 '": " fired · trade '",
    "' · 헤지 '": "' · hedge '",
    "패널 → 전문가 ": "Panel → experts ",
    "명 · 반대신문 ": " · cross-examinations ",
    "건 · 미해결 ": " · unresolved ",
    "건 · 거부권 ": " · vetoes ",
    "거래가능": "Tradable",
    ", 경계": ", borderline",
    "성격 → ": "Character → ",
    ") · 활성섹션 ": ") · active sections ",
    " (승자 ": " (winner ",
    ", 갭 ": ", gap ",
    "지평 → ": "Horizons → ",
    "거시 → 변수 ": "Macro → variables ",
    "개 · 전술 '": " · tactical '",
    "옵션 → 1M IV ": "Options → 1M IV ",
    "⚠ 미스매칭": "⚠ mismatched",

    # ── failure lines ─────────────────────────────────────────
    "레짐 식별 실패: ": "Regime identification failed: ",
    "논지 계층 실패: ": "Thesis layer failed: ",
    "전문가 패널 실패: ": "Expert panel failed: ",
    "다지평 분석 실패: ": "Multi-horizon analysis failed: ",
    "거시 대시보드 실패: ": "Macro dashboard failed: ",
    "매크로 수집 실패: ": "Macro collection failed: ",
    "프록시 수집 실패: ": "Proxy collection failed: ",
    "주식 프로파일링 실패: ": "Equity profiling failed: ",
    "ML 실패: ": "ML failed: ",
    "거래불가: ": "Not tradable: ",
    "옵션 분석 생략: ": "Option analysis skipped: ",
}
