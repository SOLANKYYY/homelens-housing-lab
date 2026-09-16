"""Export an OLS lab. Default is synthetic; --california downloads real data."""
from pathlib import Path
import argparse,json
import numpy as np,sklearn
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,r2_score
p=argparse.ArgumentParser();p.add_argument('--california',action='store_true');args=p.parse_args()
P=Path(__file__).resolve().parents[1];names=['MedInc','HouseAge','AveRooms','AveBedrms','Population','AveOccup','Latitude','Longitude']
if args.california:
 d=fetch_california_housing();X=d.data;y=d.target;kind='California Housing · 1990 census';synthetic=False
else:
 rng=np.random.default_rng(42);X=np.column_stack([rng.uniform(1,10,600),rng.uniform(1,52,600),rng.uniform(2,9,600),rng.uniform(.8,2,600),rng.uniform(300,5000,600),rng.uniform(1,6,600),rng.uniform(32.5,42,600),rng.uniform(-124,-114,600)])
 y=1.8+(X-np.mean(X,axis=0))@np.array([.35,.003,.06,-.12,.00001,-.08,-.04,-.04])+rng.normal(0,.22,len(X));kind='Synthetic teaching sample';synthetic=True
train,test=train_test_split(np.arange(len(X)),test_size=.2,random_state=42);m=LinearRegression().fit(X[train],y[train]);pred=m.predict(X[test])
data={'synthetic':synthetic,'kind':kind,'rows':len(X),'train':len(train),'test':len(test),'features':names,'model':{'coef':m.coef_.tolist(),'intercept':float(m.intercept_)},'ranges':[[float(X[:,i].min()),float(X[:,i].max())] for i in range(8)],'defaults':np.median(X[train],axis=0).tolist(),'mae':mean_absolute_error(y[test],pred),'r2':r2_score(y[test],pred),'points':[[float(a),float(b)] for a,b in zip(y[test][:150],pred[:150])],'version':sklearn.__version__}
(P/'docs'/'data.js').write_text('window.PROJECT_DATA='+json.dumps(data,separators=(',',':'))+';\n')
(P/'research'/'evaluation.json').write_text(json.dumps(data,indent=2))
(P/'tests'/'fixtures.json').write_text(json.dumps([{'input':a.tolist(),'expected':float(b)} for a,b in zip(X[test],pred)]))
print(kind,'MAE',data['mae'],'R2',data['r2'])
