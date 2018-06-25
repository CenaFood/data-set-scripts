SELECT  "AnswerText", "LocalTime", "Longitude", "Latitude", "UserID", C2."FileName"
FROM   "Annotations"
LEFT JOIN "Challenges" C2 on "Annotations"."ChallengeID" = C2."ID"
