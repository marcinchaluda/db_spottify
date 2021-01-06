DROP INDEX IF EXISTS idx_user_email;

CREATE INDEX idx_user_email ON user_account(email);

EXPLAIN ANALYZE SELECT * FROM user_account
            WHERE email = 'TodSpe@ebay.co.uk';