import pandas as pd

from db_read import db_read
from db_write import db_write
from features import features
from predict import predict


datapath = 'dynamic_pricing.csv'
df = db_read(datapath)
df = features(df)
res = predict(df)
db_write(res, 'result.csv')