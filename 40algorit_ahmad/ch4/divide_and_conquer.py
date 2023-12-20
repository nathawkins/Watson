"""
Example of a divide and conquer approach using Apache Spark implemented
using the pyspark framework.
"""

# Imports ---------------------------------------------------------------------
import findspark
from pyspark.sql import SparkSession

def createSparkContext():
    findspark.init()
    spark = SparkSession.builder.master("local[*]").getOrCreate()
    sc = spark.sparkContext
    return sc


if __name__ == '__main__':
    # Divide-and-conquer ~ map-reduce framework
    sc = createSparkContext()
    
    # Create list of words to calculate frequency of
    words = ['python', 'java', 'ottawa', 'ottawa', 'java','news']

    # Parallelize across 4 processes
    wordsRDD = sc.parallelize(words, 4)

    # Use map to assign key-value pair (will sum the values up during the shuffle and 
    # collect stage)
    wordPairs = wordsRDD.map(lambda w: (w,1))

    # Reduce and collect word pairs
    wordCountsCollected = wordPairs.reduceByKey(lambda x,y: x+y)

    # Print final result
    print(wordCountsCollected.collect())
