DROP INDEX IF EXISTS idx_user_email;

EXPLAIN ANALYZE SELECT * FROM user_account
            WHERE email = 'TodSpe@ebay.co.uk';