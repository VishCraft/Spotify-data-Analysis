import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Track
Track_node1716433728982 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://spotify-data-bucket1/staging/track.csv"], "recurse": True}, transformation_ctx="Track_node1716433728982")

# Script generated for node Album
Album_node1716433728199 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://spotify-data-bucket1/staging/albums.csv"], "recurse": True}, transformation_ctx="Album_node1716433728199")

# Script generated for node Artist
Artist_node1716433726998 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://spotify-data-bucket1/staging/artists.csv"], "recurse": True}, transformation_ctx="Artist_node1716433726998")

# Script generated for node Join album and artist
Joinalbumandartist_node1716433904587 = Join.apply(frame1=Album_node1716433728199, frame2=Artist_node1716433726998, keys1=["artist_id"], keys2=["id"], transformation_ctx="Joinalbumandartist_node1716433904587")

# Script generated for node Join with track
Joinwithtrack_node1716434007117 = Join.apply(frame1=Track_node1716433728982, frame2=Joinalbumandartist_node1716433904587, keys1=["track_id"], keys2=["track_id"], transformation_ctx="Joinwithtrack_node1716434007117")

# Script generated for node Drop Fields
DropFields_node1716434121153 = DropFields.apply(frame=Joinwithtrack_node1716434007117, paths=["`.track_id`", "id"], transformation_ctx="DropFields_node1716434121153")

# Script generated for node Destination
Destination_node1716434196755 = glueContext.write_dynamic_frame.from_options(frame=DropFields_node1716434121153, connection_type="s3", format="glueparquet", connection_options={"path": "s3://spotify-data-bucket1/datawarehouse/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="Destination_node1716434196755")

job.commit()