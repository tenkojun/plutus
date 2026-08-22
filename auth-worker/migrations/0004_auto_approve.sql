-- 가입 즉시 활성화로 정책을 바꾸면서, 이미 승인만 기다리고 있던 계정을
-- 남겨 두면 그 사람들만 영영 못 들어온다. 한 번에 열어 준다.
-- 여러 번 돌려도 안전하다 (pending 이 아니면 건드리지 않는다).
UPDATE users
   SET status = 'active',
       approved_at = COALESCE(approved_at, datetime('now'))
 WHERE status = 'pending';
