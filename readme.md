# AI Apps Exam Project --- AI Trading Card Price Prediction
## Readme
### Made by Frederik Kruse Christiansen.
this project utilises AI to guess at the value of collectible trading cards based on multiple weeks and/or months value.

Below is the insert into used to create a local database to test the model

insert into cards values
(1,'Manamorphose','Double_Masters','Uncommon','English'),
(2,'Fighter Class','Adventures in the Forgotten Realms','Rare','English'),
(3,'Engineered Explosives','Fifth Dawn','Rare','English')


INSERT INTO card_prices
(card_id, price, available_items, is_foil, condition, language, is_signed, is_altered, updated_at)
VALUES


-- =========================
-- CARD 1
-- =========================
(1, 3.99, 730, 0, 'NM', 'English', 0, 0, '2026-04-18'),
(1, 3.99, 730, 0, 'NM', 'English', 0, 0, '2026-04-19'),
(1, 3.00, 730, 0, 'NM', 'English', 0, 0, '2026-04-20'),
(1, 3.25, 730, 0, 'NM', 'English', 0, 0, '2026-04-21'),
(1, 3.11, 730, 0, 'NM', 'English', 0, 0, '2026-04-22'),
(1, 3.48, 730, 0, 'NM', 'English', 0, 0, '2026-04-23'),


-- =========================
-- CARD 2
-- =========================
(2, 6.90, 768, 0, 'NM', 'English', 0, 0, '2026-04-18'),
(2, 8.31, 768, 0, 'NM', 'English', 0, 0, '2026-04-19'),
(2, 7.24, 768, 0, 'NM', 'English', 0, 0, '2026-04-20'),
(2, 7.57, 768, 0, 'NM', 'English', 0, 0, '2026-04-21'),
(2, 9.35, 768, 0, 'NM', 'English', 0, 0, '2026-04-22'),
(2, 7.85, 768, 0, 'NM', 'English', 0, 0, '2026-04-23'),


-- =========================
-- CARD 3
-- =========================
(3, 4.17, 787, 0, 'NM', 'English', 0, 0, '2026-04-18'),
(3, 3.49, 787, 0, 'NM', 'English', 0, 0, '2026-04-19'),
(3, 2.50, 787, 0, 'NM', 'English', 0, 0, '2026-04-20'),
(3, 4.16, 787, 0, 'NM', 'English', 0, 0, '2026-04-21'),
(3, 3.92, 787, 0, 'NM', 'English', 0, 0, '2026-04-22'),
(3, 3.45, 787, 0, 'NM', 'English', 0, 0, '2026-04-23');


