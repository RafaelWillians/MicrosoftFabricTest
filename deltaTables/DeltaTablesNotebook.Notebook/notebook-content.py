# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "a4042216-07c2-46e2-840a-5a5414a9b6fd",
# META       "default_lakehouse_name": "lakehouseDeltaTable",
# META       "default_lakehouse_workspace_id": "8fb3e71f-f4ce-4f5f-a159-4da9b4cfe6f0",
# META       "known_lakehouses": [
# META         {
# META           "id": "a4042216-07c2-46e2-840a-5a5414a9b6fd"
# META         }
# META       ]
# META     }
# META   }
# META }

# MARKDOWN ********************

# # Delta Lake tables
# Use this notebook to explore Delta Lake functionality


# CELL ********************

from pyspark.sql.types import StructType, IntegerType, StringType, DoubleType

# define the schema
schema = StructType() \
.add("ProductID", IntegerType(), True) \
.add("ProductName", StringType(), True) \
.add("Category", StringType(), True) \
.add("ListPrice", DoubleType(), True)

df = spark.read.format("csv").option("header","true").schema(schema).load("Files/products/products.csv")

# df now is a Spark DataFrame containing CSV data from "Fiels/products/products.csv"

display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
