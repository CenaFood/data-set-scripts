SELECT "UserID", U."Email", count("ID") as annotation_count
FROM   "Annotations"
LEFT JOIN "Users" U on "Annotations"."UserID" = U."Id"
GROUP BY U."Email", "UserID"
