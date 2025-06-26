import os

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

COUNTRY = "Brazil"

datasetDir = "lastfm-dataset-1K"
if os.getenv("RUNNING_IN_CLUSTER"):
    print("Job running in cluster")
    datasetDir = "file:///opt/spark-data"

USERS_INPUT_FILE = f"{datasetDir}/userid-profile.tsv"
SONGS_INPUT_FILE = f"{datasetDir}/userid-timestamp-artid-artname-traid-traname.tsv"

spark = (SparkSession.builder
         .appName("LastFMAnalyzer")
         .config("spark.hadoop.fs.defaultFS", "file:///")
         .getOrCreate())

print("Reading users file")
df_user = (spark.read
           .option("header", True)
           .option("inferSchema", True)
           .option("delimiter", "\t")
           .option("mode", "FAILFAST")
           .csv(USERS_INPUT_FILE))
df_user = df_user.withColumnRenamed("#id", "user_id")

print("Reading songs file")
df_songs = (spark.read
            .option("header", False)
            .option("delimiter", "\t")
            .csv(SONGS_INPUT_FILE))
df_songs = (df_songs
            .withColumnRenamed("_c0", "user_id")
            .withColumnRenamed("_c1", "timestamp")
            .withColumnRenamed("_c2", "artist_id")
            .withColumnRenamed("_c3", "artist_name")
            .withColumnRenamed("_c4", "track_id")
            .withColumnRenamed("_c5", "track_name"))

print("Filtering by country")
df_user_country_filtered = df_user.filter(col("country") == COUNTRY)

print("Finding songs by users in country")
df_songs_by_user = df_songs.join(df_user_country_filtered, on="user_id", how="inner")

print("Finding top artists by users in country")
(df_songs_by_user
 .groupby("artist_name")
 .count()
 .orderBy("count", ascending=False)
 .show(truncate=False))

print("Finding top songs by users in country")
(df_songs_by_user
 .groupby("artist_name", "track_name")
 .count()
 .orderBy("count", ascending=False)
 .show(truncate=False))

spark.stop()
