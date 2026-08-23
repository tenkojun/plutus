/* Plutus — 화면 언어 (한국어 · English · 日本語 · 简体中文)
 * ============================================================
 * 이 앱의 UI 는 11,000 줄짜리 단일 HTML 이다. 요소마다 data-i18n 키를
 * 박으려면 사실상 전 파일을 고쳐야 하고, 그 과정에서 조용히 깨지는 곳이
 * 반드시 생긴다. 그래서 **한국어 원문 자체를 키로 쓰는 런타임 치환**을 쓴다.
 *
 *   - 사전에 있는 문자열만 바꾼다. 없으면 한국어 그대로 둔다.
 *     종목명·뉴스 제목·사용자 입력처럼 사전에 없는 값은 절대 건드리지 않는다.
 *   - 정적 DOM 과 JS 가 나중에 그린 DOM 을 같은 함수로 처리한다
 *     (MutationObserver). 위젯을 새로 그려도 언어가 되돌아가지 않는다.
 *   - characterData 는 보지 않는다. 시세 숫자가 초당 여러 번 바뀌는데
 *     그때마다 트리를 훑으면 스크롤이 끊긴다. 노드 추가만 본다.
 *
 * 한국어가 기본값이고, 사전에 없는 문장은 한국어로 남는다 — 반쯤 번역된
 * 화면이 되긴 하지만, 틀린 번역보다는 원문이 낫다.
 */
(function () {
  'use strict';

  var LANGS = {
    ko:      { label: '한국어',   html: 'ko',    locale: 'ko-KR' },
    en:      { label: 'English',  html: 'en',    locale: 'en-US' },
    ja:      { label: '日本語',    html: 'ja',    locale: 'ja-JP' },
    'zh-CN': { label: '简体中文',  html: 'zh-CN', locale: 'zh-CN' }
  };
  var KEY = 'iaw.lang';

  // ── 사전 ────────────────────────────────────────────────────
  // 키는 화면에 실제로 나오는 한국어 문자열(trim 후)이다.
  var DICT = {
    en: {
      // 헤더 · 전역
      // 지수 · 섹션 헤더 — 화면에 상시 떠 있는 라벨
      '코스피': 'KOSPI',
      '코스닥': 'KOSDAQ',
      '나스닥': 'Nasdaq',
      '다우': 'Dow',
      '원/달러': 'KRW/USD',
      'VIX 공포': 'VIX',
      '금': 'Gold',
      'WTI 유가': 'WTI crude',
      '비트코인': 'Bitcoin',
      '☷ NEWS · 뉴스피드': '☷ NEWS · feed',
      '◈ ANALYSIS · 분석': '◈ ANALYSIS',
      '[◈ 현재 종목 분석]': '[◈ Analyse this ticker]',
      '한국': 'Korea',
      '미국': 'USA',
      '일본': 'Japan',
      '중국': 'China',
      '유럽': 'Europe',
      'Plutus · 기관급 퀀트 분석 터미널': 'Plutus · Institutional Quant Terminal',
      'Plutus · 인증 확인 중…': 'Plutus · Checking sign-in…',
      '기관급 퀀트 분석 터미널': 'Institutional Quant Terminal',
      '정밀 분석 · 수급 · 리스크': 'Analysis · Flow · Risk',
      '좋은 아침입니다': 'Good morning',
      '님': '',
      '로그인이 필요합니다': 'Sign-in required',
      '로그인': 'Sign in',
      '가입 신청': 'Sign up',
      '가입하면 바로 사용할 수 있습니다 — 무료 등급(보고서 3회/일)으로 시작합니다.':
        'Your account works immediately — you start on the free tier (3 reports/day).',
      '새 계정 만들기 (바로 사용 · 보고서 3회/일)':
        'Create an account (instant · 3 reports/day)',
      '가입 완료 — 바로 로그인하세요': 'Account created — sign in now',
      'NICKNAME · 닉네임': 'NICKNAME',
      '화면에 표시될 이름 (선택)': 'Display name (optional)',
      '⏻ 로그아웃': '⏻ Sign out',
      '로그아웃': 'Sign out',

      // 내비게이션 · 탭
      '차트': 'Chart',
      '정밀 분석': 'Analysis',
      '뉴스': 'News',
      '분석 이력': 'History',
      '설정': 'Settings',
      '커뮤니티': 'Community',
      '작업': 'Tasks',
      '클라우드': 'Cloud',
      '이력': 'History',
      '위젯': 'Widgets',
      '보관함': 'Library',
      '실시간': 'Live',
      '히스토리': 'History',
      '시급만': 'Urgent only',
      '속보': 'Breaking',
      '속보 전체': 'All breaking',
      '관련 뉴스': 'Related news',
      '★ 즐겨찾기': '★ Favourites',
      '▸ 검색 결과': '▸ Search results',
      '검색 결과 없음': 'No results',

      // 공통 동작
      '저장': 'Save',
      '취소': 'Cancel',
      '삭제': 'Delete',
      '등록': 'Register',
      '검증': 'Verify',
      '테스트': 'Test',
      '진단': 'Diagnose',
      '재시작': 'Restart',
      '중지': 'Stop',
      '열기': 'Open',
      '다운로드': 'Download',
      '새로고침': 'Refresh',
      '↻ 새로고침': '↻ Refresh',
      '✕ 닫기': '✕ Close',
      '닫기 (ESC)': 'Close (ESC)',
      '만들기': 'Create',
      '다음에': 'Later',
      '나중에': 'Later',
      '기본값': 'Default',
      '↺ 기본값': '↺ Reset',
      '전송': 'Send',
      '이름': 'Name',
      '제목': 'Title',
      '본문': 'Body',
      '이전': 'Previous',
      '다음': 'Next',
      '없음': 'None',
      '데이터 없음': 'No data',
      '로딩 중…': 'Loading…',
      '로딩 중...': 'Loading…',
      '불러오는 중…': 'Loading…',
      '확인 중…': 'Checking…',
      '분석 중…': 'Analysing…',
      '진행 중…': 'Working…',
      '로딩 실패': 'Failed to load',
      '상태 로드 실패': 'Failed to load status',
      '네트워크 오류': 'Network error',
      '⌛ 추론 중…': '⌛ Thinking…',

      // 설정 — 카테고리
      'Plutus 설정': 'Plutus settings',
      '내 계정': 'My account',
      '계정': 'Account',
      '중앙 인증': 'Central auth',
      '화면': 'Appearance',
      '언어': 'Language',
      '테마·이펙트': 'Theme & effects',
      '위젯 배치': 'Widget layout',
      '연결': 'Connections',
      'API 키': 'API keys',
      '외부 접근': 'Remote access',
      '한국투자증권': 'Korea Investment',
      '로컬 LLM': 'Local LLM',
      '기타': 'Other',
      '정보': 'About',
      '현재 로그인': 'Signed in as',
      'CLAUDE 잔여': 'Claude remaining',
      '메인 PC': 'Main PC',
      '메인 PC 미지정': 'No main PC set',
      '외부 접근은 "외부 접근" 카테고리에서 설정.':
        'Configure this under the "Remote access" category.',
      '데이터 소스 API 키 설정': 'Data source API keys',
      '키가 없어도': 'Even without keys',

      // 설정 — 언어
      '앱 화면에 표시되는 언어입니다.': 'The language used across the app interface.',
      '분석 보고서와 용어 설명은 한국어로 나옵니다.':
        'Analysis reports and the glossary remain in Korean.',
      '언어를 바꿨습니다.': 'Language changed.',

      // 설정 — 화면
      '테마 (C2)': 'Theme (C2)',
      '전체 UI 색상 팔레트를 변경합니다.': 'Changes the colour palette of the whole UI.',
      '보고서 테마': 'Report theme',
      '만드는 시점에 테마가 정해집니다': 'the theme is fixed when it is generated',
      '배경 이펙트': 'Background effect',
      '끄기': 'Off',
      '약하게': 'Subtle',
      '기본': 'Default',
      '강하게': 'Strong',
      '・ 다른 탭으로 넘어가면 자동으로 멈춥니다':
        '・ Pauses automatically when you switch tabs',
      "・ 시스템이 '동작 줄이기'로 설정돼 있으면 자동으로 꺼집니다":
        '・ Turns itself off when the system prefers reduced motion',
      '글자 크기 (C1)': 'Font size (C1)',
      '전체 인터페이스의 기본 글자 크기.': 'Base font size for the whole interface.',
      '작 (S)': 'Small (S)',
      '중 (M)': 'Medium (M)',
      '14.5px · 기본': '14.5px · default',
      '대 (L)': 'Large (L)',
      '특대 (XL)': 'Extra large (XL)',
      '사운드 마스터 (C5)': 'Master sound (C5)',
      '모든 앱 사운드(부팅음·알림·효과음)를 한 번에 끄거나 켭니다.':
        'Turns every app sound (boot, alerts, effects) on or off at once.',
      '전체 사운드': 'All sounds',
      '앱 전체 음소거 토글': 'Mute the entire app',
      '알림 효과음 (C3)': 'Alert sounds (C3)',
      '뉴스/속보 효과음': 'News and breaking-news sounds',
      '"뿅" 사운드 재생': 'Play the chime',
      '소리 테스트': 'Test sound',
      '속보 알림': 'Breaking-news alerts',
      '새 high-impact 속보가 들어오면 즉시 알려줍니다.':
        'Notifies you the moment a high-impact story lands.',
      '🔊 소리 알림 (짧은 beep, Web Audio)': '🔊 Sound alert (short beep, Web Audio)',
      '⚡ 상단 스트립 플래시 + 토스트 메시지': '⚡ Top-strip flash + toast message',
      '▸ 커스텀 색상 (즉시 반영)': '▸ Custom colours (applied instantly)',
      '💾 자동 저장 (localStorage) · 새로고침해도 유지':
        '💾 Saved automatically (localStorage) · survives a reload',

      // 설정 — 레이아웃
      '레이아웃 템플릿': 'Layout template',
      '전체 화면 분할 방식을 선택하세요. 슬롯 수에 따라 자동 마운트됩니다.':
        'Choose how the screen is split. Widgets mount automatically by slot count.',
      '현재 배치': 'Current layout',
      '기본 배치로 초기화': 'Reset to the default layout',
      '사용 가능한 위젯': 'Available widgets',
      '슬롯 배치 중': 'Placing in slot',
      'dock 대기': 'waiting in dock',
      '슬롯 A —': 'Slot A —',
      '슬롯 B —': 'Slot B —',
      '슬롯 C —': 'Slot C —',
      '슬롯 D —': 'Slot D —',

      // 설정 — 중앙 인증
      '중앙 인증 서버': 'Central auth server',
      '기본 서버가 내장': 'a default server is built in',
      '서버': 'Server',
      '저장 + 검증': 'Save + verify',
      '배포 가이드': 'Deployment guide',
      '(비워 두면 기본 서버 사용)': '(leave empty to use the default server)',
      '앱에 내장된 기본 서버로 되돌립니다': 'Restores the server built into the app',
      '○ 서버 없음 — 로컬 모드': '○ No server — local mode',
      '기본 서버': 'Default server',
      '직접 지정': 'Custom',
      '● 로그인됨 —': '● Signed in —',
      '○ 미로그인': '○ Not signed in',

      // 설정 — 외부 접근
      'PC 정보': 'PC info',
      'PC 라벨': 'PC label',
      'Tunnel 상태': 'Tunnel status',
      '1단계 · cloudflared 설치': 'Step 1 · install cloudflared',
      '자동 다운로드': 'Download automatically',
      '2단계 · Quick Tunnel 시작 (즉시, 계정 불필요)':
        'Step 2 · start a Quick Tunnel (instant, no account)',
      '발급된 URL · 핸드폰에서 접속': 'Issued URL · open it on your phone',
      'URL 복사': 'Copy URL',
      '복사됨!': 'Copied.',
      '외부 접근 켜기': 'Enable remote access',
      '3단계 · QR로 핸드폰 자동 로그인': 'Step 3 · sign in on your phone by QR',
      '현재 PC 계정으로 자동 로그인': 'Signs in automatically as this PC’s account',
      'QR 생성 대기': 'Waiting to generate a QR code',
      'QR 정보': 'QR details',
      'QR 생성': 'Generate QR',
      '핸드폰 카메라 앱 → QR 스캔 → URL 자동 열림 → 즉시 로그인':
        'Phone camera → scan the QR → the URL opens → you are signed in',
      '자동 로그인 URL': 'Auto sign-in URL',
      '⏱ 토큰 만료': '⏱ Token expired',
      '● 감시 중': '● Watching',
      '◐ 주소 발급 대기': '◐ Waiting for an address',
      '○ 끊김': '○ Disconnected',
      '📱 폰에는 이 주소를 저장하세요': '📱 Save this address on your phone',
      '✓ 현재 주소 등록됨': '✓ Current address registered',
      '◐ 주소 등록 대기': '◐ Waiting to register the address',
      '내 PC 외부 URL (Quick Tunnel 또는 정식 Tunnel)':
        'This PC’s external URL (Quick or Named Tunnel)',
      '⟲ 현재 Tunnel URL 자동 채우기': '⟲ Fill in the current tunnel URL',
      '📱 핸드폰에서 접근:': '📱 From your phone:',
      '도메인 (Zone)': 'Domain (zone)',
      '서브도메인 (전체 hostname)': 'Subdomain (full hostname)',
      'Tunnel 이름 (Cloudflare 대시보드에 표시)':
        'Tunnel name (shown in the Cloudflare dashboard)',
      '📌 사전 준비 (1회만)': '📌 One-time setup',
      'API Token 발급': 'Create an API token',
      '(무료)': '(free)',
      '■ 중지': '■ Stop',
      '▶ 시작': '▶ Start',

      // 설정 — 시스템
      'Plutus 시스템': 'Plutus system',
      '버전': 'Version',
      '자체 PC (로컬)': 'This PC (local)',
      '업데이트 확인': 'Check for updates',
      '바로가기 만들기': 'Create a shortcut',
      'GitHub 릴리스를 확인합니다. 설정·키·계정은 유지됩니다.':
        'Checks GitHub releases. Your settings, keys and account are kept.',
      '폰으로 보기 (같은 와이파이)': 'View on your phone (same Wi-Fi)',
      '같은 와이파이의 다른 기기에서 접속 허용':
        'Allow other devices on the same Wi-Fi to connect',
      '변경은 앱을 다시 켜야 적용됩니다.': 'Takes effect after you restart the app.',
      '개발자': 'Developer',
      '새 버전이 있습니다': 'A new version is available',
      '그대로 유지': 'are kept as they are',
      '릴리스 보기': 'View release',
      '업데이트': 'Update',
      '바로가기를 만들까요?': 'Create a shortcut?',
      '바탕화면에 바로가기': 'Desktop shortcut',
      '바탕화면에서 바로 실행합니다.': 'Launches straight from the desktop.',
      '시작 메뉴에 등록': 'Add to the Start menu',
      '이걸 켜야': 'This is what lets you',
      '윈도우 검색창에서 "Plutus" 로 찾을 수': 'find "Plutus" in Windows search',
      '있습니다.': '.',

      // 하드웨어 · LLM
      '하드웨어': 'Hardware',
      '하드웨어 감지 중…': 'Detecting hardware…',
      'Ollama 상태 확인 중…': 'Checking Ollama…',
      '권장 모델': 'Recommended model',
      '자동 셋업 시작': 'Run automatic setup',
      '설치 모델': 'Installed models',
      'LLM DEEP ANALYSIS · 로컬 추론': 'LLM DEEP ANALYSIS · local inference',
      '심층분석 실행': 'Run deep analysis',
      'FOLLOW-UP · 분석에 대한 질문': 'FOLLOW-UP · questions about this analysis',
      '로컬 LLM · 무료 · 대화 미저장': 'Local LLM · free · nothing is stored',
      '위 분석에 대해 자유롭게 질문하세요': 'Ask anything about the analysis above',
      '질문 입력 (Shift+Enter 줄바꿈, Enter 전송)':
        'Type a question (Shift+Enter for a new line, Enter to send)',
      '예: 데이터센터 매출이 왜 중요한가요?':
        'e.g. why does data-centre revenue matter?',

      // 시장 · 차트 위젯
      'MARKET OVERVIEW · 시장 개요': 'MARKET OVERVIEW',
      'CHART · 종목 차트': 'CHART',
      '차트 클릭…': 'Click the chart…',
      '슬라이드 ▸': 'Slide ▸',
      '시장 변동 색 매트릭스': 'Market colour matrix',
      'S&amp;P 거시 히트맵 · 섹터 × 시총': 'S&amp;P macro heatmap · sector × market cap',
      '시장 수급 · 당일': 'Market flow · today',
      '자금 이동': 'Money migration',
      '매수 / 매도': 'Buy / sell',
      '섹터 강약': 'Sector strength',
      '수급 계산 중… (최초 10~30초)': 'Computing flow… (10–30s the first time)',
      '어제 데이터가 없어 비교할 수 없습니다.': 'No data for yesterday to compare against.',
      '어제 같은 시각 대비 거래대금 비중 변화':
        'Change in share of traded value vs. the same time yesterday',
      '섹터 강약 — 등락과 자금이 함께 말할 때만 라벨':
        'Sector strength — labelled only when price and flow agree',
      '경제 캘린더 로딩 중…': 'Loading the economic calendar…',
      '예측': 'Forecast',
      '실제': 'Actual',
      '관심 종목을 추가하세요.': 'Add a ticker to your watchlist.',
      '상단에서 종목 조회': 'Search for a ticker above',
      '뉴스 불러오는 중…': 'Loading news…',
      '표시할 뉴스가 없습니다.': 'No news to show.',
      '뉴스 로딩 실패.': 'Failed to load news.',
      '속보 로딩 중…': 'Loading breaking news…',
      '현재 매핑된 속보 없음.': 'No breaking news mapped right now.',
      '감지된 키워드 없음': 'No keywords detected',
      '실시간 라이브 · 24/7': 'Live · 24/7',
      '채널을 선택해주세요…': 'Pick a channel…',
      'SENTIMENT · 감성 분석': 'SENTIMENT',
      'ANALYST CONSENSUS · 애널리스트 컨센서스': 'ANALYST CONSENSUS',
      'ANALYST · 애널리스트': 'ANALYST',
      '애널리스트 컨센서스 로딩…': 'Loading analyst consensus…',
      'DEEPL · 핵심 내용 (한글)': 'DEEPL · key points',
      '▸ 원문 보기 ↗': '▸ Read the original ↗',
      '차트를 표시할 수 없습니다': 'The chart cannot be displayed',

      // 분석
      '◈ 현재 종목 분석': '◈ Analyse this ticker',
      '◆ 포트폴리오': '◆ Portfolio',
      '◆ 포트폴리오 관리': '◆ Portfolio management',
      '데이터 무결성 → 자산군 분류 → 유동성 →':
        'Data integrity → asset class → liquidity →',
      '변동성·레짐 → 팩터 → ML 게이트 →': 'volatility & regime → factors → ML gate →',
      '시뮬레이션 → 리스크 → 전문가 패널 심의':
        'simulation → risk → expert panel deliberation',
      '순으로 돌고, 자기완결 HTML 보고서를 만듭니다.':
        ' — in that order, ending in a self-contained HTML report.',
      '게이트를 통과하지 못한 모듈은 점수가 깎이는 대신':
        'A module that fails its gate is not marked down; it is marked',
      '무효(abstain)': 'abstain',
      '로 표시됩니다.': '.',
      '1~3분 걸립니다.': 'This takes 1–3 minutes.',
      '(ML·몬테카를로 포함 — 30초~2분 소요)':
        '(includes ML and Monte Carlo — 30s to 2 min)',
      '1~3분 걸립니다. 이 창을 닫아도 계속 진행됩니다.':
        'This takes 1–3 minutes. You can close this window; it keeps running.',
      '오늘 보고서 한도를 다 썼습니다': 'You have used today’s report quota',
      '프리미엄으로 올리면 무제한입니다 (관리자 문의)':
        'Premium removes the limit (ask the administrator)',
      '✗ 정밀 분석 실패': '✗ Analysis failed',
      '상승확률': 'P(up)',
      '· 배분': '· allocation',
      '거부권 발동': 'Veto raised',
      '판정 근거': 'Basis for the verdict',
      '◈ 간단 리서치': '◈ Quick research',
      '▸ 전문 보고서': '▸ Full report',
      '로 처리됩니다 — 약한 신호가 아니라 신호 없음입니다.':
        ' — that is not a weak signal, it is no signal.',
      'INSIGHTS · 인사이트': 'INSIGHTS',
      '분석가 관점 · KEY POINTS': 'ANALYST VIEW · KEY POINTS',
      '시장 컨센서스': 'Market consensus',
      'RISKS · 주의 요인': 'RISKS',
      'RATIONALE · 종합 결론': 'RATIONALE',
      '신뢰도': 'Confidence',
      '참신성': 'Novelty',

      // 포트폴리오
      '포트폴리오 종합 분석 중… (보유 종목별 시세/펀더 fetch + 상관행렬)':
        'Analysing the portfolio… (quotes and fundamentals per holding + correlations)',
      '종목 수에 따라 30초~2분 소요': '30s to 2 min depending on how many holdings',
      '✗ 포트폴리오 분석 실패': '✗ Portfolio analysis failed',
      '평가액': 'Market value',
      '총 손익': 'Total P&L',
      '연수익률': 'Annual return',
      '변동성': 'Volatility',
      '평균상관': 'Mean correlation',
      '분산효과': 'Diversification',
      '종목별 기여도': 'Contribution by holding',
      '종목': 'Ticker',
      '비중': 'Weight',
      '연수익': 'Annual return',
      '기여': 'Contribution',
      '평가': 'Valuation',
      '새 종목 추가': 'Add a holding',
      '현재 보유 종목': 'Current holdings',
      '보유 종목 없음': 'No holdings',
      '보유 종목 없음 — 위 입력으로 추가': 'No holdings — add one above',
      '관리 ⛶': 'Manage ⛶',
      '+ 추가': '+ Add',
      '수량': 'Quantity',
      '평균단가': 'Average cost',
      '티커/회사명': 'Ticker / company',

      // 보관함 · 이력
      '📁 REPORTS · 보고서 보관함': '📁 REPORTS · library',
      '아직 생성된 보고서가 없습니다.': 'No reports yet.',
      '보관': 'Archive',
      '최신': 'Latest',
      '📜 ANALYSIS HISTORY · 분석 이력': '📜 ANALYSIS HISTORY',
      '아직 분석 이력이 없습니다.': 'No analysis history yet.',
      '▸ 리포트': '▸ Report',

      // 작업 관리자
      '📋 작업 관리자': '📋 Task manager',
      '백그라운드로 돌아가는 분석 작업 — 자동 갱신':
        'Analyses running in the background — refreshes itself',
      '📭 작업 없음': '📭 No tasks',
      'MEGA grid / AUTO / WFA 등 무거운 작업이 백그라운드로 돌아가면 여기에 표시됩니다':
        'Heavy jobs (MEGA grid, AUTO, WFA) show up here while they run',
      '⊘ 중단': '⊘ Cancel',
      '→ 결과 보기': '→ View result',

      // 커뮤니티
      '공지 · 글 · 댓글': 'Notices · posts · comments',
      '+ 새 글': '+ New post',
      '💬 클릭하면 글 목록이 표시됩니다': '💬 Click to see the posts',
      '공지': 'Notice',
      '📌 공지': '📌 Notice',
      '[관리자]': '[admin]',
      '⭐ 전략': '⭐ Strategy',
      '아직 댓글 없음': 'No comments yet',
      '글 삭제': 'Delete post',
      '📌 공지로 등록': '📌 Post as a notice',
      '(어드민 전용 — 목록 상단 고정)': '(admin only — pinned to the top)',
      '+ 등록': '+ Post',
      '댓글 입력…': 'Write a comment…',
      '제목 입력 (최소 2자)': 'Title (at least 2 characters)',
      '내용 입력 (최소 2자)': 'Body (at least 2 characters)',

      // 에이전트 · 관리자
      '🤖 AGENT · Claude 분석가': '🤖 AGENT · Claude analyst',
      '+ 새 대화': '+ New chat',
      '새 대화를 시작하거나 좌측에서 이전 대화를 선택하세요.':
        'Start a new chat, or pick an earlier one on the left.',
      '대화가 없습니다.': 'No conversations.',
      '예시: "오늘 코스피 어때?" / "지금 보고 있는 종목 어때?"':
        'e.g. "How is the KOSPI today?" / "What about the ticker I have open?"',
      '⛨ ADMIN · 사용자 관리': '⛨ ADMIN · user management',
      'TOP CLAUDE (오늘)': 'TOP CLAUDE (today)',
      'TOP 로그인 (누적)': 'TOP sign-ins (all time)',
      '승인': 'Approve',
      '거부': 'Reject',
      '정지': 'Suspend',
      '쿼터 리셋': 'Reset quota',

      // 툴팁 · 속성
      '실시간 SSE 연결 상태': 'Live SSE connection status',
      '보고서 일일 한도': 'Daily report limit',
      'Claude 일일 사용량': 'Daily Claude usage',
      '에이전트 채팅': 'Agent chat',
      '커뮤니티 (공지/글/댓글)': 'Community (notices, posts, comments)',
      '관리자': 'Administrator',
      '종목 검색 (클릭)': 'Search tickers (click)',
      '추세선 (2점 클릭)': 'Trend line (click two points)',
      '수평선 (1점 클릭)': 'Horizontal line (click one point)',
      '피보나치 (2점 클릭)': 'Fibonacci (click two points)',
      '모두 지우기': 'Clear all',
      '드래그하여 좌우 크기 조절': 'Drag to resize horizontally',
      '드래그하여 상하 크기 조절': 'Drag to resize vertically',
      '클릭 시 전체화면': 'Click for full screen',
      '전체화면 (ESC로 닫기)': 'Full screen (ESC to close)',
      '끌어서 옮기기': 'Drag to move',
      '커뮤니티 — 공지/글/댓글/전략 공유':
        'Community — notices, posts, comments, shared strategies',
      '작업 관리자 — 백그라운드 진행 중인 분석 보기/중단':
        'Task manager — view or cancel background analyses',
      '외부 접근 — Cloudflare Tunnel · QR 로그인':
        'Remote access — Cloudflare Tunnel · QR sign-in',
      '분석 이력 — 과거 분석 결과 검색': 'History — search past analyses',
      '심볼 추가 (예: AAPL, TSLA, BTC-USD)': 'Add a symbol (e.g. AAPL, TSLA, BTC-USD)',
      '보유 종목 전체 포괄 분석': 'Analyse every holding together',
      '새로 계산': 'Recalculate',
      '포트폴리오 관리 (큰 화면)': 'Portfolio management (large view)',
      '종목·티커·키워드 입력  (예: 삼성전자 / AAPL / 비트코인)':
        'Ticker, company or keyword (e.g. AAPL, Samsung Electronics, bitcoin)',
      '티커 또는 회사명 (예: AAPL, 삼성전자, 비트코인)':
        'Ticker or company (e.g. AAPL, Samsung Electronics, bitcoin)',
      '글자 작게': 'Smaller text',
      '글자 크게': 'Larger text',
      '브라우저 새 창에서 열기': 'Open in a new browser window',
      '잘라 붙여넣기': 'Cut and paste',
      '즐겨찾기 추가': 'Add to favourites',
      '즐겨찾기 해제': 'Remove from favourites',
      '첨부된 전략이 있습니다 — 가져오기 가능':
        'A strategy is attached — you can import it',
      '종목의 ☆ 별을 눌러 즐겨찾기에 추가하세요':
        'Tap the ☆ on a ticker to add it to your favourites'
    },

    ja: {
      'Plutus · 기관급 퀀트 분석 터미널': 'Plutus · 機関級クオンツ分析ターミナル',
      '코스피': 'KOSPI',
      '코스닥': 'KOSDAQ',
      '나스닥': 'ナスダック',
      '다우': 'ダウ',
      '원/달러': 'ウォン/ドル',
      'VIX 공포': 'VIX 恐怖指数',
      '금': '金',
      'WTI 유가': 'WTI 原油',
      '비트코인': 'ビットコイン',
      '☷ NEWS · 뉴스피드': '☷ NEWS · ニュースフィード',
      '◈ ANALYSIS · 분석': '◈ ANALYSIS · 分析',
      '[◈ 현재 종목 분석]': '[◈ この銘柄を分析]',
      '한국': '韓国',
      '미국': '米国',
      '일본': '日本',
      '중국': '中国',
      '유럽': '欧州',
      'Plutus · 인증 확인 중…': 'Plutus · 認証を確認中…',
      '기관급 퀀트 분석 터미널': '機関級クオンツ分析ターミナル',
      '정밀 분석 · 수급 · 리스크': '精密分析 · フロー · リスク',
      '좋은 아침입니다': 'おはようございます',
      '님': 'さん',
      '로그인이 필요합니다': 'ログインが必要です',
      '로그인': 'ログイン',
      '가입 신청': '新規登録',
      '가입하면 바로 사용할 수 있습니다 — 무료 등급(보고서 3회/일)으로 시작합니다.':
        '登録すればすぐに使えます — 無料グレード（レポート 3 回/日）から始まります。',
      '새 계정 만들기 (바로 사용 · 보고서 3회/일)':
        'アカウント作成（即時利用 · レポート 3 回/日）',
      '가입 완료 — 바로 로그인하세요': '登録完了 — そのままログインできます',
      'NICKNAME · 닉네임': 'NICKNAME · ニックネーム',
      '화면에 표시될 이름 (선택)': '表示名（任意）',
      '⏻ 로그아웃': '⏻ ログアウト',
      '로그아웃': 'ログアウト',

      '차트': 'チャート',
      '정밀 분석': '精密分析',
      '뉴스': 'ニュース',
      '분석 이력': '分析履歴',
      '설정': '設定',
      '커뮤니티': 'コミュニティ',
      '작업': 'タスク',
      '클라우드': 'クラウド',
      '이력': '履歴',
      '위젯': 'ウィジェット',
      '보관함': '保管庫',
      '실시간': 'リアルタイム',
      '히스토리': '履歴',
      '시급만': '緊急のみ',
      '속보': '速報',
      '속보 전체': '速報すべて',
      '관련 뉴스': '関連ニュース',
      '★ 즐겨찾기': '★ お気に入り',
      '▸ 검색 결과': '▸ 検索結果',
      '검색 결과 없음': '検索結果なし',

      '저장': '保存',
      '취소': 'キャンセル',
      '삭제': '削除',
      '등록': '登録',
      '검증': '検証',
      '테스트': 'テスト',
      '진단': '診断',
      '재시작': '再起動',
      '중지': '停止',
      '열기': '開く',
      '다운로드': 'ダウンロード',
      '새로고침': '更新',
      '↻ 새로고침': '↻ 更新',
      '✕ 닫기': '✕ 閉じる',
      '닫기 (ESC)': '閉じる（ESC）',
      '만들기': '作成',
      '다음에': '後で',
      '나중에': '後で',
      '기본값': '既定値',
      '↺ 기본값': '↺ 既定値',
      '전송': '送信',
      '이름': '名前',
      '제목': 'タイトル',
      '본문': '本文',
      '이전': '前',
      '다음': '次',
      '없음': 'なし',
      '데이터 없음': 'データなし',
      '로딩 중…': '読み込み中…',
      '로딩 중...': '読み込み中…',
      '불러오는 중…': '読み込み中…',
      '확인 중…': '確認中…',
      '분석 중…': '分析中…',
      '진행 중…': '処理中…',
      '로딩 실패': '読み込み失敗',
      '상태 로드 실패': '状態の読み込みに失敗',
      '네트워크 오류': 'ネットワークエラー',
      '⌛ 추론 중…': '⌛ 推論中…',

      'Plutus 설정': 'Plutus 設定',
      '내 계정': 'マイアカウント',
      '계정': 'アカウント',
      '중앙 인증': '中央認証',
      '화면': '表示',
      '언어': '言語',
      '테마·이펙트': 'テーマ・エフェクト',
      '위젯 배치': 'ウィジェット配置',
      '연결': '接続',
      'API 키': 'API キー',
      '외부 접근': '外部アクセス',
      '한국투자증권': '韓国投資証券',
      '로컬 LLM': 'ローカル LLM',
      '기타': 'その他',
      '정보': '情報',
      '현재 로그인': 'ログイン中',
      'CLAUDE 잔여': 'Claude 残り',
      '메인 PC': 'メイン PC',
      '메인 PC 미지정': 'メイン PC 未指定',
      '외부 접근은 "외부 접근" 카테고리에서 설정.':
        '外部アクセスは「外部アクセス」カテゴリで設定します。',
      '데이터 소스 API 키 설정': 'データソース API キー設定',
      '키가 없어도': 'キーが無くても',

      '앱 화면에 표시되는 언어입니다.': 'アプリ画面に表示される言語です。',
      '분석 보고서와 용어 설명은 한국어로 나옵니다.':
        '分析レポートと用語解説は韓国語のままです。',
      '언어를 바꿨습니다.': '言語を変更しました。',

      '테마 (C2)': 'テーマ (C2)',
      '전체 UI 색상 팔레트를 변경합니다.': 'UI 全体の配色パレットを変更します。',
      '보고서 테마': 'レポートテーマ',
      '만드는 시점에 테마가 정해집니다': '生成した時点でテーマが決まります',
      '배경 이펙트': '背景エフェクト',
      '끄기': 'オフ',
      '약하게': '弱め',
      '기본': '標準',
      '강하게': '強め',
      '・ 다른 탭으로 넘어가면 자동으로 멈춥니다':
        '・ 別のタブに移ると自動的に停止します',
      "・ 시스템이 '동작 줄이기'로 설정돼 있으면 자동으로 꺼집니다":
        '・ システムが「視差効果を減らす」設定なら自動的にオフになります',
      '글자 크기 (C1)': '文字サイズ (C1)',
      '전체 인터페이스의 기본 글자 크기.': 'インターフェース全体の基本文字サイズ。',
      '작 (S)': '小 (S)',
      '중 (M)': '中 (M)',
      '14.5px · 기본': '14.5px · 標準',
      '대 (L)': '大 (L)',
      '특대 (XL)': '特大 (XL)',
      '사운드 마스터 (C5)': 'サウンドマスター (C5)',
      '모든 앱 사운드(부팅음·알림·효과음)를 한 번에 끄거나 켭니다.':
        'アプリの全サウンド（起動音・通知・効果音）を一括で切り替えます。',
      '전체 사운드': '全サウンド',
      '앱 전체 음소거 토글': 'アプリ全体のミュート切り替え',
      '알림 효과음 (C3)': '通知効果音 (C3)',
      '뉴스/속보 효과음': 'ニュース・速報の効果音',
      '"뿅" 사운드 재생': '通知音を再生',
      '소리 테스트': 'サウンドテスト',
      '속보 알림': '速報通知',
      '새 high-impact 속보가 들어오면 즉시 알려줍니다.':
        'インパクトの大きい速報が入ったら即座に知らせます。',
      '🔊 소리 알림 (짧은 beep, Web Audio)': '🔊 音で通知（短いビープ、Web Audio）',
      '⚡ 상단 스트립 플래시 + 토스트 메시지': '⚡ 上部ストリップの点滅＋トースト表示',
      '▸ 커스텀 색상 (즉시 반영)': '▸ カスタムカラー（即時反映）',
      '💾 자동 저장 (localStorage) · 새로고침해도 유지':
        '💾 自動保存（localStorage）· 再読み込みしても保持',

      '레이아웃 템플릿': 'レイアウトテンプレート',
      '전체 화면 분할 방식을 선택하세요. 슬롯 수에 따라 자동 마운트됩니다.':
        '画面の分割方法を選んでください。スロット数に応じて自動配置されます。',
      '현재 배치': '現在の配置',
      '기본 배치로 초기화': '既定の配置に戻す',
      '사용 가능한 위젯': '利用できるウィジェット',
      '슬롯 배치 중': 'スロットに配置中',
      'dock 대기': 'dock で待機',
      '슬롯 A —': 'スロット A —',
      '슬롯 B —': 'スロット B —',
      '슬롯 C —': 'スロット C —',
      '슬롯 D —': 'スロット D —',

      '중앙 인증 서버': '中央認証サーバー',
      '기본 서버가 내장': '既定サーバーが内蔵',
      '서버': 'サーバー',
      '저장 + 검증': '保存 + 検証',
      '배포 가이드': 'デプロイガイド',
      '(비워 두면 기본 서버 사용)': '（空欄なら既定サーバーを使用）',
      '앱에 내장된 기본 서버로 되돌립니다': 'アプリ内蔵の既定サーバーに戻します',
      '○ 서버 없음 — 로컬 모드': '○ サーバー無し — ローカルモード',
      '기본 서버': '既定サーバー',
      '직접 지정': '手動指定',
      '● 로그인됨 —': '● ログイン中 —',
      '○ 미로그인': '○ 未ログイン',

      'PC 정보': 'PC 情報',
      'PC 라벨': 'PC ラベル',
      'Tunnel 상태': 'Tunnel の状態',
      '1단계 · cloudflared 설치': 'ステップ 1 · cloudflared のインストール',
      '자동 다운로드': '自動ダウンロード',
      '2단계 · Quick Tunnel 시작 (즉시, 계정 불필요)':
        'ステップ 2 · Quick Tunnel 開始（即時・アカウント不要）',
      '발급된 URL · 핸드폰에서 접속': '発行された URL · スマホから接続',
      'URL 복사': 'URL をコピー',
      '복사됨!': 'コピーしました。',
      '외부 접근 켜기': '外部アクセスを有効化',
      '3단계 · QR로 핸드폰 자동 로그인':
        'ステップ 3 · QR でスマホから自動ログイン',
      '현재 PC 계정으로 자동 로그인': 'この PC のアカウントで自動ログインします',
      'QR 생성 대기': 'QR 生成待ち',
      'QR 정보': 'QR 情報',
      'QR 생성': 'QR 生成',
      '핸드폰 카메라 앱 → QR 스캔 → URL 자동 열림 → 즉시 로그인':
        'スマホのカメラ → QR を読む → URL が開く → すぐログイン',
      '자동 로그인 URL': '自動ログイン URL',
      '⏱ 토큰 만료': '⏱ トークン期限切れ',
      '● 감시 중': '● 監視中',
      '◐ 주소 발급 대기': '◐ アドレス発行待ち',
      '○ 끊김': '○ 切断',
      '📱 폰에는 이 주소를 저장하세요': '📱 スマホにはこのアドレスを保存してください',
      '✓ 현재 주소 등록됨': '✓ 現在のアドレスを登録済み',
      '◐ 주소 등록 대기': '◐ アドレス登録待ち',
      '내 PC 외부 URL (Quick Tunnel 또는 정식 Tunnel)':
        'この PC の外部 URL（Quick Tunnel または Named Tunnel）',
      '⟲ 현재 Tunnel URL 자동 채우기': '⟲ 現在の Tunnel URL を自動入力',
      '📱 핸드폰에서 접근:': '📱 スマホからのアクセス:',
      '도메인 (Zone)': 'ドメイン（Zone）',
      '서브도메인 (전체 hostname)': 'サブドメイン（完全な hostname）',
      'Tunnel 이름 (Cloudflare 대시보드에 표시)':
        'Tunnel 名（Cloudflare ダッシュボードに表示）',
      '📌 사전 준비 (1회만)': '📌 事前準備（1 回だけ）',
      'API Token 발급': 'API トークン発行',
      '(무료)': '（無料）',
      '■ 중지': '■ 停止',
      '▶ 시작': '▶ 開始',

      'Plutus 시스템': 'Plutus システム',
      '버전': 'バージョン',
      '자체 PC (로컬)': 'この PC（ローカル）',
      '업데이트 확인': '更新を確認',
      '바로가기 만들기': 'ショートカットを作成',
      'GitHub 릴리스를 확인합니다. 설정·키·계정은 유지됩니다.':
        'GitHub のリリースを確認します。設定・キー・アカウントは保持されます。',
      '폰으로 보기 (같은 와이파이)': 'スマホで見る（同じ Wi-Fi）',
      '같은 와이파이의 다른 기기에서 접속 허용':
        '同じ Wi-Fi の他の端末からの接続を許可',
      '변경은 앱을 다시 켜야 적용됩니다.': '変更はアプリの再起動後に反映されます。',
      '개발자': '開発者',
      '새 버전이 있습니다': '新しいバージョンがあります',
      '그대로 유지': 'そのまま保持されます',
      '릴리스 보기': 'リリースを見る',
      '업데이트': '更新',
      '바로가기를 만들까요?': 'ショートカットを作成しますか？',
      '바탕화면에 바로가기': 'デスクトップにショートカット',
      '바탕화면에서 바로 실행합니다.': 'デスクトップから直接起動します。',
      '시작 메뉴에 등록': 'スタートメニューに登録',
      '이걸 켜야': 'これを有効にすると',
      '윈도우 검색창에서 "Plutus" 로 찾을 수':
        'Windows の検索から「Plutus」で見つけられます',
      '있습니다.': '。',

      '하드웨어': 'ハードウェア',
      '하드웨어 감지 중…': 'ハードウェアを検出中…',
      'Ollama 상태 확인 중…': 'Ollama の状態を確認中…',
      '권장 모델': '推奨モデル',
      '자동 셋업 시작': '自動セットアップを開始',
      '설치 모델': 'インストール済みモデル',
      'LLM DEEP ANALYSIS · 로컬 추론': 'LLM DEEP ANALYSIS · ローカル推論',
      '심층분석 실행': '深層分析を実行',
      'FOLLOW-UP · 분석에 대한 질문': 'FOLLOW-UP · 分析への質問',
      '로컬 LLM · 무료 · 대화 미저장': 'ローカル LLM · 無料 · 会話は保存しません',
      '위 분석에 대해 자유롭게 질문하세요': '上の分析について自由に質問してください',
      '질문 입력 (Shift+Enter 줄바꿈, Enter 전송)':
        '質問を入力（Shift+Enter で改行、Enter で送信）',
      '예: 데이터센터 매출이 왜 중요한가요?':
        '例: データセンター売上はなぜ重要ですか？',

      'MARKET OVERVIEW · 시장 개요': 'MARKET OVERVIEW · 市場概況',
      'CHART · 종목 차트': 'CHART · チャート',
      '차트 클릭…': 'チャートをクリック…',
      '슬라이드 ▸': 'スライド ▸',
      '시장 변동 색 매트릭스': '市場変動カラーマトリクス',
      'S&amp;P 거시 히트맵 · 섹터 × 시총': 'S&amp;P マクロヒートマップ · セクター × 時価総額',
      '시장 수급 · 당일': 'マーケットフロー · 当日',
      '자금 이동': '資金移動',
      '매수 / 매도': '買い / 売り',
      '섹터 강약': 'セクター強弱',
      '수급 계산 중… (최초 10~30초)': 'フローを計算中…（初回は 10〜30 秒）',
      '어제 데이터가 없어 비교할 수 없습니다.': '昨日のデータが無いため比較できません。',
      '어제 같은 시각 대비 거래대금 비중 변화':
        '昨日の同時刻比での売買代金シェアの変化',
      '섹터 강약 — 등락과 자금이 함께 말할 때만 라벨':
        'セクター強弱 — 値動きと資金が一致したときだけラベルを付ける',
      '경제 캘린더 로딩 중…': '経済カレンダーを読み込み中…',
      '예측': '予想',
      '실제': '実績',
      '관심 종목을 추가하세요.': 'ウォッチリストに銘柄を追加してください。',
      '상단에서 종목 조회': '上部で銘柄を検索',
      '뉴스 불러오는 중…': 'ニュースを読み込み中…',
      '표시할 뉴스가 없습니다.': '表示するニュースがありません。',
      '뉴스 로딩 실패.': 'ニュースの読み込みに失敗しました。',
      '속보 로딩 중…': '速報を読み込み中…',
      '현재 매핑된 속보 없음.': '現在ひも付いた速報はありません。',
      '감지된 키워드 없음': '検出されたキーワードなし',
      '실시간 라이브 · 24/7': 'ライブ配信 · 24/7',
      '채널을 선택해주세요…': 'チャンネルを選んでください…',
      'SENTIMENT · 감성 분석': 'SENTIMENT · センチメント分析',
      'ANALYST CONSENSUS · 애널리스트 컨센서스': 'ANALYST CONSENSUS · アナリスト予想',
      'ANALYST · 애널리스트': 'ANALYST · アナリスト',
      '애널리스트 컨센서스 로딩…': 'アナリスト予想を読み込み中…',
      'DEEPL · 핵심 내용 (한글)': 'DEEPL · 要点',
      '▸ 원문 보기 ↗': '▸ 原文を見る ↗',
      '차트를 표시할 수 없습니다': 'チャートを表示できません',

      '◈ 현재 종목 분석': '◈ この銘柄を分析',
      '◆ 포트폴리오': '◆ ポートフォリオ',
      '◆ 포트폴리오 관리': '◆ ポートフォリオ管理',
      '데이터 무결성 → 자산군 분류 → 유동성 →':
        'データ健全性 → 資産クラス分類 → 流動性 →',
      '변동성·레짐 → 팩터 → ML 게이트 →': 'ボラ・レジーム → ファクター → ML ゲート →',
      '시뮬레이션 → 리스크 → 전문가 패널 심의':
        'シミュレーション → リスク → 専門家パネル審議',
      '순으로 돌고, 자기완결 HTML 보고서를 만듭니다.':
        'の順に回り、自己完結 HTML レポートを生成します。',
      '게이트를 통과하지 못한 모듈은 점수가 깎이는 대신':
        'ゲートを通らなかったモジュールは減点ではなく',
      '무효(abstain)': '無効（abstain）',
      '로 표시됩니다.': 'と表示されます。',
      '1~3분 걸립니다.': '1〜3 分かかります。',
      '(ML·몬테카를로 포함 — 30초~2분 소요)':
        '（ML・モンテカルロを含む — 30 秒〜2 分）',
      '1~3분 걸립니다. 이 창을 닫아도 계속 진행됩니다.':
        '1〜3 分かかります。この窓を閉じても処理は続きます。',
      '오늘 보고서 한도를 다 썼습니다': '本日のレポート上限に達しました',
      '프리미엄으로 올리면 무제한입니다 (관리자 문의)':
        'プレミアムなら無制限です（管理者にお問い合わせください）',
      '✗ 정밀 분석 실패': '✗ 精密分析に失敗',
      '상승확률': '上昇確率',
      '· 배분': '· 配分',
      '거부권 발동': '拒否権の発動',
      '판정 근거': '判定の根拠',
      '◈ 간단 리서치': '◈ 簡易リサーチ',
      '▸ 전문 보고서': '▸ 詳細レポート',
      '로 처리됩니다 — 약한 신호가 아니라 신호 없음입니다.':
        'として扱われます — 弱いシグナルではなく、シグナル無しです。',
      'INSIGHTS · 인사이트': 'INSIGHTS · インサイト',
      '분석가 관점 · KEY POINTS': 'アナリスト視点 · KEY POINTS',
      '시장 컨센서스': '市場コンセンサス',
      'RISKS · 주의 요인': 'RISKS · 注意点',
      'RATIONALE · 종합 결론': 'RATIONALE · 総合結論',
      '신뢰도': '信頼度',
      '참신성': '新規性',

      '포트폴리오 종합 분석 중… (보유 종목별 시세/펀더 fetch + 상관행렬)':
        'ポートフォリオを総合分析中…（保有銘柄ごとの相場・ファンダ取得＋相関行列）',
      '종목 수에 따라 30초~2분 소요': '銘柄数によって 30 秒〜2 分',
      '✗ 포트폴리오 분석 실패': '✗ ポートフォリオ分析に失敗',
      '평가액': '評価額',
      '총 손익': '総損益',
      '연수익률': '年率リターン',
      '변동성': 'ボラティリティ',
      '평균상관': '平均相関',
      '분산효과': '分散効果',
      '종목별 기여도': '銘柄別の寄与',
      '종목': '銘柄',
      '비중': '比率',
      '연수익': '年率リターン',
      '기여': '寄与',
      '평가': '評価',
      '새 종목 추가': '銘柄を追加',
      '현재 보유 종목': '現在の保有銘柄',
      '보유 종목 없음': '保有銘柄なし',
      '보유 종목 없음 — 위 입력으로 추가': '保有銘柄なし — 上の入力から追加',
      '관리 ⛶': '管理 ⛶',
      '+ 추가': '+ 追加',
      '수량': '数量',
      '평균단가': '平均取得単価',
      '티커/회사명': 'ティッカー / 会社名',

      '📁 REPORTS · 보고서 보관함': '📁 REPORTS · レポート保管庫',
      '아직 생성된 보고서가 없습니다.': 'まだレポートがありません。',
      '보관': '保管',
      '최신': '最新',
      '📜 ANALYSIS HISTORY · 분석 이력': '📜 ANALYSIS HISTORY · 分析履歴',
      '아직 분석 이력이 없습니다.': 'まだ分析履歴がありません。',
      '▸ 리포트': '▸ レポート',

      '📋 작업 관리자': '📋 タスクマネージャ',
      '백그라운드로 돌아가는 분석 작업 — 자동 갱신':
        'バックグラウンドで走っている分析 — 自動更新',
      '📭 작업 없음': '📭 タスクなし',
      'MEGA grid / AUTO / WFA 등 무거운 작업이 백그라운드로 돌아가면 여기에 표시됩니다':
        'MEGA grid / AUTO / WFA などの重い処理が走るとここに出ます',
      '⊘ 중단': '⊘ 中断',
      '→ 결과 보기': '→ 結果を見る',

      '공지 · 글 · 댓글': 'お知らせ · 投稿 · コメント',
      '+ 새 글': '+ 新規投稿',
      '💬 클릭하면 글 목록이 표시됩니다': '💬 クリックすると投稿一覧が出ます',
      '공지': 'お知らせ',
      '📌 공지': '📌 お知らせ',
      '[관리자]': '[管理者]',
      '⭐ 전략': '⭐ 戦略',
      '아직 댓글 없음': 'コメントはまだありません',
      '글 삭제': '投稿を削除',
      '📌 공지로 등록': '📌 お知らせとして投稿',
      '(어드민 전용 — 목록 상단 고정)': '（管理者専用 — 一覧の先頭に固定）',
      '+ 등록': '+ 投稿',
      '댓글 입력…': 'コメントを入力…',
      '제목 입력 (최소 2자)': 'タイトル（2 文字以上）',
      '내용 입력 (최소 2자)': '本文（2 文字以上）',

      '🤖 AGENT · Claude 분석가': '🤖 AGENT · Claude アナリスト',
      '+ 새 대화': '+ 新しい会話',
      '새 대화를 시작하거나 좌측에서 이전 대화를 선택하세요.':
        '新しい会話を始めるか、左から過去の会話を選んでください。',
      '대화가 없습니다.': '会話がありません。',
      '예시: "오늘 코스피 어때?" / "지금 보고 있는 종목 어때?"':
        '例:「今日の KOSPI は？」/「今見ている銘柄はどう？」',
      '⛨ ADMIN · 사용자 관리': '⛨ ADMIN · ユーザー管理',
      'TOP CLAUDE (오늘)': 'TOP CLAUDE（本日）',
      'TOP 로그인 (누적)': 'TOP ログイン（累計）',
      '승인': '承認',
      '거부': '拒否',
      '정지': '停止',
      '쿼터 리셋': 'クォータをリセット',

      '실시간 SSE 연결 상태': 'リアルタイム SSE 接続状態',
      '보고서 일일 한도': 'レポートの 1 日上限',
      'Claude 일일 사용량': 'Claude の 1 日使用量',
      '에이전트 채팅': 'エージェントチャット',
      '커뮤니티 (공지/글/댓글)': 'コミュニティ（お知らせ/投稿/コメント）',
      '관리자': '管理者',
      '종목 검색 (클릭)': '銘柄検索（クリック）',
      '추세선 (2점 클릭)': 'トレンドライン（2 点クリック）',
      '수평선 (1점 클릭)': '水平線（1 点クリック）',
      '피보나치 (2점 클릭)': 'フィボナッチ（2 点クリック）',
      '모두 지우기': 'すべて消去',
      '드래그하여 좌우 크기 조절': 'ドラッグで左右の幅を調整',
      '드래그하여 상하 크기 조절': 'ドラッグで上下の高さを調整',
      '클릭 시 전체화면': 'クリックで全画面',
      '전체화면 (ESC로 닫기)': '全画面（ESC で閉じる）',
      '끌어서 옮기기': 'ドラッグで移動',
      '커뮤니티 — 공지/글/댓글/전략 공유':
        'コミュニティ — お知らせ・投稿・コメント・戦略共有',
      '작업 관리자 — 백그라운드 진행 중인 분석 보기/중단':
        'タスクマネージャ — バックグラウンド分析の確認・中断',
      '외부 접근 — Cloudflare Tunnel · QR 로그인':
        '外部アクセス — Cloudflare Tunnel · QR ログイン',
      '분석 이력 — 과거 분석 결과 검색': '分析履歴 — 過去の分析結果を検索',
      '심볼 추가 (예: AAPL, TSLA, BTC-USD)': 'シンボルを追加（例: AAPL, TSLA, BTC-USD）',
      '보유 종목 전체 포괄 분석': '保有銘柄をまとめて分析',
      '새로 계산': '再計算',
      '포트폴리오 관리 (큰 화면)': 'ポートフォリオ管理（大画面）',
      '종목·티커·키워드 입력  (예: 삼성전자 / AAPL / 비트코인)':
        '銘柄・ティッカー・キーワード（例: サムスン電子 / AAPL / ビットコイン）',
      '티커 또는 회사명 (예: AAPL, 삼성전자, 비트코인)':
        'ティッカーまたは会社名（例: AAPL, サムスン電子, ビットコイン）',
      '글자 작게': '文字を小さく',
      '글자 크게': '文字を大きく',
      '브라우저 새 창에서 열기': 'ブラウザの新しい窓で開く',
      '잘라 붙여넣기': '切り取って貼り付け',
      '즐겨찾기 추가': 'お気に入りに追加',
      '즐겨찾기 해제': 'お気に入りから外す',
      '첨부된 전략이 있습니다 — 가져오기 가능':
        '添付された戦略があります — 取り込めます',
      '종목의 ☆ 별을 눌러 즐겨찾기에 추가하세요':
        '銘柄の ☆ を押すとお気に入りに追加されます'
    },

    'zh-CN': {
      'Plutus · 기관급 퀀트 분석 터미널': 'Plutus · 机构级量化分析终端',
      '코스피': '韩国综合指数',
      '코스닥': 'KOSDAQ',
      '나스닥': '纳斯达克',
      '다우': '道琼斯',
      '원/달러': '韩元/美元',
      'VIX 공포': 'VIX 恐慌指数',
      '금': '黄金',
      'WTI 유가': 'WTI 原油',
      '비트코인': '比特币',
      '☷ NEWS · 뉴스피드': '☷ NEWS · 新闻流',
      '◈ ANALYSIS · 분석': '◈ ANALYSIS · 分析',
      '[◈ 현재 종목 분석]': '[◈ 分析当前标的]',
      '한국': '韩国',
      '미국': '美国',
      '일본': '日本',
      '중국': '中国',
      '유럽': '欧洲',
      'Plutus · 인증 확인 중…': 'Plutus · 正在校验登录…',
      '기관급 퀀트 분석 터미널': '机构级量化分析终端',
      '정밀 분석 · 수급 · 리스크': '精密分析 · 资金流 · 风险',
      '좋은 아침입니다': '早上好',
      '님': '',
      '로그인이 필요합니다': '需要登录',
      '로그인': '登录',
      '가입 신청': '注册',
      '가입하면 바로 사용할 수 있습니다 — 무료 등급(보고서 3회/일)으로 시작합니다.':
        '注册后立即可用 —— 从免费等级开始（每日 3 份报告）。',
      '새 계정 만들기 (바로 사용 · 보고서 3회/일)':
        '创建账号（即时可用 · 每日 3 份报告）',
      '가입 완료 — 바로 로그인하세요': '注册完成 —— 现在就能登录',
      'NICKNAME · 닉네임': 'NICKNAME · 昵称',
      '화면에 표시될 이름 (선택)': '显示名称（可选）',
      '⏻ 로그아웃': '⏻ 退出登录',
      '로그아웃': '退出登录',

      '차트': '图表',
      '정밀 분석': '精密分析',
      '뉴스': '新闻',
      '분석 이력': '分析历史',
      '설정': '设置',
      '커뮤니티': '社区',
      '작업': '任务',
      '클라우드': '云端',
      '이력': '历史',
      '위젯': '组件',
      '보관함': '归档库',
      '실시간': '实时',
      '히스토리': '历史',
      '시급만': '仅紧急',
      '속보': '快讯',
      '속보 전체': '全部快讯',
      '관련 뉴스': '相关新闻',
      '★ 즐겨찾기': '★ 收藏',
      '▸ 검색 결과': '▸ 搜索结果',
      '검색 결과 없음': '没有结果',

      '저장': '保存',
      '취소': '取消',
      '삭제': '删除',
      '등록': '注册',
      '검증': '校验',
      '테스트': '测试',
      '진단': '诊断',
      '재시작': '重启',
      '중지': '停止',
      '열기': '打开',
      '다운로드': '下载',
      '새로고침': '刷新',
      '↻ 새로고침': '↻ 刷新',
      '✕ 닫기': '✕ 关闭',
      '닫기 (ESC)': '关闭（ESC）',
      '만들기': '创建',
      '다음에': '以后再说',
      '나중에': '以后再说',
      '기본값': '默认值',
      '↺ 기본값': '↺ 恢复默认',
      '전송': '发送',
      '이름': '名称',
      '제목': '标题',
      '본문': '正文',
      '이전': '上一个',
      '다음': '下一个',
      '없음': '无',
      '데이터 없음': '无数据',
      '로딩 중…': '加载中…',
      '로딩 중...': '加载中…',
      '불러오는 중…': '加载中…',
      '확인 중…': '检查中…',
      '분석 중…': '分析中…',
      '진행 중…': '处理中…',
      '로딩 실패': '加载失败',
      '상태 로드 실패': '状态加载失败',
      '네트워크 오류': '网络错误',
      '⌛ 추론 중…': '⌛ 推理中…',

      'Plutus 설정': 'Plutus 设置',
      '내 계정': '我的账号',
      '계정': '账号',
      '중앙 인증': '中央认证',
      '화면': '界面',
      '언어': '语言',
      '테마·이펙트': '主题与特效',
      '위젯 배치': '组件布局',
      '연결': '连接',
      'API 키': 'API 密钥',
      '외부 접근': '外部访问',
      '한국투자증권': '韩国投资证券',
      '로컬 LLM': '本地 LLM',
      '기타': '其他',
      '정보': '关于',
      '현재 로그인': '当前登录',
      'CLAUDE 잔여': 'Claude 剩余',
      '메인 PC': '主电脑',
      '메인 PC 미지정': '未指定主电脑',
      '외부 접근은 "외부 접근" 카테고리에서 설정.':
        '外部访问请在"外部访问"分类中设置。',
      '데이터 소스 API 키 설정': '数据源 API 密钥设置',
      '키가 없어도': '即使没有密钥',

      '앱 화면에 표시되는 언어입니다.': '应用界面所使用的语言。',
      '분석 보고서와 용어 설명은 한국어로 나옵니다.':
        '分析报告与术语说明仍为韩语。',
      '언어를 바꿨습니다.': '已切换语言。',

      '테마 (C2)': '主题 (C2)',
      '전체 UI 색상 팔레트를 변경합니다.': '更改整个界面的配色方案。',
      '보고서 테마': '报告主题',
      '만드는 시점에 테마가 정해집니다': '主题在生成那一刻就固定了',
      '배경 이펙트': '背景特效',
      '끄기': '关闭',
      '약하게': '弱',
      '기본': '默认',
      '강하게': '强',
      '・ 다른 탭으로 넘어가면 자동으로 멈춥니다': '・ 切换到其他标签页会自动暂停',
      "・ 시스템이 '동작 줄이기'로 설정돼 있으면 자동으로 꺼집니다":
        '・ 系统开启"减弱动态效果"时会自动关闭',
      '글자 크기 (C1)': '字号 (C1)',
      '전체 인터페이스의 기본 글자 크기.': '整个界面的基础字号。',
      '작 (S)': '小 (S)',
      '중 (M)': '中 (M)',
      '14.5px · 기본': '14.5px · 默认',
      '대 (L)': '大 (L)',
      '특대 (XL)': '特大 (XL)',
      '사운드 마스터 (C5)': '总音量开关 (C5)',
      '모든 앱 사운드(부팅음·알림·효과음)를 한 번에 끄거나 켭니다.':
        '一次性开关所有应用声音（启动音、提示音、音效）。',
      '전체 사운드': '全部声音',
      '앱 전체 음소거 토글': '整个应用静音开关',
      '알림 효과음 (C3)': '提示音效 (C3)',
      '뉴스/속보 효과음': '新闻/快讯音效',
      '"뿅" 사운드 재생': '播放提示音',
      '소리 테스트': '声音测试',
      '속보 알림': '快讯提醒',
      '새 high-impact 속보가 들어오면 즉시 알려줍니다.':
        '出现高影响力快讯时立即提醒你。',
      '🔊 소리 알림 (짧은 beep, Web Audio)': '🔊 声音提醒（短促蜂鸣，Web Audio）',
      '⚡ 상단 스트립 플래시 + 토스트 메시지': '⚡ 顶部条闪烁 + 弹出提示',
      '▸ 커스텀 색상 (즉시 반영)': '▸ 自定义配色（立即生效）',
      '💾 자동 저장 (localStorage) · 새로고침해도 유지':
        '💾 自动保存（localStorage）· 刷新后仍保留',

      '레이아웃 템플릿': '布局模板',
      '전체 화면 분할 방식을 선택하세요. 슬롯 수에 따라 자동 마운트됩니다.':
        '选择整个界面的分栏方式，组件会按槽位数量自动装载。',
      '현재 배치': '当前布局',
      '기본 배치로 초기화': '恢复默认布局',
      '사용 가능한 위젯': '可用组件',
      '슬롯 배치 중': '正在放入槽位',
      'dock 대기': '在 dock 中等待',
      '슬롯 A —': '槽位 A —',
      '슬롯 B —': '槽位 B —',
      '슬롯 C —': '槽位 C —',
      '슬롯 D —': '槽位 D —',

      '중앙 인증 서버': '中央认证服务器',
      '기본 서버가 내장': '内置了默认服务器',
      '서버': '服务器',
      '저장 + 검증': '保存 + 校验',
      '배포 가이드': '部署指南',
      '(비워 두면 기본 서버 사용)': '（留空则使用默认服务器）',
      '앱에 내장된 기본 서버로 되돌립니다': '恢复为应用内置的默认服务器',
      '○ 서버 없음 — 로컬 모드': '○ 无服务器 —— 本地模式',
      '기본 서버': '默认服务器',
      '직접 지정': '自定义',
      '● 로그인됨 —': '● 已登录 ——',
      '○ 미로그인': '○ 未登录',

      'PC 정보': '电脑信息',
      'PC 라벨': '电脑标签',
      'Tunnel 상태': '隧道状态',
      '1단계 · cloudflared 설치': '第 1 步 · 安装 cloudflared',
      '자동 다운로드': '自动下载',
      '2단계 · Quick Tunnel 시작 (즉시, 계정 불필요)':
        '第 2 步 · 启动 Quick Tunnel（即时，无需账号）',
      '발급된 URL · 핸드폰에서 접속': '已签发的 URL · 用手机访问',
      'URL 복사': '复制 URL',
      '복사됨!': '已复制。',
      '외부 접근 켜기': '开启外部访问',
      '3단계 · QR로 핸드폰 자동 로그인': '第 3 步 · 用二维码在手机上自动登录',
      '현재 PC 계정으로 자동 로그인': '以本机账号自动登录',
      'QR 생성 대기': '等待生成二维码',
      'QR 정보': '二维码信息',
      'QR 생성': '生成二维码',
      '핸드폰 카메라 앱 → QR 스캔 → URL 자동 열림 → 즉시 로그인':
        '手机相机 → 扫码 → 自动打开 URL → 立即登录',
      '자동 로그인 URL': '自动登录 URL',
      '⏱ 토큰 만료': '⏱ 令牌已过期',
      '● 감시 중': '● 监视中',
      '◐ 주소 발급 대기': '◐ 等待地址签发',
      '○ 끊김': '○ 已断开',
      '📱 폰에는 이 주소를 저장하세요': '📱 请在手机上保存这个地址',
      '✓ 현재 주소 등록됨': '✓ 当前地址已注册',
      '◐ 주소 등록 대기': '◐ 等待注册地址',
      '내 PC 외부 URL (Quick Tunnel 또는 정식 Tunnel)':
        '本机的外部 URL（Quick Tunnel 或 Named Tunnel）',
      '⟲ 현재 Tunnel URL 자동 채우기': '⟲ 自动填入当前隧道 URL',
      '📱 핸드폰에서 접근:': '📱 从手机访问：',
      '도메인 (Zone)': '域名（Zone）',
      '서브도메인 (전체 hostname)': '子域名（完整 hostname）',
      'Tunnel 이름 (Cloudflare 대시보드에 표시)':
        '隧道名称（显示在 Cloudflare 控制台）',
      '📌 사전 준비 (1회만)': '📌 一次性准备',
      'API Token 발급': '创建 API 令牌',
      '(무료)': '（免费）',
      '■ 중지': '■ 停止',
      '▶ 시작': '▶ 启动',

      'Plutus 시스템': 'Plutus 系统',
      '버전': '版本',
      '자체 PC (로컬)': '本机（本地）',
      '업데이트 확인': '检查更新',
      '바로가기 만들기': '创建快捷方式',
      'GitHub 릴리스를 확인합니다. 설정·키·계정은 유지됩니다.':
        '检查 GitHub 上的发布版本。设置、密钥和账号都会保留。',
      '폰으로 보기 (같은 와이파이)': '在手机上查看（同一 Wi-Fi）',
      '같은 와이파이의 다른 기기에서 접속 허용': '允许同一 Wi-Fi 下的其他设备连接',
      '변경은 앱을 다시 켜야 적용됩니다.': '需要重启应用才会生效。',
      '개발자': '开发者',
      '새 버전이 있습니다': '有新版本',
      '그대로 유지': '会原样保留',
      '릴리스 보기': '查看发布',
      '업데이트': '更新',
      '바로가기를 만들까요?': '要创建快捷方式吗？',
      '바탕화면에 바로가기': '桌面快捷方式',
      '바탕화면에서 바로 실행합니다.': '从桌面直接启动。',
      '시작 메뉴에 등록': '添加到开始菜单',
      '이걸 켜야': '开启后才能',
      '윈도우 검색창에서 "Plutus" 로 찾을 수': '在 Windows 搜索里找到 "Plutus"',
      '있습니다.': '。',

      '하드웨어': '硬件',
      '하드웨어 감지 중…': '正在检测硬件…',
      'Ollama 상태 확인 중…': '正在检查 Ollama…',
      '권장 모델': '推荐模型',
      '자동 셋업 시작': '开始自动配置',
      '설치 모델': '已安装模型',
      'LLM DEEP ANALYSIS · 로컬 추론': 'LLM DEEP ANALYSIS · 本地推理',
      '심층분석 실행': '运行深度分析',
      'FOLLOW-UP · 분석에 대한 질문': 'FOLLOW-UP · 关于本次分析的提问',
      '로컬 LLM · 무료 · 대화 미저장': '本地 LLM · 免费 · 不保存对话',
      '위 분석에 대해 자유롭게 질문하세요': '可以随意提问上面的分析',
      '질문 입력 (Shift+Enter 줄바꿈, Enter 전송)':
        '输入问题（Shift+Enter 换行，Enter 发送）',
      '예: 데이터센터 매출이 왜 중요한가요?': '例如：数据中心营收为什么重要？',

      'MARKET OVERVIEW · 시장 개요': 'MARKET OVERVIEW · 市场概览',
      'CHART · 종목 차트': 'CHART · 行情图',
      '차트 클릭…': '点击图表…',
      '슬라이드 ▸': '滑动 ▸',
      '시장 변동 색 매트릭스': '市场涨跌色彩矩阵',
      'S&amp;P 거시 히트맵 · 섹터 × 시총': 'S&amp;P 宏观热力图 · 板块 × 市值',
      '시장 수급 · 당일': '市场资金流 · 当日',
      '자금 이동': '资金迁移',
      '매수 / 매도': '买入 / 卖出',
      '섹터 강약': '板块强弱',
      '수급 계산 중… (최초 10~30초)': '正在计算资金流…（首次 10~30 秒）',
      '어제 데이터가 없어 비교할 수 없습니다.': '没有昨日数据，无法比较。',
      '어제 같은 시각 대비 거래대금 비중 변화':
        '相对昨日同一时刻的成交额占比变化',
      '섹터 강약 — 등락과 자금이 함께 말할 때만 라벨':
        '板块强弱 —— 只有价格和资金一致时才打标签',
      '경제 캘린더 로딩 중…': '正在加载经济日历…',
      '예측': '预期',
      '실제': '实际',
      '관심 종목을 추가하세요.': '请添加自选标的。',
      '상단에서 종목 조회': '在上方搜索标的',
      '뉴스 불러오는 중…': '正在加载新闻…',
      '표시할 뉴스가 없습니다.': '没有可显示的新闻。',
      '뉴스 로딩 실패.': '新闻加载失败。',
      '속보 로딩 중…': '正在加载快讯…',
      '현재 매핑된 속보 없음.': '当前没有关联的快讯。',
      '감지된 키워드 없음': '未检测到关键词',
      '실시간 라이브 · 24/7': '实时直播 · 24/7',
      '채널을 선택해주세요…': '请选择频道…',
      'SENTIMENT · 감성 분석': 'SENTIMENT · 情绪分析',
      'ANALYST CONSENSUS · 애널리스트 컨센서스': 'ANALYST CONSENSUS · 分析师一致预期',
      'ANALYST · 애널리스트': 'ANALYST · 分析师',
      '애널리스트 컨센서스 로딩…': '正在加载分析师一致预期…',
      'DEEPL · 핵심 내용 (한글)': 'DEEPL · 要点',
      '▸ 원문 보기 ↗': '▸ 查看原文 ↗',
      '차트를 표시할 수 없습니다': '无法显示图表',

      '◈ 현재 종목 분석': '◈ 分析当前标的',
      '◆ 포트폴리오': '◆ 投资组合',
      '◆ 포트폴리오 관리': '◆ 投资组合管理',
      '데이터 무결성 → 자산군 분류 → 유동성 →':
        '数据完整性 → 资产类别归类 → 流动性 →',
      '변동성·레짐 → 팩터 → ML 게이트 →': '波动率与状态 → 因子 → ML 闸门 →',
      '시뮬레이션 → 리스크 → 전문가 패널 심의':
        '模拟 → 风险 → 专家小组审议',
      '순으로 돌고, 자기완결 HTML 보고서를 만듭니다.':
        '按此顺序运行，最后产出自包含的 HTML 报告。',
      '게이트를 통과하지 못한 모듈은 점수가 깎이는 대신':
        '未通过闸门的模块不会被扣分，而是标记为',
      '무효(abstain)': '无效（abstain）',
      '로 표시됩니다.': '。',
      '1~3분 걸립니다.': '需要 1~3 分钟。',
      '(ML·몬테카를로 포함 — 30초~2분 소요)':
        '（含 ML 与蒙特卡洛 —— 约 30 秒至 2 分钟）',
      '1~3분 걸립니다. 이 창을 닫아도 계속 진행됩니다.':
        '需要 1~3 分钟。关掉这个窗口也会继续跑。',
      '오늘 보고서 한도를 다 썼습니다': '今天的报告额度已用完',
      '프리미엄으로 올리면 무제한입니다 (관리자 문의)':
        '升级到高级版即为无限（请联系管理员）',
      '✗ 정밀 분석 실패': '✗ 精密分析失败',
      '상승확률': '上涨概率',
      '· 배분': '· 配置',
      '거부권 발동': '触发否决权',
      '판정 근거': '判定依据',
      '◈ 간단 리서치': '◈ 快速研究',
      '▸ 전문 보고서': '▸ 完整报告',
      '로 처리됩니다 — 약한 신호가 아니라 신호 없음입니다.':
        '—— 这不是弱信号，而是没有信号。',
      'INSIGHTS · 인사이트': 'INSIGHTS · 洞察',
      '분석가 관점 · KEY POINTS': '分析师视角 · KEY POINTS',
      '시장 컨센서스': '市场一致预期',
      'RISKS · 주의 요인': 'RISKS · 风险点',
      'RATIONALE · 종합 결론': 'RATIONALE · 综合结论',
      '신뢰도': '置信度',
      '참신성': '新颖度',

      '포트폴리오 종합 분석 중… (보유 종목별 시세/펀더 fetch + 상관행렬)':
        '正在综合分析投资组合…（逐个标的取行情/基本面 + 相关矩阵）',
      '종목 수에 따라 30초~2분 소요': '视标的数量约 30 秒至 2 分钟',
      '✗ 포트폴리오 분석 실패': '✗ 投资组合分析失败',
      '평가액': '市值',
      '총 손익': '总盈亏',
      '연수익률': '年化收益率',
      '변동성': '波动率',
      '평균상관': '平均相关性',
      '분산효과': '分散效果',
      '종목별 기여도': '各标的贡献',
      '종목': '标的',
      '비중': '权重',
      '연수익': '年化收益',
      '기여': '贡献',
      '평가': '估值',
      '새 종목 추가': '添加标的',
      '현재 보유 종목': '当前持仓',
      '보유 종목 없음': '没有持仓',
      '보유 종목 없음 — 위 입력으로 추가': '没有持仓 —— 从上方输入添加',
      '관리 ⛶': '管理 ⛶',
      '+ 추가': '+ 添加',
      '수량': '数量',
      '평균단가': '平均成本',
      '티커/회사명': '代码 / 公司名',

      '📁 REPORTS · 보고서 보관함': '📁 REPORTS · 报告归档库',
      '아직 생성된 보고서가 없습니다.': '还没有生成过报告。',
      '보관': '归档',
      '최신': '最新',
      '📜 ANALYSIS HISTORY · 분석 이력': '📜 ANALYSIS HISTORY · 分析历史',
      '아직 분석 이력이 없습니다.': '还没有分析历史。',
      '▸ 리포트': '▸ 报告',

      '📋 작업 관리자': '📋 任务管理器',
      '백그라운드로 돌아가는 분석 작업 — 자동 갱신':
        '在后台运行的分析任务 —— 自动刷新',
      '📭 작업 없음': '📭 没有任务',
      'MEGA grid / AUTO / WFA 등 무거운 작업이 백그라운드로 돌아가면 여기에 표시됩니다':
        'MEGA grid / AUTO / WFA 等重任务在后台运行时会出现在这里',
      '⊘ 중단': '⊘ 中断',
      '→ 결과 보기': '→ 查看结果',

      '공지 · 글 · 댓글': '公告 · 帖子 · 评论',
      '+ 새 글': '+ 新帖',
      '💬 클릭하면 글 목록이 표시됩니다': '💬 点击查看帖子列表',
      '공지': '公告',
      '📌 공지': '📌 公告',
      '[관리자]': '[管理员]',
      '⭐ 전략': '⭐ 策略',
      '아직 댓글 없음': '还没有评论',
      '글 삭제': '删除帖子',
      '📌 공지로 등록': '📌 作为公告发布',
      '(어드민 전용 — 목록 상단 고정)': '（仅管理员 —— 置顶显示）',
      '+ 등록': '+ 发布',
      '댓글 입력…': '写评论…',
      '제목 입력 (최소 2자)': '标题（至少 2 个字）',
      '내용 입력 (최소 2자)': '正文（至少 2 个字）',

      '🤖 AGENT · Claude 분석가': '🤖 AGENT · Claude 分析师',
      '+ 새 대화': '+ 新对话',
      '새 대화를 시작하거나 좌측에서 이전 대화를 선택하세요.':
        '开始一段新对话，或在左侧选择之前的对话。',
      '대화가 없습니다.': '没有对话。',
      '예시: "오늘 코스피 어때?" / "지금 보고 있는 종목 어때?"':
        '例如："今天韩国综合指数怎么样？" / "我正在看的这只标的呢？"',
      '⛨ ADMIN · 사용자 관리': '⛨ ADMIN · 用户管理',
      'TOP CLAUDE (오늘)': 'TOP CLAUDE（今日）',
      'TOP 로그인 (누적)': 'TOP 登录（累计）',
      '승인': '批准',
      '거부': '拒绝',
      '정지': '停用',
      '쿼터 리셋': '重置额度',

      '실시간 SSE 연결 상태': '实时 SSE 连接状态',
      '보고서 일일 한도': '每日报告额度',
      'Claude 일일 사용량': 'Claude 每日用量',
      '에이전트 채팅': '智能体对话',
      '커뮤니티 (공지/글/댓글)': '社区（公告/帖子/评论）',
      '관리자': '管理员',
      '종목 검색 (클릭)': '搜索标的（点击）',
      '추세선 (2점 클릭)': '趋势线（点两个点）',
      '수평선 (1점 클릭)': '水平线（点一个点）',
      '피보나치 (2점 클릭)': '斐波那契（点两个点）',
      '모두 지우기': '全部清除',
      '드래그하여 좌우 크기 조절': '拖动调整左右宽度',
      '드래그하여 상하 크기 조절': '拖动调整上下高度',
      '클릭 시 전체화면': '点击进入全屏',
      '전체화면 (ESC로 닫기)': '全屏（按 ESC 关闭）',
      '끌어서 옮기기': '拖动移动',
      '커뮤니티 — 공지/글/댓글/전략 공유':
        '社区 —— 公告、帖子、评论、策略分享',
      '작업 관리자 — 백그라운드 진행 중인 분석 보기/중단':
        '任务管理器 —— 查看或中断后台分析',
      '외부 접근 — Cloudflare Tunnel · QR 로그인':
        '外部访问 —— Cloudflare Tunnel · 二维码登录',
      '분석 이력 — 과거 분석 결과 검색': '分析历史 —— 搜索过往结果',
      '심볼 추가 (예: AAPL, TSLA, BTC-USD)': '添加代码（例如 AAPL, TSLA, BTC-USD）',
      '보유 종목 전체 포괄 분석': '把全部持仓一起分析',
      '새로 계산': '重新计算',
      '포트폴리오 관리 (큰 화면)': '投资组合管理（大屏）',
      '종목·티커·키워드 입력  (예: 삼성전자 / AAPL / 비트코인)':
        '标的、代码或关键词（例如 三星电子 / AAPL / 比特币）',
      '티커 또는 회사명 (예: AAPL, 삼성전자, 비트코인)':
        '代码或公司名（例如 AAPL、三星电子、比特币）',
      '글자 작게': '缩小字号',
      '글자 크게': '放大字号',
      '브라우저 새 창에서 열기': '在浏览器新窗口打开',
      '잘라 붙여넣기': '剪切并粘贴',
      '즐겨찾기 추가': '加入收藏',
      '즐겨찾기 해제': '取消收藏',
      '첨부된 전략이 있습니다 — 가져오기 가능': '附带了一个策略 —— 可以导入',
      '종목의 ☆ 별을 눌러 즐겨찾기에 추가하세요': '点标的旁的 ☆ 即可加入收藏'
    }
  };

  // ── 상태 ────────────────────────────────────────────────────
  var cur = 'ko';
  try {
    var saved = localStorage.getItem(KEY);
    if (saved && LANGS[saved]) cur = saved;
  } catch (e) { /* 시크릿 모드 등 — 한국어로 간다 */ }

  var table = DICT[cur] || null;

  function t(s) {
    if (!table || !s) return s;
    var v = table[s];
    return (typeof v === 'string') ? v : s;
  }

  // ── DOM 치환 ────────────────────────────────────────────────
  var ATTRS = ['placeholder', 'title', 'aria-label', 'alt'];
  var SKIP = { SCRIPT: 1, STYLE: 1, TEXTAREA: 1, CODE: 1, PRE: 1, SVG: 1 };

  function translateEl(el) {
    for (var i = 0; i < ATTRS.length; i++) {
      var a = ATTRS[i];
      if (!el.hasAttribute || !el.hasAttribute(a)) continue;
      var raw = el.getAttribute(a);
      var hit = t(raw.trim());
      if (hit !== raw.trim()) {
        // 원문을 남겨 둔다. 언어를 다시 바꿀 때 이미 번역된 값을 키로
        // 찾으면 못 찾는다 — 한 번 바꾸면 되돌릴 수 없게 된다.
        if (!el.hasAttribute('data-i18n-' + a))
          el.setAttribute('data-i18n-' + a, raw);
        el.setAttribute(a, hit);
      }
    }
  }

  function walk(root) {
    if (!root) return;
    if (root.nodeType === 1) {
      translateEl(root);
      var q = root.querySelectorAll('[placeholder],[title],[aria-label],[alt]');
      for (var i = 0; i < q.length; i++) translateEl(q[i]);
    }
    var w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        var p = n.parentNode;
        if (!p || SKIP[p.nodeName]) return NodeFilter.FILTER_REJECT;
        return n.nodeValue && n.nodeValue.trim()
          ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT;
      }
    });
    var nodes = [], n;
    while ((n = w.nextNode())) nodes.push(n);
    for (var j = 0; j < nodes.length; j++) {
      var node = nodes[j], raw = node.nodeValue, key = raw.trim();
      var hit = t(key);
      if (hit === key) continue;
      // 앞뒤 공백은 그대로 둔다. 인라인 요소 사이 간격이 붙어 버린다.
      var lead = raw.slice(0, raw.indexOf(key));
      var tail = raw.slice(raw.indexOf(key) + key.length);
      node.nodeValue = lead + hit + tail;
    }
  }

  function apply(root) {
    if (cur === 'ko' || !table) return;
    try { walk(root || document.body); } catch (e) { }
  }

  // 새로 그려진 DOM 도 같은 언어로. characterData 는 보지 않는다 —
  // 시세 숫자가 초당 여러 번 바뀌는데 그때마다 트리를 훑을 이유가 없다.
  var pending = [], scheduled = false;
  function flush() {
    scheduled = false;
    var batch = pending; pending = [];
    for (var i = 0; i < batch.length; i++) apply(batch[i]);
  }
  function startObserver() {
    if (cur === 'ko' || !window.MutationObserver) return;
    // 치환 중에 들어온 변경도 버리지 않는다. apply() 는 텍스트 값과
    // 속성만 건드리므로 childList 변경을 스스로 만들지 않는다 — 즉
    // 자기 자신과 부딪힐 일이 없다. 예전에 busy 플래그로 걸러 냈더니
    // 부팅 중 첫 치환과 위젯 렌더가 겹칠 때 그 위젯만 한국어로 남았다.
    new MutationObserver(function (muts) {
      for (var i = 0; i < muts.length; i++) {
        var added = muts[i].addedNodes;
        for (var j = 0; j < added.length; j++) {
          if (added[j].nodeType === 1) pending.push(added[j]);
        }
      }
      if (pending.length && !scheduled) {
        scheduled = true;
        setTimeout(flush, 80);
      }
    }).observe(document.body, { childList: true, subtree: true });
  }

  function setLang(code) {
    if (!LANGS[code]) return;
    try { localStorage.setItem(KEY, code); } catch (e) { }
    // 부분 치환을 되돌리는 안전한 방법은 다시 그리는 것뿐이다. 사전에
    // 없는 조각은 원문이 남아 있어서, 언어만 갈아 끼우면 두 언어가 섞인다.
    location.reload();
  }

  window.PlutusI18N = {
    langs: LANGS,
    current: function () { return cur; },
    // 날짜·시각·숫자 포매팅용 BCP-47. 화면 언어를 바꿨는데 시계만
    // "12시 43분" 으로 남아 있으면 안 바뀐 것처럼 보인다.
    locale: function () { return LANGS[cur].locale; },
    t: t,
    apply: apply,
    setLang: setLang
  };

  document.documentElement.setAttribute('lang', LANGS[cur].html);

  function boot() {
    apply(document.body);
    startObserver();
    // 부팅 시퀀스가 관측 시작보다 먼저 그려 놓은 것이 있을 수 있다.
    // 한 번 더 쓸어 주는 비용은 한 번의 트리 순회뿐이다.
    setTimeout(function () { apply(document.body); }, 1200);
  }
  if (document.readyState === 'loading')
    document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
