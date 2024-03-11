CREATE TABLE IF NOT EXISTS task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(128),
    summary VARCHAR(256),
    description TEXT,
    is_done BOOLEAN DEFAULT 0
    );

INSERT INTO task (
    name,
    summary,
    description
) VALUES
(
    "groceries",
    "shop for food",
    "eat out"
),
(
    "dishes",
    "workout",
    "run"
),
(
    "clothes",
    "hike",
    "sleep"
);
