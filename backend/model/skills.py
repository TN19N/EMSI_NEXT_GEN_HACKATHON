from psycopg2.extensions import connection as Connection
import numpy
from sklearn.cluster import KMeans

# Use KMeans to cluster users based on their skills
def skills(con: Connection) -> list:
    cur = con.cursor()
    cur.execute("SELECT * FROM User")
    users = cur.fetchall()

    data_points = numpy.array(users)[:, 2:]
    data_points = data_points.astype('float64')

    kmeans = KMeans(n_clusters=10, n_init='auto').fit(data_points)

    return [(users[i][1], int(kmeans.labels_[i])) for i in range(len(users))]