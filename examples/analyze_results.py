"""Small numerical and tabular analysis exercise."""
import numpy as np
import pandas as pd

results=pd.DataFrame({
    'test':['login','search','profile','login'],
    'browser':['chromium','chromium','chromium','firefox'],
    'passed':[True,False,True,True],
    'seconds':[1.2,0.8,2.1,1.4],
})
durations=results['seconds'].to_numpy(dtype=np.float64)
print(f'Mean duration: {durations.mean():.3f} seconds')
print(f'95th percentile: {np.percentile(durations,95):.3f} seconds')
summary=results.groupby('browser').agg(tests=('test','count'),pass_rate=('passed','mean'),mean_seconds=('seconds','mean'))
print(summary.to_string())
print('Failing tests:',results.loc[~results['passed'],'test'].tolist())
assert results.loc[~results['passed'],'test'].tolist() == ['search']
