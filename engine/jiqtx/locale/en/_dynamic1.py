# -*- coding: utf-8 -*-
"""
English — dynamic_report, part 1: verdict strip, thesis notes, archetypes.

Now that the extractor decomposes HTML literals, these keys are the actual
text nodes the renderer emits, so they match exactly.

On the subject markers ('이 ', '가 '): Korean attaches them after a noun and
English has no equivalent, so they map to a plain space. They are safe to
include *because of* the Hangul-boundary rule — they can only fire when the
following character is not Hangul, which in practice means the marker sits
right before a tag. In running Korean text (marker followed by a word) the
rule blocks the match, so nothing gets shredded.
"""

CATALOG = {

    # ── subject markers (see module docstring) ────────────────
    "이 ": " ",
    "가 ": " ",

    # ── empty states ──────────────────────────────────────────
    "데이터 없음": "No data",
    "귀인 산출 불가": "Attribution cannot be computed",
    "팩터 데이터 없음": "No factor data",
    "델타 패널 산출 불가": "Delta panel cannot be computed",
    "사이징 미산출": "Sizing not computed",
    "금리 팩터 부재로 듀레이션 추정 불가.":
        "No rate factor, so duration cannot be estimated.",
    "금리 팩터가 이 자산의 후보군에 없거나 데이터가 부족합니다.":
        "A rate factor is not in this asset's candidate set, or there is "
        "not enough data.",
    "유의한 팩터 노출이 없어 헤지 레그가 없습니다.":
        "There is no significant factor exposure, so there is no hedge leg.",

    # ── chrome ────────────────────────────────────────────────
    "접기": "Collapse",
    "펼치기": "Expand",
    " · Plutus 정밀 분석": " · Plutus analysis",
    "활성 섹션 ": "Active sections ",
    " / 전체 ": " / total ",

    # ── verdict grades ────────────────────────────────────────
    "매수": "Buy",
    "분할 매집": "Accumulate",
    "보유/관망": "Hold",
    "비중 축소": "Reduce",
    "신규 진입 불가": "No new entry",
    "판단 보류": "Abstain",

    # ── verdict strip ─────────────────────────────────────────
    "방향 등급": "Direction grade",
    "확률 ": "P ",
    "구속: ": "Binding: ",
    "모델 신뢰도": "Model confidence",
    "무효화 모듈 ": "Invalidated modules ",
    "이고 리스크 예산 ": " and the risk budget is ",
    "사전등록된 kill criteria": "Pre-registered kill criteria",
    "방향 예측 모듈은 게이트를 통과하지 못해 ":
        "The direction forecast module did not pass its gate, so it ",
    "확률을 출력하지 않았습니다": "published no probability",
    "배리어 확률 (시뮬 경로 기반)":
        "Barrier probabilities (from simulated paths)",
    "드리프트 신뢰도": "Drift confidence",
    "스트레스 — 자산군 고유 충격":
        "Stress — asset-class-specific shocks",

    # ── section intros ────────────────────────────────────────
    "이 요약은 아래 섹션의 산출물에서 기계적으로 조립됩니다. 서술이 아니라 ":
        "This summary is assembled mechanically from the sections below. "
        "It is not prose but ",
    "계산 결과": "a computed result",

    "시나리오를 분위수로 자르지 않고 ":
        "Scenarios are not cut by quantile but ",
    "드라이버로 정의": "defined by driver",
    "합니다. 손익은 팩터 델타 × 충격으로 계산하고, 확률은 그 충격 조합의 ":
        ". P&L is factor delta × shock, and the probability is estimated "
        "from that shock combination's ",
    "역사적 동시 발생 빈도": "historical joint frequency",
    "에서 추정합니다.": ".",

    '"비중 15%"는 결론이 아닙니다. 어디서 들어가고, 어디서 ':
        '"15% weight" is not a conclusion. Where you enter, where you ',
    "틀렸다고 인정하고": "admit you were wrong",
    ", 어디를 목표로 하며, 그 확률이 얼마이고, 비용 후 기대값이 양수인지가 "
    "트레이드입니다.":
        ", what you target, the probability of getting there, and whether "
        "the expected value after costs is positive — that is the trade.",

    "최소분산 헤지비율은 ": "The minimum-variance hedge ratio is ",
    "다변량 팩터 회귀 계수와 동일":
        "the multivariate factor regression coefficient",
    "합니다. 따라서 팩터 모델이 미스매칭이면 헤지도 함께 무효입니다. 이 "
    "연결을 끊고 헤지를 논하면 안 됩니다.":
        ". So if the factor model is mismatched, the hedge is void with "
        "it. You cannot discuss the hedge as though that link were not "
        "there.",

    "최근 성과가 ": "Whether recent performance was ",
    "종목 고유(알파)": "idiosyncratic (alpha)",
    "인지 ": " or ",
    "그냥 베타": "just beta",
    "였는지 분해합니다. 알파 비중이 낮으면 같은 노출을 훨씬 싸게 복제할 수 "
    "있다는 뜻입니다.":
        " is decomposed here. A low alpha share means the same exposure "
        "can be replicated far more cheaply.",

    "게이트 실패는 ": "A failed gate is ",
    "감점이 아니라 모듈 무효화":
        "not a deduction but an invalidation of the module",
    "입니다. OOS 50%는 약한 신호가 아니라 신호 없음이고, 올바른 출력은 감점된 "
    "점수가 아니라 ":
        ". 50% out of sample is not a weak signal but no signal, and the "
        "correct output is not a marked-down score but ",
    "출력 없음": "no output",

    # ── delta panel reading guide ─────────────────────────────
    "보다 크면 하방에서 노출이 확대되는 비대칭 자산입니다. 정적 베타 "
    "스트레스는 이걸 놓칩니다.":
        " means the asset is asymmetric — exposure widens to the downside. "
        "Static-beta stress testing misses this.",
    ": 정상 국면과 극단 국면 상관은 다른 숫자입니다. 분산 효과가 위기에 "
    "사라지는지 여기서 보입니다.":
        ": correlation in a normal regime and in an extreme one are "
        "different numbers. This is where you see whether the "
        "diversification benefit disappears in a crisis.",
    "β안정성CV &gt; 0.8": "β stability CV &gt; 0.8",
    "이면 그 베타를 헤지 비율로 쓰면 안 됩니다.":
        " means that beta must not be used as a hedge ratio.",
    "R² 붕괴": "An R² collapse",
    "는 버그가 아니라 구조 변화 신호입니다. 금-10년TIPS R²가 2005–2021 약 "
    "84%에서 2022년 이후 한 자릿수로 무너진 것이 대표 사례입니다.":
        " is not a bug but a signal of structural change. The classic case "
        "is gold against 10-year TIPS, whose R² fell from roughly 84% over "
        "2005–2021 to single digits after 2022.",

    # ── earnings / PEAD ───────────────────────────────────────
    "관측 이벤트 수": "Events observed",
    "다음 발표": "Next release",
    "발표 다음날 |초과수익| 평균":
        "Mean |excess return| the day after a release",
    "중앙값 / 90분위 / 최대": "Median / 90th percentile / max",
    "평균 방향": "Mean direction",
    "서프라이즈 양수 비율": "Share of positive surprises",
    "PEAD (양수 서프라이즈 t+1~20)": "PEAD (positive surprise, t+1 to 20)",
    "PEAD (음수 서프라이즈 t+1~20)": "PEAD (negative surprise, t+1 to 20)",
    "PEAD 스프레드": "PEAD spread",
    "연 분산 중 어닝일 기여":
        "Earnings days' contribution to annual variance",

    # ── growth / burn archetype ───────────────────────────────
    "시가총액": "Market cap",
    "적자 고성장주에 PER은 무의미합니다. EV/Sales와 Rule of 40, 그리고 ":
        "P/E is meaningless for a loss-making high-growth name. EV/Sales, "
        "the Rule of 40 and ",
    "현금소진 잔여기간": "the cash runway",
    "이 실질 앵커입니다. 금리 상승 시 현금흐름 듀레이션이 길어 멀티플 축소 "
    "폭이 가장 큰 유형입니다.":
        " are the real anchors. Cash-flow duration is long, so this is the "
        "type whose multiple compresses most when rates rise.",
    "연간 현금소진 (−FCF)": "Annual cash burn (−FCF)",
    "순현금": "Net cash",
    "순현금 / 시총": "Net cash / market cap",
    "2년 미만이면 자금조달 압력":
        "Under two years means funding pressure",
    "매출성장": "Revenue growth",
    "영업이익률": "Operating margin",
    "유동비율": "Current ratio",
    "적자 기업의 에쿼티 가치는 ":
        "The equity value of a loss-making company is ",
    "미래 현금흐름의 현재가치":
        "the present value of future cash flows",
    "이므로 듀레이션이 길고, 금리 상승 시 멀티플 축소 폭이 가장 큽니다. 아래 "
    "금리 델타 섹션을 반드시 함께 보십시오.":
        ", so its duration is long and its multiple compresses most when "
        "rates rise. Read the rate-delta section below alongside this.",
    "적자/성장 전용": "Loss-making / growth only",

    # ── crowding ──────────────────────────────────────────────
    "크라우딩·포지셔닝 리스크: ": "Crowding and positioning risk: ",
    " (점수 ": " (score ",
    "크라우딩은 평상시엔 보이지 않다가 청산 국면에서만 드러납니다. 공매도 "
    "잔고가 높으면 상방 스퀴즈와 하방 가속이 ":
        "Crowding is invisible in normal times and only shows up when "
        "people try to get out. High short interest makes both an upside "
        "squeeze and a downside acceleration larger ",
    "동시에": "at the same time",
    " 커지며, 이는 변동성이 아니라 ":
        ", which is a problem of ",
    "의 문제입니다. 포지션 사이징으로만 관리 가능합니다.":
        " rather than volatility. It can only be managed through position "
        "sizing.",
    "투기/이벤트형": "Speculative / event driven",

    # ── duration ──────────────────────────────────────────────
    "현금흐름 듀레이션이 긴 자산(고성장 적자주, 인컴주, 리츠, 장기채)은 금리 "
    "민감도가 실질적으로 ":
        "For long-duration cash flows — high-growth loss makers, income "
        "names, REITs, long bonds — rate sensitivity is effectively ",
    "가장 큰 단일 리스크": "the single largest risk",
    "이 듀레이션은 가격-금리 회귀에서 역산한 ":
        "This duration is backed out of a price-on-rates regression — an ",
    "실효(empirical) 듀레이션": "empirical duration",
    "이며, 현금흐름 기반 수정듀레이션과 다릅니다. 볼록성과 스프레드 "
    "듀레이션은 별도이며, 크레딧물의 경우 금리보다 OAS가 지배할 수 있습니다.":
        " — and differs from cash-flow-based modified duration. Convexity "
        "and spread duration are separate, and for credit the OAS can "
        "dominate rates.",
    "채권 전용": "Bonds only",
    "레버리지 전용": "Leveraged products only",

    # ── regime ────────────────────────────────────────────────
    "K-means 라벨 0·1·2는 강약 순서를 뜻하지 않아 경제적 해석이 "
    "불가능합니다. Statistical Jump Model은 전환마다 점프 페널티를 부과해 "
    "지속성을 강제하고, 각 국면에 ":
        "K-means labels 0, 1 and 2 imply no ordering of strength, so they "
        "cannot be interpreted economically. The Statistical Jump Model "
        "charges a penalty per transition to enforce persistence, and "
        "gives each regime ",
    "경제적 이름": "an economic name",
    "을 붙입니다.": ".",

    # ── factor names and labels ───────────────────────────────
    "소형(SMB)": "Size (SMB)",
    "가치(HML)": "Value (HML)",
    "보수적투자(CMA)": "Investment (CMA)",
    "높음": "High",
    "중간": "Medium",
    "낮음": "Low",
    "이벤트형": "Event driven",
}
